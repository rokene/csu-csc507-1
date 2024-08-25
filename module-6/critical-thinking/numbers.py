#!/usr/bin/env python3

import time
import random


output_filename = 'file1.txt'


def count_lines(filename):
    """ Counts the number of lines in the specified file """
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0


def generate_and_write_numbers(filename, total_numbers):
    """ Generate random numbers and write them to a file """
    with open(filename, 'w') as file:
        for _ in range(total_numbers):
            number = random.randint(-1000000, 1000000)
            file.write(f"{number}\n")


if __name__ == "__main__":
    start_time = time.time()
    generate_and_write_numbers(output_filename, 10000000)
    end_time = time.time()
    numbers_count = count_lines(output_filename)
    print(f"Python single-threaded processing {numbers_count} numbers took {end_time - start_time} seconds")
