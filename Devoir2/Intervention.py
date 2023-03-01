class Intervention:
    def __init__(self, numero, date, duree, tarifkm, technicien):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifkm = tarifkm
        self.technicien = technicien
    
    def affiche(self):
        # afficher les informations de l'intervention
        print(f"Intervention numéro {self.numero} effectuée le {self.date} par l'employé {self.technicien.getNom()}")
    
    def fraisKm(self, dist):
        # calculer les frais kilométriques
        return self.tarifkm * dist
    
    def fraisMo(self):
        # calculer les frais de main d'oeuvre
        return self.technicien.coutHoraire() * self.duree