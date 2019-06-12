import sys
import pandas as pd

def load_file(file):
    data = pd.read_csv(file)
    return data

def main():
    argv = sys.argv
    data = load_file(argv[1])
    print(data)

if __name__ == "__main__":
    main()
