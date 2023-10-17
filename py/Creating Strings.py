s = set()

def permutate(prefix, sufix):
    if len(prefix)==0:
        s.add(sufix)
        return
    for i in range(len(prefix)):
        permutate(prefix[0:i]+prefix[i+1:], prefix[i]+sufix)
        # permutate(prefix+sufix[i], sufix[0: i]+sufix[i+1: ])

permutate(input(), '')
print(len(s))
print(*sorted(s), sep='\n')
