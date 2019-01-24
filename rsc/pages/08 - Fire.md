#Forest Fire
---
<br>
<br>
<br>
<br>

For this challenge, we'll be simulating a simplified forest fire using a grid 'map' and a turn-based time system. No new data structures or concepts will be explicitly introduced, but the nature of the problem will likely encourage you to seek them out.

The first part of the problem is the generation of the forest. A forest is represented by a grid, where each tile in the grid either has a tree or does not have a tree. For the sake of introducing some uniformity to your solutions, your forest generator must take into consideration 3 parameters: `width`, `height`, and `density` (density is the probability of there being a tree on any square [0.0 - 1.0]). This will also make the problem more interesting, as you will be able to fiddle with these values and observe their effects on the outcome. If `#` = tree and `_` = no tree, a map with input parameters(10, 10, 0.4) might look something like the following. 

${fire_forest.py}

You need not necessarily render it like that, but it could be very useful for testing/debugging purposes.

Second, you are to set fire to the beautiful little forest that you worked so hard on creating. While unfortunate, this will present us with a second part to the challenge. And that's what matters. Challenges.

Before you set fire to your forest, though, you should understand how fire works. Fire burns trees. Each turn, fire will spread to immediately adjacent trees (not diagonally). Fire lasts for a single turn before burning out. That's about it. That's fire. Now for the remaining challenges:

- Light a fire at a random location in your forest.
	- How long does it burn for?
	- How many trees burnt?

- Given a forest and a single well-placed starting fire:
	- What is the largest fire possible?
	- What is the longest fire duration possible?

- Bonus problems!
	- Load custom forests from an external file (this allows you to experiment with different non-random forests)
	- Render the forests and fires - this is very open-ended and I would only recommend this if you are interested in graphics. There are many ways to go about this, but I would recommend HTML.

<br>
<br>
<br>

<div class='alert'>The problems get progressively harder. I highly encourage peer-to-peer discussion, but if it proves to be a little too challenging we can discuss this as a group.</div>


<div class='footer'></div>