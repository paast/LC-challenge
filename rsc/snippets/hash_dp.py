key, value = ("name", "Theodore")

dictionary = [] * 100

khash = hash(key)

dictionary[khash % 100] = value