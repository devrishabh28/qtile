from libqtile.widget.textbox import TextBox
from libqtile.lazy import lazy


def text_box(text, bg_color, fg_color, size=16, padding=0):
    return TextBox(
        text=text,
        padding=padding,
        fontsize=size,
        background=bg_color,
        foreground=fg_color
    )


def clickable(text, bg_color, fg_color, mouse_callback, size=16, padding=8):
    return TextBox(
        text=text,
        padding=padding,
        fontsize=size,
        background=bg_color,
        foreground=fg_color,
        mouse_callbacks={'Button1': lazy.spawn(mouse_callback)}
    )


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color
    )


def lower_right_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e3',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color
    )


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color
    )


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color
    )


def clickable_left_arrow(bg_color, fg_color, mouse_callback):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color,
        mouse_callbacks={'Button1': lazy.spawn(mouse_callback)}
    )


def clickable_right_arrow(bg_color, fg_color, mouse_callback):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=32,
        background=bg_color,
        foreground=fg_color,
        mouse_callbacks={'Button1': lazy.spawn(mouse_callback)}
    )
