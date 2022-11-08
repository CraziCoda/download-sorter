import os
downloads = os.path.expanduser("~\downloads")


#Creates folders given an array of folder names
def create_folders(folders):
    # A loop to read the folders array element by element
    for folder in folders:
        # create a folder path for the folder to be created
        path = os.path.join(downloads, folder)
        try:
            # Tries to create folder
            os.mkdir(path)
            print(folder  + " has been created in " + downloads)
        except FileExistsError:
            # Handling error if folder already exists
            print(f"{folder} already exits in {downloads}")

# It gets filenames of all files in ownloads
def get_files():
    # gets all files names and folders names within downloads
    dirs = os.listdir(downloads)
    # array to store filenames
    files = []
    # runs through array of files and folders names
    for dir in dirs:
        # create path a file or folder 
        path = os.path.join(downloads, dir)
        # checks if the path is a file
        if os.path.isfile(path):
            # adds file to array of filenames
            files.append(dir)
    # returns array of files
    return files

# It places files inside respective folders
def sort_files(files, folders, keys: dict):
    # runs for each file in files
    for file in files:
        # finds index of last dot in filename
        last_dot = file.rfind(".")
        # gets file extension from file name
        file_extension = file[last_dot:len(file):1]
        # runs for each folder in folders
        for folder in folders:
            # creates a path to current downloads folder
            dest = os.path.join(downloads, folder)
            # creates a path to where file is at
            source = os.path.join(downloads, file)
            if file_extension in keys[folder]:
                # creates a path to where we want to move file
                dest = os.path.join(dest, file)
                print(f"{file} is in {folder}")
                # moves file to the destination
                os.rename(source, dest)
        

