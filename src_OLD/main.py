import os

from command_line.CLParser import CLParser
from script.FileHandler import FileHandler
from script.TableMaker import TableMaker
from script.PrintHandler import PrintHandler


def main():

    cl_parser = CLParser()

    args = cl_parser()
    cl_parser.print_namespace()

    table_maker = TableMaker(header=not args.header_disabled)
    file_handler = FileHandler()

    if args.files_mapping:
        file_handler.handle_json(args.files_mapping)
    else:
        file_handler(args.input, args.output)

    print_handler = PrintHandler()

    print_handler.print_separator(symbol='@')
    for input_file, output_file in zip(file_handler.input_files, file_handler.output_files):
        if (not os.path.exists(input_file)) or (os.path.getsize(input_file) == 0):
            print_handler.print_status_skipped(input_file)
            print_handler.update_resume(output_file, 0)
            print_handler.print_separator()
            continue

        table = table_maker(input_file, output_file)
        written = file_handler.write_table(table, output_file)

        if written:
            print_handler.print_status_updated(input_file, output_file, table)
            print_handler.update_resume(output_file, 1)
        else:
            print_handler.print_status_unchanged(output_file, table)
            print_handler.update_resume(output_file, 2)

        print_handler.print_separator()

    print_handler.print_separator(symbol='@')
    print_handler.print_resume()


if __name__ == '__main__':
    main()

