from proposition.Proposition import Proposition
from transitionSystem.State import State
from transitionSystem.TransitionSystem import TransitionSystem


#   This file contains the implementation of the algorithm given in the subject

#   This procedure "visit" is based on the pseudocode given in the paper
#   Note: In the paper, the procedure "visit" only have 1 parameter which is State s
#           But in this implementation, for the sake of simplicity, we will use 5 parameters
def visit(u: list[State], _r: set[State], _s: State, _b: bool, phi: Proposition) -> tuple[
    list[State], set[State], bool]:
    # push(s, U)
    u.insert(-1, _s)
    # R <- R U {s}
    _r.add(_s)

    # while U is not empty do
    # Emulate a do-while loop
    while True:
        # s <- top(U)
        s_prime = u[-1]
        # If Post(s') strictly contains R then
        s_prime_next_states_set = set(s_prime.get_next_states())
        if s_prime_next_states_set.issubset(_r) is False:
            # Pop(U)
            u.pop()
            # b <- b AND s' |= phi
            _b = _b and phi.eval(s_prime.get_labels())
        # Else
        else:
            # Choose s'' in Post(s') \ R
            s_double_prime = s_prime_next_states_set.difference(_r).pop()
            # Push(s'', U)
            u.insert(-1, s_double_prime)
            # R <- R U {s''}
            _r.add(s_double_prime)
        # if U is empty then
        if len(u) == 0:
            # break
            break

    return u, _r, _b


#   This procedure "verify" is based on the pseudocode given in the paper
def verify(transition_system: TransitionSystem, proposition: Proposition) -> tuple[bool, list[State]]:
    # R <- {}
    r: set[State] = set()
    # U <- {}
    u: list[State] = []
    # b <- True
    b: bool = True

    i = set(transition_system.get_initial_states())

    # while I \ R is not empty AND b is True do
    while i.difference(r) and b:
        # Choose s in I \ R
        s = i.difference(r).pop()
        # U, R, b <- visit(U, R, s, b, phi)
        u, r, b = visit(u, r, s, b, proposition)

    # if b is True then
    if b:
        # return True
        return b, []

    return b, u
