class Graph:
  def __init__(self, directed=False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False
  


class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def get_edge_weight(self, edge):
    return self.edges[edge]







import random
from random import randrange

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:
def visited_all_nodes(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True


def traveling_salesperson(graph):
  ts_path = ""
  visited_vertices = {x: "unvisited" for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertices[current_vertex] = "visited"
  ts_path += current_vertex 
  
  visited_all_vertices = visited_all_nodes(visited_vertices)  

  while not visited_all_vertices:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    
    # Collect the weights for each edge
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)
      
    # Find the next vertex with the minimum weight
    found_next_vertex = False
    while current_vertex_edge_weights and not found_next_vertex:
      next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
      if visited_vertices[next_vertex] == "visited":
        current_vertex_edge_weights.pop(next_vertex)  # Remove visited vertices
      else:
        found_next_vertex = True

    # If no unvisited vertices are left, break out of the loop
    if not current_vertex_edge_weights:
      visited_all_vertices = True
    else:
      current_vertex = next_vertex
      visited_vertices[current_vertex] = "visited"
      ts_path += current_vertex

    visited_all_vertices = visited_all_nodes(visited_vertices)

  return ts_path  # Return the path instead of printing it


# Testing the code
graph = build_tsp_graph(False)
print(traveling_salesperson(graph))










