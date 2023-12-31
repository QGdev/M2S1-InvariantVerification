from proposition.Proposition import Proposition


#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteurs:
#       -   Quentin GOMES DOS REIS
#       -   Matthéo LÉCRIVAIN
#   M2 ALMA - Nantes Université
#   2023-2024

#   This class stands as a representation of an NOT logical operator

class Not(Proposition):

    # Attributes
    #   Stores the unique term of the NOT operator
    term: Proposition

    # Constructor
    def __init__(self, term: Proposition):
        super().__init__()
        self.term = term

    # Evaluate the proposition
    #   Which is just an implementation of the NOT operator
    def eval(self, labels: list[str]) -> bool:
        return not self.term.eval(labels)

    # Get the string representation of the proposition
    def __str__(self) -> str:
        return f"(NOT {self.term})"

