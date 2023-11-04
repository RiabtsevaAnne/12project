import shelve

def d(car):
    for _ in range(3):
        model = input("Введіть назву моделі автомобіля: ")
        power = input("Введіть потужність двигуна: ")
        car[model] = power

with shelve.open('file1.dat') as file:
    if 'cars' in file:
        car = file['cars']
    else:
        car = {}
    
    d(car)

    file['cars'] = car
