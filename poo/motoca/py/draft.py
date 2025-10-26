class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}:{self.__age}"


class Motorcycle:
    def __init__(self, power: int):
        self.__power = power or 1
        self.__person = None
        self.__time = 0

    def insertPerson(self, person: Person) -> bool:
        if self.__person is not None:
            print("fail: busy motorcycle")
            return False
        self.__person = person
        return True

    def remove(self):
        if self.__person is None:
            print("fail: empty motorcycle")
            return
        person_removed = self.__person
        self.__person = None
        return person_removed

    def buyTime(self, time: int):
        self.__time += time

    def drive(self, time: int):
        if self.__time <= 0:
            print("fail: buy time first")
            return
        if self.__person is None:
            print("fail: empty motorcycle")
            return
        if self.__person.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time


    def honk(self):
        return "P" + ("e" * self.__power) + "m"

    def __str__(self):
        person_str = "empty" if self.__person is None else str(self.__person)
        return f"power:{self.__power}, time:{self.__time}, person:({person_str})"


def main():
    motoca = Motorcycle(1)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(motoca)
        elif args[0] == "init":
            power = int(args[1])
            motoca = Motorcycle(power)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            person = Person(nome, idade)
            motoca.insertPerson(person)
        elif args[0] == "leave":
            result = motoca.remove()
            if result is not None:
                print(result)
        elif args[0] == "buy":
            time = int(args[1])
            motoca.buyTime(time)
        elif args[0] == "drive":
            time = int(args[1])
            motoca.drive(time)
        elif args[0] == "honk":
            print(motoca.honk())


main()
