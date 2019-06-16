def reverse(str) :
    if not str : 
        print(str)
    chars = list(str)
    i = 0
    j = len(chars)-1;
    t = 0;
    while i < j :
        swap (chars, i, j)
        i += 1
        j -= 1
    for x in chars :
        print x
def swap (chars, i, j) :
    temp = chars[i];
    chars[i] = chars[j];
    chars[j] = temp;
