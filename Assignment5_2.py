def main():
    print("Enter a single character:")
    char=input()
    if char in ('a', 'e', 'i', 'o', 'u'):
        print("Character is a vowel")
    else:
        print("Character is a consonant")



if __name__=="__main__":
    main()