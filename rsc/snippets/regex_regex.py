import re

# 1 - Variable Pattern Matching
string_3 = "abc1defg23hij4"
regex = r"\d+"
x = re.sub(regex, "", string_3)
print(x)

# 2 - Grouping Sub-Patterns
string_4 = "[2018-12-06 19:45]"
regex = r"\[(\d+-\d+-\d+)\ (\d+:\d+)\]"
date, time = re.match(regex, string_4).groups()
print(date, time)
