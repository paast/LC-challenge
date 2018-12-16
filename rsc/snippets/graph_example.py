class Node:

	def __init__(self, name):
		self.name = name
		self.edges = []

	def add_edge(self, node):
		self.edges.append(node)

	def print_edges(self):
		for node in self.edges:
			print(node.name)

	def __eq__(self, other):
		return (self.name == other.name)

# make nodes
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")

# connect nodes
node_A.add_edge(node_B)
node_A.add_edge(node_C)
node_A.print_edges()

# put them in a container if you want
graph = [node_A, node_B]