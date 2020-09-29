"""Menu.py file for nuke."""
import os
import platform

import nuke


def get_nuke_dir():
    """Get the .nuke directory based off the system.

    Returns:
        str: The directory path.
    """
    win_dir = os.path.join("C:", "Users", "thomas", ".nuke")
    mac_dir = os.path.join("Users", "thomas", ".nuke")
    linux_dir = os.path.join("home", "thomas", ".nuke")

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


def create_utilities_menu():
    """Create the utilities menu."""
    utilities_menu = nuke.menu("Nuke").addMenu("Utilities")
    utilities_menu.addCommand("Autocrop", "nukescripts.autocrop()")


def create_gizmos_menu():
    """Create the custom gizmos menu."""
    gizmos_menu = nuke.menu("Nodes").addMenu(
        "myGizmos",
        icon="myGizmos_icon.png"
    )
    gizmos_menu.addCommand(
        "bm_CameraShake",
        "nuke.createNode('bm_CameraShake')",
        icon="bm_CameraShake_icon.png"
    )


def create_keyboard_shortcuts():
    """Create keyboard shotcuts."""
    nuke.menu('Nodes').addCommand(
        "Transform/Tracker4",
        "nuke.createNode('Tracker4')",
        "ctrl+alt+t",
        icon="Tracker.png",
        shortcutContext=2
    )


def main():
    """Run functions to setup nuke.

    Will call functions to run.
    """
    directory = get_nuke_dir()
    create_utilities_menu()
    create_gizmos_menu()
    create_keyboard_shortcuts()


if __name__ == "__main__":
    main()
