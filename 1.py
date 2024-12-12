# კალკულატორის პროგრამა რომელიც ასრულებს კალუკულატორის ძირითად ფუნქციონალს


Pir_ricxvi = int(input("შეიყვანეთ რიცხვი:     "))
Meo_ricxvi = int(input("შეიყვანეთ მეორე რიცხვი:    "))

Moqmedeba = input("მიუთითეთ ერთ-ერთ შემდეგი მოქმედება: plus, minus, divide, multiply:     ")
Archeuli_moqmedeba = Moqmedeba.lower()

if Archeuli_moqmedeba == "plus":
    print (Pir_ricxvi + Meo_ricxvi)
elif Archeuli_moqmedeba == "minus":
    print (Pir_ricxvi - Meo_ricxvi)
elif Archeuli_moqmedeba == "divide":
    print (Pir_ricxvi / Meo_ricxvi)
elif Archeuli_moqmedeba == "multiply":
    print (Pir_ricxvi * Meo_ricxvi)
else:
    print("თქვენს მიერ არჩეული ქმედება არასწორია, კიდევ სცადეთ!")
