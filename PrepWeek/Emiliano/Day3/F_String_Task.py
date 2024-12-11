s = list(input().lower())
out = []
for i in s:
    if i not in ['a','e','i','o','u','y']:
        out.append('.'+i)
print(''.join(out))
