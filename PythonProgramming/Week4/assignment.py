# File Handling and Exception Handling Assignment

def read_and_write_file(input_filename, output_filename):
    """
    Reads a file and writes a modified version to a new file.

    Parameters:
    input_filename (str): The name of the file to read.
    output_filename (str): The name of the file to write the modified content.
    """
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content: Add line numbers to each line
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file '{input_filename}' or '{output_filename}'.")


# Main program
def main():
    # Prompt the user for the input file name
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content: ")

    # Call the function to process the file
    read_and_write_file(input_filename, output_filename)


# Execute the program
if __name__ == "__main__":
    main()
