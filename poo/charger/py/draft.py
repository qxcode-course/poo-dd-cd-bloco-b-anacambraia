class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__tempo_uso = 0
        self.__bateria = None  
        self.__carregador = None  

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        saida = f"Notebook: {status}"
        if self.__ligado:
            saida += f" por {self.__tempo_uso} min"
        if self.__carregador is not None:
            saida += f", Carregador {self.__carregador}W"
        if self.__bateria is not None:
            saida += f", Bateria {self.__bateria['carga']}/{self.__bateria['capacidade']}"
        print(saida)

    def turn_on(self):
        if (self.__bateria and self.__bateria['carga'] > 0) or self.__carregador:
            self.__ligado = True
            self.__tempo_uso = 0
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        self.__tempo_uso += tempo
        if self.__bateria:
            if self.__carregador:
                self.__bateria['carga'] += self.__carregador * tempo
                if self.__bateria['carga'] > self.__bateria['capacidade']:
                    self.__bateria['carga'] = self.__bateria['capacidade']
            else:
                self.__bateria['carga'] -= tempo
                if self.__bateria['carga'] <= 0:
                    self.__bateria['carga'] = 0
                    self.__ligado = False
                    print("fail: descarregou")

    def set_charger(self, potencia: int):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = potencia

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__carregador}W")
        self.__carregador = None
        if self.__ligado and not ((self.__bateria and self.__bateria['carga'] > 0) or self.__carregador):
            self.__ligado = False

    def set_battery(self, capacidade: int):
        self.__bateria = {'carga': capacidade, 'capacidade': capacidade}

    def rm_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria['carga']}/{self.__bateria['capacidade']}")
        self.__bateria = None
        if self.__ligado and not ((self.__bateria and self.__bateria['carga'] > 0) or self.__carregador):
            self.__ligado = False

def main():
    notebook = Notebook()
    while True:
        line = input()
        print("$" + line)
        if line.startswith("#TEST_CASE"):
            notebook = Notebook()
            continue
        if line.startswith("#"):
            continue
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.show()
        elif args[0] == "turn_on":
            notebook.turn_on()
        elif args[0] == "turn_off":
            notebook.turn_off()
        elif args[0] == "use":
            notebook.use(int(args[1]))
        elif args[0] == "set_charger":
            notebook.set_charger(int(args[1]))
        elif args[0] == "rm_charger":
            notebook.rm_charger()
        elif args[0] == "set_battery":
            notebook.set_battery(int(args[1]))
        elif args[0] == "rm_battery":
            notebook.rm_battery()

main()
