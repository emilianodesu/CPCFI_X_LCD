"""
Problem:
You are given a string s. Your task is to determine if the given string s contains 
two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).

Input:
The only line of input contains a string s of length between 1 and 10^5 consisting 
of uppercase Latin letters.

Output:
Print "YES" if the string s contains two non-overlapping substrings "AB" and "BA", 
and "NO" otherwise.
"""

def main():
    s = input().strip()
    
    if "AB" in s and "BA" in s.replace("AB", "  ", 1):
        print("YES")
        return
    if "BA" in s and "AB" in s.replace("BA", "  ", 1):
        print("YES")
        return
    print("NO")

if __name__ == "__main__":
    main()

