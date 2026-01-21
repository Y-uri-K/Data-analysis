from time import sleep
from generator.data_generator import DataGenerator


def main() -> None:
    while True:
        DataGenerator()
        sleep(1)


if __name__ == "__main__":
    main()