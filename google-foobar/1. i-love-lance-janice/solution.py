
def solution(x):
    # Your code here
    letter = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([letter[25-(ord(l)-97)] if l in letter else l for l in x])

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
