def main():
    
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

   
    area = length * width
    perimeter = 2 * (length + width)

  
    print("Area of the rectangle:" ,area)
    print("Perimeter of the rectangle:", perimeter)

if __name__ == "__main__":
    main()
