import os

# Create a new directory
os.mkdir("sample_dir")
print("Directory 'sample_dir' created.")

# List all files and directories in the current directory
print("Contents of current directory:")
print(os.listdir())

# Remove the created directory
os.rmdir("sample_dir")
print("Directory 'sample_dir' removed.")