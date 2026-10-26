
import os
import shutil
import platform
import subprocess
from pathlib import Path


def show_system_info():
    print("\n--- System Information ---")
    print("Operating System:", platform.system())
    print("OS Release:", platform.release())
    print("Machine:", platform.machine())
    print("Python Version:", platform.python_version())
    print("Current Directory:", os.getcwd())


def list_files():
    path = input("Enter directory path (default: current): ").strip()
    directory = Path(path or ".")

    if not directory.is_dir():
        print("Error: Directory does not exist.")
        return

    print(f"\nContents of {directory.resolve()}:")

    for item in sorted(directory.iterdir()):
        kind = "Directory" if item.is_dir() else "File"
        print(f"{kind:10} {item.name}")


def show_disk_usage():
    path = input("Enter path (default: current directory): ").strip()
    target = Path(path or ".")

    if not target.exists():
        print("Error: Path does not exist.")
        return

    usage = shutil.disk_usage(target.resolve())

    print("\n--- Disk Usage ---")
    print(f"Total:     {usage.total / (1024**3):.2f} GB")
    print(f"Used:      {usage.used / (1024**3):.2f} GB")
    print(f"Free:      {usage.free / (1024**3):.2f} GB")


def create_directory():
    name = input("Enter new directory name: ").strip()

    if not name:
        print("Error: Directory name cannot be empty.")
        return

    path = Path(name)

    if path.exists():
        print("Error: Path already exists.")
        return

    path.mkdir(parents=True)
    print("Directory created:", path.resolve())


def search_files():
    folder = input("Enter directory to search: ").strip() or "."
    keyword = input("Enter filename keyword: ").strip()

    root = Path(folder)

    if not root.is_dir():
        print("Error: Directory does not exist.")
        return

    if not keyword:
        print("Error: Keyword cannot be empty.")
        return

    print("\n--- Search Results ---")
    found = False

    for path in root.rglob("*"):
        if keyword.lower() in path.name.lower():
            print(path)
            found = True

    if not found:
        print("No matching files found.")


def run_linux_command():
    if platform.system() != "Linux":
        print("This option is available only on Linux.")
        return

    commands = {
        "1": ("Current directory", ["pwd"]),
        "2": ("Current user", ["whoami"]),
        "3": ("System uptime", ["uptime"]),
        "4": ("Memory usage", ["free", "-h"]),
        "5": ("Filesystem usage", ["df", "-h"]),
        "6": ("Kernel information", ["uname", "-a"]),
    }

    print("\n--- Linux Commands ---")
    for key, (description, _) in commands.items():
        print(f"{key}. {description}")

    choice = input("Choose command: ").strip()

    if choice not in commands:
        print("Invalid choice.")
        return

    description, command = commands[choice]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        print(f"\n--- {description} ---")
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print("Error:", result.stderr.strip())
        if result.returncode != 0:
            print("Command exit code:", result.returncode)

    except (OSError, subprocess.TimeoutExpired) as error:
        print("Command failed:", error)


def main():
    while True:
        print("\n===== Linux System Operations Toolkit =====")
        print("1. Show system information")
        print("2. List directory contents")
        print("3. Show disk usage")
        print("4. Create a directory")
        print("5. Search for files")
        print("6. Run a safe Linux command")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_system_info()
        elif choice == "2":
            list_files()
        elif choice == "3":
            show_disk_usage()
        elif choice == "4":
            create_directory()
        elif choice == "5":
            search_files()
        elif choice == "6":
            run_linux_command()
        elif choice == "0":
            print("Exiting toolkit. Keep building!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
