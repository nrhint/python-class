import pickle

faves = {
    "food", "games", "programming"
    }

favesFile = open("favorits.dat", 'wb')
pickle.dump(faves, favesFile)
favesFile.close()
