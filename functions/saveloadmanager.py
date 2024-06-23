import json, os
import utils.data as data

def create_saves_folder():
    folder_path = 'saves'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def Save(data, filename):
    create_saves_folder()
    with open(f'saves/{filename}.txt', 'w') as json_file:
        json.dump(data, json_file)

def Load(filename):
    with open(f'saves/{filename}.txt', 'r') as json_file:
        data.userdata = json.load(json_file)