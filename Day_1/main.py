import os

def read_file(filepath:str) -> list:
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    return data

def solve_p1(filepath:str) -> str:
    data = read_file(filepath)
    data = [int(x) for x in data]

    count = 0
    for i in range(len(data)-1):
        # print(f'{data[i]} vs {data[i+1]} -> {data[i] < data[i+1]}')
        if data[i] < data[i+1]:
            count += 1
    
    return count

def solve_p2(filepath:str) -> str:
    data = read_file(filepath)
    data = [int(x) for x in data]

    count = 0
    for i in range(len(data)-3):
        a = sum([data[i], data[i+1], data[i+2]])
        b = sum([data[i+1], data[i+2], data[i+3]])
        # print(f'{a} vs {b} -> {a < b}')
        if a < b :
            count += 1
    
    return count

def main():
    test_filepath = os.path.join(os.path.dirname(__file__) , 'test_input.txt')
    input_filepath = os.path.join(os.path.dirname(__file__) , 'input.txt')
    
    print(f'Test p1: {solve_p1(test_filepath)}')
    print(f'Real p1: {solve_p1(input_filepath)}')

    print(f'Test p2: {solve_p2(test_filepath)}')
    print(f'Real p2: {solve_p2(input_filepath)}')

    ...

if __name__ == "__main__":
    main()