from penguin_game import *
from sendAble import send_able


def check_who_should_send(self, penguin_group):
    my_icebergs = self.game.get_my_icebergs()
    amount_acquired = 0
    counter = 0
    while True:
        sent = send_able(my_icebergs[counter], penguin_group)
        if sent:
            break
        else:
            counter += 1