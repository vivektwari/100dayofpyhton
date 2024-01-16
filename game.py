print("Welcome To Game Of guess")

c1 = input("Enter Left or Right to Procude.\n").lower()
if c1 == "left":
  c2 = input("Enter swim to cross the river or wait for a board to cross.\n").lower()
  if c2 == "wait":
    c3 = input("Enter Blue , Green or Yellow to procude.\n").lower()
    if c3 == "blue":
     print("You win")
    elif c3 == "yellow":
      print("Game over: You died by snake bite lol")
    elif c3 == "red":
      print("Game Over: You got Eaten by King of  the Jungle")
    else:
      print("Game Over: Plase Enter Given Options ")
  else:
    print("Game Over")
else:
  print("Game Over")
