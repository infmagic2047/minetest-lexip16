from rules.unifieddyes import _unifieddyes_color_map


_coloredwood_fence_textures = {
    'coloredwood_fence_' + name: (color, 'fence', 'fence')
    for name, color in _unifieddyes_color_map.items()
}

_coloredwood_stick_textures = {
    'coloredwood_stick_' + name: (color, 'simple_block', 'stick')
    for name, color in _unifieddyes_color_map.items()
}

_coloredwood_wood_textures = {
    'coloredwood_wood_' + name: (color, 'wood')
    for name, color in _unifieddyes_color_map.items()
}


textures = {
    **_coloredwood_fence_textures,
    **_coloredwood_stick_textures,
    **_coloredwood_wood_textures,
}
