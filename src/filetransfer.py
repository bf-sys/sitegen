import os
import shutil
from pathlib import Path



def delete_public(public_folder: Path):
     #clean out the public directory
    for item in public_folder.iterdir():
        if public_folder.is_dir() and not any(public_folder.iterdir()):
            print(f"Nothing to delete")
            break
        if item.is_file():
            print(f"Deleting item {item}")
            item.unlink()
        elif item.is_dir():
            print(f"Removing directory {item}")
            shutil.rmtree(item)

def copy_static_to_public(static_folder: Path, public_folder: Path):
    #broke out this functionality to make a cleaner recursive function
    for item in static_folder.iterdir():
        if item.is_file():
            file_name = item.name
            current_public_file = Path(public_folder / f"{file_name}" )
            print(f"Copying file = {item} to {current_public_file}")
            shutil.copy(item, current_public_file)

        elif item.is_dir():
            dir_name = item.name
            current_public_folder = Path(public_folder / f"{dir_name}")
            current_static_folder = Path(item)
            print(f"Creating directory - {current_public_folder}")
            os.mkdir(current_public_folder)
            copy_static_to_public(current_static_folder, current_public_folder)
    
    

    
   





#this is hardcoded to just use the relative static and public directories associated with this app
    # Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    # * It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    # * It should copy all files and subdirectories, nested files, etc.
    # * I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
