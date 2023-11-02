
#   This file contains the State class which represents a state in a transition system
#   which will be used in TransitionSystem.py

class State:

    # Attributes
    #   Stores the labels of the state
    labels: list[str] = []
    #   Stores the labels of the state
    #       Note: This is a list of State objects but noted as a list of 'State'
    #               objects because Python does not support cyclic imports
    next_states: list['State'] = []

    # Constructor
    def __init__(self, labels: list[str], next_states: list['State'] = []):
        self.labels = labels
        self.next_states = next_states

    # Define getters for the attributes
    def get_labels(self) -> list[str]:
        return self.labels

    def get_next_states(self) -> list['State']:
        return self.next_states

    # Define setters only for the next_states attribute
    # because the labels of a state should not change
    def set_next_states(self, next_states: list['State']):
        self.next_states = next_states

    # Get the string representation of the state
    #  Which is just the labels of the state and the labels of the next states
    def __str__(self) -> str:
        result = f"State: {self.get_labels()}\n"
        result += "Next states:\n"
        for state in self.get_next_states():
            result += f"\t{state.get_labels()}\n"
