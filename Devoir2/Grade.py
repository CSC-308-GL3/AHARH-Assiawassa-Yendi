class Grade:
    def __init__(self, code, libelle, taux):
        self.code = code
        self.libelle = libelle
        self.taux = taux
    
    def getCode(self):
        return self.code
    
    def getLibelle(self):
        return self.libelle
    
    def tauxHoraire(self):
        # calculer le taux horaire correspondant au grade
        return self.taux