#REGEX
---
<br>
<br>
<br>
<br>

A regular expression (regex) is a wonky-looking series of characters that form a pattern. This pattern can then be used to search a string for matches. Regular expressions are not unique to Python and, regardless of which language you're using regular expressions in, the expressions are going to be (nearly) identical - so I think it's best to regard regular expressions as a separate mini-language. A regex might look something like `\w*` or `regex` or even `#(\d+)\ @\ (\d+),(\d+):\ (\d+)x(\d+)`. They can look spooky - and some of them really are - but each regex can be broken down into meaningful units which are easy to understand.

Now before we get too far into how regular expressions work and how to interpret/create them, it's worth looking at *why* we might want to use such a complex-seeming string parsing tool in the first place. Let us look at a few common string manipulations and their limitations:

${regex_strings.py}

With `string_1` and `string_2`, if we want to get rid of non-alphabetic characters to create `abcdefghij` - we can accomplish this with the basic string operation `.replace()`. But what about `string_3` where there are multiple non-alphabetic characters? We could chain together multiple `.replace()`s or use a for-loop to check each and every character but with more complex operations this route quickly becomes cumbersome. And what about `string_4`? It's a `[year-month-day hour:minute]` timestamp. It wouldn't be too unreasonable to parse it using string slices (`[:]`) - but what if this timestamp is arbitrarily positioned amongst other characters? The problem becomes much more messy. It is worth noting that I say messy and not impossible. Regular expression are not introducing some new and magical capability - they just make certain string-related problems much more manageable.

${regex_regex.py}

Here I'm showing the two main uses I have found for regular expressions - though I'm sure there are many more: the ability to match variable expressions and the ability to extract groups from within a matched pattern. I'm going to link the [re Python documentation](https://docs.python.org/3/library/re.html) and encourage you all to find external videos or websites which will do the topic much greater justice than I could (as it is a pretty complex subject) - but I'll give a brief explanation of these two concepts and, generally, how regular expressions are implemented in Python. Also, here's a [neat site](https://regex101.com/) for building and testing regular expressions.

First, I'll start off by saying that in python, regular expressions are just strings. You'll see me using the `r"<string>"` format, but this is still a string - just a [raw string](https://docs.python.org/3.7/reference/lexical_analysis.html#string-and-bytes-literals). Raw strings differ from normal strings in that the backslash `\` character which is escape character in a regular string has no special significance to Python. This is useful because regular expression strings are parsed twice - first by Python and then by the regex engine - and the backslash is an escape character in both parsers. So we'd have to use `\\` in order to get a backslash to show up to in the regex - point is, it gets confusing if you don't use raw strings to represent regular expressions.

Moving on to the first example, we define our regex pattern as `r"\d+"`. `\d` matches any sequence of digits [0-9] and the `+` matches 1 or more of the preceding pattern. So we end up matching any occurrence of one or more digits. Using `re.sub()`, we substitute all occurrences of this pattern for a blank string (effectively removing them).

In the second example, we define our regex pattern as `r"\[(\d+-\d+-\d+)\ (\d+:\d+)\]"`. In a regex, parentheses `()` are used to denote a group. Groups may be referenced individually once a match is found as I'll show in a moment - but for now, lets break that regex down: 1`\[` + 2`(\d+-\d+-\d+)` + 3`\ ` + 4`(\d+:\d+)` + 5`\]`. The `[` and `]` characters have special meaning in a regex, thus we must regex-escape them. Sub-pattern 1 `\[`, then, is a direct match for the `[` character. Same goes for 5, but with the `]` character. Sub-pattern 3 matches a space. Technically, I don't think spaces have to be escaped in a regex, but they can be and to me it makes it more visually obvious that there's a space there. Now, looking at sub-pattern 2, we can remove the parentheses and we get `\d+-\d+-\d+`. This looks familiar, right? We had a `\d+` in the first example. So this translates to one or more digits followed by a dash `-` followed by another sequence of one or more digits followed by another dash followed by a final sequence of one or more digits. Easy, right? Now sub-pattern 4 should make plenty of sense. We can then use this regex to find a match and get the groups from that match with `re.match().groups()`. Thus we are able to gather the `date` and `time` strings (our two groups).

This is a lot to absorb - especially considering that you'll need to do some external research on your own to get a better feeling for regular expressions. I'm going to encourage peer-driven effort more so than usual due to this - if you find a resource that was particularly helpful, share it with your classmates. We may end up taking multiple classes to go over this, if necessary.

For the challenge problem, I've attached <a href="./assets/bonnie.txt" download>a plaintext file</a> which documents the adventures of a bee. The document is composed of many records with the format `[time]:<x, y, z>`, where time is in seconds. When I made the file everything seemed normal but my finger slipped when I uploaded it. I'm not quite sure what happened, but I'm sure you all are bright enough to figure it out. There are multiple parts to this challenge:

- Assuming that Bonnie *(the bee, of course)* started at the coordinates `(0, 0, 0)` and at `time = 0` - find out the distance to where she ended up.
- How long did it take her to reach that destination?  
	- What was her average speed across the journey? (`speed = abs(total_distance_traveled) / total_time`)
- Bonus: ¿?¿¿??¿,   ASCII char = 7 bits



<div class='footer'></div>