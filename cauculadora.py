n1=int(input("Digite um numero: "))
n2=int(input("Digite um numero: "))

def escola():
    print(" Escolha a função:")
    print(" Escolha soma ")
    print(" Escolha a mutiplicação")
    print(" Escolha a subtração ")
    print(" Escolha a divisão")


def soma():
    print(f"A soma de {n1} mais {n2} é de:{n1+n2}")

def mutiplicacao():
    print(f"A mutiplicação de {n1} por {n2} é de :{n1*n1}")

def subtracao():
    print(f"A subtração de {n1} menos {n2} é de:{n1-n2}")

def divisao():
    print(f"A divisão de {n1} por {n2} é de :{n1/n2}")

def main():

        escola()
        mostre=input("Escolha uma opição +, * ,- ou /:")

        if mostre=='+':
            soma()
        elif mostre == '*':
            mutiplicacao()
        elif mostre == '-':
            subtracao()
        elif mostre == '/':
            divisao()
        else:
            print("\n Opção invalida")

if __name__== "__main__":
    main()