import os


class PrintHandler:
    _GREEN = '\033[92m'
    _YELLOW = '\033[93m'
    _RED = '\033[91m'
    _RESET = '\033[0m'

    def __init__(self):
        self.resume = {}

    def print_status_updated(self, input_file, output_file, table):
        print(f"Computing table for {input_file}...")
        print(f"Table written to {output_file}")
        print(f"\nComputed Table:\n\n{table}\n")

    def print_status_unchanged(self, output_file, table):
        print(f"{os.path.basename(output_file)} has not changed, there is no need to update the file")
        print(f"Nothing written to {output_file}")
        print(f"\nComputed Table:\n\n{table}\n")

    def print_status_skipped(self, input_file):
        print(f"File {os.path.basename(input_file)} does not exist or is empty, skipping...\n")

    def print_separator(self, symbol='/'):
        print(f"\n{symbol * 100}\n\n")

    def update_resume(self, output_file, status):
        self.resume[os.path.basename(output_file)] = status

    def print_resume(self):
        padding = max([len(key) for key in self.resume.keys()]) + 5

        print("Resume:\n")
        for key, value in self.resume.items():
            if value == 1:
                print(f"{key:<{padding}} --> \t{self._GREEN}Updated{self._RESET}")
            elif value == 2:
                print(f"{key:<{padding}} --> \t{self._YELLOW}Unchanged{self._RESET}")
            else:
                print(f"{key:<{padding}} --> \t{self._RED}Skipped{self._RESET}")
        print("")

