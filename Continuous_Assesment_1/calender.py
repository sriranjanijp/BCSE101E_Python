import random
year = random.randint(1900,2999)
j = random.randint(1,7)
print(f"{'Calender of Year '+str(year) :^35}")
print()
for month in range(1,13,1):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif (month==2):
        if(year%4==0):
            days = 29
        else:
            days = 28
    else:
        days = 30
    if (month==1):
        print(f"{'January':^35}")
    elif(month==2):
        print(f"{'February':^35}")
    elif(month==3):
        print(f"{'March':^35}")
    elif(month==4):
        print(f"{'April':^35}")
    elif(month==5):
        print(f"{'May':^35}")
    elif(month==6):
        print(f"{'June':^35}")
    elif(month==7):
        print(f"{'July':^35}")
    elif(month==8):
        print(f"{'August':^35}")
    elif(month==9):
        print(f"{'September':^35}")
    elif(month==10):
        print(f"{'October':^35}")
    elif(month==11):
        print(f"{'November':^35}")
    else:
        print(f"{'December':^35}")
    print("-" * 35)
    print(f"{'Sun':^5}{'Mon':^5}{'Tue':^5}{'Wed':^5}{'Thu':^5}{'Fri':^5}{'Sat':^5}")
    if(j == 7):
        print(f"{' ':^5}{' ':^5}{' ':^5}{' ':^5}{' ':^5}{' ':^5}{'1':^5}")
        i = 2
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    elif(j==6):
        print(f"{' ':^5}{' ':^5}{' ':^5}{' ':^5}{' ':^5}{'1':^5}{'2':^5}")
        i = 3
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    elif(j==5):
        print(f"{' ':^5}{' ':^5}{' ':^5}{' ':^5}{'1':^5}{'2':^5}{'3':^5}")
        i = 4
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    elif(j==4):
        print(f"{' ':^5}{' ':^5}{' ':^5}{'1':^5}{'2':^5}{'3':^5}{'4':^5}")
        i = 5
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    elif(j==3):
        print(f"{' ':^5}{' ':^5}{'1':^5}{'2':^5}{'3':^5}{'4':^5}{'5':^5}")
        i = 6
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    elif(j==2):
        print(f"{' ':^5}{'1':^5}{'2':^5}{'3':^5}{'4':^5}{'5':^5}{'6':^5}")
        i = 7
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    else:
        print(f"{'1':^5}{'2':^5}{'3':^5}{'4':^5}{'5':^5}{'6':^5}{'7':^5}")
        i = 8
        j = 0
        while(i<=days):
            print(f"{i:^5}",end='')
            j = j + 1
            if (j==7):
                print()
                j = 0
            i = i+1
        j = j + 1
    print()
    print()