from rules.unifieddyes import _unifieddyes_color_modifiers, _unifieddyes_colors_base


_stained_glass_modifiers = _unifieddyes_color_modifiers | {
    "faint_{}",
    "pastel_{}",
}

_stained_glass_colors = {modifier.format(color) for color in _unifieddyes_colors_base for modifier in _stained_glass_modifiers}

_stained_glass_color_map = {name: "color_" + name for name in _stained_glass_colors}


textures = {
    "stained_glass_" + name: (color, "simple_block", "stained_glass") for name, color in _stained_glass_color_map.items()
}
