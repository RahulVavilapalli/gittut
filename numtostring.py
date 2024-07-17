def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    k = []
    r={"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','n'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
    n = len(digits)
    m = 0
    for i in digits:
        for j in range(len(r[i])):
            k.append("")
            m += 1
    return len(k)
dig=input()
n=letterCombinations(dig)
print(n)