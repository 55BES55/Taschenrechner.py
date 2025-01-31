print('''Willkommen beim Taschenrechner!
    Du kannst immer jeweils zwei Zahlen miteinander
     Addieren "+"
     Subtrahieren "-"
     Multiplizieren "*"
     Dividieren "/"
    Gib dafür einfach deine erste zahl ein danach deinen gewünschten operanten und dann die zweite zahl
    ''')
while True:
    num1 = float(input("Eingabe erste Zahl:"))
    operant = input("Eingabe Operator:")
    num2 = float(input("Eingabe zweite Zahl:"))

    if operant == "+":
        print(num1 + num2)
    elif operant == "-":
        print(num1 - num2)
    elif operant == "*":
        print(num1 * num2)
    elif operant == "/":
        if num2 == 0:
            print("Fehler: Division durch 0!")
        else:
            print(num1 / num2)


    if input("Nochmal? (j/n) ")  != "j":
        break