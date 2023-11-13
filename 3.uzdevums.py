skaitlis = input("Ievadiet naturālu skaitli: ")
try:
    if int(skaitlis) % 2 == 0:
        print("Ievadītais skaitlis ir pāra")
    else:
        print("Ievadītais skaitlis ir nepāra")
except:
    print("Nav pareizi ievadīts naturāls skaitlis")