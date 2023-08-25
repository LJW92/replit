from art import logo
from art import vs
from game_data import data
import random
from replit import clear
data_local = data
score = 0
is_user_right = True

def random_pick():
  data1 = random.choice(data_local)
  data_local.remove(data1)
  
  data2 = random.choice(data_local)
  data_local.remove(data2)
  return  [data1, data2]

def is_A_grater_than_B(data_list):
  A = data_list[0]['follower_count']
  B = data_list[1]['follower_count']
  if A > B:
    return True
  else:
    return False

def output_string_function(picked_data):
  A = picked_data[0]
  B = picked_data[1]
  string_A = f"Compare A: {A['name']}, {A['description']}, {A['country']}."
  string_B = f"Against B: {B['name']}, {B['description']}, {B['country']}."
  return [string_A, string_B]

def is_right_guess(two_data, user_choice):
  is_A_greater = two_data[0]['follower_count'] > two_data[1]['follower_count']
  if user_choice == 'A' and is_A_greater:
    return True
  elif user_choice == 'B' and not is_A_greater:
    return True
  else:
    return False
    

while is_user_right:
  picked_data = random_pick()
  output_string = output_string_function(picked_data)
  print(logo)
  if score >= 1:
    print(f"You're right! Current score: {score}.")
  print(output_string[0])
  print(vs)
  print(output_string[1])
  is_user_right = is_right_guess(picked_data, input("Who has more followers? Type 'A' or 'B': ").upper())
  if is_user_right == False:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
  else:
    score += 1
    clear()
    
