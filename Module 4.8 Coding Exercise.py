#for loops
furniture = ["table", "chair", "cabinet", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)

#while loops
i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")