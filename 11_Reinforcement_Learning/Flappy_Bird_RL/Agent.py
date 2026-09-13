
import argparse
import random
import flappy_bird_gymnasium
import gymnasium as gym
from dqn import DQN
from experience_replay import ReplayMemory
import itertools as itr
import yaml
import torch
import torch.nn as nn
import torch.optim as optim
import os

RUNS_DIR = "runs"
os.makedirs(RUNS_DIR, exist_ok=True)

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")




class Agent:

    

    def __init__(self, param_set):

        self.param_set = param_set

        with open("parameters.yaml","r") as f:
            all_param = yaml.safe_load(f)
            params = all_param[param_set]

        self.alpha = params["alpha"]
        self.gamma = params["gamma"]
        self.env_id = params["env_id"]

        self.epsilon_init = params["epsilon_init"]
        self.epsilon_min = params["epsilon_min"]
        self.epsilon_decay = params["epsilon_decay"]
        self.replay_memory_size = params["replay_memory_size"]
        self.mini_batch_size  = params["mini_batch_size"]
        self.network_sync_rate = params["network_sync_rate"]
        self.reward_threshold = params["reward_threshold"]
        
        self.loss_fn = nn.MSELoss()
        self.optimizer = None 

        self.LOG_FILE = os.path.join(RUNS_DIR, f"{self.param_set}.log")
        self.MODEL_FILE = os.path.join(RUNS_DIR, f"{self.param_set}.pt")

    def run(self, is_Training=True, render=False):

        env = gym.make(
            self.env_id, 
            render_mode="human" if render else None,
            use_lidar=True
        )

        num_states = env.observation_space.shape[0] # input dimensions
        num_actions = env.action_space.n # output dim..

        policy_dqn = DQN(num_states,num_actions).to(device)


        if is_Training :
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init

            target_dqn = DQN(num_states,num_actions).to(device)
            # copy the wt & bias vals from policy => target
            target_dqn.load_state_dict(policy_dqn.state_dict())

            steps = 0
            self.optimizer = optim.Adam(policy_dqn.parameters(),lr = self.alpha)
        
            best_reward = float("-inf") # - infinity
        else :
            # best policy load
            policy_dqn.load_state_dict(torch.load(self.MODEL_FILE))
            policy_dqn.eval()

        if is_Training:
            episodes = itr.count()
        else:
            episodes = range(10)   
         
        for episode in episodes:

            state, _ = env.reset()
            state = torch.tensor(state,dtype=torch.float32 , device=device)

            episode_reward = 0
            done = False

            while (not done and episode_reward < self.reward_threshold):
                if is_Training and random.random() < epsilon :
                    action = env.action_space.sample()
                    action = torch.tensor(action, dtype=torch.long, device=device)
                else :
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim=0)).squeeze(0).argmax() # Exploit
                    
                next_state, reward, terminated, truncated, _ = env.step(action.item())
                done = terminated or truncated

                episode_reward += reward

                ## Create tensors
                reward = torch.tensor(reward,dtype=torch.float32 , device=device)

                next_state = torch.tensor(next_state,dtype=torch.float32 , device=device)


                if is_Training:
                    memory.append((state,action,next_state,reward,done))
                    steps += 1

                
                state=next_state
                

            if is_Training:
                print(
                    f"episode = {episode + 1} "
                    f"with total reward = {episode_reward} "
                    f"& epsilon = {epsilon}"
                )
            else:
                print(
                    f"episode = {episode + 1} "
                    f"with total reward = {episode_reward}"
                )

        

            if is_Training:
            # Epsilon decay
                epsilon = max(epsilon * self.epsilon_decay , self.epsilon_min) 

                if  episode_reward > best_reward :
                    log_msg = f"best reward = {episode_reward} for episode = {episode+1}"

                    with open (self.LOG_FILE,"a") as f:
                        f.write(log_msg + "\n")
                    torch.save(policy_dqn.state_dict(),self.MODEL_FILE)

                    best_reward = episode_reward

                

            if is_Training and len(memory) >= self.mini_batch_size :
                # get sample
                mini_batch = memory.sample(self.mini_batch_size )

                self.optimize(mini_batch, policy_dqn, target_dqn)

                # sync the network
                if steps >= self.network_sync_rate:
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    steps = 0
                    
            # env.close() - manually stop
    
    def optimize(self, mini_batch, policy_dqn, target_dqn):
        # get batch of Experince => batch train
        states, actions,  next_states, rewards, dones = zip(*mini_batch)

        states = torch.stack(states)
        actions = torch.stack(actions)
        next_states = torch.stack(next_states)
        rewards = torch.stack(rewards)

        dones = torch.tensor(
            dones,
            dtype=torch.float32,
            device=device
        )



        # calculate target Q-values - if terminations = true => zero
        with torch.no_grad():
            target_q = rewards + (1 - dones) * self.gamma * target_dqn(next_states).max(dim=1)[0]


        # calculate y_pred i.e Q-value  from current policy
        current_q = policy_dqn(states).gather(dim=1, index= actions.unsqueeze(dim=1)).squeeze()





        # compute  loss
        loss = self.loss_fn(current_q, target_q)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


if __name__ == "__main__":
    # Parse command line inputs
    parser = argparse.ArgumentParser(description='Train or test model.')
    parser.add_argument('hyperparameters', help='')
    parser.add_argument('--train', help='Training mode', action='store_true')
    args = parser.parse_args()

    dql = Agent(param_set=args.hyperparameters)

    if args.train:
        dql.run(is_Training=True)
    else:
        dql.run(is_Training=False, render=True)
