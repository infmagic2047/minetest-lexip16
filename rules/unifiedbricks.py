from rules.unifieddyes import _unifieddyes_color_map, _unifieddyes_colors_base


_unifiedbricks_multicolor_modifiers = {
    ("dark_{}", "dark_{}", "medium_{}", "medium_{}_s50"),
    ("medium_{}", "medium_{}", "dark_{}", "{}_s50"),
    ("light_{}", "{}", "light_{}", "medium_{}_s50"),
}

_unifiedbricks_multicolor_colors = {
    tuple(modifier.format(color) for modifier in modifiers)
    for color in _unifieddyes_colors_base
    for modifiers in _unifiedbricks_multicolor_modifiers
}

_unifiedbricks_multicolor_colors.update(
    {
        ("darkgrey", "dark_gray", "gray", "light_gray"),
        ("grey", "gray", "dark_gray", "light_gray"),
        ("lightgrey", "light_gray", "dark_gray", "gray"),
    }
)

_unifiedbricks_multicolor_color_map = {
    name[0]: tuple("color_" + color for color in name[1:]) for name in _unifiedbricks_multicolor_colors
}

_unifiedbricks_multicolor_textures = {
    "unifiedbricks_multicolor_" + name: (color, "brick_multicolor")
    for name, color in _unifiedbricks_multicolor_color_map.items()
}

_unifiedbricks_brick_textures = {
    "unifiedbricks_brick_" + name: (color, "cuboid", "cuboid") for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_brickblock_textures = {
    "unifiedbricks_brickblock_" + name: (color, "brick") for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_clay_textures = {
    "unifiedbricks_clay_" + name: (color, "circle", "circle") for name, color in _unifieddyes_color_map.items()
}

_unifiedbricks_clayblock_textures = {
    "unifiedbricks_clayblock_" + name: (color, "sand") for name, color in _unifieddyes_color_map.items()
}


textures = {
    **_unifiedbricks_brick_textures,
    **_unifiedbricks_brickblock_textures,
    **_unifiedbricks_clay_textures,
    **_unifiedbricks_clayblock_textures,
    **_unifiedbricks_multicolor_textures,
}
