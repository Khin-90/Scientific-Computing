start = 5
diff = 3
terms = 8

sequence = []

for i in range(terms):
    term = start + i * diff
    sequence.append(term)

print("Arithmetic sequence:", sequence)
