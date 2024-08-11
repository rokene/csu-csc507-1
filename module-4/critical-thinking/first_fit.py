#!/usr/bin/env python3

import random


def generate_test_data(num_blocks=10, max_block_size=500, num_processes=15, max_process_size=200):
  """
  Generates test data for memory allocation algorithms.

  Args:
      num_blocks: Number of memory blocks.
      max_block_size: Maximum size of a memory block.
      num_processes: Number of processes.
      max_process_size: Maximum size of a process.

  Returns:
      A tuple containing two lists: memory_blocks and process_sizes.
  """

  memory_blocks = [random.randint(1, max_block_size) for _ in range(num_blocks)]
  process_sizes = [random.randint(1, max_process_size) for _ in range(num_processes)]

  return memory_blocks, process_sizes


def first_fit(memory_blocks, process_size):
    """
    Implements the First-Fit memory allocation algorithm.

    Args:
        memory_blocks: A list representing available memory blocks and their sizes.
        process_size: The size of the process to be allocated.

    Returns:
        A tuple containing:
            - The size of the allocated block if successful, otherwise -1.
            - The updated list of memory blocks after allocation (or the original 
              list if allocation failed).
    """
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= process_size:
            allocated = memory_blocks[i]
            memory_blocks[i] -= process_size
            return allocated, memory_blocks
    return -1, memory_blocks  # No suitable block found


def main():
  # Generate test data
    memory_blocks, process_sizes = generate_test_data()
    unallocated_process = []

    print("Initial Process Sizes:", process_sizes)
    print("Initial Memory Blocks:", memory_blocks)

    # Simulate First-Fit allocation
    for process_size in process_sizes:
        allocated, memory_blocks = first_fit(memory_blocks, process_size)
        if allocated != -1:
            print(f"Process of size {process_size} allocated {allocated} units.")
        else:
            print(f"Process of size {process_size} could not be allocated.")
            unallocated_process.append(process_size)

    print("Final Memory Blocks:", memory_blocks)

    if len(unallocated_process) > 0:
      print("Unallocated processes: ", unallocated_process)


if __name__ == "__main__":
  main()
