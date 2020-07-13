# Graphs

A *graph* is a collegtion of data represented by nodes and connections between nodes.
     - similar to trees, except connections can be from any node to any other, even forming loops.
     - all trees are graphs, but not all graphs are trees

## Components
 - *nodes of vertices*: represent objects in a data set (cities, animals, web pages)
 - *edges*: connections between verticies; can be bidirectional
 - *weight* (optional): cost to travel across an edge

## Types
 - *directed graph*: can only move on direction along edges
 - *undirected graph*: allows movement in both directions along edges
 - *cyclic graph*: edges allow you to revisit at least one vert
 - *acyclic graph*: verticies can only be visited once

## Graph Representations
 - *adjacency list*:  the graph stores a list of vertices
     - For each vertex, it stores a list of each connected vertex.
     - The vertices collection is a dictionary which lets us access each collection of edges in O(1) constant time
     - Because the edges are contained in a set we can check for the existence of edges in O(1) constant time.

 - *adjacency matrices*: represented as a two-dimensional array – a list of lists
     - With this implementation, we get the benefit of built-in edge weights. 
     - 0 denotes no relationship, but any other value that is present represents an edge label or edge weight. 
     - The drawback is that we do not have a built-in association between the vertex values and their index.





