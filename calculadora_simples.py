
def adicione(x, y):
    return x + y


def subtraia(x, y):
    return x - y


def multiplique(x, y):
    return x * y


def divida(x, y):
    return x / y


print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")


choice = input("Escolha uma operação(1/2/3/4):")
num1 = int(input("Escolha o primeiro número: "))
num2 = int(input("Escolha o segundo número: "))

if choice == '1':
    print(num1, "+", num2, "=", adicione(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtraia(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplique(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divida(num1, num2))
else:
    print("A operação que você escolheu não existe kkkkkkkkkkjjjjjj")