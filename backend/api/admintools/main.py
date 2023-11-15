from core.args import ArgParser
from core.cli import CLI
from data.db import UserDB

if __name__ == "__main__":
    args = ArgParser()
    # todo evaluate args

    cli = CLI()
    cli.start()
