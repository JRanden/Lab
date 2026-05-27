from pathlib import Path
import shutil

files_dict = {
         '.txt': 'Text',
         '.log': 'Logs'
        }

p = Path('.')
#print(files.keys)
# To do / flyt: 
# Sjekke etter filtype: DONE 
# Sjekke om dir finnes, hvis ikke lage: 
# Flytte filtyper til gitt mapper. 

def check_dir(extensions):
    
    print("ran dir check")
    for values in extensions:
        move_files(values)

def move_files(extention):
    # Funksjon som iterer og sjekker om filer er i listen over extenions og mapper
    for dicts in files_dict:
        #print(f"{dicts} entry")
        if extention in dicts:
            print(f"{files_dict[extention]} {extention}")
        else:
            #print(f"Warning {extention} does not have a folder selected")
            continue
            # print("Extention in dictionary!")
                


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
        
    check_dir(file_extensions)


            

    




# shutil.move()

if __name__ == "__main__":
    get_file_extensions()