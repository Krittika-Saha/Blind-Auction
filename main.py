from os import system
from art import logo
#HINT: You can call clear() to clear the output in the console.
bids = {}
def compare(dictionary):
  highest_bid = 0
  winner = ''

  for i in dictionary:
    if dictionary[i] > highest_bid:
      highest_bid = dictionary[i]
      winner = i
  print(f'The winner is {winner} with a bid of ${highest_bid}.')

print(logo)
while True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?:$ "))
  bids[name] = bid
  other_bidder = input("Is there any other bidder? Type 'yes' or 'no': ")
  if other_bidder == 'yes':
    #Pls change CLS to cls in Unix
    system('CLS')
    pass
  elif other_bidder == 'no':
    break
compare(bids)

