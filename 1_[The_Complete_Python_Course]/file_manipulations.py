import glob, os

files = glob.glob("codes/*py")
# print(files)

for single_file in files:
    file_to_be_moved = single_file
    folder_name = file_to_be_moved[:-3]
    folder_name = folder_name.replace(".", "_")
    os.makedirs(folder_name)

    old_file = file_to_be_moved
    destination = folder_name + "/" + file_to_be_moved[6:]

    os.rename(old_file, destination)
