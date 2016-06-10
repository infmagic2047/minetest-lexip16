import itertools

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


textures = dict(itertools.chain(
    _coloredwood_fence_textures.items(),
    _coloredwood_stick_textures.items(),
    _coloredwood_wood_textures.items(),
))
