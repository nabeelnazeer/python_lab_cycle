import json

jsonfile = open('iris.json','r')
jsondata =  jsonfile.readlines()

json_list = []

for line in jsondata:
    json_obj = json.loads(jsondata)
    json_list.append(json_obj)

for line in json_list:
    print(line)


