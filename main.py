#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from proposition.Unary import Unary
from proposition.Not import Not
from proposition.And import And
from proposition.Or import Or
from transitionSystem.State import State
from transitionSystem.TransitionSystem import TransitionSystem
from verify import verify


#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteurs:
#       -   Quentin GOMES DOS REIS
#       -   Matthéo LÉCRIVAIN
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


#    Verify a system of transitions that models two processes that are running in parallel
#    where the entry in the critical section is exclusive and controlled by a binary semaphore.
def verify_semaphores():
    #   States
    s1 = State(["nc1", "nc2", "y=1"])
    s2 = State(["p1", "nc2", "y=1"])
    s3 = State(["c1", "nc2", "y=0"])
    s4 = State(["nc1", "p2", "y=1"])
    s5 = State(["nc1", "c2", "y=0"])
    s6 = State(["p1", "p2", "y=1"])
    s7 = State(["c1", "p2", "y=0"])
    s8 = State(["p1", "c2", "y=0"])

    #   Transitions
    s1.set_next_states([s2, s4])
    s2.set_next_states([s3, s6])
    s3.set_next_states([s1, s7])
    s4.set_next_states([s5, s6])
    s5.set_next_states([s1, s8])
    s6.set_next_states([s7, s8])
    s7.set_next_states([s4])
    s8.set_next_states([s2])

    #   Transition system
    transition_system = TransitionSystem([s1])

    #   Proposition
    #   The proposition is that the two processes are never in the critical section at the same time
    proposition = Not(And(Unary("c1"), Unary("c2")))

    print(transition_system)
    print(proposition)

    #   Verify the proposition and print the result
    print(verify(transition_system, proposition))


if __name__ == '__main__':
    # proposition_test()
    verify_semaphores()
