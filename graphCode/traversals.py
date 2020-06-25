#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e Ingeniería de Datos
#                 Facultade de Informática
#                 Universidade da Coruña


from graph import Graph
from array_queue import ArrayQueue

def mark_visited(g):
    visited = {}
    for u in g.vertices():
        visited[u]=False
    return visited    

def DFS_recursive(g,u,visited,process):
    ''' Recorrido en profundidad a partir de un vértice (version recursiva)
    '''    
    visited[u.get_id()]=True
    process(u.get_id())
    for v in u.get_connections():
        if not visited[v.get_id()]:
            DFS_recursive(g,v,visited,process)
    

def traverse_vertex(g,u,process):
    visited = mark_visited(g)
    DFS_recursive(g,u,visited,process)

def DFSit(g,u,process):
    ''' Recorrido en profundiad a partir de un vértice (version iterativa)
    '''
    visited = mark_visited(g)
    allDfs = set()
    allDfs.add(u)
    while len(allDfs) != 0:
        v = allDfs.pop()
        if not visited[v.get_id()]:
            visited[v.get_id()]=True
            process(v.get_id())
            for w in v.get_connections():
                if not visited[w.get_id()]:
                    allDfs.add(w)
                    
def traverseAll(g,process):
    '''Recorrido en profundidad a partir de todos los vértices 
       (versión recursiva)
    '''
    visited = mark_visited(g)
    for u in g:
        if not visited[u.get_id()]:
            DFS_recursive(g,u,visited,process)
    
def traverseAllit(g,process):
    '''Recorrido en profundidad a partir de todos los vértices 
       (versión iterativa)
    '''
    visited = mark_visited(g)
    allTraverse = set()
    for u in g:
        if not visited[u.get_id()]:
            allTraverse.add(u)
        while (len(allTraverse) != 0):
            v = allTraverse.pop()
            if not visited[v.get_id()]:
                visited[v.get_id()]=True
                process(v.get_id())
                for w in v.get_connections():
                    if not visited[w.get_id()]:
                        allTraverse.add(w)
              
    
def BFS(g,u,process):
    '''Recorrido en anchura a partir de un vértice
    '''
    visited = mark_visited(g)
    q = ArrayQueue()
    q.enqueue(u)
    visited[u.get_id()]=True
    process(u)
    while not q.is_empty():
        v = q.dequeue()
        for w in v.get_connections():
            if not visited[w.get_id()]:
                visited[w.get_id()]=True
                process(w)
                q.enqueue(w)