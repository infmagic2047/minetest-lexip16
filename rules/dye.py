_dye_colors = {
    'black', 'blue', 'brown', 'cyan', 'dark_green', 'dark_grey',
    'green', 'grey', 'magenta', 'orange', 'pink', 'red', 'violet',
    'white', 'yellow',
}

_dye_color_map = {
    name: ('color_' +
           name.replace('grey', 'gray').replace('pink', 'light_red'))
    for name in _dye_colors
}


textures = {
    'dye_' + name: (color, 'dye', 'dye')
    for name, color in _dye_color_map.items()
}
