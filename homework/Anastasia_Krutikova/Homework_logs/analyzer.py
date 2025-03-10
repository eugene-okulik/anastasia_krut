import argparse
import os

# ERROR, WARN
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File name")
    parser.add_argument("-d", '--date', help="Data for search")
    # parser.add_argument("--full", help="Full", action="store_true")
    parser.add_argument("--text", help="Text to search")
    return parser.parse_args()

def search_in_file(file_path, search_text, filename):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if search_text in line:
                print_result(line_number, line, search_text, filename)


def print_result(line_number, line, search_text, filename):
    words = line.split()
    if search_text in words:
        search_index = words.index(search_text)

        start_index = max(search_index - 5, 0)
        end_index = min(search_index + 6, len(words))

        segment = ' '.join(words[start_index:end_index])
        print(f"Файл: {filename}, Строка: {line_number}, Текст: {segment}")


def search_logs(log_path, search_text):
    for filename in os.listdir(log_path):
        if filename.endswith('.log'):
            file_path = os.path.join(log_path, filename)
            search_in_file(file_path, search_text, filename)


args = parse_arguments()
search_logs(args.file, args.text)

