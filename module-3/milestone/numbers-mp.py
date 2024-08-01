#!/usr/bin/env python3

import os
import time
import random
from multiprocessing import Pool, cpu_count

output_filename = 'file2-mp.txt'

def generate_numbers(start, segment_size):
    """ Generate a segment of the total numbers with buffering """
    end = start + segment_size
    buffer_size = 10000  # Size of the buffer
    buffer = []  # Initialize the buffer

    with open(f"temp_{start}.txt", 'w') as file:
        for _ in range(start, end):
            number = random.randint(-1000000, 1000000)
            buffer.append(f"{number}\n")
            if len(buffer) >= buffer_size:
                file.writelines(buffer)  # Write buffer to file when full
                buffer = []  # Reset the buffer
        
        if buffer:  # Write any remaining numbers in the buffer
            file.writelines(buffer)

def combine_files(num_segments, segment_size):
    """ Combine all temporary files into the final output file """
    with open(output_filename, 'w') as outfile:
        for i in range(num_segments):
            temp_file = f"temp_{i * segment_size}.txt"
            with open(temp_file, 'r') as infile:
                outfile.write(infile.read())
            os.remove(temp_file)

def count_lines(filename):
    """ Counts the number of lines in the specified file """
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0

if __name__ == "__main__":
    start_time = time.time()
    num_cores = cpu_count()
    total_numbers = 1000000

    # Ensure the total_numbers can be evenly divided by num_cores
    segment_size = total_numbers // num_cores
    if total_numbers % num_cores != 0:
        segment_size += 1  # Adjust segment size to cover all numbers

    num_segments = (total_numbers + segment_size - 1) // segment_size  # Adjust the number of segments

    with Pool(num_cores) as pool:
        pool.starmap(generate_numbers, [(i * segment_size, min(segment_size, total_numbers - i * segment_size)) for i in range(num_segments)])

    combine_files(num_segments, segment_size)

    end_time = time.time()
    numbers_count = count_lines(output_filename)
    print(f"Multiprocessing {numbers_count} numbers with {num_cores} cores took {end_time - start_time} seconds")
