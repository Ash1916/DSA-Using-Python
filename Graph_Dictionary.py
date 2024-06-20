class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {v:[] for v in range(vertex_count)}
        
    def add_edge(self, u, v, weight = 1):
        if 0<=u < self.vertex_count and 0<= v < self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else: 
            print("Invalid vertices")
    def remove_eage(self, u, v):
        if 0<=u < self.vertex_count and 0<= v < self.vertex_count:
            self.adj_list[u] = [(vertex,weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex,weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else: 
            print("Invalid vertices")
            
    def has_eage(self,u,v):
        if 0<=u < self.vertex_count and 0<= v < self.vertex_count:
            return any(vertex == v for vertex, x in self.adj_list[u])
        else: 
            print("Invalid vertices")
    def print_adj_matrix(self):
        for vertex,n in self.adj_list.items():
            print("v",vertex,":", n)
        
g=Graph(5) 
'''
g.add_edge(0,1)
g.add_edge(0,2) 
g.add_edge(2,3) 
g.add_edge(0,3) 
g.add_edge(0,4)
'''
g.add_edge(0,1) 
g.add_edge(1,2) 
g.add_edge(1,3) 
g.add_edge(2,3) 
g.add_edge(3,4)
#g.remove_eage(3,4)
#print(g.has_eage(1,2))
g.print_adj_matrix()
        
            
        