import csv
import secrets
import subprocess
from pathlib import Path

# Set the working directory to locate the data files
cwd = Path.cwd() / "drive/MyDrive/Colab Notebooks"

# Open the input and output CSV files
with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    
    # Write the header to the output file
    writer.writeheader()
    
    # Process each user in the input file
    for user in reader:
        # Generate a secure random password
        user["password"] = secrets.token_hex(8)
        
        # Prepare the useradd command
        useradd_cmd = [
            "/sbin/useradd",
            "-c", user["real_name"],
            "-m",
            "-G", "users",
            "-p", user["password"],
            user["username"]
        ]
        
        # Execute the useradd command
        subprocess.run(useradd_cmd, check=True)
        
        # Write the updated user data to the output file
        writer.writerow(user)
