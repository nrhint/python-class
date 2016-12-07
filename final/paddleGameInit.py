import pickle

file = open("dontDeleteMe!!!", mode = 'w')
file.close()

def __init__():
    data = [0, 0, 0, 0, 0]

    file = open("highScores.dat", mode = 'wb')
    pickle.dump(data, file)
    file.close()

def run(fileName):
    file = open(str(fileName), mode = 'r')
    fileData = file.read()
    if str(fileData) == '':
        file = open(str(fileName), mode = 'w')
        file.write('Joanna is a silly donught')
        __init__()
        return True
    else:
        return False

run('dontDeleteMe!!!')
