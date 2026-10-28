languages_one = ["Python", "Ruby", "C++", "HTML"]
languages_two = ["Java", "Python", "HTML", "Rust"]

set_one = set(languages_one)
set_two = set(languages_two)

print(set_one.union(set_two))
print(set_one.intersection(set_two))
print(set_one.difference(set_two))
