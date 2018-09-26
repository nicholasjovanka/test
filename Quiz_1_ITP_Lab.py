top_list={}
new_top_list={}
mid_list={}
new_mid_list={}
bot_list={}
new_bot_list={}
top_capacity=15
mid_capacity=15
bot_capacity=15

while True:
    input1=str(input("Do you want to access the fridge y/n"))
    if input1=="n":
        break
    elif input1=="y":
        input2=str(input("Top,Mid,or Bottom"))
        if input2=="Top":
            put_or_take=str(input("Do you wanna put or take"))
            if put_or_take=="put":
                item_name=str(input("Insert item name"))
                item_volume=int(input("Insert item volume"))
                if item_volume>top_capacity:
                    print("Reinsert Value")
                    continue
                top_capacity=top_capacity-item_volume
                top_list.update({item_name:item_volume})
                for i in top_list.keys():
                    new_top_list.setdefault(i,0)
                    new_top_list[i]=new_top_list[i]+top_list.get(i)
                print(new_top_list)
            elif put_or_take=="take":
                item_name=str(input("Insert item name"))
                for b in new_top_list.keys():
                    if item_name!=b:
                        print("No item avaiable")
                        break
                item_volume=int(input("Insert item volume"))
                top_capacity=top_capacity+item_volume
                if top_capacity>15 or top_capacity<=0:
                    print("Reinsert Value")
                    continue
                top_list.update({item_name:item_volume})
                for i in top_list.keys():
                    new_top_list.setdefault(i,0)
                    new_top_list[i]=new_top_list[i]-top_list.get(i)
                print(new_top_list)
        elif input2=="Mid":
            put_or_take=str(input("Do you wanna put or take"))
            if put_or_take=="put":
                item_name=str(input("Insert item name"))
                item_volume=int(input("Insert item volume"))
                if item_volume>mid_capacity:
                    print("Reinsert Value")
                    continue
                mid_capacity=mid_capacity-item_volume
                mid_list.update({item_name:item_volume})
                for i in mid_list.keys():
                    new_mid_list.setdefault(i,0)
                    new_mid_list[i]=new_mid_list[i]+mid_list.get(i)
                print(new_mid_list)
            elif put_or_take=="take":
                item_name=str(input("Insert item name"))
                for b in new_mid_list.keys():
                    if item_name!=b:
                        print("No item avaiable")
                        break
                item_volume=int(input("Insert item volume"))
                mid_capacity=mid_capacity+item_volume
                if mid_capacity>15 or mid_capacity<=0:
                    print("Reinsert Value")
                    continue
                mid_list.update({item_name:item_volume})
                for i in mid_list.keys():
                    new_mid_list.setdefault(i,0)
                    new_mid_list[i]=new_mid_list[i]-mid_list.get(i)
                print(new_mid_list)
        elif input2=="Bottom":
            put_or_take=str(input("Do you wanna put or take"))
            if put_or_take=="put":
                item_name=str(input("Insert item name"))
                item_volume=int(input("Insert item volume"))
                if item_volume>bot_capacity:
                    print("Reinsert Value")
                    continue
                bot_capacity=bot_capacity-item_volume
                bot_list.update({item_name:item_volume})
                for i in bot_list.keys():
                    new_bot_list.setdefault(i,0)
                    new_bot_list[i]=new_bot_list[i]+bot_list.get(i)
                print(new_bot_list)
            elif put_or_take=="take":
                item_name=str(input("Insert item name"))
                for b in new_bot_list.keys():
                    if item_name!=b:
                        print("No item avaiable")
                        break
                item_volume=int(input("Insert item volume"))
                bot_capacity=bot_capacity+item_volume
                if bot_capacity>15 or bot_capacity<=0:
                    print("Reinsert Value")
                    continue
                bot_list.update({item_name:item_volume})
                for i in bot_list.keys():
                    new_bot_list.setdefault(i,0)
                    new_bot_list[i]=new_bot_list[i]-bot_list.get(i)
                print(new_bot_list)










