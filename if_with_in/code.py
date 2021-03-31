number = 7
user_input = input("enter y if you want to play ").lower()

if user_input == 'y':
  user_number = int(input("Guess pur number: "))
  if user_number == number:
    print("you guessed correctly")
  elif abs(number - user_number) == 1:
    print("you were off by one")
  else:
    print("sorry, it's wrong")
