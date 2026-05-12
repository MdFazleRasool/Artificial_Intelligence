import json

'''
py_ob = {
    "name" : "Md Fazle RAsool",
    "age" : 22
}
# Convert Python object to JSON string
json_str = json.dumps(py_ob)  # Convert the Python object to a JSON string  
print(json_str)  # Print the JSON string
print(type(json_str))  # Print the type of json_str (should be str)     


# Convert JSON string back to Python object
py_ob2 = json.loads(json_str)  # Convert the JSON string back to a Python object
print(py_ob2)  # Print the Python object
print(type(py_ob2))  # Print the type of the Python object (should be dict) 

'''

with open('data.json', 'r') as file:  # Open a file named 'data.json' in write mode
    py_ob =  json.load(file)
    print(py_ob)
    print(type(py_ob))


d = {
    "name" : "Md Fazle RAsool",
    "age" : 22,
    "is_student" : True
}

with open('data.json', 'w') as file:  # Open a file named 'data.json' in write mode
    json.dump(d, file, indent=4 , sort_keys=False)  # Write the Python object 'd' to the file in JSON format    
