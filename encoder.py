# Neha Bangalore
def encode(phrase):
    global result
    result = " "
    for i in phrase:
            i=int(i)+3
            if i>9:
                i-=10
            result+=str(i)
    return result










def decode(phrase):
    print("The encoded password is"+encode(phrase)+" , and the original password is "+phrase+".")



def main():
    # looping menu
    coder = True
    phrase = ''
    while coder == True:

        # print menu
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
            print('Your password has been encoded and stored!')
        elif option == '2':
            decode(phrase)
        elif option == '3':
            break


if __name__ == "__main__":
    main()
