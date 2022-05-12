import string

def Palindromo(str):

  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()

  if str == str[::-1]:
    return True
  else:
    return False

def main():
  Palavra = input("Digite uma palavra:")

  if (Palindromo(Palavra)):
    print(Palavra + " é um Palindromo")
  else:
    print(Palavra + " NÃO é um Palindromo")

if __name__ == "__main__":
    main()