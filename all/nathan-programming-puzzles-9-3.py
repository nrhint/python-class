#file coppier
readFile = None
writeFile = None

readFileName = input("What is the name of the file that you want to coppy?  ")
writeFileName = input("What is the name of the coppied file?  ")

readFile = open(str(readFileName), mode = 'r')
writeFile = open(str(writeFileName), mode = 'w')

fileContents = readFile.read()

readFile.close()

writeFile.write(str(fileContents))

writeFile.close()

print("Done")
