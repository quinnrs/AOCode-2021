

# +_+_+_+_+_+_+_  part 1 +_+_+_+_+_+__

# copy directly into a list
posits = [16,1,2,0,4,2,7,1,2,14]
# fuel_opt = len[posits] * 5
# fuel_opt = 50
for k in posits:
    # fuel_opt = 50
    meet_point = k
    fuel = 0
    for n in posits:
        # travel = abs(k-n)
        fuel+= abs(k-n)
        # if fuel_opt > fuel:
            # fuel_opt = fuel
        # print(f"fuel_opt = ", fuel_opt)
    print(f"\nfor meet point at ", k, "fuel = ", fuel)

# make a dict with key = position and value = fuel
pos_fuel =  dict()
for item in posits:
    pos_fuel[k] = str(k)
    