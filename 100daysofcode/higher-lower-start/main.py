import random
from game_data import data
from art import logo
from art import vs

print(logo)

def a(random_data_for_a):
  print(f"Compare A: {random_data_for_a['name']}, a {random_data_for_a['description']}, from {random_data_for_a['country']}")
  print(vs)



def b(random_data_for_b):
  print(f"Against B: {random_data_for_b['name']}, a {random_data_for_b['description']}, from {random_data_for_b['country']}")

game_continue = True
score = 0

while game_continue:
  random_data = random.choices(data, k=2)
  a(random_data[0])
  b(random_data[1])

  follower_count_for_a = random_data[0]['follower_count']
  follower_count_for_b = random_data[1]['follower_count']

  users_choice = input("Who has more followers? Type A or B: ").lower()

  if users_choice == "a":
    print(f"Your score is {score}")
    if follower_count_for_a > follower_count_for_b:
      score+=1
    else:
      print(f"YOU LOSS' Your score is {score}")
      game_continue = False
  else:
    print(f"Your score is {score}")
    if follower_count_for_b > follower_count_for_a:
      score+=1
    else:
      print(f"YOU LOSS Your score is {score}")
      game_continue = False