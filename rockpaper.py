import random

rock = 'rock'


paper = 'paper'

scissors = 'scissors'
k=input("what do you choose? type  rock, paper or scissors.")
p=random.randint(0,2)
if k=="rock":
  print(rock)
  if p==1:
    print("computer choose")
    print(paper)
    print("you lose")
  elif p==2:
    print("computer choose")
    print(scissors)
    print("you win")
  elif p==0:
    print("computer choose")
    print(rock)
    print("draw")
elif k=="paper":
  print(paper)
  if p==1:
    print("computer choose")
    print(paper)
    print("draw")
  elif p==2:
    print("computer choose")
    print(scissors)
    print("you lose")
  elif p==0:
    print("computer choose")
    print(rock)
    print("you win")
elif k=="scissors":
  print(scissors)
  if p==0:
    print(rock)
    print("you lose")
  elif p==1:
    print(paper)
    print("you win")
  elif p==2:
    print(scissors)
    print("draw")
