import argparse
import os
import subprocess

from . import corpus
from interaction_network import interaction_network


def run_file(file_path):

    if os.path.isfile(file_path):
        try:
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run a Python file from the command line.")

    subparsers = parser.add_subparsers(dest='command', help="Script to run")

    corpus_parser = subparsers.add_parser('corpus', help="Search PubMed")
    corpus_parser.add_argument('term', type=str,
                               help="The search term for PubMed")

    graph_parser = subparsers.add_parser('interaction network',
                                          help="Generate graph")
    graph_parser.add_argument('term', type=str,
                               help="The search term for PubMed")

    parser.add_argument('file', type=str, nargs='?',
                        help='The path to the Python file to run')

    args = parser.parse_args()

    if args.command == 'corpus':
        ids = corpus.get_ids(args.term)
        corpus.make_text_folder(args.term, ids)
    elif args.command == 'interaction network':
        interaction_network(args.term)
    elif args.file:
        run_file(args.file)
    else:
        print("Please specify a file to run or a valid subcommand.")


if __name__ == "__main__":
    main()
