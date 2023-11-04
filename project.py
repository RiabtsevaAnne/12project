import pickle

def name(a1, d1, N1, b1, d2, N2):
    f = set()

    for i in range(N1):
        a = a1 + i * d1
        for j in range(N2):
            b = b1 + j * d2
            if a == b:
                f.add(a)

    with open('digits.bin', 'wb') as file:
        pickle.dump(list(f), file)

a1 = 0.7
d1 = 2.7
N1 = 40

b1 = 4.3
d2 = 5.2
N2 = 38

name(a1, d1, N1, b1, d2, N2)





