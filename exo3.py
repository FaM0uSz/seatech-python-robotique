from abc import ABCMeta, abstractmethod

class Robot():
    @abstractmethod  # un décorateur pour définir une méthode abstraite
    def turn_on(self):
        pass

class Nao(Robot):
    def turn_on(self):
        print("J'ai reveillé mon robot NAO !")

class Delta(Robot):
    def turn_on(self):
        print("J'ai reveillé mon robot DELTA !")

class Alpha(Robot):
    def turn_on(self):
        print("J'ai reveillé mon robot ALPHA !")

class Naya(Nao, Delta): # Fille de NAO et Delta
    def turn_on(self):
        return super().turn_on()
    
    def hello_mom_dad():
        print("Coucou papa maman !")

if __name__ == '__main__':

    tab_robots = [Nao(), Delta(), Alpha(), Naya()]

    for rob in tab_robots:
        rob.turn_on()

r = Naya
r.hello_mom_dad()
