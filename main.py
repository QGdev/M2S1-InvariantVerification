#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from proposition.Proposition import Proposition
from proposition.Unary import Unary
from proposition.Not import Not
from proposition.And import And
from proposition.Or import Or
from transitionSystem.State import State
from transitionSystem.TransitionSystem import TransitionSystem
from verify import verify

import sys


#   Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents
#   Auteurs:
#       -   Quentin GOMES DOS REIS
#       -   Matthéo LÉCRIVAIN
#   M2 ALMA - Nantes Université
#   2023-2024

def proposition_print_test(transition_system: TransitionSystem, proposition: Proposition):
    print(f"\t{proposition}")
    is_verified, example = verify(transition_system, proposition)

    if is_verified:
        print("\n\t\033[92m\033[1mThe proposition is verified\033[0m")
    else:
        print("\n\t\033[93m\033[1mThe proposition is not verified\033[0m")
        print("\t\033[91m\033[1mCounter-example:\033[0m")
        for state in example:
            print(f"\t\t\033[91m\033[1m{state}\033[0m")


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
    print("\n\033[1m==================================================")
    print("Semaphores verification")
    print("==================================================")
    print("\tExample imposed by the subject:")
    print(
        "\tTwo processes are running in parallel where the entry in the critical section is exclusive and controlled by a binary semaphore")
    print("==================================================\033[0m")

    #   States
    #      i for idle
    #      w for waiting
    #      cs for critical section
    s1 = State(["i1", "i2", "y=1"])
    s2 = State(["w1", "i2", "y=1"])
    s3 = State(["cs1", "i2", "y=0"])
    s4 = State(["i1", "w2", "y=1"])
    s5 = State(["i1", "cs2", "y=0"])
    s6 = State(["w1", "w2", "y=1"])
    s7 = State(["cs1", "w2", "y=0"])
    s8 = State(["w1", "cs2", "y=0"])

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

    #   Propositions
    #   Proposition 1: The critical section cannot be accessed by both processes at the same time
    print("\n\033[4m\033[1mFirst proposition:\033[0m")
    print("\tThe critical section cannot be accessed by both processes at the same time")

    proposition1 = Not(And(Unary("cs1"), Unary("cs2")))

    proposition_print_test(transition_system, proposition1)

    #   Proposition 2: Test of a proposition that is false, the fact that both processes can access the critical section at the same time
    print("\n\033[4m\033[1mSecond proposition:\033[0m")
    print("\tBoth processes can access the critical section at the same time")
    print("\t\033[94m\033[1mNOTE: This proposition is false, we will test it to see if the algorithm works\033[0m")

    proposition2 = And(Unary("cs1"), Unary("cs2"))

    proposition_print_test(transition_system, proposition2)


#    Verify a system of transitions that models a pair of traffic lights at a crossroad.
#    The traffic lights can be red (r), green (g) or yellow (y) but they cannot be both green at the same time.
def verify_traffic_lights_at_crossroad_section():
    print("\n\033[1m==================================================")
    print("Traffic lights at a crossroad verification")
    print("==================================================")
    print(
        "\tThe traffic lights can be red (r), green (g) or yellow (y) but they cannot be both green or yellow at the same time")
    print("==================================================\033[0m")
    #   States
    s1 = State(["r1", "r2"])
    s2 = State(["g1", "r2"])
    s3 = State(["y1", "r2"])
    s4 = State(["r1", "g2"])
    s5 = State(["r1", "y2"])
    s6 = State(["r1", "r2"])

    #   Transitions
    s1.set_next_states([s2])
    s2.set_next_states([s3])
    s3.set_next_states([s4])
    s4.set_next_states([s5])
    s5.set_next_states([s6])
    s6.set_next_states([s1])

    #   Transition system
    transition_system = TransitionSystem([s1])

    #   Propositions
    #   First proposition: The traffic lights cannot be both green at the same time
    proposition = Not(And(Unary("g1"), Unary("g2")))

    print("\n\033[4m\033[1mFirst proposition:\033[0m")
    print("\tThe traffic lights cannot be both green at the same time")

    proposition_print_test(transition_system, proposition)

    #   Second proposition: The traffic lights cannot be both yellow at the same time
    proposition = Not(And(Unary("y1"), Unary("y2")))

    print("\n\033[4m\033[1mSecond proposition:\033[0m")
    print("\tThe traffic lights cannot be both yellow at the same time")

    proposition_print_test(transition_system, proposition)

    #   Third proposition: The traffic lights cannot be both green and yellow at the same time
    proposition = Not(Or(And(Unary("g1"), Unary("y2")), And(Unary("y1"), Unary("g2"))))

    print("\n\033[4m\033[1mThird proposition:\033[0m")
    print("\tThe traffic lights cannot be both green and yellow at the same time")

    proposition_print_test(transition_system, proposition)

