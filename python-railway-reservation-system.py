#Write a program to manage railway reservation.
seats=300
booked_seats=0
waiting_list=0
while True:
    print("1)BOOK TICKETS:")
    print("2)CANCEL TICKETS:")
    print("3)VIEW REMAINING SEATS:")
    print("4)VIEW WAITING LIST:")
    print("5)EXIT:")
    ch=input("CHOOSE:")
    if ch=="1":
        tickets=int(input("ENTER HOW MANY TICKETS:"))
        if tickets>seats:
            seat=tickets-seats
            waiting_list+=seat
            print("ADDED TO WAITING LIST")
        else:
            booked_seats+=tickets
            seats-=tickets
            print("REMAINING TICKETS:",seats)
    if ch=="2":
        tickets=int(input("ENTER HOW MANY TO BE CANCELLED:"))
        seats=tickets+seats
        print("presents seats:",seats)
        if waiting_list>0:
            waiting_list=waiting_list-seats
            booked_seats=booked_seats+seats
            print("remaining seats:",seats)
            print("booked seats:",booked_seats)
    if ch=="3":
        print("REMAINING SEATS:",seats)
    if ch=="4":
        print("WAITING LIST:",waiting_list)
    if ch=="5":
        print("THANK YOU BYE!!")
        break
