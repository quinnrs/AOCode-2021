

fin   = open("input_data/day4_data")
drawn = map(int, fin.readline().split(','))
print(drawn)

def into_matrix(raw):
    lines = raw.strip().splitlines()
    res = []
    for l in lines:
        res.append(list(map(int, l.split())))
    return res

cards = list(map(into_matrix, fin.read().split('\n\n')))
print (cards[0:2])

def into_matrix(raw):
    lines = raw.strip().splitlines()
    return list(list(map(int, l.split())) for l in lines)


for ping_pong_ball in drawn:
    for card in cards:
        # for row in range(len(cards[card])):
        for row in card:
            for position_value in row:
                if position_value == ping_pong_ball:
                    print(position_value == ping_pong_ball)
                    # marked this positionas played - zero value
                    position_value = 0
           
        print(f"card is ", card)


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
        print(unmarked_tot, last_number)
    return unmarked_tot * last_number   


# part 1
for number in drawn:
    for card in cards:
        # if  win == mark(card, number):  # : colon was copied from repository
        win = mark(card, number) # : colon was copied from repository
        # win = mark(card, number)
        if win:
            
            score = winner_score(card, number)
            print(score, card, number)
            break

    if win:
        break

print('Part 1:', score)



