import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# v0
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# v1
# memo = {}

# for name in names_1:
#     memo[name] = name
# for name in names_2:
#     if name in memo:
#         duplicates.append(name)

# v2
# duplicates = list(set(names_1) & set(names_2))


# v3

# names_1 = ["a", "b", "c"]
# names_2 = ["a", "b", "e"]

# v4 Stretch
for i in range(len(names_1)):
    is_unique_element = names_1[i] not in names_2
    if is_unique_element:
        names_1[i] = None


duplicates = [name for name in names_1 if name is not None]


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# runtime: 4.7013099193573 seconds - Original
# runtime: 0.0035758018493652344 seconds - Using memo
# runtime: 0.002888917922973633 seconds - Using set intersection
# runtime: 1.028311014175415 seconds  - Stretch
