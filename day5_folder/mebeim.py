
# list of drawn numbers is current ping-pong-balls
# so order of play is for number in drawn_numbers
# cards comes from the data
# drawn is he list of numbers(ping-pong-balls)

# example data only
my_data = "input_data/day4_example_data/data"

def get_data(data_path):
    cards = []
    # f = open("input_data/day4_data")
    f = open("input_data/day4_example_data/data")
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
print(cards)
print(len(cards))




drawn = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]


#  check for a winning card - original
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

# streamlimed and simplified
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
    return False


# Not much to be said, just sum up all numbers which are not -1 and multiply by the last marked number:
def winner_score(card, last_number):
    unmarked_tot = 0

    for row in card:
        for x in row:
            if x != -1:
                unmarked_tot += 1

    return unmarked_tot * last_number

# part 1
for number in drawn:
    for card in cards:
        # win = mark(card, number):  # : colon was copied from repository
        win =mark(card, number)
        if win:
            score = winner_score(card, number)
            break

    if win:
        break

print('Part 1:', score) # expect 188 * 24 = 4512


# part 2
n_cards = len(cards)
n_won   = 0

for number in drawn:
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






"""    simplified ckeck_win_function 
You might have noticed that check_win() iterates over the entire card every time. Since when we find a number we automatically know its row and column, we can skip checking any other row and column and make our function way simpler by passing the indices of the marked cell:

def check_win(card, r, c):
    # Row
    if sum(x == -1 for x in card[r]) == 5:
        return True

    # Column
    if sum(row[c] == -1 for row in card) == 5:
        return True

    return False
We could even directly pass the row since we already have it available in mark():

def check_win(card, row, c):
    if sum(x == -1 for x in row) == 5:
        return True
    if sum(r[c] == -1 for r in card) == 5:
        return True
    return False


"""

