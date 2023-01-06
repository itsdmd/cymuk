# Manual

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Intallation](#intallation)
- [Boundary](#boundary)
- [Configuration](#configuration)
	- [Notes](#notes)
	- [Description](#description)
- [Automation using Script](#automation-using-script)
	- [Notes](#notes-1)
	- [List of Action Codes](#list-of-action-codes)
	- [Testing](#testing)

## Intallation

> Make sure you have `setuptools>=60` installed. Install it with `pip install setuptools`.

Run the following command to install the dependencies:

```bash
pip install -e .
```

## Boundary

"Boundary" is a terminology apply for **jump movements**, indicates the area that have the mouse cursor at the center of it. The root boundary is the screen.

Jump actions will move the cursor to the **center** of the boundary **half the area of the current** boundary in the direction of the jump.

For example, if you perform a jump to the right, the cursor will move to the center point between its current position and the right edge of the boundary, which is also the center of the boundary that takes up half the area to the right of the current boundary.

<img src="img/boundary.png" height="120">

The boundary is only used for and changed by jump actions. The cursor will not be constrained to the boundary when moving the cursor with step movement or the physical mouse.

## Configuration

The configuration file is a JSON file. You can see the template configuration file [here](template-config.json).

The initial run of the program will prompt you to generate a config file with default values. You can modify it afterwards.

> The initial run will cause the program to crash. This is to be expected. You just need to run it again.

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

**`key_centralize`**: Move the cursor to the center of the current boundary.

**`key_centralize_root`**: Move the cursor to the center of the current screen and set boundary to be the current screen.

**`key_click_left`**: Emulate left mouse button click.

**`key_jump_left`**: Move the cursor left in jump mode.

**`key_left`**: Move the cursor left in step mode.

**`key_quit`**: Quit the program.

**`key_screen_next`**: Move the cursor to the center of the next screen in the screen list.

**`key_screen_prev`**: Move the cursor to the center of the previous screen in the screen list.

**`key_scroll_up`**: Emulate scrolling up.

> :warning: Horizontal scrolling is only supported on Linux and macOS. Might work on other *nix systems but not tested.

**`key_toggle_hold_left`**: Emulate left mouse button hold/release.

**`screen_default`**: The index of the screen that will be used as the root screen.

**`screen_list`**: An ordered list of all screens' top-left and bottom-right coordination tuple relative to the combined boundary of all the screens.

**`screen_size`**: The total dimension of all screens, depends on how you set up your screens in the settings.

**`scroll_multiplier`**: Multiplier for scrolling actions.

**`step_multiplier`**: Multiplier for step movements.

## Automation using Script

Besides **Capture** mode which is used to capture key sequences, there's also **Script** mode which is used to automate the actions using a plain text file.

The structure of the script file is as follows:

```plain
<action_code> <argument_0> <argument_1> ...
```

### Notes

- All arguments MUST present and in order as shown in the list above.
- All time-related arguments are in milliseconds.
- The script must always end with `quit` action.

### List of Action Codes

```plain
centralize
centralize_root
click_left -1 -1 1 0    // x, y, clicks, delay
click_right -1 -1 1 0   // x, y, clicks, delay
down 1                  // steps
drag_abs left 0 0 0     // button, x, y, duration | Possible button names: left, right, middle
drag_rel left 0 0 0     // button, x, y, duration
jump_down
jump_left
jump_right
jump_up
left 1                  // steps
move_abs 0 0 0          // x, y | Move relative to absolute coordinate
move_rel 0 0 0          // x, y | Move relative to current position
quit 0                  // code | 0 for normal exit, other values for error
right 1                 // steps
screen_index 0          // index | Negative value to count from the end with -1 being the last screen
screen_next 1           // steps
screen_prev 1           // steps
scroll_down 1 10        // multiplier, delay
scroll_left 1 10        // multiplier, delay
scroll_right 1 10       // multiplier, delay
scroll_up 1 10          // multiplier, delay
toggle_hold_left
toggle_hold_middle
toggle_hold_right
up 1                    // steps
wait 0                  // duration
```

### Testing

You can see the sample script file [here](sample-script.txt). Test it out by running

```bash
python cymuk.py -s ./docs/sample-script.txt
```

A handy website for you to test out the script: [Link](https://www.onlinemictest.com/mouse-test/).
