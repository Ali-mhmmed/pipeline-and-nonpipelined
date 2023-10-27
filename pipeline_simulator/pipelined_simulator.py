import time
import threading

# Function to simulate an instruction execution
def simulate_instruction(thread_number, instruction):
    global total_operations
    for _ in range(10):  # Simulating 10 instructions per thread
        time.sleep(0.00082)  # Sleep for 0.0008 seconds (simulating pipeline delay)
        counter_lock.acquire()  # Acquire the lock to update the counter safely
        total_operations += 1  # Update the total_operations counter
        counter_lock.release()  # Release the lock after updating the counter
        time.sleep(0.0002)  # Sleep for an additional 0.0002 seconds between instructions

def read_instructions_from_file(filename):
    with open(filename, 'r') as file:
        instructions = file.readlines()
    return instructions

if __name__ == "__main__":
    start_time = time.time()
    total_operations = 0
    counter_lock = threading.Lock()  # Lock to ensure thread-safe counter updates

    threads = []
    instructions = read_instructions_from_file("mips_instructions.asm")
    counter = 1

    # Create and start five threads
    for i in range(1, 6):
        thread = threading.Thread(target=simulate_instruction, args=(i, instructions[i-1].strip()))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"\n\nTotal operations executed: {total_operations}")
    print(f"Time taken by Pipelined Execution = {(end_time - start_time)} seconds\n\n")
