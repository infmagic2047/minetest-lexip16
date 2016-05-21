from rules.dye import _dye_colors


_unifieddyes_colors_base = {
    'red', 'orange', 'yellow', 'lime', 'green', 'aqua', 'cyan',
    'skyblue', 'blue', 'violet', 'magenta', 'redviolet',
}

_unifieddyes_color_modifiers = {
    '{}', '{}_s50', 'medium_{}', 'medium_{}_s50', 'dark_{}',
    'dark_{}_s50', 'light_{}',
}

_unifieddyes_colors = {
    modifier.format(color)
    for color in _unifieddyes_colors_base
    for modifier in _unifieddyes_color_modifiers
}

_unifieddyes_colors.update({
    'black', 'dark_grey', 'grey', 'light_grey', 'white',
})

_unifieddyes_color_map = {
    name.replace('light_grey', 'lightgrey'):
        'color_' + name.replace('grey', 'gray')
    for name in _unifieddyes_colors
}

_unifieddyes_dye_color_map = {
    name: color
    for name, color in _unifieddyes_color_map.items()
    if name not in _dye_colors
}


textures = {
    'unifieddyes_' + name: (color, 'dye', 'dye')
    for name, color in _unifieddyes_dye_color_map.items()
}
