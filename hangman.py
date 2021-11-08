import random
player = input("Enter the player's name ")
print("-----------------------------")
print("Welcome to the game "+player)
print("-----------------------------")

print("Choose a topic\n1)Movies\n2)Cities\n3)Fruits\n4)Flowers\n")
topic = int(input())
if topic==1:
    list=["titanic", "up", "aladdin", "ratatouille", "batman", "inception",  "alien", "superman", "shrek", "ghostbusters"]
elif topic==2:
    list=["mumbai", "delhi", "bangalore", "hyderabad", "chennai", "surat", "kolkata", "pune", "kanpur", "thane"]
elif topic==3:
    list=["apple", "banana", "orange", "mango", "guava", "cherry", "durian", "grapes", "jackfruit", "kiwi"]
elif topic==4:
    list=["rose", "lily", "orchid", "tulip", "daffodil", "poppy", "sunflower", "daisy", "jasmine", "lotus"]
else:
    print("not a valid option")

def hangman():
    word=random.choice(list)
    chances=10
    guessmade=''

    while len(word)>0:
        main=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main=main+'_'+' '
        
        if main==word:
            print(word)
            print("Congratulations.. you win!!")
            break

        print(main)
        guess= input("guess the word\n")
        guess=guess.lower()
        
        if guess.isalpha()==True:
            guessmade+=guess
        else:
            print("enter a valid character\n")
            guess=input()

        if guess not in word:
            chances-=1
            if chances==9:
                print("9 chances left")
                print(" __________ ")

            if chances==8:
                print("8 chances left")
                print(" __________ ")
                print("      O     ")

            if chances==7:
                print("7 chances left")
                print(" __________ ")
                print("      O     ")
                print("      |     ")
           
            if chances==6:
                print("6 chances left")
                print(" __________ ")
                print("      O     ")
                print("      |     ")
                print("     /      ")
            
            if chances==5:
                print("5 chances left")
                print(" __________ ")
                print("      O     ")
                print("      |     ")
                print("     /\     ")

            if chances==4:
                print("4 chances left")
                print(" __________ ")
                print("     \O     ")
                print("      |     ")
                print("     /\     ")

            if chances==3:
                print("3 chances left")
                print(" __________ ")
                print("     \O/    ")
                print("      |     ")
                print("     /\     ")

            if chances==2:
                print("2 chances left")
                print(" __________ ")
                print("     \O/ | ")
                print("      |     ")
                print("     /\     ")

            if chances==1:
                print("only 1 chance left")
                print(" __________ ")
                print("     \O/__| ")
                print("      |     ")
                print("     /\     ")
            
            if chances==0:
                print("You lose!!")
                print(" __________ ")
                print("      O__|  ")
                print("     /|\    ")
                print("     /\     ")
                break
            
print("try to guess the word in less than 10 attempts")
hangman()





