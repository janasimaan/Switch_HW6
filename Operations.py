import sys

#this function checks if a string is a palindrome
def Palindrome_Check(s):
    length = len(s)
    for i in range(0, length // 2):
        if s[i] != s[length - i - 1]:  # Compare characters from the beginning and end
            return False
    return True

#this function checks if all characters are lowercase, ignoring spaces and tabs
def Lowercase_Check(s):
    for i in s:
        if i == ' ' or i == '\t':
            continue
        if not i.islower():
            return False
    return True

#this function checks if the string contains only digits
def Digit_Check(s):
    return s.isdigit()

#this function checks if the length of the string exceeds a given threshold
def Length_Check(s, threshold):
    return len(s) > threshold

#this function checks if the string is empty
def Empty_Check(s):
    return len(s) == 0

#this function exit the program
def Exit_Program():
    sys.exit(1)

# Display the menu of operations
def menu():
    print("""
        the available operations are:
        1: Palindrome_Check - check if the input is palindrome
        2: Lowercase_Check - check if all characters in the input are lowercase
        3: Digit_Check - check if all characters in the input are digits
        4: Length_Check - check if the input length is longer that threshold
        5: Empty_Check - check if the input is empty
        6: Exit_Program - exit successfully from the application
    """)

# Main function to run the application
def main():
    while True:
        menu()
        choice = int(input("Enter the number of operation: "))
        if choice >= 1 and choice <= 5:
            input_s = input("Enter an input: ")

        match choice:
            case 1:
                r = Palindrome_Check(input_s)
                print("the answer of Palindrome Check is: ", True if r else False)
            case 2:
                r = Lowercase_Check(input_s)
                print("the answer of Lowercase Check: ", True if r else False)
            case 3:
                r = Digit_Check(input_s)
                print("the answer of Digit Check: ", True if r else False)
            case 4:
                threshold = int(input("Enter a threshold value: "))
                r = Length_Check(input_s, threshold)
                print("the answer of Length Check: ", True if r else False)
            case 5:
                r = Empty_Check(input_s)
                print("the answer of Empty Check: ", True if r else False)
            case 6:
                Exit_Program()
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
