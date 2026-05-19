from pathlib import Path
import shutil

files_dict = {
         '.txt': 'Text',
         '.log': 'Logs'
        }

p = Path('.')
#print(files.keys)
# To do / flyt: 
# Sjekke etter filtype
# Sjekke om dir finnes, hvis ikke lage 
# Flytte filtyper til gitt mapper. 

def check_dir(extensions, folders):
    
    #
    for object in extensions:
        for entries in files_dict:
            if object in (entries):
                path = f".{files_dict[entries]}"
                folder_path = Path(path)
                print(f"In dict {object}")
                if folder_path.exists():
                


# Får alle extensionsene i en liste. 
def get_file_extensions():
    file_extensions = []
    folders = []
    for items in p.iterdir():
        if items.is_file():
            sp = p / items
            filetype= sp.suffix
            file_extensions.append(filetype)
        if items.is_dir():
            folders.append(items)
        
    return file_extensions, folders


            

    




# shutil.move()

if __name__ == "__main__":
    check_dir(get_file_extensions())