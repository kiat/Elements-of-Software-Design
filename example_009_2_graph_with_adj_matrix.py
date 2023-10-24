""" 
Run this python script like this 
python3  example_009_2_graph_with_adj_matrix.py < graph.txt
"""

import sys

###########################################
class Stack():
  """Stack implementation"""
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push(self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop(self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek(self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty(self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

###########################################
class Queue():
  """Queue Implementation"""
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue(self, item):
    self.queue.append(item)

  # remove an item from the beginning of the queue
  def dequeue(self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty(self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size(self):
    return (len (self.queue))

###########################################
class Vertex():
  """A single vertex of a Graph."""
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

###########################################
class Graph():
  """A Graph Class G(V, E)"""

  def __init__(self):
    """A graph has a list of vertices and a adjacency matrix"""
    self.vertices = []
    self.adj_mat = []

  
  def has_vertex(self, label):
    """Check if a vertex is already in the graph"""
    for i in range (len(self.vertices)):
      if label == (self.vertices[i]).get_label():
        return True
    return False


  def get_index(self, label):
    """Given the label get the index of a vertex"""
    for i in range(len(self.vertices)):
      if label == (self.vertices[i]).get_label():
        return i
    return -1


  def add_vertex(self, label):
    """Add a Vertex with a given label to the graph"""
    if self.has_vertex(label):
      return

    # add vertex to the list of vertices
    self.vertices.append(Vertex(label))

    # add a new column in the adjacency matrix
    nVert = len(self.vertices)
    for i in range(nVert - 1):
      (self.adj_mat[i]).append(0)

    # add a new row for the new vertex
    new_row = []
    for i in range(nVert):
      new_row.append(0)
    self.adj_mat.append(new_row)

  
  def add_directed_edge(self, start, finish, weight = 1):
    """Add weighted directed edge to graph"""
    self.adj_mat[start][finish] = weight

  def add_undirected_edge(self, start, finish, weight = 1):
    """Add weighted undirected edge to graph"""
    self.adj_mat[start][finish] = weight
    self.adj_mat[finish][start] = weight

  def get_adj_unvisited_vertex(self, v):
    """Return an unvisited vertex adjacent to vertex v (index)"""
    nVert = len (self.vertices)
    for i in range (nVert):
      if (self.adj_mat[v][i] > 0) and (not (self.vertices[i]).was_visited()):
        return i
    return -1


  def __str__(self):
    '''
    A simple string representation of the graph in Adjancy Matrix. 
    '''
    tmp = "\nVerticies are: \n"
    for vertex in self.vertices:
      tmp += str(vertex) + str("\n")
    
    tmp += "Adjancy Matrix is: \n"
    for i in range(len(self.adj_mat)):
      tmp +="\n"
      tmp += str(self.adj_mat[i])

    tmp += "\n"
    return tmp

  ###########################################


  def dfs(self, v):
    '''
    Do a Depth First Search in a given Graph. 
    '''

    # create the Stack
    the_stack = Stack()

    # mark the vertex v as visited and push it on the Stack
    (self.vertices[v]).visited = True

    print(self.vertices[v])
    

    the_stack.push(v)
    time_counter = 1
    
    finish_times = dict()
    finish_times[v] = time_counter


    # visit all the other vertices according to depth
    while(not the_stack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex(the_stack.peek())     
      time_counter += 1   
      
      if u == -1:
        u = the_stack.pop()
        time_counter += 1
      else:
        (self.vertices[u]).visited = True
        print(self.vertices[u]) # output this vertext. 
        # Add the finishing time for this vertex. 
        finish_times[u] = time_counter        
        the_stack.push(u)
    
    # the stack is empty, let us rest the flags
    for i in range(len(self.vertices)):
      (self.vertices[i]).visited = False
    
    print(finish_times)


###########################################

  def bfs(self, start):
    '''
    Do the breadth first search in a graph
    '''
    level_counter = 1
    # create the Queue to do FIFO
    frontier = Queue()

    level = dict()

    # add the start vertext into the queue
    frontier.enqueue(start)
    # set the level of start point
    level[start] = 0

    # While frontier is not empty open level by level. 
    while not frontier.is_empty():
      s = frontier.dequeue()
      
      # mark the vertex v as visited and push it on the Stack
      (self.vertices[s]).visited = True
      print(self.vertices[s])

      next_nodes = [i for i, e in enumerate(self.adj_mat[s]) if e != 0]

      for vertex in next_nodes:
        if not self.vertices[vertex].visited:
          (self.vertices[vertex]).visited = True
          frontier.enqueue(vertex)
          level[vertex]=level_counter
      
      level_counter += 1

    print(level)


    
    
def main():
  """A main function to create a graph of cities."""
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int(line)
  print("Number of vertices is: ", num_vertices)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex(city)
    print("added vertex: ", city)


  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  print("Number of edges is: ", num_edges)

  print(cities)

  # # read each edge and place it in the adjacency matrix
  for i in range(num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()

    start = int(edge[0])
    finish = int(edge[1])
    weight = int(edge[2])
    print("Create an edge from " + str(start) + " to " + str(finish) + " with weight of " + str(weight))


    cities.add_directed_edge(start, finish, weight)

  print(cities)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  # do the depth first search
  print ("Depth First Search")
  cities.dfs(start_index)
  print()

  print ("Breath First Search")
  cities.bfs(start_index)
  print()

if __name__ == "__main__":
  main()
