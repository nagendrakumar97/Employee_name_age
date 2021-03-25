l=list()
i=1
while True:
    print("\n","-"*100)
    print("*********Enter Employee {0} Details*********".format(i))
    try:
        l.append({'name':str(input("Enter your name: ")), 'Age': int(input("Enter your age: "))})
        i+=1
    except ValueError as x :
        print(x)
    
    if(input("\nTo stop Press 'q' else press any other key")== 'q'):
        print(l)
        break

print("\nNAME\t\t\t\tAGE\t\t\t")
for x in l:
    print("{0}\t\t\t\t{1}".format(x['name'],x['Age']))


   
