import json

user_info = {'name':'丹丹','age':19,'add':'上海','grade':'py01'}
json_str = json.dumps(user_info)
print(json_str)
print(type(json_str))
print()

print(json.dumps([1,2,3,4,5,6]))
print()

t=(1,2,3,4,5)
print(json.dumps(t))
print(type(t))

