import os

def read_gitignore(path):
    ignore_list = []

    gitignore_path = os.path.join(path, '.gitignore')

    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            for line in file:
                # Strip whitespace and comments
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_list.append(line.rstrip('/'))
    return ignore_list


def get_directory_tree(startpath, exclude_dirs=None):
    lines = []

    exclude_dirs = set(exclude_dirs or [])

    for root, dirs, files in os.walk(startpath):

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        root_dir = os.path.basename(root)

        if any(os.path.basename(root) == item for item in exclude_dirs):
            lines.append(f"{indent}|-- {root_dir}/")
            dirs[:] = []  # Skip all subdirectories
            files[:] = []  # Skip all files
        else:
            line = f"{indent}|-- {root_dir}/"
            lines.append(line)

            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                if file == "DirectoryTreeGenerator.py":
                    continue
                lines.append(f"{sub_indent}| {file}")

    return lines


def save_tree_to_text(tree_structure, output_file):
    """Saves the directory tree structure to a text file."""
    with open(output_file, 'w') as file:
        for line in tree_structure:
            file.write(line + '\n')


def create_directory_tree_image():
    startpath = input("Enter the directory path: ")
    
    if not os.path.exists(startpath):
        print("Invalid directory path! Please try again.")
        return
    
    exclude_dirs = read_gitignore(startpath)
    
    # Get the directory tree structure as a list of lines
    tree_structure = get_directory_tree(startpath, exclude_dirs)
    
    # Output file name
    output_file = input("Enter the output text file name (e.g., tree_structure.txt): ")
    
    
    save_tree_to_text(tree_structure, output_file)


if __name__ == "__main__":
    create_directory_tree_image()