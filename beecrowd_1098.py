i = 0
j = 0

print(f"I={i} J={j + 1}")
print(f"I={i} J={j + 2}")
print(f"I={i} J={j + 3}")

j = 0.2

while i < 1.9:
# for b in range(10):
    i += 0.2

    if i >= 0.2:
        for a in range(3):
            if int(j + (a + 1)) == (j + (a + 1)):
                print(f"I={i:.1f} J={(int(j + (a + 1))):.1f}")
            else:
                print(f"I={i:.1f} J={(j + (a + 1)):.1f}")
            
            if a == 2:
                j += 0.2

            # print(f"I={i} J={j}")
            # if j == 5:
            #     j = 8