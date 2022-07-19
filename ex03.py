###################################
#dictionary

d = {"야구": 5, "축구":11, "농구": 9}
keys = d.keys()
print(keys)
print(type(keys))

values = d.values()
print(values)
print(type(values))

print(len(d))

d = {"야구": 5, "축구":11, "농구": 9}
keys = d.keys()
print(keys)

for key in keys:
    print(key,d[key])
