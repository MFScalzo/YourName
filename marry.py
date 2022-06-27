# first letter in s1, going left to right is it in s2?
# remove chars until it is
# if you run out of chars, NO

def canMarry(s1, s2):
    if (s1 in s2 or s2 in s1):
        return "YES"

    string1 = s1
    string2 = s2

    for x in range(len(s1)):
        while s1[x] != string2[x]:
            string2 = string2[0 : x :] + string2[x + 1 : :]
            
            if len(string2) <= x:
                return "NO"

    if (s1 in string2 or string2 in s1):
        return "YES"

    for x in range(len(s2)):
        while string1[x] != s2[x]:
            string1 = string1[0 : x :] + string1[x + 1 : :]

            if len(string1) <= x:
                return "NO"

    if (string1 in s2 or s2 in string1):
        return "YES"

    return "NO"

T = int(input())
A = []
for i in range(T):
    A.append(input())

for x in A:
    names = x.split()
    print(canMarry(names[0], names[1]))