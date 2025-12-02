result = 0;

with open("input", "r") as f:
    line = f.readline()
    for ids in line.strip().split(','):
        left, right = (int(x) for x in ids.split('-'))
        for n in range(left, right + 1):
            idnum = str(n)
            mid = len(idnum) // 2
            l = idnum[:mid]
            r = idnum[mid:]
            if l == r:
                result += n

print(result)