#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from proposition.Proposition import Proposition
from proposition.Unary import Unary
from proposition.Not import Not
from proposition.And import And
from proposition.Or import Or


#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteur:
#       -   Quentin GOMES DOS REIS
#   M2 ALMA - Nantes Université
#   2023-2024

def proposition_test():
    #   Test of the propositions

    #   Propositions
    proposition1 = And(Not(Unary("a")), Unary("b"))
    proposition2 = Or(And(Unary("a"), Unary("b")), And(Unary("c"), Unary("d")))

    #   labels
    labels = ["a", "b", "c", "d"]

    #   Print the labels
    print("Labels:")
    print(f'\t{labels}\n')

    #   Print the propositions and their results
    print("Propositions:")
    print(f'\t-   {proposition1}')
    print(f'\t\tResult: {proposition1.eval(labels)}')
    print(f'\t-   {proposition2}')
    print(f'\t\tResult: {proposition2.eval(labels)}')

if __name__ == '__main__':
    proposition_test()
