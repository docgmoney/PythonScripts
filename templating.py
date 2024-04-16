import os
import sys

def create_dir_structure(base_path, structure):
    for directory in structure:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

        # If the directory is an enumeration type, create a corresponding .txt file.
        if directory.startswith('Enumeration/'):
            file_name = f"{directory.split('/')[-1]}.txt"
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'w') as f:
                f.write('')  # Create an empty text file.
            print(f"Created file: {file_path}")

    print("Directory structure creation complete.")

def main():
    # Check if the user provided a path argument.
    if len(sys.argv) != 2:
        print("Usage: python3 templating_directories.py <full_path_to_directory>")
        sys.exit(1)

    # Define the base path for the OSCP directory from the first argument.
    base_path = sys.argv[1]

    # Define the structure of directories as a list.
    directory_structure = [
        'Setting up connections',
        'Enumeration/Nmap_Scans',
        'Enumeration/Web_Portion',
        'Enumeration/gobuster',
        'Enumeration/dirbuster',
        'Enumeration/google dorks',
        'Enumeration/shodan',
        'Enumeration/nikto',
        'exploits/exploit_code',
        'Priv_Esc',
        'Proof',
        'Helpful tips & Comms'
    ]

    # Call the function with the base path and the directory structure.
    create_dir_structure(base_path, directory_structure)

if __name__ == "__main__":
    main()
