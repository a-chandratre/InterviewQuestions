def anagram(s1, s2) :
    chars1 = list(s1.lower())
    chars2 = list(s2.lower())
    len1 = len(chars1)
    anagram = True
    if len1 != len(chars2) :
        anagram = False
    else :
        sort(chars1, chars2)
    for x in range(len1):
        if (chars1[x] != chars2[x]) :
            anagram = False
             
    return anagram

def sort(chars1, chars2) :
    len1 = len(chars1)
    for i in range(len1) :
        for j in range(1, len1-i) :
            if chars1[j-1] < chars1[j] :
                (chars1[j-1], chars1[j]) = (chars1[j], chars1[j-1])
            if chars2[j-1] < chars2[j] :
                (chars2[j-1], chars2[j]) = (chars2[j], chars2[j-1])

if anagram("Silent", "Listen") == True :
    print("This is an anagram")
else : 
    print("This is not an anagram")

