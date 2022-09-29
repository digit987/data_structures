inp = 'ABC'
len_inp = len(inp)
perm_list = []

if len(perm_list) == 0:
    perm_list = list(inp)
for length in range(1, len_inp + 1):
    for i in perm_list:
        if len(i) == length:
            for j in inp:
                if j not in i:
                    perm_list.append(i+j)

combination_count = 0
for i in perm_list:
    if len(i) == len_inp:
        combination_count += 1
        print(i)
print("Total Permutations", combination_count)          