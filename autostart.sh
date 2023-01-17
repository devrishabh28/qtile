#!/bin/sh

# Disable beep
xset -b

#  Unblock Bluetooth
rfkill unblock bluetooth

# Start compositor for fancy visuals
picom &

#  Start Player controls.
playerctld &

#  Unclutter - hide the mouse cursor
unclutter --jitter 10 --ignore-scrolling --start-hidden --fork

#  Nitrogen for wallpaper
nitrogen --restore &

