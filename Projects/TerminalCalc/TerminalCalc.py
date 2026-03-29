import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
operations={'+':add,'-':sub,'*':mult,'/':div}

logo=art.logo
print(logo)
flag=True
k=0
while flag:
    if k!=0:
        calcStop=input("Do you want to stop the calculation?(y/n) ")
        if calcStop=="y" or calcStop=="Y":
            flag=False
    if flag==True:
        fNumber=input("What's the first number? ")
        fNumber=float(fNumber)
        innerflag = True
        n=0
        while innerflag:
            if n!=0:
                print(fNumber)
            oper=input("+\n-\n*\n/\nPick an operation: ")
            nNumber=input("What's the next number? ")
            nNumber=float(nNumber)
            print(f"{fNumber} {oper} {nNumber} = {operations[oper](fNumber,nNumber)}")
            answer=input(f"Type y to continue calculating with {fNumber} or type n to start a new calculation ")
            if answer=="n" or answer=="N":
                innerflag=False
            n+=1
        k+=1