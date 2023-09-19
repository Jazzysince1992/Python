# Define the file paths for the input and output files
input_file_path = "Glen/OOPS/input.txt"
output_file_path = "Glen/OOPS/output.txt"

# Read the content of the input file
with open(input_file_path, "r") as input_file:
    input_content = input_file.read()

# Manipulate the content as needed (e.g., let's convert it to uppercase)
manipulated_content = input_content.upper()

# Write the manipulated content to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(manipulated_content)

print("File manipulation complete. Check the output in 'output.txt'.")
