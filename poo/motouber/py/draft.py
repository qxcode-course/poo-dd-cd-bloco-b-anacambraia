class Pessoa:
    def __init__(self, nome : str, dinheiro : int):
        self.__nome : str = nome or None
        self.__dinheiro : int = dinheiro or 0

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro

    def setDinheiro(self, valor: float):
        self.__dinheiro = valor

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro:.0f}"

class Moto:
    def __init__(self):
        self.__custo = 0.0
        self.__motorista = None
        self.__passageiro = None
    
    def setDriver(self, pessoa: Pessoa):
        self.__motorista = pessoa

    def setPass(self, pessoa: Pessoa):
        if self.__motorista is None:
            print("fail: no driver")
            return
        self.__passageiro = pessoa
        self.__custo = 0.0

    def drive(self, km: int):
        if self.__passageiro is None:
            print("fail: no passenger")
            return
        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None:
            print("fail: no passenger")
            return
        custo = self.__custo
        dinheiro_pass = self.__passageiro.getDinheiro()
        if dinheiro_pass < custo:
            print("fail: Passenger does not have enough money")
        self.__motorista.setDinheiro(self.__motorista.getDinheiro() + custo)
        pago = min(dinheiro_pass, custo)
        self.__passageiro.setDinheiro(dinheiro_pass - pago)
        print(f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro():.0f} left")
        self.__passageiro = None
        self.__custo = 0.0

    def show(self):
        driver_str = str(self.__motorista) if self.__motorista else "None"
        pass_str = str(self.__passageiro) if self.__passageiro else "None"
        print(f"Cost: {self.__custo:.0f}, Driver: {driver_str}, Passenger: {pass_str}")

def main():
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            moto.show()
        elif args[0] == "setDriver":
            moto.setDriver(Pessoa(args[1], float(args[2])))
        elif args[0] == "setPass":
            moto.setPass(Pessoa(args[1], float(args[2])))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "leavePass":
            moto.leavePass()
main()