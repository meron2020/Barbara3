from penguin_game import *
from send_able import send_able_defense


# Function returns list of dictionaries of surrounding icebergs that should send help.
# The key is the iceberg and the value is the amount they should send.
# If needed it should ask for help from all our icebergs.
def icebergs_to_send_to_capital(game, our_icebergs_sorted):
    our_capital = game.get_my_icepital_icebergs()[0]
    defending_icebergs = []
    last_attacker_arrival = 0
    enemy_attackers = 0
    defenders = our_capital.penguin_amount

    # Counts how many are attacking the capital
    for attacker_group in game.get_enemy_penguin_groups():
        if attacker_group.destination == our_capital:
            enemy_attackers += attacker_group.penguin_amount
            if attacker_group.turns_till_arrival > last_attacker_arrival:
                last_attacker_arrival = attacker_group.turns_till_arrival

    current_iceberg = our_icebergs_sorted[0]
    # Iterates through our icebergs by distance and adds the amount the need to send according
    # to how many defenders are already on their way.
    while defenders < enemy_attackers:
        if current_iceberg.penguin_amount > enemy_attackers - defenders:
            defending_icebergs.append({current_iceberg: enemy_attackers - defenders})
            break
        else:
            defending_icebergs.append({current_iceberg: current_iceberg.penguin_amount})
            current_iceberg = our_icebergs_sorted[our_icebergs_sorted.index(current_iceberg) + 1]
            continue

    return defending_icebergs


def find_two_closest_friendly_icebergs(iceberg_to_defend, game):
    friendly_icebergs = game.get_my_icebergs()
    closest_icebergs = []
    for i in range(2):
        closest_iceberg = friendly_icebergs[0]
        for iceberg in friendly_icebergs:
            if iceberg != iceberg_to_defend:
                current_distance = iceberg.get_turns_till_arrival(iceberg_to_defend)
                smallest_distance = closest_iceberg.get_turns_till_arrival(iceberg_to_defend)
                if current_distance < smallest_distance:
                    closest_iceberg = iceberg
        closest_icebergs.append(closest_iceberg)
        friendly_icebergs.remove(closest_iceberg)
    return closest_icebergs


# Function returns list of surrounding icebergs that should send help. Maximum helpers should be 2 for now.
# We can change later if needed.
def check_who_should_send_to_iceberg(iceberg_to_defend):
    return
