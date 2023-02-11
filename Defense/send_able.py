from penguin_game import *


# Ok, I kept the old version of this in case I misunderstood something here,
# but I didn't think we need to send penguins if they won't arrive in time and will just die.
# If we wanted to send them, we should send them as attack, not as defense. 
# Again, I might be wrong so I'm keeping the code that was here before.

# Function checks each penguin group and if they are targeting the to_iceberg. 
# If so, we want to send reinforcements FROM the from_iceberg TO the to_iceberg.
def send_able_defense(from_iceberg, to_iceberg, game):
    enemy_penguin_groups = game.get_enemy_penguin_groups
    for enemy_penguin_group in enemy_penguin_groups:
        if enemy_penguin_group.destination != to_iceberg:
            enemy_penguin_groups.remove(enemy_penguin_group)
    did_send_help = False
    for enemy_penguin_group in enemy_penguin_groups:
        if from_iceberg.get_turns_till_arrival(to_iceberg) < enemy_penguin_group.turns_till_arrival:
            amount_needed = enemy_penguin_group.penguin_amount - (
                    to_iceberg.penguin_amount + to_iceberg.penguins_per_turn * enemy_penguin_group.turns_till_arrival)
            if amount_needed < from_iceberg.penguin_amount:
                from_iceberg.send_penguins(to_iceberg, amount_needed)
                did_send_help = True
    return did_send_help

# Needs to change to look at all penguins sent to our iceberg
# def send_able_defense(from_iceberg, to_iceberg, penguin_group):
#     if to_iceberg.get_turns_till_arrival() < penguin_group.turns_till_arrival:
#         amount_needed = penguin_group.penguin_amount - (
#                 from_iceberg.penguin_amount + from_iceberg.penguins_per_turn * penguin_group.turns_till_arrival)
#         if amount_needed < to_iceberg.penguin_amount:
#             to_iceberg.send_help(amount_needed)
#         else:
#             return False
#     else:
#         amount_needed = penguin_group.penguin_amount - from_iceberg.penguin_amount + from_iceberg.penguins_per_turn * (
#                 to_iceberg.get_turns_till_arrival() - penguin_group.turns_till_arrival)
#         if amount_needed < to_iceberg.penguin_amount:
#             to_iceberg.send_help(amount_needed)
#             return True
#         return False
