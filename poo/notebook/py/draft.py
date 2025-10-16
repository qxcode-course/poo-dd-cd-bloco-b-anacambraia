class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def mostrar(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"status: {status}")

    def getCarga(self):
        return self.__carga

    def setCarga(self, valor):
        if 0 <= valor <= self.__capacidade:
            self.__carga = valor
        else:
            print("fail: valor de carga inválido")

    def descarregar(self, tempo):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0
class Notebook:
    def __init__(self):
        self.__ligado : bool = False
        self.__bateria: Bateria | None = None 
        self.__carregador: Carregador | None = None 

    def getLigado(self):
        return self.__ligado

    def setLigado(self, valor: bool):
        self.__ligado = valor

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("notebook já está ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado =  False
            print("notebook desligado")
        else:
            print("notebook já está desligado")

    def mostrar(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"status: {status}")

    def usar(self, tempo):
        if self.__ligado:
            print(f"usando por {tempo} minutos")
        else:
            print("erro: ligue o notebook primeiro")

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
notebook.ligar()      # msg: não foi possível ligar
notebook.usar(10)     # msg: notebook desligado

bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.setBateria(bateria) # coloca a bateria no notebook

notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 30 minutos
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

bateria = notebook.rmBateria() # msg: bateria removida
bateria.mostrar()  # (0/50)
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

carregador = Carregador(2) # criando carregador com 2 de potencia
carregador.mostrar() # (Potência 2)

notebook.setCarregador(carregador) # adicionando carregador no notebook
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

notebook.setBateria(bateria)
notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
notebook.usar(10)  # msg: Notebook utilizado com sucesso
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)