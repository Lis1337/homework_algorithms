with open('input.txt') as f:
    n = f.readline()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k = 0

def alpha(n, k):
    if n == alphabet[k]:
        return n
    return alphabet[k] + ' ' + alpha(n, k+1)

print(alpha(n, k))