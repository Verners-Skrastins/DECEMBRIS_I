import time
laiks_stundas = int(time.strftime("%H",time.localtime()))
if laiks_stundas > 17 or laiks_stundas < 6:
    print("Labvakar!")
elif laiks_stundas > 10:
    print("Labdien!")
else:
    print("Labrīt!")