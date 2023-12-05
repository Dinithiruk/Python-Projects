import random

"inti method contains the characteristics or attributes \
of the each person that we want to create"

"we assign characteristics to a name that include self \
is that to allow us to make those characteristics available \
for the init method as well as the other methods"
class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    # self introduce method - ( All people introduce themselves )
    def introduce(self):
        print("Hello,my name is {} {}".format(self.firstname, self.lastname))

    # emotion express method
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    # healthy status showing method
    def status_change(self):
        self.health = (self.health - 25)
        if self.health ==100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >=76:
            print("{} is a little tired today".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell".format(self.firstname))

        elif self.health >=40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious".format(self.firstname))

# peoples
Maria = Person("Maria", "Gutierrez", 95, status=True)
Peter= Person("Peter","Parker",55,status=True)
Selena = Person("Selena","Gomez", 99,status=False)
Tom = Person("Tom","Holland",62,status=True)

print("{} is my friend? {}".format(Peter.firstname,Peter.status))
print("{} is my friend? {}".format(Selena.firstname,Selena.status))
print("\n")

Peter.introduce()
Selena.introduce()
Tom.introduce()

print("\n")

Peter.status_change()
Selena.status_change()
Tom.status_change()






