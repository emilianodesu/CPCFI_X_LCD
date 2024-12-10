s = input()
found_ab = False
found_ba = False

for i in range(len(s) - 1):
    if not found_ab and s[i:i+2] == "AB":
        found_ab = True
        i += 1
    elif found_ab and s[i:i+2] == "BA":
        print("YES")
        break

if not found_ab:
    for i in range(len(s) - 1):
        if not found_ba and s[i:i+2] == "BA":
            found_ba = True
            i += 1
        elif found_ba and s[i:i+2] == "AB":
            print("YES")
            break
else:
    print("NO")
