vowels = "aoyeuiAOYEUI"
s = input().strip()
result = ""

for char in s:
    if char not in vowels:
        result += "." + char.lower()

print(result)