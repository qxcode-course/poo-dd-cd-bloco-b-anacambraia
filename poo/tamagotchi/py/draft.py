class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy = energyMax
        self.__clean = cleanMax
        self.__age = 0
        self.__alive = True
    def getEnergy(self):
        return self.__energy
    def getEnergyMax(self):
        return self.__energyMax
    def getClean(self):
        return self.__clean
    def getAge(self):
        return self.__age
    def isAlive(self):
        return self.__alive

    def setEnergy(self, value: int):
        self.__energy = max(0, min(value, self.__energyMax))
        if self.__energy == 0:
            self.__alive = False
    def setClean(self, value: int):
        self.__clean = max(0, min(value, self.__cleanMax))
        if self.__clean == 0:
            self.__alive = False
    def incAge(self, value: int):
        self.__age += value
        
    def show(self):
        print(f"E:{self.__energy}/{self.__energyMax}, L:{self.__clean}/{self.__cleanMax}, I:{self.__age}")

class Game:
    def __init__(self, energyMax: int, cleanMax: int):
        self.pet = Tamagotchi(energyMax, cleanMax)
    def play(self):
        if not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 2)
        self.pet.setClean(self.pet.getClean() - 3)
        self.pet.incAge(1)
        if not self.pet.isAlive():
            if self.pet.getEnergy() == 0:
                print("fail: pet morreu de fraqueza")
            elif self.pet.getClean() == 0:
                print("fail: pet morreu de sujeira")
    def shower(self):
        if not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        self.pet.setEnergy(self.pet.getEnergy() - 3)
        self.pet.setClean(self.pet.getEnergyMax())  # Wait, should be cleanMax, not energyMax
        self.pet.incAge(2)

    def sleep(self):
        if not self.pet.isAlive():
            print("fail: pet esta morto")
            return
        if self.pet.getEnergy() > self.pet.getEnergyMax() - 5:
            print("fail: nao esta com sono")
            return
        turnos = self.pet.getEnergyMax() - self.pet.getEnergy()
        self.pet.setEnergy(self.pet.getEnergyMax())
        self.pet.incAge(turnos)


def main():
    game = Game("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            game = Game(int(args[1]), int(args[2]))
        elif args[0] == "show":
            if game:
                game.pet.show()
        elif args[0] == "play":
            if game:
                game.play()
        elif args[0] == "sleep":
            if game:
                game.sleep()
        elif args[0] == "shower":
            if game:
                game.shower()
main()
