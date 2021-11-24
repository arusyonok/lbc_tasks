import unittest
from scripts.leagues import LeagueTable


class TestLeagueTable(unittest.TestCase):

    def setUp(self) -> None:
        self.league = LeagueTable(["V", "A", "T"])

    def test_add_score_ok(self):
        self.league.add_score("V", 123)

    def test_add_score_athlete_does_not_exist(self):
        with self.assertRaises(AttributeError):
            self.league.add_score("J", 123)

    def test_get_scores(self):
        score = self.league.get_scores("V")
        assert score == 0

    def test_get_scores_raises_error(self):
        with self.assertRaises(AttributeError):
            self.league.get_scores("J")

    def test_get_player_by_rank(self):
        self.league.add_score("V", 23)
        self.league.add_score("A", 13)
        self.league.add_score("T", 413)
        player = self.league.get_player_by_rank(1)
        expected_result = self.league.get_athlete_by_name("T")
        assert player.name == expected_result.name

    def test_get_player_by_rank_too_big(self):
        with self.assertRaises(ValueError):
            self.league.get_player_by_rank(3)

    def test_get_player_by_rank_too_small(self):
        with self.assertRaises(ValueError):
            self.league.get_player_by_rank(0)

