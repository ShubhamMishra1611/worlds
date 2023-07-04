import os
import json

def make_folder(name):
    if os.path.exists(name):
        return 0
    else:
        os.mkdir(name)
        return 1

def make_file(name, content):
    if os.path.exists(name):
        return 0
    else:
        file = open(name, 'w')
        file.write(content)
        file.close()
        return 1
    
def push_file(filename):
    try:
        os.system("git add " + filename)
        os.system("git commit -m \"Add " + filename + "\"")
        os.system("git push -u origin main")
        return 1
    except:
        return 0

FOLDER_NAME = "hello_world"

def main_json():
    if not os.path.exists(FOLDER_NAME):
        make_folder(FOLDER_NAME)
        print("Folder " + FOLDER_NAME + " created.")
    file = open("scapped.json", 'r', encoding="utf-8")
    data = json.load(file)
    file.close()
    for language in data["programming_languages"]:
        name = language["name"]
        extension = language["extension"]
        hello_world = language["hello_world"]
        print("Language: " + name + ", Extension: " + extension + ", Hello World: " + hello_world)
        succe = make_file(FOLDER_NAME + "/hello_world_"+ name + extension, hello_world)
        if succe:
            print("File " + FOLDER_NAME + "/hello_world_"+ name + extension + " created.")
        else:
            continue
        succ = push_file(FOLDER_NAME + "/hello_world_"+ name + extension)
        if succ:
            print("File " + FOLDER_NAME + "/hello_world" + extension + " pushed.")
        else:
            print("File " + FOLDER_NAME + "/hello_world" + extension + " not pushed.")
        # break # so that only one language is pushed for now

if __name__ == "__main__":
    main_json()
    

    