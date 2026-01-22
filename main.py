from time import sleep
from generator.data_generator import DataGenerator

def main() -> None:
    generator = DataGenerator()
    while True:
        result = generator.generate_and_save(players_count=5, events_per_player=15)
        print(f"Создано игроков: {result['players_count']}, событий: {result['events_count']}", flush=True)
        sleep(1)


if __name__ == "__main__":
    main()