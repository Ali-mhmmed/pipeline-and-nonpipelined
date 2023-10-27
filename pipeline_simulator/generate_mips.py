import random
import sys

instructions = [
    "add $t0, $t1, $t2",
    "sub $t3, $t4, $t5",
    "mul $t6, $t7, $t8",
    "div $t9, $t0",
    "lw $t0, 0($t1)",
    "sw $t2, 4($t3)",
    "beq $t4, $t5, label",
    "bne $t6, $t7, label",
    "j label",
]


if len(sys.argv) != 2:
    print("Usage: python generate_random_mips.py <number_of_instructions>")
    sys.exit(1)

try:
    num_instructions = int(sys.argv[1])
except ValueError:
    print("Invalid number of instructions. Please provide an integer.")
    sys.exit(1)


output_filename = f"mips_instructions.asm"
with open(output_filename, "w") as file:
    for _ in range(num_instructions):
        # Generate a random instruction
        random_instruction = random.choice(instructions)
        file.write(random_instruction + "\n")


