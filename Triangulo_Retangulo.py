def isTriangulo(a, b, c):
    if (max(a, b, c) != c):

        tmp = c
        c = max(a, b, c)

        if a == c:
            a = tmp
        elif b == c:
            b = tmp

    if a ** 2 + b ** 2 == c ** 2:
        print("É um triângulo Retângulo")
        return True
        print("NÃO é um triângulo Retângulo")
        return False


def main():
    a = input("Digite o valor de A do triângulo: ")
    b = input("Digite o valor de B do triângulo: ")
    c = input("Digite o valor de C do triângulo: ")

    return isTriangulo(int(a), int(b), int(c))


if __name__ == "__main__":
    main()
