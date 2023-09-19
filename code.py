import os

path = "names"

names = []

for file in os.listdir(path):
    file_path = os.path.join(path,file)

    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            name = f.read()
            names.append(name)

for name in names:
    print(f"Имя: {name}")