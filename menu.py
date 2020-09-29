"""Menu.py file for nuke."""
import platform


def get_nuke_dir():
    """Get the .nuke directory based off the system.

    Returns:
        str: The directory path.
    """
    win_dir = "C:/Users/thomas/.nuke"
    mac_dir = "/Users/thomas/.nuke"
    linux_dir = "/home/thomas/.nuke"

    platform_system = platform.system()

    if platform_system == "Windows":
        directory = win_dir

    elif platform_system == "Darwin":
        directory = mac_dir

    elif platform_system == "Linux":
        directory = linux_dir

    else:
        directory = None

    return directory


def main():
    """Run functions to setup nuke.

    Will call functions to run.
    """
    directory = get_nuke_dir()


if __name__ == "__main__":
    main()
