from distutils.command.build_scripts import first_line_re



open_file = open("FinalGrades.csv")
total_a = 0
total_b = 0
total_c = 0

for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values)
    for value in values:
        if value == 'A':
            total_a += 1
        elif value == 'B':
            total_b += 1
        elif value == 'C':
            total_c += 1

print("A's:", total_a)
print("B's:", total_b)
print("C's:", total_c)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2: 5])

open_file.close()

prime_numer = float(1)

