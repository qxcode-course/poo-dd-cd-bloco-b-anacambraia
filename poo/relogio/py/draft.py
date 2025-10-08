class Time:
    def __init__(self, hora, minuto, segundo):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
        self.setHour(hora)
        self.setMinute(minuto)
        self.setSecond(segundo)

    def getsegundo(self):
        return self.segundo

    def setHour(self, value):
        if value < 0 or value > 23:
            print("fail: hora invalida")
            return
        self.hora = value

    def setMinute(self, value):
        if value < 0 or value > 59:
            print("fail: minuto invalido")
            return
        self.minuto = value

    def setSecond(self, value):
        if value < 0 or value > 59:
            print("fail: segundo invalido")
            return
        self.segundo = value

    def nextSecond(self):
        self.segundo += 1
        if self.segundo > 59:
            self.segundo = 0
            self.minuto += 1
        if self.minuto > 59:
            self.minuto = 0
            self.hora += 1
        if self.hora > 23:
            self.hora = 0

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

def main():
    tempo = Time(0, 0, 0)

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            tempo = Time(hora, minuto, segundo)

        elif args[0] == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            tempo.setHour(hora)
            tempo.setMinute(minuto)
            tempo.setSecond(segundo)

        elif args[0] == "show":
            print(tempo)

        elif args[0] == "next":
            tempo.nextSecond()

        else:
            print("fail: comando invalido")
main()