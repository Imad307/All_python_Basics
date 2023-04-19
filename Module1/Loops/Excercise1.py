def check_balance(brackets):
    lentin= len(brackets)
    if (brackets[0]=='[' and brackets[lentin-1]==']'):
        for i in range (0, (lentin/2)-1):
            if (brackets[i]=='[' and brackets[lentin-i+1]==']'):
                continue
            else:
                print("Not Balanced according to [[[]]]")
    elif (brackets[0]=='[' and brackets[1]==']'):
        for i in range (0, lentin-1):
            if (brackets[i]=='[' and brackets[i+1]==']'):
                continue
            else:
                print("Not Balanced according to [][][]")
brackets="[][][]"
check_balance("[][][]")
print(brackets[0])