list1 = [9, 10, 8, 12, 6, 12, ]
list1.sort()
list1 = list(dict.fromkeys(list1))
print("spordivõistluse tulemused paremuselt teise tulemuselt:", list1[-2])
