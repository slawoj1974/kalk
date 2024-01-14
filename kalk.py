def dodawanie(a, b):    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"


liczba1 = 10
liczba2 = 5

suma = dodawanie(liczba1, liczba2)
roznica = odejmowanie(liczba1, liczba2)
iloczyn = mnozenie(liczba1, liczba2)
iloraz = dzielenie(liczba1, liczba2)

print("Liczba 1:", liczba1)
print("Liczba 2:", liczba2)
print("Suma:", suma)
print("Różnica:", roznica)
print("Iloczyn:", iloczyn)
print("Iloraz:", iloraz)

