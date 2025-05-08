def register():
    print("===============Registration===============")

    #Patient's Detail
    name=input("Patient's Fullname: ")
    age=input("Patient's Age: ")
    birth=input("Patient's Birth (DD/MM/YY): ")
    gender=input("Patient's gender: ")
    contact=input("Patient's Contact: ")

    #Replace filename
    filename=f"{name.replace(" ","_")}_record.txt"
    with open(filename,"w") as file:
        file.write("===============Patient's Record===============\n")
        file.write(f"Name: {name.capitalize()}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Birth (DD/MM/YY): {birth.capitalize()}\n")
        file.write(f"Gender: {gender.capitalize()}\n")
        file.write(f"Contact: {contact}\n")

    print(f"Patient record saved as {filename}\n")

def view():
    name=input("Patient's Fullname: ")
    filename = f"{name.replace(" ", "_")}_record.txt"

    try:
        with open(filename) as file:
            print("Patient's Record: \n")
            record=file.read()
            print(record)

    except:
        print(f"{filename} not found, pls try again")


def update():
    print("===============Updating===============")

    name=input("Patient's Fullname: ")
    filename=f"{name.replace(" ","_")}_record.txt"

    #finding the file
    try:
        with open(filename) as file:
            print("Patient's Record: \n")
            record=file.read()
            print(record)

        date=input("\nEnter date (dd/mm/yy): ")

        print("\nOptions: \n1. Update Contact \n2. Custom Notes")
        options_r=input("Choose an option (1/2): ")

        #temporary save
        updates=""

        if options_r=="1":
            new_contact=input("Enter patient's new contact: ")
            updates=f"\nUpdated Contact: {new_contact}"

        elif options_r=="2":
            notes=input("Enter notes: ")
            updates=f"\nAdditional Notes: {notes}"

        else:
            print("Error occurred, pls try again! ")
            print("Options: \n1. Update Contact \n2. Custom Notes")
            options_r=input("Choose again: ")

        #append(update the notes) so "a"
        with open(filename,"a") as file:
            file.write(f"\nUpdated on {date}")
            file.write(updates)
            print(f"Updates saved to {filename}\n")

        #show updated file
        with open(filename,"r") as file:
            print("Updated record\n")
            print(file.read())

    except:
        print(f"{filename} not found, pls try again")

#making schedule
def schedule_a():
    print("===============Appointments===============")


    name = input("Patient's Fullname: ")
    filename_p = f"{name.replace(" ", "_")}_schedule.txt"

    #appointment information
    date=input("Appointment on (Date): ")
    time=input("Time: ")
    doctor=input("Doctor: ")

    with open(filename_p, "w") as file:
        file.write("===============Appointments===============")
        file.write(f"Patient's Fullname: {name.capitalize()}")
        file.write(f"Appointment on {date} at {time}")
        file.write(f"Appointed Doctor: {doctor.capitalize()}")

#doctor availability
def block():
    doc = input("Doctor (Name): ")
    doc=doc.capitalize()
    filename = f"{doc.replace(" ", "_")}_unable.txt"
    try:
        with open(filename, "a") as file:
            print("Enter the dates that are unavailable (Exp: 11/6/2025, 14/5-24/5/2025")
            date = input("Enter here: ")
            date=date.split(",")
            for days in date:
                file.write(f"{days}\n")

    except:
        print(f"{filename} not found, pls try again")


def unblock():
    doc = input("Doctor (Name): ")
    doc=doc.capitalize()
    filename=f"{doc.replace(" ","_")}_unable.txt"

    try:
        with open(filename, "r") as file:
            print("\nUnavailable: ")
            lines = file.readlines()
            unable = ''.join(lines)
            print(unable)
            file.close()

        print("Enter the dates to remove (Exp: 11/6/2025, 14/5-24/5/2025")
        date = input("Enter here: ")
        date = date.split(",")

        with open(filename,"w")as file:
            for line in lines:
                if line.rstrip() not in date:
                    file.write(line)
            file.close()

        print("Date has been removed")
        with open(filename,"r") as file:
            print("\nUnavailable: ")
            unable=file.read()
            print(unable)

    except:
        print(f"{filename} not found, pls try again")

def view_ap(doc):
    filename=f"{doc.replace(" ", "_")}_schedule.txt"

    try:
        with open(filename,"r") as file:
            appointment=file.read()
            print(appointment)

    except:
        print(f"{filename} not found, pls try again")

def show_u():
    with open("Doctors.txt", "r") as file:
        lines=file.readlines()
        l=0
        for line in lines:
            print(lines[l])

            file1 = f"{lines[l].replace(" ", "_")}_unable.txt"

            with open(file1, "r") as files:
                unable = files.read()
                print(unable)
            #change to another doctor
            l+=1

def appoint(doc):
    filename=f"{doc.replace(" ", "_")}_appointment.txt"