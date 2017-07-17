import os
import sys
import shutil
import zipfile


def get_dir():
    print('''Enter the location with zipped file
        for example:  /home/username/Documents/zipped''')
    location = input('..')
    if location:
        return location
    else:
        print("Please enter the location")


dir_location = get_dir()


def delete_zipped_files():
    for file in os.listdir(dir_location):
        if file.endswith('.zip'):
            os.unlink(file)
    print("program finished.")


def move_zipped_files():
    try:
        os.makedirs('zipped_files')
        for file in os.listdir(dir_location):
            if file.endswith('.zip'):
                shutil.move(file, 'zipped_files')
    except FileExistsError:
        print("folder named zipped_files already exists")
        print("Would the files moved into the zipped_files directory? Y/N")
        response = input('..')
        if response.lower() == 'y':
            for file in os.listdir(dir_location):
                if file.endswith('.zip'):
                    shutil.move(file, 'zipped_files')
            print("program finished.")
        else:
            sys.exit()
    else:
        print("zipped files move to 'zipped_files' directory")


def unzip_files():
    for zipped_file in os.listdir(dir_location):
        os.chdir(dir_location)
        if zipped_file.endswith('.zip'):
            file_unzipped = zipfile.ZipFile(zipped_file)
            file_unzipped.extractall()
            file_unzipped.close()
            print(zipped_file + " successfuly extracted.")

    print('''Do you want to move or deleted the zipped files?
                Enter : 1. Delete all zipped files
                        2. Move all zipped files into one folder
                        3. Do nothing
            ''')
    choice = int(input('..'))
    if choice == 1:
        delete_zipped_files()
    elif choice == 2:
        move_zipped_files()


def get_action():
    print('''Do you want to zip or unzip files.
          Enter:
               1. zip
               2.unzip
          ''')
    action = int(input('..'))

    if action == 1:
        print("not yet implemented")
    else:
        unzip_files()

get_action()
