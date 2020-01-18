price_per_pack = float(input('Cost per pack? '))
cigs_per_pack = int(input('How many cigs per pack? '))
cigs_per_day = int(input('How many cigs per day? '))
days_since_quit = int(input('How many days quit? '))
time_saved_per_cig = float(10.0)

cigs_not_smoked = cigs_per_day * days_since_quit
packs_not_bought = cigs_not_smoked / cigs_per_pack
money_saved = price_per_pack * packs_not_bought
time_saved_total = time_saved_per_cig * float(cigs_not_smoked)

print('Cigs not smoked: ' + (str(cigs_not_smoked)) + '. Great Job!')
print('Packs not bought: ' + (str(packs_not_bought)))
print('Money saved: ' + (str(money_saved)))
print('Time saved: ' + (str(time_saved_total/ 60.00)) + ' priceless hours')

