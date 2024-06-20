class Graph:
    def __init__(self, vn0):
        self.Vertex_count = vn0
        self.adj_matrix = [[0]*vn0 for _ in range(vn0)]
        
    def add_edge(self, u, v, weight = 1):
        if 0<=u < self.Vertex_count and 0<= v < self.Vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def remove_eage(self, u, v):
        if 0<=u < self.Vertex_count and 0<= v < self.Vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
    def has_eage(self,u,v):
        if 0<=u < self.Vertex_count and 0<= v < self.Vertex_count:
            return self.adj_matrix[u][v] != 0
    def print_adj_matrix(self):
        for row_mat in self.adj_matrix:
            print(" ".join(map(str, row_mat)))
            
g=Graph(5) 
g.add_edge(0,1)
g.add_edge(0,2) 
g.add_edge(2,3) 
g.add_edge(0,3) 
g.add_edge(0,4)
#print(g.has_eage(1,2))
g.print_adj_matrix()
        
    
        