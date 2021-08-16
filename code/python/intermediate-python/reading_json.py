import json
#convert string into json object
j_ob = '{"name": "Tim", "height": "5\'10", "age": "38"}'
j_ob = json.loads(j_ob) #load string
print(j_ob['height'])
print(type(j_ob))
j_ob["age"] = 75
j_ob_str = json.dumps(j_ob) #dump string
print(j_ob_str)