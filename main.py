import os
from shutil import move

# Enter folder path
folder_path = input("Enter your folder path: ")


def find_all_extension(path_of_folder):
    """
    Find all extension for the files in source folder.\n
    :param path_of_folder: The path of source folder.
    :return: Return A list.
    """
    # Define an empty list
    extension = []
    for file in os.listdir(path_of_folder):
        the_path = os.path.join(folder_path, file)
        if os.path.isfile(the_path):
            file_name = file.split(".")
            if len(extension) == 0:
                extension.append(file_name[len(file_name) - 1])
            else:
                check = True
                for element in extension:
                    if element == file_name[len(file_name) - 1]:
                        check = False
                    else:
                        continue
                if check:
                    extension.append(file_name[len(file_name) - 1])
        else:
            continue
    return extension


def create_folders(extension_list, full_folder_path):
    """
    Create folder for each extension type.\n
    :param extension_list: Extension for all file in the folder.
    :param full_folder_path: The path of source folder.
    :return: if something incorrect it returns TypeError else not return anything.
    """
    # Check if parameter `extension_list` is list or not
    assert isinstance(extension_list, list), "Parameter `extension_list` must be a list"
    # If parameter `extension_list` is list continue
    for extension_name in extension_list:
        # Convert extension's name to Uppercase
        EXTENSION_NAME = str(extension_name).upper()
        # Create folders
        folders_path = os.path.join(full_folder_path, EXTENSION_NAME)
        if not os.path.exists(folders_path):
            os.mkdir(folders_path)


def files_organize(extension_list, full_folder_path):
    """
    Organize each file to correct folder.\n
    :param extension_list: Extension for all file in the folder.
    :param full_folder_path: The path of source folder.
    :return: no return.
    """
    # Check if parameter `extension_list` is list or not
    assert isinstance(extension_list, list), "Parameter `extension_list` must be a list"
    # If parameter `extension_list` is list continue
    for extension in extension_list:
        for file in os.listdir(full_folder_path):
            # Get full file path
            file_path = os.path.join(full_folder_path, file)
            if os.path.isfile(file_path):
                if file.endswith(str(extension).lower()):
                    # Get full path for destination folder
                    destination_path = os.path.join(full_folder_path, str(extension).upper())
                    # Move files from source folder to destination folder
                    move(file_path, destination_path)
                    print(file, "moved successfully")
            else:
                continue


# Check if path exists
if os.path.exists(folder_path):
    # Call functions
    EXTENSION_LIST = find_all_extension(folder_path)
    create_folders(EXTENSION_LIST, folder_path)
    files_organize(EXTENSION_LIST, folder_path)
    # Finished message
    print("----All File Moved Successfully----")
else:
    # Error message
    print("The path is incorrect!!")
