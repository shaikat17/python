from logo import logo

print(logo)

bidContinue = True
bidBook = {}
moreBid = 'yes'

def getWinner(bidBook):
  winner = max(zip(bidBook.values(),bidBook.keys()))[1]
  print(f"{winner} wins the bid...")

while bidContinue:
  if moreBid == 'yes':
    name = input("Enter Your Name: ")
    bidAmount = int(input("Enter Your Bid Amount: "))
    bidBook[name] = bidAmount
    moreBid = input("More bider input Yes else No: ").lower()
  elif moreBid == "no":
    bidContinue = False
    print('\n'*50)
    getWinner(bidBook)
  else:
    print("Please Enter Yes or No")
    moreBid = input("More bider input Yes else No: ").lower()
    
