from stateTree import StateTree
from state import State

def main():
    testTree = StateTree(16)
    state = State(8)
    state.setTime(100)
    state.setAltitude(200)
    state.setVelocity(300)
    state.setAcceleration(500)

    print(state)
    
#    print(testTree)

    print(testTree.get(8))

    testTree.replace(8, state)

    print(testTree.get(8))

main()
