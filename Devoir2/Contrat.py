class Contrat:
    def __init__(self, numero, date, client, montantContrat):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = []
        self.nbIntervention = 0
    
    def montant(self):
        return self.montantContrat
    
    def ecart(self):
        coutInterventions = 0
        for intervention in self.interventions:
            coutInterventions += intervention.fraisMo() + intervention.fraisKm(100) # 100 est une distance arbitraire
            
        return self.montantContrat - coutInterventions