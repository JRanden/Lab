from pathlib import Path
import shutil

files_dict = {
         '.txt': 'Text',
         '.log': 'Logs'
        }

p = Path('.')

file_extensions = []
folders = []
files_list = []
#print(files.keys)
# To do / flyt: 
# Sjekke etter filtype: DONE 
# Sjekke om dir finnes, hvis ikke lage: 
# Flytte filtyper til gitt mapper. 

## Forbederinger 
# Heller iterer over suffixer. Deretter lag en list med unike suffixer som sjekkes opp mot listen
# Deretter kan man putte alle med x suffix inn i y dir. 
# Samle hvor mange filer man puttet i de ulike directoriene? 

def check_dir(extensions):
    
    print("ran Dircheck")
    for values in extensions:
        create_dirs(values)

def create_dirs(extention):
    # Funksjon som iterer og sjekker om filer er i listen over extenions og mapper
    for dicts in files_dict:
        #print(f"{dicts} entry")
        if extention in dicts:
            folder_name = files_dict[extention]
            folder_name_path = Path(folder_name)
            print(f"{files_dict[extention]} {extention}")
            folder_name_path.mkdir(exist_ok=True)
            continue
        else:
            print(f"Warning {extention} does not have a folder selected")
            continue
    move_files()

                
# Får alle extensionsene i en liste. 
def get_file_extensions():
    for items in p.iterdir():
        if items.is_file():
            sp = p / items
            filetype= sp.suffix
            files = sp
            files_list.append(str(files))
            file_extensions.append(filetype)
        if items.is_dir():
            folders.append(str(items))
        
    check_dir(file_extensions)

# Mover
def move_files():
    for file in files_list:
        file_path = Path(file)
        print(file_path, file)
        if file_path.suffix in files_dict.keys():
            print("In")
            folder = files_dict.get(file_path.suffix, "default_value")
            print(folder)
            shutil.move(src=file, dst=folder)
        else:
            continue
if __name__ == "__main__":
    get_file_extensions()
