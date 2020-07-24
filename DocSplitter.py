# opening the text file
with open('./lit.txt', 'r') as file:
    wc = 0
    # reading each line
    for line in file:

        # reading each word
        for word in line.split():
            f = open("result.txt", "w")
            if((wc/1000).is_integer()):
                print('\n\n\n')
            # displaying the words
            print(word + ' ', end='')
            wc = wc + 1

# Use redirector to save it into a file if needed
