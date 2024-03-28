import os
try:
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
except:
  os.system("pip install pystyle")
os.system("clear")
print(Colorate.Vertical(Colors.red_to_yellow,Center.XCenter("""
                                              No idea
                 ╔═══════════════════════════════════════════════════════════════════════╗
                 ║    { 1 } +                       ║   { 3 } /                          ║
                 ║    { 2 } -                       ║                                    ║ 
                 ║    { 4 } *                       ║   { x } close                      ║
                 ╚═══════════════════════════════════════════════════════════════════════╝
""")))
r = input(" : ")
while True:
    if r == "1":
        print("running..")
        f = int(input("Enter The Number To Be Added\n>>> "))
        g = int(input("Enter Another Number To Be Added\n>>> "))
        l = f + g
        print("\nThe Result Is : ",l)
        break
    elif r == "2":
        print("running..")
        k = int(input("Enter The Number To Be Minus\n>>>"))
        m = int(input("Enter Another Number To Be Minus\n>>>"))
        n = k - m
        print("\nThe Result Is : ",n)
        break
    elif r == "3":
        print("Running...")
        j = int(input("Enter The  Divided Number \n>>>:"))
        i = int(input("Enter The Number To Be Divided By \n>>>:"))
        h = i/j
        print("\nThe Result Is : ",h)
        break
    elif r == "4":
        print("running...")
        q = int(input("Enter The Number To Be Multiply  \n>>>:"))
        w = int(input("Enter The Number To Be Multiplied With \n>>>:"))
        e = q*w
        print("\nThe Result Is : ",e)
        break
