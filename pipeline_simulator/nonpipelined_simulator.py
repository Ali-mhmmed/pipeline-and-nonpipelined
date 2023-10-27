import time

def simulate_instruction(instruction):
    # Simulate the execution of a single instruction here
    
    # Simulate a delay to represent the time taken by each instruction
    time.sleep(0.000802)  # Wait for 0.008 seconds for each instruction

def simulate_time(file_path):
    # Read instructions from the file and simulate their execution
    with open(file_path, 'r') as file:
        instructions = file.readlines()
        for instruction in instructions:
            # Remove leading and trailing whitespaces
            instruction = instruction.strip()
            # Simulate the execution of the instruction
            simulate_instruction(instruction)

if __name__ == "__main__":
    # Specify the file path containing instructions
    file_path = "mips_instructions.asm"  # Replace this with the actual file path

    start_time = time.time()

    # Simulate non-pipelined execution by reading instructions from the file
    simulate_time(file_path)

    end_time = time.time()
    print(f"\n\nTime taken by Non-pipelined Execution = {(end_time - start_time)} seconds\n\n")
