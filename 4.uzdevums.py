ievade = input("Ievadiet naturālu skaitli: ")
try:
    skaitlis = int(ievade)
except:
    print("Nav pareizi ievadīts naturāls skaitlis")
    exit()
rezultats = 1
for i in range(1,skaitlis + 1):
    rezultats = rezultats * i
print(f"Ievadītā skaitļa faktoriāls ir {rezultats}")