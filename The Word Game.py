import random
word_list = ["advertise"]
chosen_word= random.choice(word_list)
num=len(chosen_word)
display=[]
for i in range(num):
    display.append("_")

rem_lives=["_0_","_1_","_2_","_3_","_4_","_5_",]

end=False
lives=6
while not end and lives>0:
    guess=input("enter the letter\n").lower()

    if guess not in chosen_word:
         print("not in word there") 
    else: 
        if guess in display :
                print("guessed again")
            

    for i in range(num):
        j= chosen_word[i]
        if guess==j:
            display[i]=guess   
            
    if guess not in chosen_word:
            print(f"lives remaining{rem_lives[lives-1]}")
            lives=lives-1

   

    print(f"{' '.join(display)}")

    if lives==0:
        print("you lose")

    if "_" not in display:
        end= True
        print("you win")