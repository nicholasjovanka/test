while True:
    try:                                                                                                 #Try Box
        pascal_triangle_length=int(input("Insert the triangle height"))#To insert the triangle length
        break
    except ValueError:
        print("Reinsert Value")
firstlist=[1]#The list that contains the first value and will be used as the list that is shown on screen
for i in range(pascal_triangle_length):#To limit the amount of list printed so it will match the desired triangle height
    print(firstlist)
    containerlist=[]#A list that is only used as a temporary list to add value to the firstlist
    containerlist.append(firstlist[0])
    for i in range(len(firstlist)-1):#Used to add the value for the continuation of the middle of the pascal triangle starting from the 2nd line of the pascal triangle -
        containerlist.append(firstlist[i]+firstlist[i+1])#This line is to imitate pascal triangle where the mid value is the left value+the value to the right so this
    containerlist.append(firstlist[-1])#To put the value one to the right of the triangle in each line where it will take the value of 1 from the firstlist in the previous line)
    firstlist=containerlist#to update the firstlist value
