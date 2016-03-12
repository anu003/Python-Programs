import os

def rename_files():

    # get the list of files from a directory
    list_filenames = os.listdir(r"/Users/KittusMac/Downloads/prank")
    saved_path = os.getcwd()
    os.chdir(r"/Users/KittusMac/Downloads/prank")
    for filename in list_filenames:
        
        os.rename(filename, filename.translate(None, "0123456789"))
                  
    os.chdir(saved_path)
    print list_filenames
rename_files()
