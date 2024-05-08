#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    player = Player("Sleepy")
    player_2 = Player("Toad")
    game = Game("Valorant")
    Result(player, game, 3000)
    Result(player, game, 1500)
    Result(player_2, game, 2000)

    player.num_times_played(game)

    ipdb.set_trace()
