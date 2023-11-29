import heapq


class Node:

    # creating the node of the tree
    def __init__(self, node_freq, symbol, left_node=None, right_node=None):
        self.freq = node_freq
        self.symbol = symbol
        self.left = left_node
        self.right = right_node
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


#create and print the tree
def print_nodes(Node, val=''):
    new_val = val + str(Node.huff)
    if Node.left:
        print_nodes(Node.left, new_val)
    if Node.right:
        print_nodes(Node.right, new_val)
    if not Node.left and not Node.right:
        print(f"{Node.symbol} -> {new_val}")


characters = ['a', 'b', 'c', 'd', 'e', 'f']
freq_values = [5, 9, 12, 13, 16, 45]

nodes = [] # empty nodes

for x in range(len(characters)):
    heapq.heappush(nodes, Node(freq_values[x], characters[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    heapq.heappush(nodes, new_node)

print_nodes(nodes[0])
