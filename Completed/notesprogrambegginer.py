
import os
os.system("clear")
# i can input my notes as a variable accesed anytime within the program
print("=================================================")
print("> type in to save the data (info=/help) <".upper() )
print("=================================================")
print("write here = ".upper())
notes_input = str(input())
if notes_input == "/load":
    load_input = open("notes_input.txt", "r")
    print(f"> {notes_input} <")

# mini help corner
if(notes_input == "/help"):
    print(" hello to my notes program made by specialcodes !")
    print("functionality :")
    print("> Only one time run save menory. it will not saved after rerun")
    print("type something to save it then type /load to load it and /remove to delete")
    print("happy codings :) now rerun the program")
print("=================================================")



# for looping until user inputs load to load the data
load_input = str(input())
while load_input not in ["/load" , "/remove"]:
    print("its not a valid command".upper())
    load_input = str(input())

if(load_input=="/load"):
    load_input = open("notes_input.txt", "a")
    print(f"> {notes_input} <")
    print("=================================================")
elif load_input == "/remove":
    os.remove("notes_input.pkl")
    print("successfully removed".upper())
else:
    print("its not a valid command".upper())


# now making th save remove
print("=================================================")
print("if U want to remove or load type /remove or /load".upper())
remove_input = str(input())

while remove_input not in ["/remove","/load"]:
    print("its not a valid command".upper())
    remove_input = str(input())
if(remove_input=="/remove"):
    os.remove("notes_input.pkl")
    print("successfully removed".upper())
elif remove_input == "/load":
    load_input = open("notes_input.txt", "r")
    print(f"> {notes_input} <")
    print("=================================================")  
else:
    print("invalid command".upper())


    

