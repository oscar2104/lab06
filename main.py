def encoder(password):
    result = ''
    for i in range(0, len(password)):
        if int(password[i])+3 >=10:
            x = ((int(password[i])+3) % 10)
        else:
            x = int(password[i]) + 3
        result += str(x)

    return result
def decoder(orgStr):
    newStr = ""
    for i in orgStr:
        if int(i) - 3 < 0:
            i = str(10 + (int(i)-3)) # goes the other way and add the negative number to ten
        else:
            i = str(int(i)-3)
        newStr = newStr + i
    return newStr


def main():
    choice = 0
    var1 = ""
    password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            var1 = encoder(password)
            print("Your password has been saved and stored")
        if choice == 2:
            print(f"The encoded password is {var1}, and the original password is {password} ")
        if choice == 3:
            break



if __name__ == '__main__':
    main()