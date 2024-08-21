import os

def read_file(filepath:str) -> list:
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    return data


def main():
    test_filepath = os.path.join(os.path.dirname(__file__) , 'test_input.txt')
    input_filepath = os.path.join(os.path.dirname(__file__) , 'input.txt')

    ...

if __name__ == "__main__":
    main()