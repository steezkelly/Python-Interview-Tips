z = []
for x in range(1,5):
  for y in range(1,5):
    z.append(y)
  z.append([x])

print(z)

z2 = set()

for x in range(1,5):
    for y in range(1,5):
        z2.add(y)
    z2.add(x)
print(z2)
