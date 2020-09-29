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


def set_knob_defaults():
    """Set the knob defaults."""
    # Shutter Offset default
    nuke.knobDefault("shutteroffset", "centered")
    # For some reason, TimeBlur doesn't get affected by the previous command.
    # As far as I can see, it's the only node that doesn't get affected.
    nuke.knobDefault("TimeBlur.shutteroffset", "centered")

    # Tracker defaults
    nuke.knobDefault(
        "Tracker4.label",
        "Motion: [value transform]\nRef Frame: [value reference_frame]"
    )


def main():
    """Execute code on initialization."""
    add_custom_plugin_paths()
    set_knob_defaults()


if __name__ == "__main__":
    main()
