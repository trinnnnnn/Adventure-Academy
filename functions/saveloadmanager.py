# import necessary modules
import json, os
import utils.data as data

# create savedata folder if it doesnt exist
def create_saves_folder():
    folder_path = 'saves'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Save function
def Save(data, filename):
    create_saves_folder()
    with open(f'saves/{filename}.txt', 'w') as json_file:
        json.dump(data, json_file)

# Load function
def Load(filename):
    with open(f'saves/{filename}.txt', 'r') as json_file:
        data.data = json.load(json_file)