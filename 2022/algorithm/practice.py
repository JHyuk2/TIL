
N= 5
temp_dict = {n+1:[] for n in range(N)}
print(temp_dict, type(temp_dict))

temp_dict[1].append(set([1, 2]))
print(temp_dict[1])