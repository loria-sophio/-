
from random import randint

a = (randint(1, 10))

print (a)
mcdeloba = 0
while True:
    she_cifri = int(input("დაასახელეთ ციფრი :  "))

    mcdeloba += 1

    if she_cifri > a:
        print ("დასახელებული ციფრი მეტია ჩაფიქრებულ ციფრზე")

    if she_cifri < a:
       print ("დასახელებული ციფრი ნაკლებია ჩაფიქრებულ ციფრზე")


    if a == she_cifri:
        print(f"გილოცავთ თქვენ გამოიცანით ჩაფიქრებული ციფრი! ციფრი შეარჩიეთ {mcdeloba} მცდელობით.")
        break

