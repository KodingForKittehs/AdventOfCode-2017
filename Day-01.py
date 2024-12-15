# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
inp = "input"

def file_as_grid(file, ctype=str):
    with open(file, encoding="utf-8") as f:
        return list(list(ctype(c) for c in line.strip()) for line in f.readlines())

line = file_as_grid(inp)[0]

p1 = 0
for i, c in enumerate(line):
    j = (i + 1) % len(line)
    if line[i] == line[j]:
        p1 += int(line[i])

print(f"P1: {p1}")

p2 = 0
for i, c in enumerate(line):
    j = (i + len(line)//2) % len(line)
    if line[i] == line[j]:
        p2 += int(line[i])

print(f"P2: {p2}")
