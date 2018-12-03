#File IO
---
<br>
<br>
<br>
<br>

In this lesson, we'll be looking at file I/O in python, along with a few file types that are particularly useful for data storage/sharing and you will almost certainly find in the wild - CSV, JSON, and XML.

In a computer system, everything is data. Any representation of any concept is data - and concepts have limited use in isolation. [Input/Output](https://docs.python.org/3/library/io.html) (I/O) allows a program to break this isolation, thus gaining vastly increased potential. I/O comes in many different varieties - file, network, device, etc. - and we've already worked with standard input/output in the form of `input()` and `print()`. But here we'll only be looking at file I/O. File I/O allows us to interact with the file system, reading data in from files and writing data out to files.

Python abstracts a lot of the complexity of file I/O away, so it's as simple as:

${file_io.py}

As you can see, we create a file object by calling `open()`. Here, we have two arguments - the first is the relative file path, and the second is the operation type ('r' = read, 'w' = write, etc.). We can then use the file, before finally closing it once we're done. Closing the file releases the allocated resources associated with file I/O. Alternatively, a `with` statement may be used to handle this process automatically - implicitly cleaning up after the with-block is finished.

${file_with.py}

Once we have the file open, we can use any variety of methods defined in the [documentation](https://docs.python.org/3/library/io.html#io.IOBase) to interact with the file (`read()`, `write()`, etc).

${file_full.py}

When it comes to file I/O for local data, there are 3 predominant file types (that I've been exposed to) - [CVS](https://en.wikipedia.org/wiki/Comma-separated_values) (comma separated values), [JSON](https://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation), and [XML](https://www.w3schools.com/xml/xml_whatis.asp) (eXtensible Markup Language). A CSV file is literally just a file with a bunch of comma-separated values. JSON is based on JavaScript objects, but has gained massive popularity - probably from its wide usage in Web APIs and its relative compactness and quick parseability compared to XML. XML is a type of Markup Language (a language that uses `<tags>` to delimit) which is slower to parse but can be more human-readable than JSON - thus making it useful for things like preference files etc. CSV files are easy enough to parse - just split on commas to get separate values - but JSON and XML are much more difficult. Thus there are libraries in all modern languages that I'm aware of for translating to and from JSON/XML. I'll point to the [JSON](https://docs.python.org/3/library/json.html) module for Python as an example.

Your challenge here is twofold:

- Create a CSV file containing all primes up to `1000` named `primes.txt`.
- Load the provided JSON file <a href="./assets/challenge_3-2.json" download>[download]</a> and sum the list within.

<div class='footer'></div>



<!-- > Introduction and importance of file I/O
> Python abstracts a lot of the complexity away
> Basic introduction to file I/O in python (try + except)
> `with` statement for file I/O

> Useful file types
	> plaintext(csv)
	> XML
	> JSON
	> etc. -->
