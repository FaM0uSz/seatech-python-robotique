from abc import ABCMeta
from abc import abstractmethod

class VehiculeUnmanned(metaclass=ABCMeta):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def executer_mission(self):
        pass

class VehiculeGround(metaclass=ABCMeta):
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def ride(self):
        pass

class UUV(VehiculeUnmanned):
    def executer_mission(self):
        print(f"Le UUV {self.nom} exécute une mission subaquatique.")

class UAV(VehiculeUnmanned):
    def executer_mission(self):
        print(f"Le UAV {self.nom} exécute une mission aérienne.")

class UGV(VehiculeUnmanned,VehiculeGround):
    def executer_mission(self):
        print(f"Le UGV {self.nom} exécute une mission terrestre.")

    def ride(self):
        print(f"Le UGV {self.nom} roule sur terre.")

# Corp principal (main)
uuv1 = UUV("UUV-1")
uav1 = UAV("UAV-1")
ugv1 = UGV("UGV-1")

liste_vehicules = [uuv1, uav1, ugv1]

for vehicule in liste_vehicules:
    vehicule.executer_mission()

ugv1.ride()
