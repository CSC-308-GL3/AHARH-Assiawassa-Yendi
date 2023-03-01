from Employe import Employe
from Intervention import Intervention
from Contrat import Contrat

# Création de l'employé
employe = Employe(1, "AHARH Yohann", "A", "01/01/2020")

# Création de deux interventions
intervention1 = Intervention(1, "01/02/2021", 3, 0.5, employe)
intervention2 = Intervention(2, "01/03/2021", 2, 0.5, employe)

# Création du contrat
contrat = Contrat(1, "01/01/2023", employe, 100)

# Affichage de l'écart entre le montant du contrat et le coût des interventions
print("Montant du contrat : ", contrat.montant())
print("Coût des interventions : ", sum([intervention.fraisMo() for intervention in contrat.interventions]))
print("Écart : ", contrat.ecart())