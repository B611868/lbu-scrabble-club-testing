#!/usr/bin/env python3

import unittest

from scrabble_club.leaderboard import LeaderBoard
from scrabble_club.member import Member


class TestLeaderBoard(unittest.TestCase):

    def test_default_competition_is_none(self):
        board = LeaderBoard()
        self.assertIsNone(board.competition)

    def test_competition_name_can_be_set(self):
        board = LeaderBoard(competition="regional")
        self.assertEqual(board.competition, "regional")

    def test_add_player(self):
        board = LeaderBoard()
        member = Member(1, "Alice", "Ace")
        board.add_player(member)
        self.assertEqual(len(board.players), 1)
        self.assertIs(board.players[0], member)

    def test_sort_board_orders_by_average_score_descending(self):
        board = LeaderBoard()
        member1 = Member(1, "Alice", "Ace", games=[100])
        member2 = Member(2, "Bob", "Bolt", games=[200])
        member3 = Member(3, "Charlie", "Champ", games=[150])
        member4 = Member(4, "Dave", "Dynamo", games=[50])
        board.add_player(member1)
        board.add_player(member2)
        board.add_player(member3)
        board.add_player(member4)
        board.sort_board()
        self.assertEqual(board.players, [member2, member1, member3, member4])

    def test_players_list_is_empty_on_init(self):
        board = LeaderBoard()
        self.assertEqual(board.players, [])
