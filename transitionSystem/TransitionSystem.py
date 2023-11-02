from transitionSystem.State import State


#   This file contains the TransitionSystem class which represents a transition system
#   which will be used in order to implement assessment algorithm easily

class TransitionSystem:

    # Attributes
    #   Stores the initial states of the transition system
    initial_states: list[State] = []

    # Constructor
    def __init__(self, initial_states: list[State]):
        self.initial_states = initial_states

    # Define getters for the initial_states attribute
    def get_initial_states(self) -> list[State]:
        return self.initial_states

    # Define a method to add a new initial state to our transition system
    def add_initial_state(self, initial_state: State):
        self.initial_states.append(initial_state)

    # Get the string representation of the transition system
    #  Which is just the labels of the initial states
    def __str__(self) -> str:
        result = "Initial states:\n"
        for state in self.get_initial_states():
            result += f"\t{state.get_labels()}\n"
        return result
