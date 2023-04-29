 
import os

# Define the directory name and file names
directory_name = "CostOptimization"
file_names = ["aws_cost_explorer.py", "terraform.py", "streamlit.py", "fast_api.py", "Dockerfile"]

# Create the directory
try:
    os.mkdir(directory_name)
except FileExistsError:
    print(f"Directory '{directory_name}' already exists")

# Create empty files in the directory
for filename in file_names:
    with open(f"{directory_name}/{filename}", "w") as f:
        pass
