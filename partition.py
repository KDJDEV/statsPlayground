from itertools import combinations

def partitions_into_two_sets(s):
    n = len(s)
    s = list(s)
    partitions = []
    
    for i in range(1, n // 2 + 1):
        for comb in combinations(s, i):
            subset1 = set(comb)
            subset2 = set(s) - subset1
            partitions.append((subset1, subset2))
    
    return partitions

def find_all_differences(s):
    differences = set()
    
    for a, b in combinations(s, 2):
        differences.add(abs(a - b))
    
    return differences

s = {1, 2, 3, 4}
for n in range(5,101):
    s.add(n)
    print(s)
    result = partitions_into_two_sets(s)
    for p in result:
        if (len(find_all_differences(p[0]).intersection(p[0])) == 0 and len(find_all_differences(p[1]).intersection(p[1])) == 0):
            print("Partition:", p[0], " and", p[1], " do not contain their differences")

