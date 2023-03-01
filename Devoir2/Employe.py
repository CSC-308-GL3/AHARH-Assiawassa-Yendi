class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche
        
    def coutHoraire(self):
        # implémenter le calcul du coût horaire de l'employé
        pass
        
    def getNumero(self):
        return self.numero
    
    def getNom(self):
        return self.nom
    
    def getQualification(self):
        return self.qualification
    
    def getDateEmbauche(self):
        return self.dateEmbauche
    
    def getAnciennete(self, date):
        # implémenter le calcul de l'ancienneté de l'employé
        pass