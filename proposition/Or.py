from proposition.Proposition import Proposition


#   This class stands as a representation of an OR logical operator

class Or(Proposition):
    # Attributes
    #   Stores the two terms of the Or operator (left and right)
    term1: Proposition
    term2: Proposition

    # Constructor
    def __init__(self, term1: Proposition, term2: Proposition):
        super().__init__()
        self.term1 = term1
        self.term2 = term2

    # Evaluate the proposition
    #   Which is just an implementation of the OR operator
    def eval(self, labels: list[str]) -> bool:
        return self.term1.eval(labels) or self.term2.eval(labels)

    # Get the string representation of the proposition
    def __str__(self) -> str:
        return f"({self.term1} OR {self.term2})"