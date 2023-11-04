import shelve

with shelve.open('file1.dat') as file:
    if 'cars' in file:
        car = file['cars']
        for model, power in car.items():
            print(f"Модель: {model}, Потужність двигуна: {power}")
    else:
        print("Словник автомобілів ще не було створено.")
