from functions import *
#smaller loop todo
loop=True

while True:
    print("\nWelcome to the system, please choose ur role")
    print("\nR for Receptionist, D for Doctor, N for Nurse, P for Patient, E for Exit")
    roles=input("Enter your Roles [R/D/N/P/E]: ")

    if roles == "E" or roles == "e":
        break

    while loop == True:
        #Receptionist
        if roles=="R" or roles=="r":
            print("\nWelcome to the system, current role: Receptionist")
            print("\nR for registration, U for updating details, S for scheduling appointments, E for exit")
            action_r=input("Actions [R/U/S/E]: ")

            #Registration
            if action_r=="R" or action_r=="r":
                register()
                action_r=input("\nAny other actions [R/U/S/E]: ")

            #Updating
            elif action_r=="U" or action_r=="u":
                update()
                action_r = input("\nAny other actions [R/U/S/E]: ")

            #Schedule
            elif action_r=="S" or action_r=="s":
                show_u()
                #schedule_a()
                action_r = input("\nAny other actions [R/U/S/E]: ")

            #Exit
            elif action_r=="E" or action_r=="e":
                loop=False

            #Error
            else:
                print("\nError occurred, pls try again! ")
                action_r = input("Actions [R/U/S/E]: ")

        #Doctor
        elif roles=="D" or roles=="d":
            print("\nV for viewing patient information, U for updating details, A for showing appointment list, C for changing availability, E for exit")
            action_d = input("Actions [V/U/A/C/E]: ")

            #Viewing Patient
            if action_d=="v" or action_d=="V":
                view()
                action_d=input("\nAny other actions [V/U/A/C/E]: ")

            #Updating
            elif action_d=="U" or action_d=="u":
                update()
                action_d=input("\nAny other actions [V/U/A/C/E]: ")

            #Showing Appointments

            #Changing Availability
            elif action_d=="C" or action_d=="c":
                option_c=input("Would you like to block or unblock [B/U]: ")

                if option_c=="B" or option_c=="b":
                    block()
                    action_d=input("\nAny other actions [V/U/A/C/E]: ")

                elif option_c=="U" or option_c=="u":
                    unblock()
                    action_d=input("\nAny other actions [V/U/A/C/E]: ")
            #Exit
            elif action_d=="E" or action_d=="e":
                loop=False



        #Error
        else:
            print("\nError occurred, pls try again! ")
            continue
