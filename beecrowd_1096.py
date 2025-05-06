i = -1
j = 8

for a in range(5):
    i += 2
    for b in range(3):
        j -= 1
        print(f"I={i} J={j}")
        if j == 5:
            j = 8