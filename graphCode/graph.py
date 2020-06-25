#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e Ingeniería de Datos
#                 Facultade de Informática
#                 Universidade da Coruña


class Graph:
  """Representation of a simple graph using an adjacency list."""

  #------------------------- nested Vertex class -------------------------
  class Vertex:
      def __init__(self,key):
          self.id = key
          self.connectedTo = {}

      def add_neighbor(self,nbr,weight=0):
          self.connectedTo[nbr] = weight

      def __str__(self):
          return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

      def get_connections(self):
          return self.connectedTo.keys()
  
      def get_id(self):
          return self.id

      def get_weight(self,nbr):
          return self.connectedTo[nbr]
    
     #------------------------- Graph class methods -------------------------
     
  def __init__(self,directed=False):
      self.vertList = {}
      self.numVertices = 0
      self.directed = directed

  def insert_vertex(self,key):
      self.numVertices = self.numVertices + 1
      newVertex = self.Vertex(key)
      self.vertList[key] = newVertex
      return newVertex

  def insert_edge(self,f,t,weight=0):
      self.vertList[f].add_neighbor(self.vertList[t], weight)
      if not self.directed:
          self.vertList[t].add_neighbor(self.vertList[f], weight)

  def remove_vertex(self,v):
      self.numVertices = self.numVertices - 1
      self.vertList.pop(v)
      
  def remove_edge(self,u,v):
      self.vertList[u].connectedTo.pop(self.vertList.get(v))
      if not self.directed:
          self.vertList[v].connectedTo.pop(self.vertList.get(u))
        
  def get_vertex(self,u):
    return self.vertList.get(u)

  def vertices(self):
      return self.vertList.keys()

  def __iter__(self):
      return iter(self.vertList.values())
  
  def edges(self):
      result = set()       # avoid double-reporting edges of undirected graph
      for u in self.vertList:
        for w in self.vertList[u].connectedTo:
            result.add(tuple([self.vertList[u].id,w.id]))  # add edges to resulting set
      return result
 
  def vertex_count(self):
      return self.numVertices
  
  def edge_count(self):
      total = sum(len(self.vertList[v].connectedTo) for v in self.vertList)
      return total if self.directed else total // 2
      
  def degree(self, v):   
    """Return number of edges incident to vertex v in the graph.
    """
    count = 0
    for u in self.vertList:
        if v in self.vertList[u].connectedTo:
            count = count +1  
    return count

  def incident_edges(self,v):
      result = set()
      for u in self.vertList:
          if v in self.vertList[u].connectedTo:
              result.add(tuple([self.vertList[u].id,v.id]))
      return result