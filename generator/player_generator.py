from datetime import datetime, timedelta
from typing import List, Dict

from faker import Faker


class PlayerGenerator:
    def __init__(self, faker: Faker):
        self.faker = faker

    def generate(self, count: int) -> List[Dict]:
        players = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=730)

        for _ in range(count):
            players.append({
                "username": self.faker.user_name(),
                "registration_date": self.faker.date_time_between(
                    start_date=start_date,
                    end_date=end_date
                )
            })

        return players
