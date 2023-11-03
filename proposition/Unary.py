from proposition.Proposition import Proposition


#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteurs:
#       -   Quentin GOMES DOS REIS
#       -   Matthéo LÉCRIVAIN
#   M2 ALMA - Nantes Université
#   2023-2024

#   This class stands as a representation of a UNARY logical operator

class Unary(Proposition):

    # Attributes
    #   Stores the token of the UNARY operator
    term: str

    # Constructor
    def __init__(self, term: str):
        super().__init__()
        self.term = term

    # Evaluate the proposition
    #   Which is just an implementation of the NOT operator
    def eval(self, labels: list[str]) -> bool:
        #   Compare the provided labels with the stored term
        #   If the term is in the labels, return True
        for label in labels:
            if label == self.term:
                return True

        #   If not, return False
        return False

    # Get the string representation of the proposition
    def __str__(self) -> str:
        return self.term
