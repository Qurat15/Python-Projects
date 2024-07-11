
from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print('Welcome to the secret auction program')
auctionParticipants = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ''
  for bidder in bidding_record:
    bidamount = bidding_record[bidder]
    if bidamount > highest_bid:
      highest_bid = bidamount
      winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished:
    name = input('What is your name? ')
    bidamount = int(input('What is your bid? $'))
    auctionParticipants[name] = bidamount
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(auctionParticipants)
    elif should_continue == "yes":
        clear()
