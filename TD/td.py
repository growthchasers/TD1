import math

# exo3
print('----------exo3 started---------')

entier_1 = float(input('entrer un nombre: '))
entier_2 = float(input('entrer un nombre: '))
entier_3 = float(input('entrer un nombre: '))

print(f'somme :{entier_1 + entier_2 + entier_3}\nproduit:{entier_1 * entier_2 * entier_3}\nmoyenne:{(entier_1 + entier_2 + entier_3) / 3}')

print('----------exo3 finished---------')

# exo 4
print('----------exo4 started---------')

valeur_1 = int(input('entrer un nombre: '))
valeur_2 = int(input('entrer un nombre'))
def exchange(a, b):
    temp = a
    a = b
    b = temp
    print(f'a: {a}\nb: {b}')
    
exchange(valeur_1, valeur_2)

print('----------exo4 finished---------')

# exo 5 
print('----------exo5 started---------')

date = input('entrer une date: ').replace(' ', '')
jour = date[0:2]
mois = date[2:4]
ans = date[4:9]

print(f'jour : {jour} \nmois : {mois} \nans : {ans}')

print('----------exo5 finished---------')

# exo 6 
print('----------exo6 started---------')

vat_rate = 0.20
price_ht = float(input("Enter the price HT of the article: "))
quantity = int(input("Enter the number of articles: "))
total_price_ht = price_ht * quantity
total_vat = total_price_ht * vat_rate
total_price_ttc = total_price_ht + total_vat
print(f"The total price TTC is: {total_price_ttc:.2f} €")

print('----------exo6 finished---------')

# exo 7
print('----------exo7 started---------')

x1, y1, z1 = map(float, input("Enter the coordinates of the first point (x1, y1, z1): ").split())
x2, y2, z2 = map(float, input("Enter the coordinates of the second point (x2, y2, z2): ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print(f"The distance between the two points is: {distance:.2f}")

print('----------exo7 finished---------')

# exo 8
print('----------exo8 started---------')

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12:
    print("Invalid month.")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid day.")
else:
    print("The date is valid.")


print('----------exo8 finished---------')