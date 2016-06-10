import itertools

from rules.unifieddyes import (_unifieddyes_color_map,
                               _unifieddyes_colors_base)


_unifiedbricks_multicolor_modifiers = {
    ('medium_{}', '{}', 'medium_{}', 'light_{}'),
    ('dark_{}', 'medium_{}', 'dark_{}', '{}'),
    ('light_{}', 'light_{}', '{}', 'pastel_{}'),
}

_unifiedbricks_multicolor_colors = {
    tuple(modifier.format(color) for modifier in modifiers)
    for color in _unifieddyes_colors_base
    for modifiers in _unifiedbricks_multicolor_modifiers
}

_unifiedbricks_multicolor_colors.update({
    ('darkgrey', 'dark_gray', 'black', 'gray'),
    ('grey', 'gray', 'dark_gray', 'light_gray'),
    ('lightgrey', 'light_gray', 'gray', 'white'),
})

_unifiedbricks_multicolor_color_map = {
    name[0]: tuple('color_' + color for color in name[1:])
    for name in _unifiedbricks_multicolor_colors
}

_unifiedbricks_multicolor_textures = {
    'unifiedbricks_multicolor_' + name: (color, 'brick_multicolor')
    for name, color in _unifiedbricks_multicolor_color_map.items()
}

_unifiedbricks_brick_textures = {
    'unifiedbricks_brick_' + name: (color, 'cuboid', 'cuboid')
    for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_brickblock_textures = {
    'unifiedbricks_brickblock_' + name: (color, 'brick')
    for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_clay_textures = {
    'unifiedbricks_clay_' + name: (color, 'circle', 'circle')
    for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_clayblock_textures = {
    'unifiedbricks_clayblock_' + name: (color, 'sand')
    for name, color in _unifieddyes_color_map.items()
}


textures = dict(itertools.chain(
    _unifiedbricks_brick_textures.items(),
    _unifiedbricks_brickblock_textures.items(),
    _unifiedbricks_clay_textures.items(),
    _unifiedbricks_clayblock_textures.items(),
    _unifiedbricks_multicolor_textures.items(),
))
