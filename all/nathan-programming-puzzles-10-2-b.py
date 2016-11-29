import pickle

loadedFavesFiles = open('favorits.dat', 'rb')
loadedFaves = pickle.load(loadedFavesFiles)
loadedFavesFiles.close()
print(loadedFaves)
