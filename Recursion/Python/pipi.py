def pi(text, n=0):

    if n >= len(text):
        return ''
    
    if text[n:n+2] == 'pi':
        return '3.14' + pi(text, n+2)

    return text[n] + pi(text, n+1)

print(pi(input()))