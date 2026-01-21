import argparse
from typing import Dict

from faker import Faker

from generator.database import Session
from generator.models import Player, Action, Level, GameEvent

from generator.player_generator import PlayerGenerator
from generator.event_generator import EventGenerator
from generator.points_calculator import PointsCalculator

class DataGenerator:
    def __init__(self, locale: str = "ru_RU"):
        self.session = Session()
        self.faker = Faker(locale)

        self.actions = self.session.query(Action).all()
        self.levels = self.session.query(Level).all()

        self.points_calculator = PointsCalculator()
        self.player_generator = PlayerGenerator(self.faker)
        self.event_generator = EventGenerator(
            faker=self.faker,
            actions=self.actions,
            levels=self.levels,
            points_calculator=self.points_calculator
        )

    def generate_and_save(
        self,
        players_count: int,
        events_per_player: int
    ) -> Dict:

        players_data = self.player_generator.generate(players_count)
        self.session.bulk_insert_mappings(Player, players_data)
        self.session.commit()

        player_ids = [
            p.id for p in self.session.query(Player.id).order_by(Player.id.desc()).limit(players_count)
        ]

        events_data = self.event_generator.generate(
            player_ids=player_ids,
            events_per_player=events_per_player
        )

        self.session.bulk_insert_mappings(GameEvent, events_data)
        self.session.commit()

        return {
            "players_count": players_count,
            "events_count": len(events_data)
        }

    def close(self):
        self.session.close()


def main():
    parser = argparse.ArgumentParser(description="Генератор игровых данных")

    parser.add_argument("--players", type=int, default=100)
    parser.add_argument("--events-per-player", type=int, default=100)
    parser.add_argument("--locale", type=str, default="ru_RU")

    args = parser.parse_args()

    generator = DataGenerator(locale=args.locale)

    try:
        result = generator.generate_and_save(
            players_count=args.players,
            events_per_player=args.events_per_player
        )

        print("Генерация завершена")
        print(f"Игроков: {result['players_count']}")
        print(f"Событий: {result['events_count']}")

    finally:
        generator.close()

if __name__ == "__main__":
    main()