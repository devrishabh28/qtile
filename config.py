# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from unicodes import *
import os
import subprocess

from libqtile import hook

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(['mod1'], "1", lazy.spawn('kitty'), desc="Spawn Kitty"),
    Key(['mod1'], "2", lazy.spawn('thunar'), desc="Spawn Thunar"),
    Key(['mod1'], "3", lazy.spawn('code'), desc="Spawn VS Code"),
    Key(['mod1'], "4", lazy.spawn('firefox'), desc="Spawn Firefox"),
    Key(['mod1'], "5", lazy.spawn('android-studio'), desc="Spawn Android Studio"),
    Key(['mod1'], "6", lazy.spawn('spotify'), desc="Spawn Spotify"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ +1000'), desc="Increase volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ -1000'), desc="Decrease volume"),
    Key([], "XF86AudioMute", lazy.spawn(
        'pactl set-sink-mute @DEFAULT_SINK@ toggle'), desc="Mute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        'xbacklight -inc 5'), desc="Increase Backlight"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
            'xbacklight -dec 5'), desc="Decrease Backlight"),
    Key([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioStop", lazy.spawn(
        "playerctl pause"), desc="Stop player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"), desc="Skip to previous"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=[
                   "#d75f5f", "#8f3d3d"], border_width=0, margin=8, margin_on_single=12),
    layout.Max(margin=12),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Caskaydia Cove Nerd Font Complete",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = {
    'transparent': '#00000000',
    'raisin-black': '#231B1B',
    'oxford-blue': '#001B2E',
    'charcoal': '#294C60',
    'antique-ruby': '#93032E',
    'light-cyan': '#DDFFF7',
    'dark-purple': '#330C2F',
    'apricot': '#FAC9B8',
    'independence': '#444054',
    'rich-black': '#101419',
    'forga-black': '#06070E',
    'carmine': '#91171F',
    'space-cadet': '#1B1F3B',
    'blood-red': '#621708',
    'honey-yellow': '#F6AE2D',
    'orange-red': '#F26419',
    'minion-yellow': '#ECD444',
    'sapphire': '#082567',
    'celeste': '#B2FFFF',
    'angels-red': '#BA0021',
    'platinum': '#E5E5E5',
    'misty-rose': '#FDE8E9',
    'lavender-blue': '#E3D7FF',
    'metallic-seaweed': '#028090',
    'silk': '#F4D8CD',
    'code-blue': '#274690',
    'lavender-floral': '#B388EB',
    'spotify-green': '#1DB954',
    'cyan-process': '#8EF9F3',
    'green-pantone': '#4DAA57',
    'pewter-blue': '#719FAB'
}


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=15, background=colors['rich-black']),

                # -----------User-Group-----------#
                text_box('{}@{}'.format(os.environ.get('USER'),
                         os.uname()[1]), colors['rich-black'], colors['light-cyan']),
                right_arrow(colors['platinum'], colors['rich-black']),
                # -----------User-Group-----------#

                # -----------Kitty-----------#
                clickable('', colors['platinum'],
                          colors['space-cadet'], 'kitty', 28),
                widget.Prompt(
                    background=colors['platinum'], foreground=colors['space-cadet'], cursor_color=colors['space-cadet']),
                clickable_right_arrow(
                    colors['lavender-floral'], colors['platinum'], 'kitty'),
                # -----------Kitty-----------#

                # -----------Files-----------#
                clickable('', colors['lavender-floral'],
                          colors['dark-purple'], 'thunar', 20, 10),
                clickable_right_arrow(
                    colors['code-blue'], colors['lavender-floral'], 'thunar'),
                # -----------Files-----------#

                # -----------VS-Code-----------#
                clickable('', colors['code-blue'],
                          colors['lavender-blue'], 'code', 24, 12),
                clickable_right_arrow(
                    colors['orange-red'], colors['code-blue'], 'code'),
                # -----------VS-Code-----------#

                # -----------Firefox-----------#
                clickable('', colors['orange-red'],
                          colors['forga-black'], 'firefox', 28, 10),
                clickable_right_arrow(
                    colors['oxford-blue'], colors['orange-red'], 'firefox'),
                # -----------Firefox-----------#

                # -----------Android-Studio-----------#
                clickable('', colors['oxford-blue'],
                          colors['platinum'], 'android-studio', 28, 10),
                clickable_right_arrow(
                    colors['spotify-green'], colors['oxford-blue'], 'android-studio'),
                # -----------Android-Studio-----------#

                # -----------Spotify-----------#
                clickable('', colors['spotify-green'],
                          colors['forga-black'], 'spotify', 28, 10),
                clickable_right_arrow(
                    colors['transparent'], colors['spotify-green'], 'spotify'),
                # -----------Spotify-----------#

                # -----------LEFT-SIDE-------------------------------------------------------#
                widget.Spacer(length=bar.STRETCH),
                # -----------RIGHT-SIDE-------------------------------------------------------#

                # -----------Weather-----------#
                # widget.OpenWeather(location='Guwahati', background=''),
                # -----------Weather-----------#

                # -----------Net-----------#
                left_arrow(colors['transparent'], colors['celeste']),
                widget.Net(
                    background=colors['celeste'], foreground=colors['space-cadet']),
                widget.NetGraph(
                    background=colors['celeste'], foreground=colors['space-cadet'], border_color=colors['space-cadet'], border_width=0.1, graph_color=colors['space-cadet'], fill_color=colors['code-blue']),
                # -----------Net-----------#


                # -----------CPU-----------#
                text_box('', colors['celeste'],
                         colors['dark-purple'], 36),
                widget.CPU(
                    background=colors['dark-purple'], foreground=colors['celeste']),
                widget.CPUGraph(
                    background=colors['dark-purple'], foreground=colors['celeste'], border_color=colors['celeste'], border_width=0.1, graph_color=colors['celeste'], fill_color=colors['platinum']),
                # -----------CPU-----------#

                # -----------SSD Space-----------#
                text_box('', colors['dark-purple'],
                         colors['pewter-blue'], 36),
                text_box(' SSD', colors['pewter-blue'],
                         colors['raisin-black'], 12, 1),
                widget.Spacer(length=6, background=colors['pewter-blue']),
                widget.DF(visible_on_warn=False,
                          format='{f}/{s} | {r:.0f}%', background=colors['pewter-blue'], foreground=colors['forga-black']),
                widget.HDDBusyGraph(
                    background=colors['pewter-blue'], graph_color=colors['forga-black'], fill_color=colors['oxford-blue'], border_color=colors['forga-black']),
                # -----------SSD Space-----------#

                # -----------Temperature-----------#
                text_box('', colors['pewter-blue'], colors['charcoal'], 36),
                text_box(' ', colors['charcoal'],
                         colors['platinum'], padding=8),

                text_box('RYZEN ', colors['charcoal'],
                         colors['platinum'], 12),
                widget.ThermalSensor(
                    background=colors['charcoal']),

                widget.Spacer(length=12, background=colors['charcoal']),
                text_box('NVIDIA ', colors['charcoal'],
                         colors['platinum'], 12),
                widget.NvidiaSensors(
                    background=colors['charcoal']),


                widget.Spacer(length=12, background=colors['charcoal']),
                # -----------Temperature-----------#


                # -----------System-Tray--------------------------------------------#
                left_arrow(colors['charcoal'], colors['oxford-blue']),

                # -----------Backlight-----------#
                text_box("", colors['oxford-blue'],
                         colors['platinum'], 20),
                widget.Backlight(
                    backlight_name="nvidia_0", background=colors['oxford-blue'], foreground=colors['platinum']),
                # -----------Backlight-----------#

                widget.Spacer(length=12, background=colors['oxford-blue']),

                # -----------Volume-----------#
                clickable("墳", colors['oxford-blue'],
                          colors['platinum'], 'pavucontrol', 20, 0),
                widget.Volume(
                    background=colors['oxford-blue'], foreground=colors['platinum'], mouse_callbacks={'Button1': lazy.spawn('pavucontrol')}),
                # -----------Volume-----------#

                widget.Spacer(length=12, background=colors['oxford-blue']),

                # -----------Date-----------#
                text_box("", colors['oxford-blue'], colors['platinum'], 20),
                widget.Clock(
                    format="%A %m/%d/%Y", background=colors['oxford-blue'], foreground=colors['platinum']),
                # -----------Date-----------#

                widget.Spacer(length=12, background=colors['oxford-blue']),

                # -----------Clock-----------#
                text_box("", colors['oxford-blue'], colors['platinum'], 20),
                widget.Clock(
                    background=colors['oxford-blue'], foreground=colors['platinum']),
                # -----------Clock-----------#

                widget.Spacer(length=12, background=colors['oxford-blue']),
                # -----------System-Tray--------------------------------------------#

                # -----------Battery-----------#
                left_arrow(colors['oxford-blue'], colors['minion-yellow']),
                text_box("", colors['minion-yellow'], '#000', 32),
                widget.Battery(
                    format='{percent:2.0%}', background=colors['minion-yellow'], foreground=colors['raisin-black'], update_interval=0.5),
                widget.QuickExit(
                    default_text='', countdown_format='{}', background=colors['minion-yellow'], foreground=colors['raisin-black'], fontsize=16),
                # -----------Battery-----------#

                widget.Spacer(length=15, background=colors['minion-yellow']),

            ],
            24,
            background=colors['transparent']

            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                # widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
