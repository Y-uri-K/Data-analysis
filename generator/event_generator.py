import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from faker import Faker

from generator.models import Action, Level
from generator.points_calculator import PointsCalculator


class EventGenerator:
    def __init__(
        self,
        faker: Faker,
        actions: List[Action],
        levels: List[Level],
        points_calculator: PointsCalculator
    ):
        self.faker = faker
        self.actions = actions
        self.levels = levels
        self.points_calculator = points_calculator

    def generate(
        self,
        player_ids: List[int],
        events_per_player: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict]:

        if start_date is None:
            start_date = datetime.now() - timedelta(days=30)
        if end_date is None:
            end_date = datetime.now()

        events = []

        for player_id in player_ids:
            for _ in range(events_per_player):
                action = random.choice(self.actions)
                level = random.choice(self.levels)

                points = self.points_calculator.calculate(
                    action_name=action.action_name,
                    action_type=action.action_type,
                    difficulty=level.difficulty
                )

                events.append({
                    "player_id": player_id,
                    "action_id": action.action_id,
                    "level_id": level.level_id,
                    "points": points,
                    "event_time": self.faker.date_time_between(
                        start_date=start_date,
                        end_date=end_date
                    )
                })

        events.sort(key=lambda e: e["event_time"])
        return events
