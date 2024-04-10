import sys

class Vertex(object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited(self):
    return self.visited

  # determine the label of the vertex
  def get_label(self):
    return self.label

  # string representation of the vertex
  def __str__(self):
    return str(self.label)


class Graph(object):
  def __init__(self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex(self, label):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index(self, label):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex(self, label):
    if (self.has_vertex(label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append(Vertex(label))

    # add a new column in the adjacency matrix
    nVert = len(self.Vertices)
    for i in range(nVert - 1):
      (self.adjMat[i]).append(0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append(0)
    self.adjMat.append(new_row)

  # Add a list of verticies  
  def add_verticies(self, list_verticies):
      for v in list_verticies:
        self.add_vertex(v)
    
    
  # add weighted directed edge to graph
  def add_directed_edge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex(self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1


  def __str__(self):
    '''
    A simple string representation of the graph in Adjancy Matrix. 
    '''
    tmp = "\nVerticies are: \n"
    for vertex in self.Vertices:
      tmp += str(vertex) + str("\n")
    
    tmp += "Adjancy Matrix is: \n"
    for i in range(len(self.adjMat)):
      tmp +="\n"
      tmp += str(self.adjMat[i])

    tmp += "\n"
    return tmp

  
  def prims_algorithm(self):
    
    # number of vertices in graph
    V = len(self.Vertices)
    
    
    # An Array to track of we select the specific vertex or not to be in the minimum spanning tree
    # selected will become true otherwise false
    selected = [False] * V
    
    # set number of edge to 0
    no_edge = 0
    
    # Select a node to start with it. 
    selected[0] = True
    edges = []
    # print for edge and weight
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        
        # Here is an implementation without priority queue (heap)
        
        # For every vertex, find the all adjacent vertices
        #, get the edge weight from the vertex selected.
        # if the vertex is already in the set S, discard it otherwise
        # choose another vertex nearest to selected vertex at the past step 
        
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and self.adjMat[i][j]):  
                        # not in selected and there is an edge
                        if minimum > self.adjMat[i][j]:
                            minimum = self.adjMat[i][j]
                            x = i
                            y = j
        print(f"{x}-{y}: {self.adjMat[x][y]}")
        edges.append((x,y))
        selected[y] = True
        no_edge += 1

    return edges

   


def main():
  # create the Graph object
  g1 = Graph()
  
  g1.add_verticies(range(7))


  g1.add_undirected_edge(0, 1, 30)
  g1.add_undirected_edge(0, 6, 10)
  g1.add_undirected_edge(1, 4, 13)
  g1.add_undirected_edge(1, 2, 15)
  g1.add_undirected_edge(2, 3, 12)
  g1.add_undirected_edge(3, 4, 16)
  g1.add_undirected_edge(3, 5, 20)
  g1.add_undirected_edge(4, 5, 21)
  g1.add_undirected_edge(5, 6, 22)
  
  
  

  

  print(g1)
  g1.prims_algorithm()


if __name__ == "__main__":
  main()
