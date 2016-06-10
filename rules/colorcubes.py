import itertools


_colorcubes_colors = {
    'yellow', 'orange', 'brown', 'red', 'pink', 'magenta', 'violet',
    'redviolet', 'blue', 'cyan', 'green', 'dark_green', 'white',
    'light_gray', 'dark_gray', 'black', 'lime', 'aqua', 'skyblue',
}

_colorcubes_color_map = {
    name: 'color_' + name.replace('pink', 'light_red')
    for name in _colorcubes_colors
}

_colorcubes_1_textures = {
    'colorcubes_1_' + name: (color, 'colorcubes_1')
    for name, color in _colorcubes_color_map.items()
}

_colorcubes_4_textures = {
    'colorcubes_4_' + name: (color, 'colorcubes_4')
    for name, color in _colorcubes_color_map.items()
}

_colorcubes_inward_textures = {
    'colorcubes_inward_' + name: (color, 'colorcubes_inward')
    for name, color in _colorcubes_color_map.items()
}

_colorcubes_window_textures = {
    'colorcubes_window_' + name: (
        color, 'colorcubes_1', 'colorcubes_window')
    for name, color in _colorcubes_color_map.items()
}


textures = dict(itertools.chain(
    _colorcubes_1_textures.items(),
    _colorcubes_4_textures.items(),
    _colorcubes_inward_textures.items(),
    _colorcubes_window_textures.items(),
))
