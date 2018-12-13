#Hashing, Dictionaries & More
---
<br>
<br>
<br>
<br>

Chapter 11 introduces dictionaries and how they may be used - but it doesn't explain how they work under the hood. They're actually really fascinating data structures which are much better at certain tasks than other data structures like lists. What Python calls a dictionary is typically referred to as a **hashtable** or **hashmap**, named such because their implementations are dependent on hashing the input or **key** and using the resulting hash to index the **value**. What does it mean to "hash the input", though? A hash function is any function that takes data of arbitrary size and maps it to data of a fixed size. So hashing an input key will return a value of fixed size. For example:
<br><br>
`"apple" --> 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b`
<br><br>
`"orange" -> 1b4c9133da73a711322404314402765ab0d23fd362a167d6f0c65bb215113d94`
<br><br>
As you can see despite apples and oranges being different, the output values are of the same length and all random looking. This was done using the `sha256` hashing algorithm which can be found in [hashlib](https://docs.python.org/3/library/hashlib.html). There are many different types of hashing algorithms - some 'safe' for cryptographic use (infeasible to reverse) and others definitely not.

Lets get back to dictionaries, though. You can think of a dictionary as a list with indices that only it can see. And it accesses these indices using the truncated hashes of keys. For example, lets say that we have a dictionary with an internal 'list' size of `100` and lets say that we want to add `{"name": "Theodore"}` to this dictionary (pseudo-code):

${hash_dp.py}

This is incredibly useful for item-lookup and searching. Say we want to find the value associated with a certain key. We don't have to search the entire 'list' to find the key, all we have to do is hash the key and that will give us the index; this is particularly useful for larger datasets as it gives us constant-time lookup at the cost of the hash algorithm (and hash algorithms designed for this purpose can be very fast). Dictionaries are not without flaw, however. I'm sure some of you are already wondering what happens if two keys hash to the same index. This is what's called a collision, and different implementations have different collision-resolution strategies which will slow the structure down, but not by much.

Another challenge with dictionaries is that the key must be hashable. When using the `sha256` function from hashlib, the value to be hashed must be a byte literal. But general-purpose hashing in python is not implemented using any hashlib functions. Instead, each object in Python can have a `__hash__()` method. If an object implements this method, it is hashable - if it doesn't, it's not. And an object can implement the hash method however it likes - for example, integers in python simple return their value. A very low-cost hash function. Also not cryptographically sound (`hash(2)` returns `2`). And as just shown, you can get the hash of an item by calling the built-in `hash()` function.

There are other data structures that make use of hashing such as [bloom filters](https://en.wikipedia.org/wiki/Bloom_filter) and [caches](https://en.wikipedia.org/wiki/Cache_(computing)) among others. However, hashing is also used for cryptographic purposes. If a hash function is designed correctly, reversing the hash is not feasible. Thus if we hash a password before storing it, it doesn't really matter if someone gets a hold of the stored hash. Then when the user enters their password in the future, we can hash their input and check it against the stored hash. If the two hashes are equal, we can say the passwords are equal.

${hash_pass.py}

This (pseudo-code) is actually something you'll be implementing in Units 2 and 3 when working on web applications. But I thought it would be neat to introduce it here in the context of hashing in general. The challenge problem is to use a JSON file as a 'database' and create a rudimentary command-line username/password log in system (with password hashing). Maybe have it store some super secret information for users and print it out when they log in. IDK. Have fun with it.

<div class='footer'></div>