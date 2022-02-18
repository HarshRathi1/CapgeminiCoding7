t=int(input())
for i in range(t):
    n=int(input())
    if n<1:
        print("invalid")
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                print("Composite")
                break
        else:
            print("Prime")