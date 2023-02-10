from penguin_game import *
from distance_sort import *
from Defense.check_if_c_safe import *
from Defense.send_able import *
from Defense.check_who_should_send import *
from Ratings.rate_my_icebergs import *
from Defense.check_if_attacked_i import *
from Ratings.rate_enemy_Icepital import *
from Attack.attack import *
from Ratings.rate_enemy_icebergs import *
from Upgrade.upgrade import upgrade
from Attack.attack_by_rating import *


def do_turn(game):
    our_capital = game.get_my_icepital_icebergs()[0]
    enemy_capital = game.get_enemy_icepital_icebergs()[0]

    # Sorts distances for all sides.
    distances_from_our_capital = distance_sort_d(game, our_capital)
    distances_from_enemy_capital = distance_sort_a(game, enemy_capital)
    sorted_enemies_from_enemy_capital = sort_enemy_icebergs_by_distance_from_enemy_capital(game)

    # Defends capital if needed
    if not check_if_C_safe(game.get_enemy_penguin_groups()):
        icebergs_to_send = check_who_should_send_to_capital()
        for iceberg in icebergs_to_send:
            send_able_defense(iceberg, our_capital, )

    # Checks if we should attack capital and attacks.
    capital_should_be_attacked = rate_enemy_C(game, distances_from_enemy_capital, sorted_enemies_from_enemy_capital)
    if capital_should_be_attacked:
        attack_capital(game)

    # Defends icebergs needing defense
    icebergs_needing_defense = rate_my_attacked_icebergs(find_all_attacked_icebergs(game), game)
    for iceberg in icebergs_needing_defense:
        icebergs_to_send_from = check_who_should_send_to_iceberg(iceberg)
        for sending_iceberg in icebergs_to_send_from:
            send_able_defense(sending_iceberg, iceberg, )

    # Attacks icebergs we want
    # The function attack_by_rating already includes the code below within it
    attack_by_rating(game)
    # icebergs_to_be_attacked = rate_enemy_icebergs(game)
    # for iceberg in icebergs_to_be_attacked:
    #     attack_iceberg(game, iceberg)

    upgrade(game)
