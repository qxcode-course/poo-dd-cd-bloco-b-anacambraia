class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def getThickness(self):
        return self.thickness

    def getSize(self):
        return self.size

    def setSize(self, value: int):
        self.size = value

    def usagePerSheet(self):
        # Gasto por folha baseado na dureza
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        else:
            return 1

    def __str__(self):
        return f"{self.thickness:.1f}:{self.hardness}:{self.size}"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None

    def hasLead(self):
        return self.tip is not None

    def insert(self, grafite: Lead):
        if self.hasLead():
            print("fail: ja existe grafite")
            return False
        if self.thickness != grafite.getThickness():
            print("fail: calibre incompativel")
            return False
        self.tip = grafite
        return True

    def remove(self):
        self.tip = None

    def writePage(self):
        if self.tip is None:
            print("fail: nao existe grafite")
            return

        if self.tip.getSize() <= 10:
            self.tip.setSize(10)
            print("fail: tamanho insuficiente")
            return

        gasto = self.tip.usagePerSheet()

        if self.tip.getSize() - gasto < 10:
            self.tip.setSize(10)
            print("fail: folha incompleta")
            return

        self.tip.setSize(self.tip.getSize() - gasto)

    def __str__(self):
        saida = f"calibre: {self.thickness:.1f}, grafite: "
        if self.tip:
            saida += f"[{self.tip}]"
        else:
            saida += "null"
        return saida


def main():
    pencil = Pencil(0.0)

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))
        elif args[0] == "insert":
            pencil.insert(Lead(float(args[1]), args[2], int(args[3])))
        elif args[0] == "remove":
            pencil.remove()
        elif args[0] == "write":
            pencil.writePage()
        



main()
