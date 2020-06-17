terms = int(input("Enter the number of terms: "))
n1,n2 = 0,1
cnt = 0

if terms <=0:
    print("Enter positive number of terms")
elif terms == 1:
    print("Fibonacci series till {}st term is {}".format(terms, n1))
else:
    print("Fibonacci Series:\n")
    while cnt < terms:
        print(n1)
        n = n1 + n2 
        n1 = n2
        n2 = n
        cnt += 1      

