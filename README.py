import random
name=input("Enter you name:")
words=["golmaal again","raaz","dangal","eye","badshah","maharaja","kabir singh","khushi","kakuda","yodha","deadpool","spiderman","time machine"]
word=random.choice(words)
for i in word:
    print("_",end=" ")
print("\n")
w=[]
for x in range(len(word)):
    w.append("_")
chances=len(word)+2
print(name,"you have",chances,"chances")
print("Hint! : Movies Name.")
c=chances
while( chances!=0 ):
    l=input("Enter one letters:")
    chances=chances-1
    if l in word:
        print("You guessed right letter\n")
        for j in range(len(word)):
            if l==word[j]:
                w[j]=l
    ww = ''.join(w)
    bb =" ".join(w)
    if word==ww:
        print(ww)
        print(name,", You won the game in",c - chances + 1,"chances\n")
        break;
    print(bb)
    if len(l)>1:
        print("you entered more then 1 letter\n",chances,"chances are left to win the match.\n")
    elif l not in word:
        print("you guessed wrong letter\n",chances,"chances are left to win the match.\n")
