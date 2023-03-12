# Neha Bangalore
def encode(phrase):
    result=" "
    for i in phrase:
            i=int(i)+3
            if i>9:
                i-=10
            result+=str(i)
    print(result)








#def decode(phrase):
    #num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    #result = ''
    #for i in phrase:
        #i = num_list[i - 3]



def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            print('Encoded phrase is', encode(phrase))
        elif option == '3':
            print('Decoded phrase is', decode(phrase))


if __name__ == "__main__":
    main()
