print('''Willkommen beim Taschenrechner!
    Du kannst immer jeweils zwei Zahlen miteinander
     Addieren "+"
     Subtrahieren "-"
     Multiplizieren "*"
     Dividieren "/"
    Gib dafür einfach deine erste zahl ein danach deinen gewünschten operanten und dann die zweite zahl
    ''')

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
    print(num1 / num2)