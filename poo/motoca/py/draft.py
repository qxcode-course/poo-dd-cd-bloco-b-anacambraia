class Person:
    def __init__(self, age : int, name : str):
        self.__age : int = age
        self.__name : str = name

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
       return f"{self.__age}:{self.__name}"

class Motorcycle:
    def __init__(self, power : int):
        self.__power = 1
        self.__person = None
        self.__time = 0

    def insertPerson(self, person : Person) -> bool:
        if self.__person is not None:
            print("fail: busy motorcycle")
            return False
        self.__person = person
        return True

    def remove(self):
        if self.__person is None:
            print("fail: empty motorcycle")
            return None
        person_remove = self.__person
        self.__person = None
        return person_remove

    def buyTime(self, time: int):
        self.__time += time

    def drive(self, time: int):
        if self.__person is None:
            print("fail: empty motorcycle")
            return
        if self.__person.getAge() > 10:
            print("fail: too old to drive")
            return
        if self.__time <= 0:
            print("fail: buy time first")
            return

        if time > self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time

    def honk(self):
        return "P" + ("e" * self.__potencia) + "m"

    def __str__(self):
        persona = "empty" if self.__person is None else str(self.__person)
        return f"power:{self.__power}, time:{self.__time}, person:({persona})"

def main():
    motoca = Motorcycle("")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(motoca)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            person = Person(nome, idade)
            motoca.insertPerson(person)
        elif args[0] == "init":
            power = int(args[1])
            motoca = Motorcycle(power)
main()

