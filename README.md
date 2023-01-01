# cymuk

## What?

**cymuk** (pronounced [/ˈsaɪmʌk/](http://ipa-reader.xyz/?text=%CB%88sa%C9%AAm%CA%8Ck&voice=Joey)) is a _simple_, _lightweight_ and _cross-platform_ Python script that allows you to control your mouse cursor with your keyboard.

It can be used as a keyboard listerner to perform actions when a key combination is pressed, or as a mouse automation tool using CLI commands and preset plain text files.

### Features

:hourglass_flowing_sand: _Work in progress._

## Why?

Who doesn't want to improve their productivity by 1%? I know I do.

Jokes aside, this project is heavily inspired by [keynav](https://github.com/jordansissel/keynav), a similar tool for X11 systems that I have been using for a few years now. I'm a huge fan of **keyboard-driven workflows** and wanted to have a similar **cross-platform** solution but didn't find any that suited my needs, so I decided to write my own.

## How?

This project is written in Python 3 and uses [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to control the mouse cursor and [pynput](https://pynput.readthedocs.io/en/latest/) to listen for keyboard events.

### Usage

#### Requirements

##### Dependencies

See [requirements.txt](requirements.txt) for list of dependencies.

##### System

- Windows 7+ (might run on older systems, but not tested)
- macOS (see [prerequisites](https://pynput.readthedocs.io/en/latest/limitations.html#macos))
	- _Note_: I have not tested this on macOS (since I can't afford one and don't know anyone that have a spare Mac :smiling_face_with_tear:), but it should work. Any issues that's **macOS-only won't be fixed** unless someone else is willing to contribute.
- Linux with _X_ server OR _uinput_ (see [prerequisites](https://pynput.readthedocs.io/en/latest/limitations.html#linux))

#### Manual

:hourglass_flowing_sand: _Work in progress._

### Contributing

:hourglass_flowing_sand: _Work in progress._
