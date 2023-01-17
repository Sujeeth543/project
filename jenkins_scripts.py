import os
List1 = [4, 5, 6, 8]
List1.reverse()
print("the reverse is", List1)

List2 = [79, 34, 11, 87, 0, 29, 66, 41, 58, 99]
List2.sort()
print("the sorted list is", List2)


List3 = []
List3 = List2.copy()+ List1.copy()
print("List3 =", List3)
