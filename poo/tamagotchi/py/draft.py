class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def getCarga(self):
        return self.__carga

    def setCarga(self, valor: int):
        if valor < 0:
            self.__carga = 0
        elif valor > self.__capacidade:
            self.__carga = self.__capacidade
        else:
            self.__carga = valor

    def descarregar(self, tempo: int):
        self.setCarga(self.__carga - tempo)

    def carregar(self, valor: int):
        self.setCarga(self.__carga + valor)

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def getLigado(self):
        return self.__ligado

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def rmBateria(self):
        if self.__bateria:
            temp = self.__bateria
            self.__bateria = None
            print("bateria removida")
            return temp
        else:
            print("fail: não há bateria")

    def ligar(self):
        if self.__ligado:
            print("notebook já está ligado")
        elif (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else:
            print("notebook já está desligado")

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"

        if self.__bateria:
            bat_info = f"({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})"
        else:
            bat_info = "Nenhuma"

        if self.__carregador:
            car_info = f"(Potência {self.__carregador.getPotencia()})"
        else:
            car_info = "Desconectado"

        print(f"Status: {status}, Bateria: {bat_info}, Carregador: {car_info}")

    def usar(self, tempo):
        if not self.__ligado:
            print("notebook desligado")
            return

        if self.__bateria and self.__carregador:
            ganho = tempo * self.__carregador.getPotencia()
            self.__bateria.carregar(ganho)
            print("Notebook utilizado com sucesso")
            return

        
        if self.__carregador and not self.__bateria:
            print("Notebook utilizado com sucesso")
            return

        
        if self.__bateria:
            carga_atual = self.__bateria.getCarga()
            if tempo <= carga_atual:
                self.__bateria.descarregar(tempo)
                print(f"Usando por {tempo} minutos")
            else:
                print(f"Usando por {carga_atual} minutos, notebook descarregou")
                self.__bateria.setCarga(0)
                self.__ligado = False
            return

        
        print("erro: sem bateria e sem carregador")

    def __str__(self):
        return f"Notebook: {status}"

def main():
    notebook = Notebook()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(notebook)
main()