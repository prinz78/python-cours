


mon_dict1 = {2: "Marcher", 1: "Partir", 4: "Travailler",5:"boir"}

mon_dict2 = {2: False, 1: False, 4: False, 5:False}

dict_trie1 = {k: mon_dict1[k] for k in sorted(mon_dict1)}
dict_trie2 = {k: mon_dict2[k] for k in sorted(mon_dict2)}

print(dict_trie1)
print(dict_trie2)
mon_dict1 = {}
mon_dict2 = {}
c = 0

for i,j in dict_trie1.items():
    c += 1
    mon_dict1[c] = dict_trie1[i]
    mon_dict2[c] = dict_trie2[i]

print(mon_dict1)
print(mon_dict2)

