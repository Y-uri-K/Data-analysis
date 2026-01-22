from time import sleep
from generator.data_generator import DataGenerator

def main() -> None:
    while True:
        generator = DataGenerator()
        generator.generate_and_save(players_count=1, events_per_player=5)
        sleep(1)


if __name__ == "__main__":
    main()