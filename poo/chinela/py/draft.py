class Chinela:
    def __init__():
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor : int):
        if (self.__tamanho <= 20 and self.__tamanho <= 50) and self.__tamanho % 2 == 0:

chinela = Chinela()

while chinela.getTamanho == 0:
    print("qual tamanho da sua chinela?")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())
