"""Init.py file for .nuke repo.

This file will be used for:

    * Adding custom plug-in paths
    * Setting knob defaults
    * Setting custom formats
"""
import nuke


def add_custom_plugin_paths():
    """Add the custom plugin paths."""
    nuke.pluginAddPath('./gizmos')
    nuke.pluginAddPath('./python')


def main():
    """Execute code on initialization."""
    add_custom_plugin_paths()


if __name__ == "__main__":
    main()
