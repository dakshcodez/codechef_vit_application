#LONG WORDS
def convert(word):
    if len(word) <= 10:  #if length of word is lesser than 10, the word remains unchanged
        return word
    else:   #concatenate the first and last element with length of word - 2 in middle
        return word[0] + str(len(word) - 2) + word[-1]  
    
# taking input

def main():
    t = int(input())
    for i in range(t):
        word = input()
        print(convert(word))

if __name__ == "__main__":
    main()