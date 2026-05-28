# Pokemon Terminal

[Pokemon Terminal](https://github.com/LazoVelko/Pokemon-Terminal) is a command line application to set Pokemon art as terminal background and wallpaper.

This repository contains the configuration file for converting Pokemon Terminal into an rpm package so that Fedora users can download and install it via [copr](https://copr.fedorainfracloud.org/coprs/chandrakishorsingh/pokemon-terminal/).

## Install

1. Enable copr repository
```bash
sudo dnf copr enable chandrakishorsingh/pokemon-terminal
```


2. Download and install Pokemon Terminal
```bash
sudo dnf install pokemon-terminal
```

## Usage

Just run `pokemon` or `pokemon <name>`(ex. `pokemon latias`) to get/update terminal wallpaper. See [this](https://github.com/LazoVelko/Pokemon-Terminal#usage) for detailed usage instructions.

## Uninstall

You can uninstall it via dnf with below command.

```bash
sudo dnf uninstall pokemon-terminal
```

## Features
- 719 unique Pokemon
- Select Pokemon by name or by index number
- Ability to change the Desktop Wallpaper & the Terminal background
- Internal search system for finding Pokemon
- Supports iTerm2, ConEmu, Terminology, Windows Terminal, Tilix and Kitty terminal emulators
- Supports Windows, MacOS, GNOME, Openbox (with feh), i3wm (with feh) and sway for desktops

## Credits

Upstream repository: https://github.com/LazoVelko/Pokemon-Terminal
