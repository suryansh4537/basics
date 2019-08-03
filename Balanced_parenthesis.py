from Stack_implementation import Stack


def is_match(p1,p2):
    if p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    elif p1=='(' and p2==')':
        return True
    else:
        return False

def is_balanced(string):
    s=Stack()
    check=True
    index=0
    while index<len(string) and check:
        paren=string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                check= False
            else:
                top=s.pop()
                if not is_match(top,paren):
                    check=False

        index+=1


    if s.is_empty and check:
        print("Balanced")
    else:
        print("Not Balanced")

is_balanced("({[]})")