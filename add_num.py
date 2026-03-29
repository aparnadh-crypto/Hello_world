# Read numbers from input.txt
with open("input.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

# Process (sum)
total = sum(numbers)

# Write to output.txt
with open("output.txt", "w") as f:
    f.write(f"Sum = {total}\n")

print("Processing complete. Output written to output.txt")
