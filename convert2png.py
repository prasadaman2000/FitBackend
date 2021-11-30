import os
from PIL import Image



def DFSConvert(path):
    files = os.listdir(path)

    for f_name in files:
        if os.path.isdir(path + f_name):
            DFSConvert(path + f_name + "/")
        if f_name.endswith(".webp"):
            os.remove(path + f_name)



if __name__ == "__main__":
    start_path = "./images/"
    DFSConvert(start_path)