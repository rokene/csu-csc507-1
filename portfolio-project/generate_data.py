#!/usr/bin/env python3

import time
import random
import os

# configuration

output_filename1 = 'file1.txt'
output_filename2 = 'file2.txt'

files = [
    output_filename1,
    output_filename2
]

file_size = 1000000

output_huge_filename1 = 'hugefile1.txt'
output_huge_filename2 = 'hugefile2.txt'

huge_file_list = [
    output_huge_filename1,
    output_huge_filename2
]

huge_file_config_attr_source_file = "source_file"
huge_file_config_attr_number_times_append = "num_times"

huge_file_config = {
    output_huge_filename1: {
        huge_file_config_attr_source_file: output_filename1,
        huge_file_config_attr_number_times_append: 1000
    },
    output_huge_filename2: {
        huge_file_config_attr_source_file: output_filename2,
        huge_file_config_attr_number_times_append: 1000
    }
}

# functions and constants

script_name = os.path.basename(__file__)


def count_lines(filename):
    """ Counts the number of lines in the specified file """
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"{script_name}: File {filename} not found.")
        return 0


def generate_and_write_numbers(filename, total_numbers):
    """ Generate random numbers and write them to a file """
    print(f"{script_name}: Creating file {filename} with {total_numbers} numbers")
    with open(filename, 'w') as file:
        for _ in range(total_numbers):
            number = random.randint(-1000000, 1000000)
            file.write(f"{number}\n")


def append_file(source, destination, num):
    print(f"{script_name}: Creating huge file from {source} to {destination} by appending {num} number of times")
    with open(source, 'r') as source_file:
        # Read content from the source file
        content = source_file.read()
        with open(destination, 'a') as destination_file:
            for i in range(num):
                # Append the content to the destination file
                destination_file.write(content)


def print_file_count_duration(filepath, start_time):
    count = count_lines(filepath)
    print(f"{script_name}: Python single-threaded processing {filepath} with {count} numbers took {time.time() - start_time} seconds")


# start


if __name__ == "__main__":
    print(f"{script_name}: Generating data")
    total_start_time = time.time()
    for file in files:
        start_time = time.time()
        generate_and_write_numbers(file, file_size)
        print_file_count_duration(file, start_time)

    for huge_file in huge_file_list:
        start_time = time.time()
        append_file(
            huge_file_config[huge_file][huge_file_config_attr_source_file],
            huge_file,
            huge_file_config[huge_file][huge_file_config_attr_number_times_append])
        print_file_count_duration(huge_file, start_time)
        
    print(f"{script_name}: Complete, script took {(time.time()-total_start_time)/60} minutes.")
