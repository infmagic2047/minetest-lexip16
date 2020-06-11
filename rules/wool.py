from rules.dye import _dye_color_map


textures = {"wool_" + name: (color, "wool") for name, color in _dye_color_map.items()}
