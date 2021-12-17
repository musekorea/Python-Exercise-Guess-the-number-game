# 정답 랜덤 넘버 : 1~100사이의 자연수 
import random
answer_number = 0

def create_random_num():
  global answer_number
  answer_number = random.randint(1,100)
  return answer_number

create_random_num()
  
chances = 10
counter = 0

print("Guess the number bewteen 1 and 100")
print("==================================")

while counter<chances:
  try:
    guess_number = int(input(f"👹 [{chances-counter} Chances] What is your number : -> "))
    if guess_number==answer_number:
      print("👌 Correct!!")
      break
    elif guess_number<answer_number:
      print(f"The number is larger than {guess_number}")
    elif guess_number>answer_number:
      print(f"THe number is smaller than {guess_number}")
    counter += 1 
    if counter==10:
      print("💀 You Lose ")
      replay = input("Do you want to replay the game? [y/n] -> ")
      while True:
        if replay.lower()=="y":
          counter=0
          create_random_num()
          print("🚧 New Game Starts 🚧")
          print("======================")
          break
        elif replay.lower()=="n":
          print("Bye Bye 🖐")
          break
        else:
          replay = input("Please select [y/n] -> ")
          continue
  except Exception as error:
    print("💥 Error : Please input a number")
    continue

