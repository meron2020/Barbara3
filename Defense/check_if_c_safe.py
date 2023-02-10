from penguin_game import *


# Checks for each group of enemy penguins if 1) They are attacking the Icepital,
# 2) If the number of penguins in the group is less than the number of
# penguins currently on the iceberg + the amount of penguins that will be added by the time they arrive + 1
def check_if_C_safe(enemy_groups):
    if not enemy_groups:
        return True
    for enemy_group in enemy_groups:
        if enemy_group.destination.is_icepital:
            target = enemy_group.destination
            turns_till_arrival = enemy_group.turns_till_arrival
            additional_penguins = target.penguins_per_turn * turns_till_arrival
            if enemy_group.penguin_amount < (target.penguin_amount + additional_penguins + 1):
                return True
    return False
