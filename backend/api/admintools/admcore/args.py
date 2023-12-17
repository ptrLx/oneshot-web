import argparse


class ArgParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Administrate oneshot-web.")

        # self.parser.add_argument(
        #     "-c",
        #     "--create-user",
        #     type=str,
        #     default="admin",
        #     help="Create a new user",
        # )
