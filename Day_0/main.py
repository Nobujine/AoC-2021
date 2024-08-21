import os

def read_file(filepath:str) -> list:
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    return data

def solve_p1(filepath:str) -> str:
    data = read_file(filepath)
    data = [int(x) for x in data]

    ...

def solve_p2(filepath:str) -> str:
    data = read_file(filepath)
    data = [int(x) for x in data]
    ...

def main():
    test_filepath = os.path.join(os.path.dirname(__file__) , 'test_input.txt')
    input_filepath = os.path.join(os.path.dirname(__file__) , 'input.txt')

    print(f'Test p1: {solve_p1(test_filepath)}')
    print(f'Real p1: {solve_p1(input_filepath)}')

    # print(f'Test p2: {solve_p2(test_filepath)}')
    # print(f'Real p2: {solve_p2(input_filepath)}')    

    ...

if __name__ == "__main__":
    main()