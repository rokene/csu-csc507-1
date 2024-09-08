#!/usr/bin/env python3

import time
import multiprocessing
import os
import shutil


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
    file1_lines = count_lines(file1)
    file1_size = os.path.getsize(file1)
    file2_size = os.path.getsize(file2)

    if file1_size != file2_size:
        ValueError(f"Source file sizes must match: {file1_size}, {file2_size}")

    total_lines = file1_lines
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
        p.join(timeout=600)
        print(f"{script_name}: Process {p} synced.")
        
    if any(p.is_alive() for p in processes):
        Exception(f"{script_name}: Error, some processes did not finish successfully.")

    # Combine part files into a single final output
    try:
        with open(output_file, 'w') as final_out:
            for i in range(num_parts):
                part_output = f"{output_file}_part_{i}"
                print(f"{script_name}: Combining results in {part_output}")
                with open(part_output, 'r') as part_in:
                    shutil.copyfileobj(part_in, final_out)
                os.remove(part_output)
    except Exception as e:
        print(f"Error combining parts: {str(e)}")

    end_time = time.time()
    return end_time - start_time, file1_lines


def main():
    print(f"{script_name}: Analysis running")
    filename1 = 'hugefile1.txt'
    filename2 = 'hugefile2.txt'
    output_filename = 'totalfile.txt'

    num_parts = 2
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

    num_parts = 6
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

    num_parts = 10
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

    num_parts = 15
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

    num_parts = 20
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

    num_parts = 25
    time_taken_sec, lines = parallel_sum(filename1, filename2, output_filename, num_parts)
    print(f"{script_name}: Time taken to process and sum files using multiprocessing ({num_parts}): {time_taken_sec:2f} second(s)")
    print(f"{script_name}: Rate of processing, {lines/time_taken_sec} lines/second")

if __name__ == "__main__":
    main()
