import operator

def sort_by_age(tuples_list):
    return sorted(tuples_list, key=operator.itemgetter(1)) 

#example
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Jane", 20)]

sorted_people = sort_by_age(people)
print(sorted_people)
