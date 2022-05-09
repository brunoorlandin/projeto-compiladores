file = open("source.rpg", "r")

line = file.readlines()

lines_split = []

lines = []

#lines.strip().split("\n")

for item in line:
  lines_split.append(item.split("\n"))

for i in range(len(lines_split)):
  if lines_split[i][0] != '':
    lines.append(lines_split[i][0])

print(lines)