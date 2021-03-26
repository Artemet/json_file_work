import json
def text(name):
    if len(name) >= 5:
        print("Not bad name!")
    else:
        print("Good name!")
name = input("Your name: ")
text(name)
arrCommand = ["Start", "Stop"]
print(arrCommand)
command = input("Command: ")
if command == arrCommand[0]:
    arrChoice = ["Sing in", "Sing up"]
    print(arrChoice)
    choice = input("Choice: ")
    if choice == arrChoice[0]:
        arrLogin = ["Artem_123", "Eagor_321", "Anna_231"]
        arrParol = ["Parol_123", "Parol_321", "Parol_231"]
        anser_login = input("Login: ")
        anser_parol = input("Parol: ")
        if anser_login == arrLogin[0] and anser_parol == arrParol[0]:
            information_json = {"Login": arrLogin[0], "Parol": arrParol[0]}
            anser_save = input("Save?: ")
            if anser_save == "yes" or anser_save == "save":
                file = open("information.json", "w")
                information = json.dump(information_json, file)
                file.close()
                print(name,"your information is in file: json")
                anser_continue = input("Continue: ")
                if anser_continue == "yes" or anseranser_continue == "continue":
                    file_task = open("task.txt", "w")
                    file_task.write("1. Task about cars\n")
                    file_task.write("2. Task about Moterbikes\n")
                    file_task.write("3. Task about Buses")
                    file_task.close()
                    print("Task are in file: task.txt")
                    anser_task = int(input("Your task: "))
                    if anser_task == 1:
                        green_car = int(input("How meny green cars are at the parking?: "))
                        yellow_car = int(input("How meny yellow cars are at the parking?: "))
                        black_car = int(input("How meny glack cars are at the parking?: "))
                        anser_car = int(input("How meny cars are at the parking?: "))
                        if anser_car == green_car + yellow_car + black_car:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 2:
                        green_moterbike = int(input("How meny green moterbikes are at the parking?: "))
                        yellow_moterbike = int(input("How meny yellow moterbikes are at the parking?: "))
                        black_moterbike = int(input("How meny black moterbikes are at the parking?: "))
                        anser_moterbike = int(input("How meny moterbikes are at the parking?: "))
                        if anser_moterbike == green_moterbike + yellow_moterbike + black_moterbike:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 3:
                        green_bus = int(input("How meny green buses are at the parking?: "))
                        yellow_bus = int(input("How meny yellow buses are at the parking?: "))
                        black_bus = int(input("How meny black buses are at the parking?: "))
                        anser_bus = int(input("How meny buses are at the parking?: "))
                        if anser_bus == green_bus + yellow_bus + black_bus:
                            print(name,"your anser is right!")
                        else:
                            print(False)
        elif anser_login == arrLogin[1] and anser_parol == arrParol[1]:
            information_json = {"Login": arrLogin[1], "Parol": arrParol[1]}
            anser_save = input("Save?: ")
            anser_continue = input("Continue: ")
            if anser_save == "yes" or anser_save == "save":
                file = open("information.json", "w")
                information = json.dump(information_json, file)
                file.close()
                print(name,"your information is in file: json")
                anser_continue = input("Continue: ")
                if anser_continue == "yes" or anseranser_continue == "continue":
                    file_task = open("task.txt", "w")
                    file_task.write("1. Task about cars\n")
                    file_task.write("2. Task about Moterbikes\n")
                    file_task.write("3. Task about Buses")
                    file_task.close()
                    print("Task are in file: task.txt")
                    anser_task = int(input("Your task: "))
                    if anser_task == 1:
                        green_car = int(input("How meny green cars are at the parking?: "))
                        yellow_car = int(input("How meny yellow cars are at the parking?: "))
                        black_car = int(input("How meny glack cars are at the parking?: "))
                        anser_car = int(input("How meny cars are at the parking?: "))
                        if anser_car == green_car + yellow_car + black_car:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 2:
                        green_moterbike = int(input("How meny green moterbikes are at the parking?: "))
                        yellow_moterbike = int(input("How meny yellow moterbikes are at the parking?: "))
                        black_moterbike = int(input("How meny black moterbikes are at the parking?: "))
                        anser_moterbike = int(input("How meny moterbikes are at the parking?: "))
                        if anser_moterbike == green_moterbike + yellow_moterbike + black_moterbike:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 3:
                        green_bus = int(input("How meny green buses are at the parking?: "))
                        yellow_bus = int(input("How meny yellow buses are at the parking?: "))
                        black_bus = int(input("How meny black buses are at the parking?: "))
                        anser_bus = int(input("How meny buses are at the parking?: "))
                        if anser_bus == green_bus + yellow_bus + black_bus:
                            print(name,"your anser is right!")
                        else:
                            print(False)
        elif anser_login == arrLogin[2] and anser_parol == arrParol[2]:
            information_json = {"Login": arrLogin[2], "Parol": arrParol[2]}
            anser_save = input("Save?: ")
            if anser_save == "yes" or anser_save == "save":
                file = open("information.json", "w")
                information = json.dump(information_json, file)
                file.close()
                print(name,"your information is in file: json")
                anser_continue = input("Continue: ")
                if anser_continue == "yes" or anseranser_continue == "continue":
                    file_task = open("task.txt", "w")
                    file_task.write("1. Task about cars\n")
                    file_task.write("2. Task about Moterbikes\n")
                    file_task.write("3. Task about Buses")
                    file_task.close()
                    print("Task are in file: task.txt")
                    anser_task = int(input("Your task: "))
                    if anser_task == 1:
                        green_car = int(input("How meny green cars are at the parking?: "))
                        yellow_car = int(input("How meny yellow cars are at the parking?: "))
                        black_car = int(input("How meny glack cars are at the parking?: "))
                        anser_car = int(input("How meny cars are at the parking?: "))
                        if anser_car == green_car + yellow_car + black_car:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 2:
                        green_moterbike = int(input("How meny green moterbikes are at the parking?: "))
                        yellow_moterbike = int(input("How meny yellow moterbikes are at the parking?: "))
                        black_moterbike = int(input("How meny black moterbikes are at the parking?: "))
                        anser_moterbike = int(input("How meny moterbikes are at the parking?: "))
                        if anser_moterbike == green_moterbike + yellow_moterbike + black_moterbike:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 3:
                        green_bus = int(input("How meny green buses are at the parking?: "))
                        yellow_bus = int(input("How meny yellow buses are at the parking?: "))
                        black_bus = int(input("How meny black buses are at the parking?: "))
                        anser_bus = int(input("How meny buses are at the parking?: "))
                        if anser_bus == green_bus + yellow_bus + black_bus:
                            print(name,"your anser is right!")
                        else:
                            print(False)
        else:
            print(name,"you have a problem!")
    elif choice == arrChoice[1]:
        login = input("Login: ")
        parol = input("Parol: ")
        information_peaple = {"Login": login, "Parol": parol}
        file = open("information.json", "w")
        information_json = json.dump(information_peaple, file)
        file.close()
        anser_continue = input("Continue: ")
        if anser_continue == "yes" or anseranser_continue == "continue":
            file_task = open("task.txt", "w")
            file_task.write("1. Task about cars\n")
            file_task.write("2. Task about Moterbikes\n")
            file_task.write("3. Task about Buses")
            file_task.close()
            print("Task are in file: task.txt")
            anser_task = int(input("Your task: "))
            if anser_task == 1:
                green_car = int(input("How meny green cars are at the parking?: "))
                yellow_car = int(input("How meny yellow cars are at the parking?: "))
                black_car = int(input("How meny glack cars are at the parking?: "))
                anser_car = int(input("How meny cars are at the parking?: "))
                if anser_car == green_car + yellow_car + black_car:
                    print(name,"your anser is right!")
                else:
                    print(False)
            elif anser_task == 2:
                green_moterbike = int(input("How meny green moterbikes are at the parking?: "))
                yellow_moterbike = int(input("How meny yellow moterbikes are at the parking?: "))
                black_moterbike = int(input("How meny black moterbikes are at the parking?: "))
                anser_moterbike = int(input("How meny moterbikes are at the parking?: "))
                if anser_moterbike == green_moterbike + yellow_moterbike + black_moterbike:
                    print(name,"your anser is right!")
                else:
                    print(False)
            elif anser_task == 3:
                green_bus = int(input("How meny green buses are at the parking?: "))
                yellow_bus = int(input("How meny yellow buses are at the parking?: "))
                black_bus = int(input("How meny black buses are at the parking?: "))
                anser_bus = int(input("How meny buses are at the parking?: "))
                if anser_bus == green_bus + yellow_bus + black_bus:
                    print(name,"your anser is right!")
                else:
                    print(False)
        elif anser_login == arrLogin[2] and anser_parol == arrParol[2]:
            information_json = {"Login": arrLogin[2], "Parol": arrParol[2]}
            anser_save = input("Save?: ")
            if anser_save == "yes" or anser_save == "save":
                file = open("information.json", "w")
                information = json.dump(information_json, file)
                file.close()
                print(name,"your information is in file: json")
                anser_continue = input("Continue: ")
                if anser_continue == "yes" or anseranser_continue == "continue":
                    file_task = open("task.txt", "w")
                    file_task.write("1. Task about cars\n")
                    file_task.write("2. Task about Moterbikes\n")
                    file_task.write("3. Task about Buses")
                    file_task.close()
                    print("Task are in file: task.txt")
                    anser_task = int(input("Your task: "))
                    if anser_task == 1:
                        green_car = int(input("How meny green cars are at the parking?: "))
                        yellow_car = int(input("How meny yellow cars are at the parking?: "))
                        black_car = int(input("How meny glack cars are at the parking?: "))
                        anser_car = int(input("How meny cars are at the parking?: "))
                        if anser_car == green_car + yellow_car + black_car:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 2:
                        green_moterbike = int(input("How meny green moterbikes are at the parking?: "))
                        yellow_moterbike = int(input("How meny yellow moterbikes are at the parking?: "))
                        black_moterbike = int(input("How meny black moterbikes are at the parking?: "))
                        anser_moterbike = int(input("How meny moterbikes are at the parking?: "))
                        if anser_moterbike == green_moterbike + yellow_moterbike + black_moterbike:
                            print(name,"your anser is right!")
                        else:
                            print(False)
                    elif anser_task == 3:
                        green_bus = int(input("How meny green buses are at the parking?: "))
                        yellow_bus = int(input("How meny yellow buses are at the parking?: "))
                        black_bus = int(input("How meny black buses are at the parking?: "))
                        anser_bus = int(input("How meny buses are at the parking?: "))
                        if anser_bus == green_bus + yellow_bus + black_bus:
                            print(name,"your anser is right!")
                        else:
                            print(False)
elif command == arrCommand[1]:
    print("Bye",name)
else:
    print(name,"you have a problem!")