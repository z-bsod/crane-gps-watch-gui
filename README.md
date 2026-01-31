# Simple Gui for crane_gps_watch_client

this is a simple Tkinter based GUI application for [mru00/crane_gps_watch](https://github.com/mru00/crane_gps_watch) written in an afternoon.

## Requirements
- python3
- build-essential to build the C++ watch client

## Installation

1. clone this repo
1. setup required submodules
   ```
   git submodule update --init
   ```
1. build crane_gps_watch application
   ```
   (
   cd lib/crane_gps_watch
   autoreconf -f -i
   ./configure
   make
   )
   ```
1. start GUI application via main.py
   ```
   python3 main.py
   ```