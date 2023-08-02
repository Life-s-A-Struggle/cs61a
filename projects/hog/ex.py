from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact
from hog import *

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #
######################

# def announce_highest(who, last_score=0, running_high=0):
#     """Return a commentary function that announces when WHO's score
#     increases by more than ever before in the game.

#     NOTE: the following game is not possible under the rules, it's just
#     an example for the sake of the doctest

#     >>> f0 = announce_highest(1) # Only announce Player 1 score gains
#     >>> f1 = f0(12, 0)
#     >>> f2 = f1(12, 9)
#     9 point(s)! The most yet for Player 1
#     >>> f3 = f2(20, 9)
#     >>> f4 = f3(20, 30)
#     21 point(s)! The most yet for Player 1
#     >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
#     >>> f6 = f5(21, 47)
#     >>> f7 = f6(21, 77)
#     30 point(s)! The most yet for Player 1
#     """
#     assert who == 0 or who == 1, 'The who argument should indicate a player.'
#     # BEGIN PROBLEM 7

#     def say(last_turn, current_turn):
#         if current_turn - last_turn > running_high:
#             running_high = current_turn - last_turn
#             print(running_high, "point(s)! The most yet for Player", who)
#         return announce_highest()
#     return say()

def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    def say(score0, score1):
        cur_score = score0 if who == 0 else score1 
        if cur_score - last_score > running_high:
            running_high = cur_score - last_score
            print(running_high, "point(s)! The most yet for Player", who)
        return announce_highest(who, cur_score, running_high)
    return say()