def first_question():
    name=str(input("Insert the last names and connect then with hypens"))
    name=name.replace("-","")
    out=[]
    answer=""
    for i in name:
        if i.isupper():
            out.append(i)
    print(answer.join(out))


def second_question():
    numlist=[]
    resultlist=[]
    filterlist=[]
    dupe=[]
    modulo=42
    for i in range(10):
        num=int(input("Insert a number for the list"))
        numlist.append(num)
    for b in numlist:
        newvalue=b%modulo
        resultlist.append(newvalue)
    print(resultlist)
    for z in resultlist:
        if z  not in dupe:
            filterlist.append(z)
            dupe.append(z)
    print("The variety is"+" "+str(filterlist))

def third_question():
    amount_of_games=int(input("Insert number of games you want"))
    stone_amount_list=[]
    odd_or_even_list=[]
    bob_win_amount_list=[]
    alice_win_amount_list=[]
    for i in range(amount_of_games):
        stone_amount=int(input("Insert the stone amount"))
        stone_amount_list.append(stone_amount)
    for z in stone_amount_list:
        odd_or_even=z%2
        odd_or_even_list.append(odd_or_even)
    for b in odd_or_even_list:
        if b==0:
            bob_win_amount_list.append("win")
        elif b==1:
            alice_win_amount_list.append("win")
    if len(bob_win_amount_list)>len(alice_win_amount_list):
        print("Bob win")
    elif len(alice_win_amount_list)>len(bob_win_amount_list):
        print("Alice win")
    else:
        print("Its a draw")

def fourth_question():
    ballmoves=str(input("Insert the moves which ranges in A,B,C"))
    ballmoves_list=list(ballmoves)
    a_cup=["ball"]
    b_cup=[" "]
    c_cup=[" "]
    for j in ballmoves_list:
        if j=="A":
            a_cup,b_cup=b_cup,a_cup
        elif j=="B":
            b_cup,c_cup=c_cup,b_cup
        elif j=="C":
            a_cup,c_cup=c_cup,a_cup
    if a_cup[0]=="ball":
        print("cup"+"1")
    if b_cup[0]=="ball":
        print(2)
    if c_cup[0]=="ball":
        print(3)


print("""
    ///////////////////////////////////////////////////////////////////////////////
    //              Which question answer do you want to see 1,2,3,or 4          //
    //                                                                           //
    //                                                                           //
    ///////////////////////////////////////////////////////////////////////////////
    """)


while True:

    first_input=int(input("Insert the number of the question you want here"+"="))
    if first_input==1:
        first_question()
    elif first_input==2:
        second_question()
    elif first_input==3:
        third_question()
    elif first_input==4:
        fourth_question()
    else:
        continue













