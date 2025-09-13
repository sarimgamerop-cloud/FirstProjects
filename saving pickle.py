import pickle
import os
os.system("clear")

# Save
pickle.dump(variable, open("variable.dat", "wb"))

# Load
variable = pickle.load(open("names.dat", "rb"))

#change
variable.remove("variable?")