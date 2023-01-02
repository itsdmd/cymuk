# Manual

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Boundary](#boundary)
- [Configuration](#configuration)
	- [Notes](#notes)
	- [Description](#description)


## Boundary

"Boundary" is a terminology apply for **jump movements**, indicates the area that have the mouse cursor at the center of it. The root boundary is the screen.

Jump actions will move the cursor to the **center** of the boundary **half the area of the current** boundary in the direction of the jump.

For example, if you perform a jump to the right, the cursor will move to the center point between its current position and the right edge of the boundary, which is also the center of the boundary that takes up half the area to the right of the current boundary.

<img src="img/boundary.png" height="120">

The boundary is only used for and changed by jump actions. The cursor will not be constrained to the boundary when moving the cursor with step movement or the physical mouse.

## Configuration

The configuration file is a JSON file. You can see the template configuration file [here](template-config.json).

I highly recommend you to do an initial run of the program to generate a config file with default values for you. You can modify it afterwards.

### Notes

- To improve stability/predictivity of key sequence capturing, **continuous movement isn't possible**, which means holding down a key will only trigger the action once.
- All alphabetic characters are **case-insensitive** but should be in lowercase.
- When using **Shift** in key sequence:
	- For `Shift+1`, the keymap will be **`shift+!`**. Same for other numeric and special characters.
	- For `Shift+Space`, the keymap will be **`shift+none`** (yes, it's weird it works).
		- When there's no `Shift` key in the sequence, **`space`** MUST be used instead.
- The config file's directory is fixed to be the same directory as the executable. If you want to place it in another directory, you can create a symbolic link.
- **All configs MUST be present** in the config file. If any config is missing, the program will ask to create a new config file with the default values.

### Description

**`screen_size`**: The total dimension of all screens, depends on how you set up
 	your screens in the settings.

**`screen_list`**: An ordered list of all screens' top-left and bottom-right coordination tuple relative to the combined boundary of all the screens.

**`screen_default`**: The index of the screen that will be used as the root screen.

**`key_quit`**: Quit the program.

**`key_centralize`**: Move the cursor to the center of the current boundary.

**`key_centralize_root`**: Move the cursor to the center of the current screen and set boundary to be the current screen.

**`key_next_screen`**: Move the cursor to the center of the next screen in the screen list.

**`key_left`**: Move the cursor left in step mode.

**`key_jump_left`**: Move the cursor left in jump mode.

**`key_click_left`**: Emulate left mouse button click.

**`key_toggle_hold_left`**: Emulate left mouse button hold/release.

**`key_scroll_up`**: Emulate scrolling up.

**`step_multiplier`**: Multiplier for step movements.

**`scroll_multiplier`**: Multiplier for scrolling actions.
