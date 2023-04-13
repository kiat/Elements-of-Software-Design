class Graph:
# A simple representation of a weighted graph

    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # A Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A Simple union Function 
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.no_vertices):
            parent.append(node)
            rank.append(0)
        
        while e < self.no_vertices - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
                
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))
        
        return result



  
  
def main():
  # create the Graph object
  g1 = Graph(7)


  g1.add_edge(0, 1, 30)
  g1.add_edge(0, 6, 10)
  g1.add_edge(1, 4, 13)
  g1.add_edge(1, 2, 15)
  g1.add_edge(2, 3, 12)
  g1.add_edge(3, 4, 16)
  g1.add_edge(3, 5, 20)
  g1.add_edge(4, 5, 21)
  g1.add_edge(5, 6, 22)
  

  

  print(g1.edges)
  g1.kruskal_algo()


if __name__ == "__main__":
  main()
