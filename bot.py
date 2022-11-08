import functions

# Name of folders we want place sorted files
folders = ["Docs", "Music", "Videos", "Apps", "Compressed", "Pictures"]

# creates the folders if they do not exist
functions.create_folders(folders)
# gets all the files in downloads folder
files = functions.get_files()

# a dictionaire of folders to the file extensions to place in them
dict_sort = {
    "Docs": [".pdf", ".xlxs", ".doc", ".docx", ".ppt", ".csv", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Apps": [".exe", ".msi"],
    "Compressed": [".zip", ".rar"],
    "Pictures": [".jpg", ".png", ".jfif", ".webp", ".jpeg"]  
}

#moves files into new destinations
functions.sort_files(files, folders, dict_sort)
