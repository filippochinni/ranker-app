import argparse


class CLParser:
    def __init__(self):
        self.DESCRIPTION = "TabularScript is a command line tool that reads files in CSV format and outputs them in a tabular format.\n" \
                            "Inputs and Output files needs to be specified as cl args; multiple I/O files couples can be specified.\n" \
                            "Alternatively, a JSON file can be provided with mapping of input files to output files.\n"
        self.parser = argparse.ArgumentParser(prog="tabularscript", description=self.DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)

        self.parser.add_argument("-i", "--input", action='append', help="Input file path, CSV format, can use relative path")
        self.parser.add_argument("-o", "--output", action='append', help="Output file path, can use relative path")
        self.parser.add_argument("--files-mapping", help="JSON file with mapping of input files to output files")
        self.parser.add_argument("--header-disabled", action="store_true", help="First row of input files is NOT header")

        self.parsed_args = None

    def __call__(self):
        self.parsed_args = self.parser.parse_args()
        self._check_args()
        return self.parsed_args

    def _check_args(self):
        both_io_and_mapping = self.parsed_args.files_mapping and (self.parsed_args.input or self.parsed_args.output)
        no_io_and_no_mapping = not self.parsed_args.files_mapping and not (self.parsed_args.input or self.parsed_args.output)
        missing_i_o = (self.parsed_args.input and not self.parsed_args.output) or (self.parsed_args.output and not self.parsed_args.input)
        inconsistent_io = self.parsed_args.input and self.parsed_args.output and (len(self.parsed_args.input) != len(self.parsed_args.output))

        if both_io_and_mapping:
            self.parser.error("Cannot use both --files-mapping and --input/--output")

        if no_io_and_no_mapping:
            self.parser.error("Either --files-mapping xor --input/--output must be provided")

        if missing_i_o:
            self.parser.error("If not using --files-mapping, both --input and --output must be provided")

        if inconsistent_io:
            self.parser.error("Number of input files must match number of output files")

    def print_namespace(self):
        print("\nParsed args: (")
        for key, value in self.parsed_args.__dict__.items():
            print(f"\t{key}: {value}")
        print(")\n")


