from collections import deque

def bfs_jug(a, b, c, target):
    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set([start])

    def get_next_states(state):
        x, y, z = state
        states = []

        
        states += [(a, y, z), (x, b, z), (x, y, c)]

        
        states += [(0, y, z), (x, 0, z), (x, y, 0)]

        
        pour = min(x, b - y)
        states.append((x - pour, y + pour, z))
        pour = min(x, c - z)
        states.append((x - pour, y, z + pour))

        
        pour = min(y, a - x)
        states.append((x + pour, y - pour, z))

        
        pour = min(y, c - z)
        states.append((x, y - pour, z + pour))

        
        pour = min(z, a - x)
        states.append((x + pour, y, z - pour))

        
        pour = min(z, b - y)
        states.append((x, y + pour, z - pour))

        return states

    while queue:
        state, path = queue.popleft()

        if state == target:
            return path + [state]

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None
