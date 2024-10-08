import random

def update(urn):
    die_roll = random.randint(1, 6)
    
    if die_roll in [2, 3, 5]:
        urn['black'] += 1
    elif die_roll == 6:
        urn['red'] += 1 
    else:
        urn['blue'] += 1 


def draw_ball(urn):
    total_balls = sum(urn.values())
    pick_val = random.randint(1, total_balls)
    
    if pick_val <= urn['red']:
        return 'red'
    elif pick_val <= urn['red'] + urn['blue']:
        return 'blue'
    else:
        return 'black'
    

trials = 100000
red_count = 0
    
for _ in range(trials):
    urn = {'red': 3, 'blue': 4, 'black': 2}
    update(urn) 
    drawn_ball = draw_ball(urn)
        
    if drawn_ball == 'red':
        red_count += 1
    
print(str(red_count / trials * 100) + '%')
