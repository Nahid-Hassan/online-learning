def swap_case(s):
    res = str()
    
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                res += ch.upper()
            else:
                res += ch.lower() 
        else:
            res += ch      

    return res

if __name__ == '__main__':
    s = input()
    res = swap_case(s)
    print(res)