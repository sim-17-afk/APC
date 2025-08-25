with open("sim.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
    
with open("sim.txt", "a") as file:
    file.seek(0)  # Move the cursor back to the beginning of the file
    file.write("Additional line added.\n")
    print("\nAfter appending:")
    print(content)