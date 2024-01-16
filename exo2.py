from exo1 import Robot
from time import sleep

class Human():   
    __sexe = 'None'

    def __init__(self, sexe='Male'):
        self.__sexe = sexe
        self.__nombre_aliment = 0
        self.__aliment_mange = []

    def eat(self, aliments):
        if type(aliments) is str:
            self.__nombre_aliment += 1
            print("J'ai mangé {}".format(aliments))
        else:
            for i in aliments:
                print("J'ai mangé {}".format(i))
                self.__nombre_aliment += 1
        self.__aliment_mange.append(aliments)

    @property
    def sexe(self):
        return self.__sexe

    def digest(self):
        digestion = ""
        for i in range(self.__nombre_aliment):
            print("Chargement digestion : {}/{}".format(i+1, self.__nombre_aliment), end='\r', flush=True)
            sleep(1)
        print()
        print("J'ai fini de digérer !")

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def truc_fun(self):
        print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)

if __name__ == "__main__":
    h = Human("Male")

    cyborg = Cyborg('Deux Ex Machina', 'M')
    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.truc_fun()
