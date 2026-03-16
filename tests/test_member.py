#!/usr/bin/env python3

import unittest

from scrabble_club.member import Member

class TestMember(unittest.TestCase):

    def test_average_score_is_zero_when_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.average_score, 0)
    
    def test_adding_score_updates_average(self):
        member = Member(1, "A", "A")
        member.play_game(100)
        self.assertEqual(member.average_score, 100)
        member.play_game(200)
        self.assertEqual(member.average_score, 150)

    def test_appending_new_score(self):
        member = Member(1, "A", "A")
        member.play_game(100)
        self.assertEqual(member.games, [100])
        member.play_game(200)
        self.assertEqual(member.games, [100, 200])
    

    def test_best_score_is_zero_when_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.best_score, 0)

    def test_best_with_one_game(self):
        member = Member(1, "A", "A")
        member.play_game(150)
        self.assertEqual(member.best_score, 150)

    def test_best_score_with_many_games(self):
        member = Member(1, "A", "A")
        member.play_game(150)
        self.assertEqual(member.best_score, 150)
        member.play_game(200)
        self.assertEqual(member.best_score, 200)
        member.play_game(100)
        self.assertEqual(member.best_score, 200)

    def test_members_are_average_scores_are_equal(self):
        member_one = Member(1, "Alice", "Ace", games=[100, 200])
        member_two = Member(2, "Bob", "Bolt", games=[150, 150])
        self.assertTrue(member_one == member_two)

    def test_members_are_average_scores_are_equal(self):
        member_one = Member(1, "Alice", "Ace")
        member_two = Member(2, "Bob", "Bolt")
        self.assertTrue(member_one == member_two)    

    def test_members_are_not_equal_when_average_scores_differ(self):
        member_one = Member(1, "Alice", "Ace", games=[100, 200])
        member_two = Member(2, "Bob", "Bolt", games=[150, 100])
        self.assertFalse(member_one == member_two)

    def test_board_entry(self):
        member = Member(1, "Alice", "Ace")
        member.play_game(100)
        member.play_game(200)
        self.assertEqual(member.board_entry, ["Alice (Ace)", 150.0, 200])

    def test_member_is_less_than_other_when_average_score_is_lower(self):
        member_one = Member(1, "Alice", "Ace", games=[100, 200])
        member_two = Member(2, "Bob", "Bolt", games=[150, 200])
        self.assertTrue(member_one < member_two)

    def test_member_is_not_less_than_other_when_average_score_is_higher(self):
        member_one = Member(1, "Alice", "Ace", games=[100, 200])
        member_two = Member(2, "Bob", "Bolt", games=[150, 200])
        self.assertFalse(member_two < member_one)

    def test_repr_representation(self):
        member = Member(1, "Alice", "Ace", games=[100, 200])
        expected_repr = "Member(member_id=1, name='Alice', nick_name='Ace', games=[100, 200])"
        self.assertEqual(repr(member), expected_repr)

    def test_str_representation(self):
        member = Member(1, "Alice", "Ace", games=[100, 200])
        expected_str = "1, Alice, Ace, 150.0"
        self.assertEqual(str(member), expected_str)