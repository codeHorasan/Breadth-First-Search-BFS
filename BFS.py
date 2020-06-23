#@author: UgurHorasan
#Breadth First Search(BFS) algorithm on unweighted graphs starting from the smallest element
from queue import Queue

class Node():
    def __init__(self, name):
        self.name = name
        self.neigh = []
        self.visited = False
        self.prev = None

class Graph():
    def __init__(self, edge_list):
        self.edge_list = edge_list
        self.create_nodes()
        self.create_edges()
    def create_nodes(self):
        self.node_names = list(set([s for s,t in self.edge_list] + [t for s,t in self.edge_list]))
        self.nodes = {n: Node(n) for n in self.node_names}
    def create_edges(self):
        for edge in self.edge_list:
            self.add_edge(edge)
    def add_edge(self, edge):
        s,t = edge
        self.nodes[s].neigh.append(self.nodes[t])

edge_list = (['A','B'],['A','S'],['S','C'],['C','D'],['S','G'],['C','E'],['C','F'],['F','G'],['E','H'],['G','H'])
edge_list2 = ([1,4],[1,3],[1,2],[2,5],[3,5],[4,6],[5,6])
edge_list3 = (['A','B'],['B','C'],['C','D'],['A','C'])
graph = Graph(edge_list)
graph2 = Graph(edge_list2)
graph3 = Graph(edge_list3)

class BFS():
    def __init__(self,graph):
        self.graph = graph
        self.traversal_list = []
        self.q = Queue()
        self.initial_act()
        self.main_function()
    def initial_act(self):
        lis = list(self.graph.node_names)
        lis.sort()
        first = lis[0]
        self.traverse(self.graph.nodes[first])
    def main_function(self):
        while self.q.empty() == False:
            taken = self.q.get()
            list_of_nodes = [node for node in self.graph.nodes[taken].neigh if node.visited == False]
            for i in list_of_nodes:
                self.traverse(i)
    def traverse(self,t):
        self.q.put(t.name)
        self.graph.nodes[t.name].visited = True
        self.traversal_list.append(t.name)

#bfs1 = BFS(graph)
#bfs2 = BFS(graph2)
#bfs3 = BFS(graph3)
#print(bfs3.traversal_list)
#print(bfs1.traversal_list)
#print(bfs2.traversal_list)

#------------Shortest Path-----------

class shortest_BFS():
    def __init__(self, graph,v_name):
        self.graph = graph
        self.v_name = v_name
        self.traversal_list = []
        self.shortest_path = []
        self.q = Queue()
        self.initial_act()
        self.main_function()
        self.find_sho(self.v_name)
        self.shortest_path = self.shortest_path[::-1]
    def initial_act(self):
        self.shortest_path.append(self.v_name)
        lis = list(self.graph.node_names)
        lis.sort()
        first = lis[0]
        self.traverse(self.graph.nodes[first])
    def main_function(self):
        while self.q.empty() == False:
            taken = self.q.get()
            list_of_nodes = [node for node in self.graph.nodes[taken].neigh if node.visited == False]
            for i in list_of_nodes:
                self.graph.nodes[i.name].prev = self.graph.nodes[taken]
                self.traverse(self.graph.nodes[i.name])
    def traverse(self, t):
        self.q.put(t.name)
        self.graph.nodes[t.name].visited = True
        self.traversal_list.append(t.name)
    def find_sho(self,vertex_name):
        if self.graph.nodes[vertex_name].prev != None:
            self.shortest_path.append(self.graph.nodes[vertex_name].prev.name)
            self.find_sho(self.graph.nodes[vertex_name].prev.name)


bfs_sho = shortest_BFS(graph,'E')
print(bfs_sho.traversal_list)
print(bfs_sho.shortest_path)
print("------------------------------------------------------")
bfs_sho2 = shortest_BFS(graph3,'D')
print(bfs_sho2.traversal_list)
print(bfs_sho2.shortest_path)