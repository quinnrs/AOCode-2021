# my_data = "input_data/day4_example_data/data"
my_data = "input_data/day4.data"

def get_data(data_path):
    cards = []
    f = open("input_data/day4.data")
    # f = open("input_data/day4_example_data/data")
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

# ping_pong_balls = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

ping_pong_balls = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,
                10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,
                71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,
                54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,
                22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]

for ping_pong_ball in ping_pong_balls:
    for card in cards:
        # for row in range(len(cards[card])):
        for row in card:
            for position_value in row:
                if position_value == ping_pong_ball:
                    # print(position_value == ping_pong_ball)
                    # marked this positionas played - zero value
                    position_value = 0
           
        # print(f"card is ", card)

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

def winner_score(card, last_number):
    unmarked_tot = 0

    for row in card:
        for x in row:
            if x != -1:
                unmarked_tot += x      
    print(ping_pong_ball, unmarked_tot, last_number)
    return unmarked_tot * last_number   


# part 2
n_cards = len(cards)
n_won   = 0

for number in ping_pong_balls:
    for i, card in enumerate(cards):
        if card is None:
            continue

        if mark(card, number):
            n_won += 1
            # print(n_won)

            if n_won == 1:
            # if n_won != 1:   
                first_winner_score = winner_score(card, number)
                score1 = first_winner_score
                # print(score1)
                # prints 44736 as expected
            # elif n_won == n_cards:
            elif n_won >= 100:
                score2 = winner_score(card, number)
                # last_winner_score = winner_score(card, number)
                # print(n_won, winner_score) as expected
                
                # score2 = last_winner_score
                # print(score2)
              

            cards[i] = None


print('Part 1:', score1) # expect 4512 ball 24 # part 1 expect 44736
print('Part 2:', score2) # expect 1924 ball 13 # part 2 expect 1827