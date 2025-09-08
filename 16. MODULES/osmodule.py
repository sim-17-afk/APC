import os

# Get and print the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Create a new directory
os.mkdir("sample_dir")
print("Directory 'sample_dir' created.")

# List all files and directories in the current directory
print("Contents of current directory:")
for entry in os.listdir(current_dir):
    print(entry)

# Remove the created directory
os.rmdir("sample_dir")
print("Directory 'sample_dir' removed.")