colors = ['Red', 'Blue', 'Green']

states = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

neighbors = {}
neighbors['A'] = ['B', 'C']
neighbors['B'] = ['A', 'C', 'D']
neighbors['C'] = ['A', 'B', 'D', 'E', 'F']
neighbors['D'] = ['B', 'C', 'E']
neighbors['E'] = ['C', 'D','F']
neighbors['F'] = ['C', 'E']
neighbors['G'] = ['']

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color
    return None


if __name__ == "__main__":
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)
    