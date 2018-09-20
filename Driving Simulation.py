v0 = 0 #initial velocity
speedlim = 60 #speedlimit
time0 = 0 #For the distance loop

while True: #Exception Handling
    try:
        acl = int(input("Enter the desired acceleration")) #acceleration wanted by the user
        dis = int(input("Enter the desired distance")) #distance wanted by the user
        time = int(input("Enter the desired time")) #time wanted by the user
        break
    except ValueError:
        print("Please reinsert an INTEGER")



#distance function
def distance(v,a,t):
    return int(((v*t)+(0.5*a*(t**2))))

#velocity function
def velocity(v,a,t):
    return int(v+(a*t))

while time0<=time:
    print("Duration"+" "+ str(time0) + " " + " = " + ("*" * int(distance(v0,acl,time0)/10)) )
    time0 +=1

if velocity(v0,acl,time)>= speedlim:
    print ("Went over the speed  limit" + "." + " " + "Max speed was" + " " + str(velocity(v0,acl,time)) + "m/s")
else:
     print ("Did not go over the speed limit" + "." + " " + "Max speed was" + " " + str(velocity(v0,acl,time)) + "m/s")

if distance(v0,acl,time0)>=dis:
    print ("The person reached the destination" + "." + " " + "Reached" + " " + str(distance(v0,acl,time0)) + "m")
else:
     print ("The person did not reach the destination" + "." + " " + "Reached" + " " + str(distance(v0,acl,time0)) + "m")
