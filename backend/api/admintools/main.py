import asyncio
import os
import sys

src_module_path = os.path.abspath("src")

sys.path.append(src_module_path)

from admcore.args import ArgParser
from admcore.cli import CLI

if __name__ == "__main__":
    args = ArgParser()

    cli = CLI()
    asyncio.run(cli.start())
