def header():
    print(60*"*")


def addevennum(start,end):
    bucket =0
    for i in range(start, end+1):
        if i%2==0:
            bucket+=i
    return(bucket)
        
        
    





def main():
    header()
    s=int(input("First value:"))
    e=int(input("Second value:"))
    result=addevennum(s,e)
    print(result)
    addevennum(s, e)

main()    

