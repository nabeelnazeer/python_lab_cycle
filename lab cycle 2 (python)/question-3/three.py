import json

def listelements(jsonpath):
  file = open(jsonpath,'r')
  jsonlist =  file.readlines()
  file.close()
  return jsonlist  
def dictionary_obj(jasonpath):
  file = open(jsonpath, 'r')
      


jsonpath = 'iris.json'
json_list = listelements(jsonpath)
print("innapidicho : ")
for line in json_list:
  print(line)