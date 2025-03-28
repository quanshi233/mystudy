from pathlib import Path
path = Path('mystudy\codes\pai.txt')
contents = path.read_text()
lines = contents.splitlines()
print(len(contents))
print(len(lines))
a = 0
for line in lines:
    a += 1
    print(len(line))
    if a ==3:
        break

