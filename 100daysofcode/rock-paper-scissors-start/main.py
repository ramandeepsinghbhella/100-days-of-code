import random

a=int(input("select one from rock, paper and scissors. type 0 for rock, 1 for scissors and type 2 for paper \n"))

if a==0:
  print("you choose rock")
  print('''
               _______
           ---'   ____)
                 (_____)
                 (_____)
                 (____)
           ---.__(___)
           ''')
elif a==1:
  print("you choose scissors")
  print('''
             _______
         ---'   ____)____
                   ______)
                __________)
               (____)
         ---.__(___)
         ''')
elif a==2:
  print("you choose paper")
  print('''
             _______
         ---'   ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
         ''')  
elif a>=3:
  print("type again")

b = ["rock", "paper", "scissors"]
c = random.choice(b)
if c=="rock":
  print("computer choose rock")
  print('''
             _______
         ---'   ____)
               (_____)
               (_____)
               (____)
         ---.__(___)
         ''')
elif c=="paper":
  print("computer choose paper")
  print('''
             _______
         ---'   ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
         ''')
elif c=="scissors":
  print("computer choose scissors")
  print('''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        ''')  

if a==0 and c=="rock":
  print("match draw")
elif a==0 and c=="scissors":
  print("you win")
elif a==0 and c=="paper":
  print("you lost")
elif a==1 and c=="rock":
  print("you lost")
elif a==1 and c=="scissors":
  print("match draw")
elif a==1 and c=="paper":
  print("you win")
elif a==2 and c=="rock":
  print("you lost")
elif a==2 and c=="scissors":
  print("you lost")
elif a==2 and c=="paper":
  print("match draw")
    


  

