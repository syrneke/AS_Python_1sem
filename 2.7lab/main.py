#вар9
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
for line in input_file:
    clean_line = line.rstrip("n")
    if clean_line != "":
        if len(clean_line) % 2 != 0:
            clean_line = " " + clean_line
        spaces = (50 - len(clean_line)) // 2
        clean_line = " " * spaces + clean_line
    output_file.write(clean_line + "n")
input_file.close()
output_file.close()
