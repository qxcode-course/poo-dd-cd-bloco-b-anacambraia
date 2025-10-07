class Time:
    def __init__(self, hour : int, minute : int, second : int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getSecond(self, second : int):
        return self.__second

    def getMinute(self, minute : int):
        return self.__minute

    def getHour(self, hour : int):
        return self.__hour

    def setHour(self, value : int) -> None:
        if value < 0 or value > 23:
            print("fail: hora invalida")
            return
        else:
            setHour = value
            

    def setMinute(self, value : int) -> None:
        if value < 0 or value > 59:
            print("fail: minuto invalido")
            return
        else:
            setMinute = value
            

    def setSecond(self, value : int) -> None:
        if value < 0 or value > 59:
            print("fail: segundo invalido")
            return
        else:
            setSecond = value

           

    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

def main():
    tempo = Time ("", "", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "set":
            __hour = args[1]
            __minute = args[2]
            __second = args[3]
            tempo = Time(__hour, __minute, __second)
        elif args[0] == "show":
            print(tempo)
main()

