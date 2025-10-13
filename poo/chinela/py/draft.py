class Chinela:
    def __init__(self):
        self.__tamanho = 0  

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor):
        if 20 <= valor <= 50 and valor % 2 == 0:
            self.__tamanho = valor
            return True
        else:
            print("Valor inválido! O tamanho deve ser um número par entre 20 e 50.")
            return False


chinela = Chinela()

while True:
    try:
        tamanho = int(input("Digite o tamanho da sua chinela: "))
        if chinela.setTamanho(tamanho):
            print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())
            break
    except erro:
            print("Entrada inválida! Digite apenas números inteiros.")
