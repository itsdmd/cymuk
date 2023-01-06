# cymuk

**cymuk** (pronounced
[/ˈsaɪmʌk/](http://ipa-reader.xyz/?text=%CB%88sa%C9%AAm%CA%8Ck&voice=Joey)) is a _lightweight_, _portable (WIP)_ and _cross-platform_ Python program that allows you to control the mouse cursor with keyboard.

This project is written in Python 3 with the helps of [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to control the mouse and [pynput](https://pynput.readthedocs.io/en/latest/) to listen for keyboard events.

## Features

- Perform actions/movements when a pre-defined key sequence is pressed using **Capture** mode _(default)_.
- Automate the actions using a plain text file in **Script** mode.
- Convinient **Monitor** mode to continuously print out the mouse cursor's position on the screen to help with scripting/configuring.
- _WIP_: **Record** mode to record your series of actions and export them as a plain text file.
- Fully **configurable** keybindings.
	- Support single keystroke (eg. `a`).
	- Support _"tricky"_ combinations (eg. `Shift+Space` and `Shift+Alt+Space` can be mapped to different actions).
- Support **multiple monitors** setup and treat each one individually.
- Two movement modes:
	- _**Step**_: move the cursor by a small amount (default: 10px).
	- _**Jump**_: move the cursor to the center of a portion of the screen (see [Boundary](docs/MANUAL.md#boundary)).

## Usage

### Requirements

#### Dependencies

- Python 3.6+
	- Can technically run on Python 3.0, but for stability 3.6 and upward is strongly recommended.
- Windows 7+
	- Might run on older systems, but not tested.
- macOS 10.12+ (see [prerequisites](https://pynput.readthedocs.io/en/latest/limitations.html#macos))
	- _Note_: This is just theoretically possible. I don't have a macOS machine (and too busy/lazy to setup a VM) to test it.
- Linux with _X_ server OR _uinput_ (see
  [prerequisites](https://pynput.readthedocs.io/en/latest/limitations.html#linux))

### Manual

See [MANUAL](docs/MANUAL.md).


## FAQ

### Why did you decided to write this?

Who doesn't want to improve their productivity by 1%? I know I do.

Jokes aside, this project is heavily inspired by [keynav](https://github.com/jordansissel/keynav), a wonderful tool for X11 systems that I have been using for a few years now (I'm a huge fan of **keyboard-driven workflows**). The [_'Jump'_ mode](docs/MANUAL.md#boundary) is basically a clone of keynav's movement style.

However, it's built for X window systems only. Other more cross-platform solutions that I found have problems or lack functionalities that I need; but most importantly, most of them are not open-sourced.

So, I decided to write my own.

### Why did you use PyAutoGUI when pynput can also control the mouse cursor?

There are too many platform-related issues and limitations that come with pynput (you can read more about those [here](https://pyautogui.readthedocs.io/en/latest/limitations.html). I want to minimize them and only use it for keyboard listening.

### Contributing

Since this is a personal, learning-by-doing project, I'm currently **don't have any plan** to accept any PRs or promise to maintain it in long term. However, if you have any suggestions or found any bugs, feel free to open an issue.
