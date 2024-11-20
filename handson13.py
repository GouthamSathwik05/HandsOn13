# -*- coding: utf-8 -*-
"""HandsOn13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C9gUXenNtJTMhANbdMfJntbRb1CT421S
"""

from collections import deque
def topological_sort(graph):
  in_degree={node: 0 for node in graph}
  for node in graph:
    for neighbor in graph[node]:
      in_degree[neighbor]+=1
  queue=deque([node for node in graph if in_degree[node]==0])
  top_order=[]
  while queue:
    node=queue.popleft()
    top_order.append(node)
    for neighbor in graph[node]:
      in_degree[neighbor]-=1
      if in_degree[neighbor]==0:
        queue.append(neighbor)
  if len(top_order)==len(graph):
    return top_order
  else:
    return "Graph has a cycle!"

graph = {'A': ['B'], 'B': ['C'], 'C': [], 'D': ['C']}
print(topological_sort(graph))

def dfs(graph, start, visited=None):
  if visited is None:
    visited=set()
  visited.add(start)
  print(start, end=' ')
  for neighbor in graph[start]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited)

graph={'A': ['B'], 'B': ['C'], 'C': [], 'D': ['C']}
dfs(graph, 'A')

class DisjointSet:
  def __init__(self, n):
    self.parent=list(range(n))
    self.rank=[0]*n
  def find(self, u):
    if self.parent[u]!=u:
      self.parent[u]=self.find(self.parent[u])
    return self.parent[u]
  def union(self, u, v):
    root_u=self.find(u)
    root_v=self.find(v)
    if root_u!=root_v:
      if self.rank[root_u]>self.rank[root_v]:
        self.parent[root_v]=root_u
      elif self.rank[root_u]<self.rank[root_v]:
        self.parent[root_u]=root_v
      else:
        self.parent[root_v]=root_u
        self.rank[root_u]+=1
      return True
    return False

def kruskal(n, edges):
  edges.sort(key=lambda x: x[2])
  disjoint_set=DisjointSet(n)
  mst=[]
  for u, v, weight in edges:
    if disjoint_set.union(u, v):
      mst.append((u, v, weight))
  return mst

edges=[(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
n=4
mst=kruskal(n, edges)
print(mst)