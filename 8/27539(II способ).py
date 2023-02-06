alph = 'БОРИС'
count = 0
for i1 in alph:
    for i2 in alph:
        for i3 in alph:
            for i4 in alph:
                for i5 in alph:
                    for i6 in alph:
                        line = i1 + i2 + i3 + i4 + i5 + i6
                        if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') <= 1:
                            count += 1
print(count)