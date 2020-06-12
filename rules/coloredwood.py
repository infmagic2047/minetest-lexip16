textures = {
    "_coloredwood_fence_base": ("color_white", "fence", "fence"),
    "_coloredwood_fence_base_sides": ("color_white", "fence_sides", "fence_sides"),
    "_coloredwood_fence_base_topbottom": ("color_white", "fence_topbottom", "fence_topbottom"),
    "coloredwood_base": ("color_white", "wood"),
}

overrides = {
    ("coloredwood:fence", "bottom"): "_coloredwood_fence_base_topbottom",
    ("coloredwood:fence", "inventory"): "_coloredwood_fence_base",
    ("coloredwood:fence", "sides"): "_coloredwood_fence_base_sides",
    ("coloredwood:fence", "top"): "_coloredwood_fence_base_topbottom",
    ("coloredwood:fence", "wield"): "_coloredwood_fence_base",
}