#    Verify a system of transitions that models a drinks vending machine.
#    The drinks vending machine can be in one of the following states:
#    -   idle
#    -   coin inserted
#       -   coin returned

#       -   drink selected
#       -   drink delivered
#
#    There are four types of drinks:
#    -   tea
#    -   coffee
#    -   hot chocolate
#    -   tomato soup
#
def verify_drinks_vending_machine():
    print("\n\033[1m==================================================")
    print("Drinks vending machine verification")
    print("==================================================")
    print("\t A drink vending machine can be in one of the following states:")
    print("\t -   idle")
    print("\t -   coin inserted")
    print("\t     -   coin returned")
    print("\t     -   drink selected")
    print("\t     -   drink delivered")
    print("\n\t There are four types of drinks:")
    print("\t -   tea")
    print("\t -   coffee")
    print("\t -   hot chocolate")
    print("\t -   tomato soup")
    print("==================================================\033[0m")

    # States

    s1 = State(["idle", "no drink selected", "no drink delivered"])
    s2 = State(["coin inserted", "no drink selected", "no drink delivered"])
    s3 = State(["coin returned", "no drink selected", "no drink delivered"])

    #   Selecting a drink
    s4_tea = State(["coin inserted", "tea selected", "no drink delivered"])
    s4_coffee = State(["coin inserted", "coffee selected", "no drink delivered"])
    s4_hot_chocolate = State(["coin inserted", "hot chocolate selected", "no drink delivered"])
    s4_tomato_soup = State(["coin inserted", "tomato soup selected", "no drink delivered"])

    #   Serving a drink
    s5_tea = State(["coin inserted", "tea_selected", "tea delivered"])
    s5_coffee = State(["coin inserted", "coffee selected", "coffee delivered"])
    s5_hot_chocolate = State(["coin inserted", "hot chocolate selected", "hot chocolate delivered"])
    s5_tomato_soup = State(["coin inserted", "tomato soup selected", "tomato soup delivered"])

    #   Transitions
    s1.set_next_states([s2])
    s2.set_next_states([s3, s4_tea, s4_coffee, s4_hot_chocolate, s4_tomato_soup])
    s3.set_next_states([s1])

    s4_tea.set_next_states([s5_tea])
    s4_coffee.set_next_states([s5_coffee])
    s4_hot_chocolate.set_next_states([s5_hot_chocolate])
    s4_tomato_soup.set_next_states([s5_tomato_soup])

    s5_tea.set_next_states([s1])
    s5_coffee.set_next_states([s1])
    s5_hot_chocolate.set_next_states([s1])
    s5_tomato_soup.set_next_states([s1])

    #   Transition system
    transition_system = TransitionSystem([s1])

    #  Propositions

    # First proposition: The drinks vending machine cannot deliver a drink if no coin has been inserted even if a
    # drink has been selected
    proposition1 = Not(And(Or(Unary("idle"),
                              Unary("coin returned")),
                           And(Unary("no drink selected"),
                               Or(Unary("tea delivered"),
                                  Or(Unary("coffee delivered"),
                                     Or(Unary("hot chocolate delivered"),
                                        Unary("tomato soup delivered")))))))

    print("\n\033[4m\033[1mFirst proposition:\033[0m")
    print("\tThe drinks vending machine cannot deliver a drink if no coin has been inserted even if a drink has been selected")

    proposition_print_test(transition_system, proposition1)

    # Second proposition: The drinks vending machine cannot deliver a drink or let select a drink if no coin has been
    # inserted.
    proposition2 = Not(And(Or(Unary("idle"),
                              Unary("coin returned")),
                           Or(Or(Unary("tea selected"),
                                 Or(Unary("coffee selected"),
                                    Or(Unary("hot chocolate selected"),
                                       Unary("tomato soup selected")))),
                              Or(Unary("tea delivered"),
                                 Or(Unary("coffee delivered"),
                                    Or(Unary("hot chocolate delivered"),
                                       Unary("tomato soup delivered")))))))

    print("\n\033[4m\033[1mSecond proposition:\033[0m")
    print("\tThe drinks vending machine cannot deliver a drink or let select a drink if no coin has been inserted")
    proposition_print_test(transition_system, proposition2)

    # Third proposition: The drinks vending machine must deliver the selected drink if a coin has been inserted and
    # a drink has been selected Must check if the selected drink is the same as the delivered drink (don't serve a
    # tea if a coffee has been selected)
    #   The proposition is too complex to be written, we will decompose it like this:
    #   -   If a coin has been inserted and a tea has been selected, the drinks vending machine must deliver a tea
    #   -   If a coin has been inserted and a coffee has been selected, the drinks vending machine must deliver a coffee
    #   -   If a coin has been inserted and a hot chocolate has been selected, the drinks vending machine must deliver
    #       a hot chocolate
    #   -   If a coin has been inserted and a tomato soup has been selected, the drinks vending machine must deliver
    #       a tomato soup
    print("\n\033[4m\033[1mThird proposition:\033[0m")
    print("\tThe drinks vending machine must deliver the selected drink if a coin has been inserted and a drink has been selected")
    print("\tMust check if the selected drink is the same as the delivered drink (don't serve a tea if a coffee has been selected")

    print("\tNote: The proposition is too complex to be written, we will decompose it like this:")
    print("\t-   Selecting a tea, the drinks vending machine must deliver a tea")
    print("\t-   Selecting a coffee, the drinks vending machine must deliver a coffee")
    print("\t-   Selecting a hot chocolate, the drinks vending machine must deliver a hot chocolate")
    print("\t-   Selecting a tomato soup, the drinks vending machine must deliver a tomato soup")
    print("\n\tEach proposition will be tested separately")

    options = ["tea", "coffee", "hot chocolate", "tomato soup"]
    proposition_tmp: Proposition
    final_proposition: Proposition

    #   For each option, we will create a proposition that must be true if the drinks vending machine must deliver
    for option in options:
        #   Copy the list of options and remove the current option
        other_options = options.copy()
        other_options.remove(option)

        proposition_tmp = Unary(f"{other_options.pop()} delivered")

        for other_option in other_options:
            proposition_tmp = Or(proposition_tmp,
                                 Unary(f"{other_option} delivered"))

        #   Now we build or final proposition
        final_proposition = Not(And(Unary("coin inserted"),
                                And(Unary(f"{option} selected"),
                                    proposition_tmp)))


        print(f"\n\t\033[4m\033[1m- {option}:\033[0m")
        print(f"\tSelected: {option}, Delivered: {option}")
        proposition_print_test(transition_system, final_proposition)


if __name__ == '__main__':

    # Need to check that Python version is >= 3.11
    # If not, print a warning message
    if sys.version_info < (3, 11):
        print("\033[93m\033[1mWARNING: You are using a version of Python that is older than 3.11, the program may not work as expected !\033[0m")

    # Print the header
    print("\033[1m==================================================")
    print("Devoir Maison n°1 - Modélisation et Vérification des Systèmes Concurrents")
    print("Auteurs:")
    print("\t-   Quentin GOMES DOS REIS")
    print("\t-   Matthéo LÉCRIVAIN")
    print("M2 ALMA - Nantes Université")
    print("2023-2024")
    print("==================================================\033[0m")

    # proposition_test()

    #   Run the subject example for the semaphores
    verify_semaphores()
    #   Run the traffic lights at a crossroad example
    verify_traffic_lights_at_crossroad_section()
    #   Run the drinks vending machine example
    verify_drinks_vending_machine()
