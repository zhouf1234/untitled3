import json

with open('data.json','r',encoding='utf-8')as f:
    data=f.read()

#反序列化
json_data = json.loads(data)
print(json_data)
print(type(json_data))

print(json_data['status'])
print(json_data['data'])
print(type(data))
print()