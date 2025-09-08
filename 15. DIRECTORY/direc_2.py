import os

# Get current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Create a new directory
os.mkdir("test_dir")
print("Directory 'test_dir' created.")

# Rename the directory
os.rename("test_dir", "renamed_dir")
print("Directory renamed to 'renamed_dir'.")

# List all files and directories in the current directory
print("Contents of current directory:")
print(os.listdir())

# Remove the renamed directory
os.rmdir("renamed_dir")
print("Directory 'renamed_dir' removed.")

os.scandir(current_dir)
print("Iterating through current directory:")
for entry in os.listdir(current_dir):
    print(entry)