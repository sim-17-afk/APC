with open("sim.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
    
with open("sim.txt", "a") as file:
    file.seek(0)  # Move the cursor back to the beginning of the file
    file.write("Additional line added.\n")
    print("\nAfter appending:")
    print(content)
    
    # Using w+ mode: Overwrites or creates the file, then writes and reads
with open("sim.txt", "w+") as file:
    file.write("This is a new file content.\n")
    file.write("Additional line added.\n")
    file.seek(0)  # Move cursor to the beginning to read
    print("File Content after w+ mode:")
    print(file.read())