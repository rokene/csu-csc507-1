#!/usr/bin/env python3

import time
import multiprocessing
import os

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


def sum_files(file1, file2, output_file):
    """
    Sum corresponding lines from two files and write the results to a new file.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line1, line2 in zip(f1, f2):
            sum_result = int(line1.strip()) + int(line2.strip())
            out.write(f"{sum_result}\n")


def worker(file1, file2, output_file, start, end):
    """
    Process a segment of two files from start to end line numbers.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Skip to the start line
        for _ in range(start):
            next(f1)
            next(f2)

        with open(output_file, 'w') as out:
            for i in range(end - start):
                line1 = next(f1, None)
                line2 = next(f2, None)
                if line1 is None or line2 is None:
                    break
                sum_result = int(line1.strip()) + int(line2.strip())
                out.write(f"{sum_result}\n")


def parallel_sum(file1, file2, output_file, num_parts):
    """
    Split the task into parts and sum files in parallel.
    """
    start_time = time.time()
    file1_size = count_lines(file1)
    file2_size = count_lines(file2)

    if file1_size != file2_size:
        ValueError(f"Source file sizes must match: {file1_size}, {file2_size}")

    total_lines = file1_size
    lines_per_part = total_lines // num_parts

    # Create and start a process for each part
    processes = []
    for i in range(num_parts):
        start_line = i * lines_per_part
        end_line = (i + 1) * lines_per_part if i != num_parts - 1 else total_lines
        part_output = f"{output_file}_part_{i}"
        p = multiprocessing.Process(target=worker, args=(file1, file2, part_output, start_line, end_line))
        processes.append(p)
        p.start()
        print(f"{script_name}: Started process {p}")

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Combine part files into a single final output
    print(f"{script_name}: Combining parts")
    with open(output_file, 'w') as final_out:
        for i in range(num_parts):
            part_output = f"{output_file}_part_{i}"
            with open(part_output, 'r') as part_in:
                final_out.writelines(part_in.readlines())

    end_time = time.time()
    return end_time - start_time


def main():
    print(f"{script_name}: Analysis running")
    filename1 = 'hugefile1.txt'
    filename2 = 'hugefile2.txt'
    output_filename = 'totalfile.txt'
    num_parts = 10  # Number of parts to divide the processing
    time_taken = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing: {time_taken:.2f} seconds")


if __name__ == "__main__":
    main()
