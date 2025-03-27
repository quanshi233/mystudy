from pathlib import Path
import json

def get_stored_information(path):
    if path.exists():
        content = path.read_text()
        informations = json.loads(content)
        return informations
    else:
        return None

def get_new_information(path,your_name):
    if your_name:
        username = your_name
    else:
        username = input("please input your username:")
    password = input("please input your password:")
    informations = {'username':username, 'password':password}
    content = json.dumps(informations)
    path.write_text(content)
    return informations

def greet_user(path):
    informations = get_stored_information(path)
    your_name = input("please input your username:")
    if (informations) and (your_name in informations['username']):
        for k,v in informations.items():
            print(f"your {k} is {v}")
    else:
        informations = get_new_information(path,your_name)
        for k,v in informations.items():
            print(f"your {k} is {v}")

path = Path(".\mystudy\codes\informations.json")
greet_user(path)