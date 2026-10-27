
from pathlib import Path


def analyze_extensions(directory):
    folder = Path(directory)

    if not folder.is_dir():
        print("Error: Directory does not exist.")
        return {}

    extension_counts = {}

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()

            if not extension:
                extension = "[no extension]"

            extension_counts[extension] = (
                extension_counts.get(extension, 0) + 1
            )

    return extension_counts


directory = input("Enter directory path: ").strip()

results = analyze_extensions(directory)

if results:
    print("\n--- File Extension Report ---")

    for extension, count in sorted(results.items()):
        print(f"{extension}: {count} file(s)")
    print("\nTotal files:", sum(results.values()))
elif Path(directory).is_dir():
    print("No files found in the directory.")
