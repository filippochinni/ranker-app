import argparse


class CLParser:
    def __init__(self):
        self.DESCRIPTION = "Ranker-App is an utility app for building Rankings and other related utility functionalities.\n" \
							"It can be used either as a command line application or navigated through a menu interface.\n"
        self.parser = argparse.ArgumentParser(prog="rankerapp", description=self.DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)

        self.parser.add_argument("-cl", action="store_true", help="Use the command line interface instead of the menu interface")

        self.parsed_args = None

    def __call__(self):
        self.parsed_args = self.parser.parse_args()
        self._check_args()
        return self.parsed_args

    def _check_args(self):
        pass

    def print_namespace(self):
        print("\nParsed args: (")
        for key, value in self.parsed_args.__dict__.items():
            print(f"\t{key}: {value}")
        print(")\n")


