from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Athlete:
    name: str
    score: Optional[int] = 0


class LeagueTable:

    def __init__(self, list_of_names: list):
        self.athletes: List[Athlete] = []
        for name in list_of_names:
            athlete: Athlete = Athlete(name=name)
            self.athletes.append(athlete)

    def get_athlete_by_name(self, name: str):
        for athlete in self.athletes:
            if athlete.name == name:
                return athlete
        return None

    def add_score(self, name: str, score: int) -> None:
        athlete: Athlete = self.get_athlete_by_name(name)
        athlete.score = score

    def get_scores(self, name: str) -> int:
        athlete: Athlete = self.get_athlete_by_name(name)
        return athlete.score

    def get_player_by_rank(self, rank) -> Athlete:
        if rank > len(self.athletes)-1 or rank < 1:
            raise ValueError("Wrong ranking number.")

        sorted_rank = sorted(self.athletes, key=lambda item: item.score, reverse=True)
        return sorted_rank[rank-1]
