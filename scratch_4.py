x="*"
mult=1
blank=" "
count=int(input("Insert the amount of row"))
while mult<count:
    print(blank*(count-mult)+(x*mult)+(x*(mult-1)))
    mult +=1
