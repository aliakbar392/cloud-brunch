import random
r_word=["pogba","dybala"]
w_w=['a','e','i','o','u']
score=3
word=r_word[random.randint(0,len(r_word))]
w_c=' '
def gen_puzzle():
    global w_c
    w_c=word
    for w in w_c:
        if w not in w_w:
            w_c=w_c.replace(w,'_')
    print w_c

def g_input():
    global w_w
    global score
    g_word=raw_input("Enter Guess word:")
    if g_word in word:
        w_w.append(g_word)
        print"Correct"
    else:
            print"Wrong!!!"
            score=score-1

while score>0:
    gen_puzzle()
    if w_c==word and score>0:
        print"You Won"
        break
    else:
        g_input()

    if score==0:
        print"You lose"
