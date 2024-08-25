#!/usr/bin/env python3

import time
import multiprocessing

def process_half(filename, start_line, end_line):
  with open(filename, 'r') as f, open('newfile1-split-read.txt', 'a') as out_f:
    for i, line in enumerate(f):
      if start_line <= i < end_line:
        number = int(line)
        out_f.write(str(number * 2) + '\n')


def split_and_read_multiprocess(filename):
  start_time = time.time()
  with open(filename, 'r') as f:
    total_lines = sum(1 for _ in f)
    mid_point = total_lines // 2

  p1 = multiprocessing.Process(target=process_half, args=(filename, 0, mid_point))
  p2 = multiprocessing.Process(target=process_half, args=(filename, mid_point, total_lines))

  p1.start()
  p2.start()
  p1.join()
  p2.join()

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

  time_split_read = split_and_read_multiprocess(filename)
  print(f"Time taken to split and read w/ multiprocessing: {time_split_read:.2f} seconds")

if __name__ == "__main__":
  main()
