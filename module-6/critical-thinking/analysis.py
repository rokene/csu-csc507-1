#!/usr/bin/env python3

import time
import multiprocessing
import os


def process_chunk(filename, start_line, end_line):
    # Add your processing logic here
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if start_line <= i < end_line:
                # Process the line
                pass

def split_and_read_multiprocess_inmem(filename, num_chunks):
    start_time = time.time()

    # Determine the total number of lines
    with open(filename, 'r') as f:
        total_lines = sum(1 for _ in f)

    # Calculate chunk size
    chunk_size = total_lines // num_chunks
    processes = []

    # Create and start a process for each chunk
    for i in range(num_chunks):
        start_line = i * chunk_size
        # Ensure the last chunk processes until the end of the file
        end_line = total_lines if i == num_chunks - 1 else (i + 1) * chunk_size
        p = multiprocessing.Process(target=process_chunk, args=(filename, start_line, end_line))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    end_time = time.time()
    return end_time - start_time


def split_file(filename, num_parts):
    """
    Splits the file into smaller files.
    """
    with open(filename, 'r') as f:
        total_lines = sum(1 for _ in f)
    
    lines_per_part = total_lines // num_parts
    file_parts = []

    with open(filename, 'r') as f:
        for part in range(num_parts):
            part_filename = f"{filename}_part_{part}"
            file_parts.append(part_filename)
            with open(part_filename, 'w') as part_file:
                start_line = part * lines_per_part
                end_line = (part + 1) * lines_per_part if part != num_parts - 1 else total_lines

                for i, line in enumerate(f):
                    if start_line <= i < end_line:
                        part_file.write(line)
                    if i >= end_line - 1:
                        break

    return file_parts

def process_file_part(part_filename):
    """
    Process each part of the file.
    """
    # Add your processing logic here
    with open(part_filename, 'r') as f:
        for line in f:
            # Process each line as needed
            pass

def split_and_read_multiprocess(filename, num_parts):
    start_time = time.time()

    # Split the file into smaller parts
    file_parts = split_file(filename, num_parts)

    # Create and start a process for each file part
    processes = []
    for part_filename in file_parts:
        p = multiprocessing.Process(target=process_file_part, args=(part_filename,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    end_time = time.time()

    return end_time - start_time


def read_entire_file(filename):
  start_time = time.time()
  with open(filename, 'r') as f, open('newfile1-in-mem.txt', 'w') as out_f:
    lines = f.readlines()
    for line in lines:
      number = int(line)
      out_f.write(str(number * 2) + '\n')
  end_time = time.time()
  return end_time - start_time


def read_one_row_at_a_time(filename):
  start_time = time.time()
  with open(filename, 'r') as f, open('newfile1-per-row.txt', 'w') as out_f:
    for line in f:
      number = int(line)
      out_f.write(str(number * 2) + '\n')
  end_time = time.time()
  return end_time - start_time


def main():
  filename = 'file1.txt'

  time_entire_file = read_entire_file(filename)
  print(f"Time taken to read entire file: {time_entire_file:.2f} seconds")

  time_one_row = read_one_row_at_a_time(filename)
  print(f"Time taken to read one row at a time: {time_one_row:.2f} seconds")

  num_parts = 10
  time_split_read_files = split_and_read_multiprocess(filename, num_parts)
  print(f"Time taken to split files into smaller files ({num_parts}) and read w/ multiprocessing: {time_split_read_files:.2f} seconds")
  
  num_parts = 5
  time_split_read_files = split_and_read_multiprocess(filename, num_parts)
  print(f"Time taken to split files into smaller files ({num_parts}) and read w/ multiprocessing: {time_split_read_files:.2f} seconds")
  
  num_parts = 20
  time_split_read_files = split_and_read_multiprocess(filename, num_parts)
  print(f"Time taken to split files into smaller files ({num_parts}) and read w/ multiprocessing: {time_split_read_files:.2f} seconds")
  
  num_parts = 10
  time_split_read_files = split_and_read_multiprocess_inmem(filename, num_parts)
  print(f"Time taken to split data in memory ({num_parts}) w/ multiprocessing: {time_split_read_files:.2f} seconds")
  
  num_parts = 5
  time_split_read_files = split_and_read_multiprocess_inmem(filename, num_parts)
  print(f"Time taken to split data in memory ({num_parts}) w/ multiprocessing: {time_split_read_files:.2f} seconds")
  
  num_parts = 20
  time_split_read_files = split_and_read_multiprocess_inmem(filename, num_parts)
  print(f"Time taken to split data in memory ({num_parts}) w/ multiprocessing: {time_split_read_files:.2f} seconds")
  

if __name__ == "__main__":
  main()
