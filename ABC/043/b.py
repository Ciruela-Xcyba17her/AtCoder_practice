s = input()
out = ''
for c in s:
    if c != 'B':
        out += c
    else:
        out = out[:-1]

print(out)