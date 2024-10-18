import argparse
import os
import subprocess

def run_file(file_path):

    '''
    Runs the file that the user enters
    '''
    if os.path.isfile(file_path):
        try:
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Run a Python file from the command line.")
    parser.add_argument('file', type=str, help='The path to the Python file to run')

    # Parse the arguments
    args = parser.parse_args()

    # Run the specified file
    run_file(args.file)

if __name__ == "__main__":
    main()
