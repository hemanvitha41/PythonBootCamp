# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
auction = {}
player_count = int(input("Number of players: "))


for _ in range(player_count):
    name = input("What is your name?\n")
    price = int(input("What is your bid amount? $\n"))

    auction[name] = price

    print("\n" * 50)


highest_bidder = max(auction, key=auction.get)
highest_bid = auction[highest_bidder]


print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")

