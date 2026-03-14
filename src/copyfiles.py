import os
import shutil


def copy_files(source, destination):
    if not os.path.exists(source):
        raise Exception("Source directory dont exist")
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    elements = os.listdir(source)

    for i in range(0, len(elements)):
        path = os.path.join(source, elements[i])
        if os.path.isdir(path):
            copy_files(path, os.path.join(destination, elements[i]))
        else:
            print(f"\t> Copy {path} to {destination}")
            shutil.copy(path, destination)



def copy_static_to_public():
    source = os.path.abspath("./static")
    destination = os.path.abspath("./public")

    print(f"> Remove directory: {destination}")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    print(f"> Create new public directory")
    os.mkdir(destination)
    
    print(f"> copy files from {source} to {destination}")
    copy_files(source, destination)


    