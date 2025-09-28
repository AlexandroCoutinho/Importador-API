"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list[-1])


peolpe_list = ["Eric", "Adil", "Jeff"]
peolpe_list[0] = "Mel"
print(peolpe_list)
print(len(peolpe_list))

print(peolpe_list[0:2])

my_list.append(1000)
my_list.insert(2, 45654)
my_list.sort()
print(my_list)