import pickle

def fname(filename):
    with open(filename, 'rb') as file:
        f = pickle.load(file)
        for element in f:
            print(element)

fname('digits.bin')