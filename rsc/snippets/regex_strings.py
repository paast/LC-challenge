
# 1 - Variable Pattern Matching
string_1 = "abc defg hij "
a = string_1.replace(' ', '') # cool

string_2 = "abc1defg1hij1"
b = string_1.replace('1', '') # cool

string_3 = "abc1defg23hij4"
c = string_1.replace('1', '').replace('2', '').replace('3', '') # not cool

# 2 - Grouping Sub-Patterns
string_4 = "[2018-12-06 19:45]"
time = # ???
