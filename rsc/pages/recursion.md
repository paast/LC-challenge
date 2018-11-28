#RECURSION
---
<br>
<br>
<br>
<br>

[One of the bonus missions](https://runestone.launchcode.org/runestone/static/thinkcspy/Studios/wagon-wheel.html#bonus-missions) for the Wagon Wheel studio was to generate the **nth** number of the Fibonacci sequence. If you happened to do this problem, you would likely have used a for-loop or while-loop to solve it. This happens to work fine for the Fibonacci sequence problem, but other problems cannot be solved using a single loop (or any well-defined amount of loops). Thus, we are going to investigate an alternate strategy for writing algorithms: **recursion**. In order to understand recursion, you must first understand recursion.

<br>

![?](https://i.redd.it/rsspb061xgz01.jpg "pooh-cursion")

<br>
<br>

In programming, recursion is often utilized by having a function call itself to solve a self-similar sub-set of the original problem. For example, say we want to print each item in a list - that's easy, we just use a for-loop:

<br>

${recursion_for-loop.py}

<br>

But what if that list can have more lists inside of it? And those lists have yet more lists inside of them? What if we don't know how many lists are nested inside of each other? There's no way to deal with this sort of problem using a single for-loop. However, the following code illustrates how a recursive function can handle this situation gracefully:

<br>

${recursion_recursion.py}

<br>

As you can see here, each time we encounter a list within a list, we recursively call our function again. Your challenge, should you accept it, is to use recursion to solve the Fibonacci sequence problem from the Wagon Wheel studio.

<br>
<br>
<br>
<div class="error">
	WARNING:<br><br>
	hover cursor below for spoiler
</div>
<br>
<br>

${recursion_solution.py+}


<div class="footer"></div>