import pickle
import os
os.system("clear")

def savefile(name):
    savefile = pickle.dump(notes, open(f"{name}.pkl", "wb"))
    return savefile

def loadfile(external_commands):
    loadfile = pickle.load(open(f"{external_commands}.pkl","rb"))

print("input file name to be saved".upper())
name = (input())
print("now enter your notes".upper())
notes = (input())

print(savefile(name))

external_commands = (input())
print(loadfile(external_commands))
if(loadfile(a) == "None"):
    pickle.load(open(f"{external_commands}.pkl","rb"))
