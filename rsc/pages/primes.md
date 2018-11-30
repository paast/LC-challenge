#TIMING CODE & PRIMES
---
<br>
<br>
<br>
<br>

In this lesson we'll look at measuring the performance of code through a few different modules. We'll also briefly mention Big O notation and its usefulness in analyzing the complexity of an algorithm. Finally, the challenge will be to take some starter code (a naive prime number generator) and have fun trying to optimize it. There is no specific end-goal, this challenge is meant to be exploratory. However, you are more than encouraged to share solutions amongst classmates and engage in some friendly competition.


The first module we'll look at is the [`time`](https://docs.python.org/3/library/time.html) module. I'll only briefly go over `time.time_ns()`, but feel free to browse the documentation for other useful features. The function time.time_ns() gives us the system time in nanoseconds since the "epoch" (Jan 1, 1970 @ 00:00:00). At the time of writing this, I get the value `1543608402547405100`. If we take the time before executing our code, take the time after, and then calculate the difference, we end up with the time it took to execute the code.

<br>

${primes_time.py}

<br>

An alternative module for timing functions is [`timeit`](https://docs.python.org/3/library/timeit.html). This one is a little more purpose-built and can be useful for dealing with some pitfalls like deviation in performance between multiple runs, etc. Feel free to investigate the documentation, and here's a snippet demonstrating the ability to run a piece of code 1000000 times:

<br>

${primes_timeit.py}

<br>

The last module that I'm going to introduce (briefly) is [`dis`](https://docs.python.org/3/library/dis.html) - it disassembles Python code into CPython bytecode. If you're interested in how this works, I'm not the one to explain in the detail - but the documentation has some interesting information. That said, the basic idea is that it allows you to see in a more accurate way what your Python code is doing. Below is an example - feel free to play around with more complex functions to get a better feel for it - though it's not necessary for what we're doing here.

<br>

${primes_dis.py}

<br>

The left column is line number, middle is the bytecode instruction, right is the opargs. Here we can see that on line 4 we do the following: `load x`, `load x` (again, for multiplication), `binary multiply` (x * x), `return value` (returning calculated value). Again this isn't key to this challenge, but it can be an interesting perspective on your code.

Anyways, for the challenge: take a function `primes(n)` that generates all primes up to `n`. Use the concepts that you've learned here to time this function and experiment with optimizing the code. Below, I'll provide a basic prime generator if you'd like somewhere to start - have fun making it better!

<br>

${primes_start.py}

<br>
<br>
<br>
<div class="error">
	WARNING:<br><br>
	hover cursor below for spoiler
</div>
<br>
<br>

${primes_solution.py+}


<div class="footer"></div>