def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])



people = [("Brian", 25), ("Joel", 30), ("Jared", 22),("Aggrey", 35)]
print(sort_by_age(people))