from core.config import welcome_msg, CMD_CREATE_USER, CMD_DELETE_USER, CMD_IMPORT, CMD_EXPORT
from InquirerPy import inquirer
import sys



class CLI:
    def __init__(self) -> None:
        self.commands =[
                    CMD_CREATE_USER,
                    #todo CMD_DELETE_USER,
                    #todo CMD_IMPORT,
                    #todo CMD_EXPORT
                ]

    def start(self) -> None:
        print(welcome_msg)

        try:
            result = inquirer.select(
                message=f"What do you want do do?",
                choices = self.commands,
            ).execute()

            if result == CMD_CREATE_USER:
                user_name = inquirer.text(message="username:").execute()
                password = inquirer.secret(message="password:").execute()
                #todo
                print("\n🪄 User created.")

        except KeyboardInterrupt:
            print("❌ Aborted.")
            sys.exit(0)
