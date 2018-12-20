#An Introduction to Graph Theory
---
<br>
<br>
<br>
<br>

In graph theory, a graph is a set of related points defined by **nodes** and **edges**. In this context, a node is a point and an edge is a connection between two nodes. This might sound a bit abstract - and that's because it is. It's abstract in the same way that a list is abstract. But as I'm sure you've integrated lists into your problem-solving repertoire, so might you integrate this. Take, for example, a mountain path that splits and winds and goes up and down hills. You enter the path at a specific location and you wish to get to another location. Among all of the possible paths, which one is the quickest? If we represent each location (or intersection) as a node and we represent each path as an edge, we now have a structured definition of the path-system. We can add **weights** to the edges - numbers which allow us to quantify how long each path will take to travel - and in doing so we can solve problems like what the quickest route is. This is used all of the time in the real world. Route optimization (think google maps), network optimization (internet routing), fluid dynamics simulations, natural language quantification... the list goes on. Lots of applicability.

There are a few defining features of graphs that I'll introduce here as they determine the effectiveness of various implementation strategies:

- **Density:** If we take density to be `Average Edges per Node / Total Nodes`, then a graph is more dense the more connected the nodes are, and inversely more sparse the less connected the nodes are.
- **Directionality:** Up until now, we've discusses edges as being connections between nodes - as if it's an undirected relationship between the two nodes (`A -> B == B -> A`). But what if we have a one-way path? We'd need to introduce the concept of a directional graph - one where `A -> B` does not necessarily equal `B -> A`.
- **Weighted Graphs:** To solve some problems, all we need consider is the boolean connectivity - whether two nodes are connected or not. But if each edge is not the same, if we are trying to model some kind of cost associated with edges, then we have to be able to assign weights to the edges.
- **Additional Considerations:** Is every node in the graph connected? Are there any loops in the graph? Can every node get to every other node?

These are all things to think about when solving a problem using graphs. But how do we actually use graphs? They're not as simple as lists, where you can just create one using `[]` and add to it using `list.append()`. Python has already done all of the heavy lifting for you when it comes to lists, probably because a programming language is not very approachable without lists. But graphs are not so necessary. Very useful - but not a necessary building block like lists are. In order to use a graph, you're going to first have to define one. This is not easy to do but having learned about classes, you will be much better prepared. This is also the subject of this challenge. Before we dive into that, however, I'm going to briefly introduce some implementation concepts using pseudo-code (this code isn't super specific to any problem, but hopefully it illustrates one way of defining a graph):

${graph_example.py}

Your challenge is to create a graph using the following <a href="./assets/matrix.txt" download>Plain Text file</a>. In the file, you will find a grid (matrix). More specifically, you will find a series of lines, each of which is occupied by space-separated values. The number of space-separated values is the same on each line and is equal to the total number of lines (thus creating a relational matrix). A relational matrix is one possible representation of a graph (albeit an inefficient one for most scenarios) where all possible connections are given (twice). You may need to do some research on this. The graph in question happens to be unweighted, undirected, and fully connected (no disconnected nodes), where an `-` is no edge and a `0` is an edge. You can refer to the nodes by their index in the matrix (0, 1, 2, ...). (Also, it is given that all nodes connect to themselves, so a connection like `1 -> 1` can safely be ignored).

<div class='alert'>
BTW, if you want to view the plain-text file, you'll have to open it in a text editor that isn't Notepad (e.g. Visual Studio, PyCharm, notepad++, sublime, etc.). Sorry!
</div>

- Find the density of the graph
- For each node in the graph, print all of its edges
- Print all edges in the graph, but only print each edge once

<div class='footer'></div>