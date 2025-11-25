filename = "test.txt"
with open(filename, 'w') as outfile:
    outfile.writelines(f"{i}\n" for i in range(0, 51, 10))

with open(filename) as infile:
    for line in infile:
        print(line.strip())
