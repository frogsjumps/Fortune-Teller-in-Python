import random

fortune_number = int(input('Input the number of fortunes you would like: '))

def fortune_teller(fortune_number):
    fortune = 0
    while fortune != fortune_number:
        fortune_sayings = ['Do not be afraid of competition.', 'An exciting opportunity lies ahead of you.', 'You love peace.', 'You will always be surrounded by true friends.', 'Sell your ideas-they have exceptional merit.']
        print(random.choice(fortune_sayings))
        fortune = fortune + 1


fortune_teller(fortune_number)
