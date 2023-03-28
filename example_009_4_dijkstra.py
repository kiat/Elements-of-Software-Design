from collections import defaultdict
import heapq as heap

def dijkstra(graph, start_node):
    
    visited = set() # A list to mark visited nodes. 
    parent_map = {} # A list to store parent of each node 
    pq = [] # A list as a priority queue 


    node_distances = defaultdict(lambda: float('inf')) # Initial all node distances to infinity 
    node_distances[start_node] = 0


    heap.heappush(pq, (0, start_node))

    while pq:
        # We search greedily by always extending the shorter cost nodes first	
        _, node = heap.heappop(pq)

        visited.add(node)

        for adj_node, weight in graph[node]:


            if adj_node in visited: # already visited.
                continue

            new_distance = node_distances[node] + weight 

            # If the current node distance is larger then replace it.
            if node_distances[adj_node] > new_distance:

                parent_map[adj_node] = node # set the so far current parent node 
                node_distances[adj_node] = new_distance # set the so far current distance. 

                # Add the node to the priority queue 
                heap.heappush(pq, (new_distance, adj_node))

    return parent_map, node_distances


def main():
  graph = defaultdict()

# We generate an Adjacency List
  graph[0] = [(1,11), (2, 5)]
  graph[1] = [(3, 2)] 
  graph[2] = [(1, 4), (3, 6)]
  graph[3] = []


  parent_map, node_distances = dijkstra(graph, 0)

  print(node_distances)

  print(parent_map)




if __name__ == "__main__":
  main()


