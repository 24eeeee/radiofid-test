import json

from src.settings import Settings
from src.conveyor import Conveyor
import src.utils as utils


def main():
    with open('../config.json') as file:
        json_data = file.read()
    settings = Settings(json.loads(json_data))

    conveyor = Conveyor()
    conveyor.q.put((utils.loader.Loader(), settings.cfg))
    conveyor.q.put((utils.parser.Parser(), settings.cfg))
    conveyor.q.put((utils.beautifier.Beautifier(), settings.cfg))
    conveyor.q.put((utils.validator.Validator(), settings.cfg))
    conveyor.q.put((utils.notifier.Notifier(settings.cfg), settings.cfg))
    conveyor.q.put((utils.git.Git(), settings.cfg))

    conveyor.run()


if __name__ == "__main__":
    main()

