def minion_game(string):
    string=string.upper()
    vowels="AEIOU"
    l=len(string)
    v,c=0,0
    for i in range(l):
        if string[i] in vowels:
            v=v+(l-i)
        else:
            c=c+(l-i)
    if v>c:
        print("Kevin",v)
    elif c>v:
        print("Stuart",c)
    else:
        print("Draw")

if __name__=="__main__":
    s=input("Enter string: ")
    minion_game(s)
