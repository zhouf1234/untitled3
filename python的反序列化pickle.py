import pickle


with open('./pick.bat', 'rb') as f:
    obj = pickle.loads(f.read())
print(obj)
print(type(obj))