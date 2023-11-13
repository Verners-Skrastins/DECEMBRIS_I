def saskaitit(a):
    try:
        int(a) >= 1
    except:
        return 'Nav pareizi ievadīts naturāls skaitlis'
    rezultats = 0
    for i in range(1,int(a) + 1):
        rezultats += i
    return f"Skaitļu summa ir {rezultats}"
skaitlis = input("Ievadi naturālu skaitli: ")
print(saskaitit(skaitlis))