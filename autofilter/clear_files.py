import os

def delete_ids():
    try:
        os.remove("id.txt")
        print("Files cleared.")
    except:
        print("Unable to clear files.")