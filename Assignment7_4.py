from functools import reduce
def main():
    numbers=list(map(int,input("Enter a numbers separed by space:").split()))
    product=reduce(lambda x,y:x*y,numbers)

    print("product of all nnumbers:",product)




if __name__=="__main__":
    main()