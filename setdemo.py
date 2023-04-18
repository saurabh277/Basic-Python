#unordered and unchangeble
import os
cities1 = {"pune", "dehradun", "jaipur","rajasthan"}

cities2 = {"chennai", "kerala","pune","jammu"}
print(cities1.intersection(cities2))

cities2.add("assam")
print(cities2)
cities1.remove("jaipur")
print(cities1)

#dictionary

marks = {"saurabh":30, "messi":21 ,"ronaldo" :5}
print((marks["mess i"]))