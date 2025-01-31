print('''Willkommen beim Taschenrechner!
    Du kannst immer jeweils zwei Zahlen miteinander
     Addieren "+"
     Subtrahieren "-"
     Multiplizieren "*"
     Dividieren "/"
    Gib dafür einfach deine erste zahl ein danach deinen gewünschten operanten und dann die zweite zahl
    ''')
def berechnung(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Fehler: Division durch 0!"
        else:
            return num1 / num2
    else:
        return f'Unzulässiger Operator {operator} Es sind nur +,-,*,/'

#Anfang des Codes
while True:
    try:
        num1 = float(input("Eingabe erste Zahl:"))
        operator = input("Eingabe Operator:")
        num2 = float(input("Eingabe zweite Zahl:"))

        solution = berechnung(num1, operator, num2)
        print(f"Ergebnis: {solution}")
    except ValueError:
        print("Fehler bei der eingabe")


    while True:
        answer = input("Nochmal? (j/n): ").lower()
        if answer not in ("j", "n"):
            print("Ungültige angabe! nur (j/n).")
        else:
            break
    if answer != "j":
       break



