class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self):
        return self.__tamanho 

    def setTamanho(self, valor):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamanhos_validos:
            self.__tamanho = valor
            return True
        elif valor == "":
            print("size: ()")
        else:
            print("Valor inválido! Os tamanhos permitidos são: PP, P, M, G, GG, XG.")
            return False

    def __str__(self):
        return f"{self.getTamanho}"

def main():
    roupa = Roupa ()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(roupa)
main()