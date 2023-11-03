#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteurs:
#       -   Quentin GOMES DOS REIS
#       -   Matthéo LÉCRIVAIN
#   M2 ALMA - Nantes Université
#   2023-2024

#   This file contains the abstract class Proposition
#   This class stands as a representation of a logical proposition
#   which is a statement made with the use of logical operators like
#   AND, OR, NOT, UNARY

class Proposition:

    # Constructor
    def __init__(self):
        pass

    # Evaluate the proposition
    def eval(self, labels: list[str]) -> bool:
        pass

    # Get the string representation of the proposition
    def __str__(self) -> str:
        pass
