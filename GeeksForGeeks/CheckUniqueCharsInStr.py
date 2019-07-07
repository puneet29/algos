# Problem Description: https://www.geeksforgeeks.org/efficiently-check-string-duplicates-without-using-additional-data-structure/


# def uniqueChars(s):
#     seen = set()
#     for char in s:
#         if(char in seen):
#             return 'No'
#         else:
#             seen.add(char)
#     return 'Yes'

def uniqueChars(s):
    return 'Yes' if len(set(s))==len(s) else 'No'


s = input()
print(uniqueChars(s))
