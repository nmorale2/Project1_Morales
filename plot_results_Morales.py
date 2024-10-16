import subprocess
import time
import matplotlib.pyplot as plt

def run_solver_and_time(csv_filename, block_number):
    """Runs the 2SatSolver.py script for a specific block and returns the time taken."""
    start_time = time.time()
    
    # Create the command to run the solver with the current block
    command = f"python3 2SatSolver.py {csv_filename} --block {block_number}"
    
    # Run the 2SatSolver.py script
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    end_time = time.time()
    return end_time - start_time

def main():
    csv_filename = '2SAT.cnf.csv'  # Your input CSV file with varying clauses
    block_times = []  # List to store times for each block
    block_numbers = []  # List to keep track of block numbers

    with open(csv_filename, 'r') as file:
        block_number = 0
        for line in file:
            # Start a new block when we encounter a line starting with 'c' and a new 'p'
            if line.startswith('c'):
                block_number += 1

            if line.startswith('p'):
                # Time the solver for this block
                elapsed_time = run_solver_and_time(csv_filename, block_number)
                block_times.append(elapsed_time)
                block_numbers.append(block_number)
                print(f"Time taken for block {block_number}: {elapsed_time:.4f} seconds")

    # Plotting the results
    plt.plot(block_numbers, block_times, marker='o')
    plt.title('2-SAT Solver Execution Time per Block')
    plt.xlabel('Block Number')
    plt.ylabel('Time (seconds)')
    plt.xticks(block_numbers)
    plt.grid()
    plt.tight_layout()
    plt.savefig('execution_time_plot.png')
    plt.show()

if __name__ == "__main__":
    main()