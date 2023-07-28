# example data only

my_data = "input_data/day4_data"

def get_data(data_path):
    cards = []
    # f = open("input_data/day4_data")
    f = open("input_data/day4_data")
    big_text = ""
    for line in f:
        big_text += line
    chops = big_text.split("\n\n")
    for raw_card in chops:
        card = []
        rows = raw_card.split("\n")
        for row in rows:
            next_row = []
            for card_number in row.split(" "):
                try:
                    next_row.append(int(card_number.strip()))
                except ValueError:
                    pass
            card.append(next_row)
        cards.append(card)
    return cards

cards = get_data(my_data)
# print(cards)
print(len(cards))
winning_cards = []
no_wins_yet = True


# ball_drawn = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
ball_drawn = [
    8,82,77,88,95,55,62,21,99,14,30,9,97,92,94,3,60,22,18,86,78,71,61,43,79, 
    33,65,81,26,49,47,51,0,89,57,75,42,35,80,1,46,83,39,53,40,36,54,70,76,38,
    50,23,67,2,20,87,37,66,84,24,98,4,7,12,44,10,29,5,48,59,32,41,90,17,56,85,
    96,93,27,74,45,25,15,6,69,16,19,8,31,13,64,63,34,73,58,91,11,68,72,52
]
print(len(ball_drawn))

# Mebium solution follows
#  check for a winning card


# original unoptimized code
# def check_win(card):
#     # Any row containing -1 five times?
#     for row in card:
#         if sum(x == -1 for x in row) == 5:
#             return True

#     # Any column containing -1 five times?
#     for c in range(len(card[0])):
#         if sum(row[c] == -1 for row in card) == 5:
#             return True

#     return False


# streamlined code
def check_win(card, row, c):
    if sum(x == -1 for x in row) == 5:
        return True
    if sum(r[c] == -1 for r in card) == 5:
        return True
    return False



# mark each card for ping-pong-ball with -1 using enumerate
def mark(card, number):
    for r, row in enumerate(card):
        for c, cell in enumerate(row):
            if cell == number:
                card[r][c] = -1
                return check_win(card, row, c)
                # return check_win(card) # True or False
    return False

"""   this worked for example data, but not for part 1 
# Not much to be said, just sum up all numbers which are not -1 and multiply by the last marked number:
def winner_score(card, last_number):
    unmarked_tot = 0

    for row in card:
        for x in row:
            if x != -1:
                unmarked_tot += x       # RSQ change gave expected results
                # unmarked_tot += 1    # RSQ change gave expected results
        print(unmarked_tot, last_number)
    return unmarked_tot * last_number
"""
# streamlined with lambda function
# def winner_score(card, last_number):
#     unmarked_tot = 0

#     for row in card:
#         unmarked_tot += sum(filter(lambda x: x != -1, row))

#     return unmarked_tot * last_number

def winner_score(card, last_number):
    unmarked_tot = 0

    for row in card:
        for x in row:
            if x != -1:
                unmarked_tot += x       # RSQ change gave expected results
                # unmarked_tot += 1    # RSQ change gave expected results
        print(unmarked_tot, last_number)
    return unmarked_tot * last_number

 

# part 1
# for number in ball_drawn:
#     for card in cards:
#         # if  win == mark(card, number):  # : colon was copied from repository
#         win = mark(card, number) # : colon was copied from repository
#         # win = mark(card, number)
#         if win:
#             score = winner_score(card, number)
#             break

#     if win:
#         break

# print('Part 1:', score)

 
"""
# part 2
n_cards = len(cards)
n_won   = 0

for number in ball_drawn:
    for i, card in enumerate(cards):
        if card is None:
            continue

        if mark(card, number):
            n_won += 1

            if n_won == 1:
                first_winner_score = winner_score(card, number)
            elif n_won == n_cards:
                last_winner_score = winner_score(card, number)

            cards[i] = None

print('Part 1:', first_winner_score)
print('Part 2:', last_winner_score)
"""
