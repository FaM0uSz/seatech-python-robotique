from time import sleep

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']

    """
    Give your best code here ( •̀ ω •́ )✧
    """

    def __init__(self, name='default'):
        self.__name = name
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0
        self.__states = ['shutown', 'running']

    def power_on(self):
        self.__power = True

    def power_off(self):
        self.__power = False

    def battery_charger(self):
        chargement = ""

        while self.__battery_level < 100:
            self.__battery_level += 1
            chargement += '#'
            sleep(0.05)
            print("Niveau de batterie : {:100s} {}%".format(chargement, self.__battery_level), end='\r', flush=True)
        print()
        print("Batterie charger au maximum !")

    @property
    def get_vitesse(self):
        return self.__current_speed

    def get_etat(self):
        print("Nom du Robot : {}".format(self.__name))
        print("Allumé ou éteint : {}".format(self.__power))
        print("Niveau de batterie : {}%".format(self.__battery_level))
        print("Vitesse de déplacement : {}".format(self.__current_speed))

        if self.__power == False:
            print("Etat du Robot : {}".format(self.__states[0]))
        else:
            print("Etat du Robot : {}".format(self.__states[1]))

        print("-------------------------")
        
    def stop_vitesse(self):
        self.__current_speed = 0

if __name__ == "__main__":
   r = Robot("TomleBg")
   r.power_on()
   r.battery_charger()
   r.get_etat()
