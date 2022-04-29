from dotenv import load_dotenv


class Configuration:
    def config(self):
        print("Starting configuration...")
        self.__config_env()
        print("Configuration done.")

    @staticmethod
    def __config_env():
        load_dotenv()
