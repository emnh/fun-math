#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re


import random

def simulate_monty_hall(num_simulations):
    switch_wins = 0
    stick_wins = 0

    for _ in range(num_simulations):
        # Randomly place the car behind one of the three doors
        doors = [0, 0, 0]
        car_position = random.randint(0, 2)
        doors[car_position] = 1  # 1 represents the car

        # Contestant makes an initial choice
        initial_choice = random.randint(0, 2)

        # Host opens a door with a goat (not the initial choice and not the car)
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] != 1]
        door_opened_by_host = random.choice(remaining_doors)

        # Determine the remaining closed door
        remaining_closed_door = [i for i in range(3) if i != initial_choice and i != door_opened_by_host][0]

        # If the contestant switches, they choose the remaining closed door
        if doors[remaining_closed_door] == 1:
            switch_wins += 1
        else:
            stick_wins += 1

    switch_win_rate = switch_wins / num_simulations
    stick_win_rate = stick_wins / num_simulations

    return switch_win_rate, stick_win_rate

# Number of simulations
num_simulations = 100000
switch_win_rate, stick_win_rate = simulate_monty_hall(num_simulations)

print(f"After {num_simulations} simulations:")
print(f"Win rate if you switch: {switch_win_rate:.4f}")
print(f"Win rate if you stick: {stick_win_rate:.4f}")



def main():
    'entry point'

if __name__ == '__main__':
    main()

