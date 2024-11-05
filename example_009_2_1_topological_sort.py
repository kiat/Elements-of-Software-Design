from collections import deque

def topological_sort(graph):
  """
  Performs topological sort on a directed graph using Kahn's Algorithm.
  https://en.wikipedia.org/wiki/Topological_sorting

  Parameters:
    graph: A dictionary representing the graph, where keys are nodes and values are lists of outgoing edges.

  Returns:
    A list of nodes in topological order, or None if the graph contains a cycle.
  """

  # Initialize the in-degree of each node to 0.
  in_degrees = {node: 0 for node in graph}
  for node in graph:
    for neighbor in graph[node]:
      in_degrees[neighbor] += 1

  # Initialize a queue with all nodes that have in-degree 0.
  queue = deque([node for node in graph if in_degrees[node] == 0])

  # Initialize the sorted list of nodes.
  sorted_nodes = []

  # While the queue is not empty, repeatedly remove a node from the queue, decrement the in-degrees of its neighbors, and add it to the sorted list.
  while queue:
    node = queue.popleft()
    sorted_nodes.append(node)
    for neighbor in graph[node]:
      in_degrees[neighbor] -= 1
      if in_degrees[neighbor] == 0:
        queue.append(neighbor)

  # If the sorted list of nodes does not contain all nodes in the graph, then the graph contains a cycle.
  if len(sorted_nodes) != len(graph):
    return None

  # Return the sorted list of nodes.
  return sorted_nodes


# Example run of the topological sort algorithm.
graph = {
  "A": ["B", "C"],
  "B": ["D"],
  "C": ["D"],
  "D": [],
}

sorted_nodes = topological_sort(graph)
print(sorted_nodes)  

# Output: 
# ['A', 'B', 'C', 'D']
# Other Ordering is: 
# ['A', 'C', 'B', 'D']