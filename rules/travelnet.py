textures = {
    "_travelnet_travelnet_topbottom": ("steel", "travelnet_topbottom"),
    "travelnet_travelnet_back": "travelnet_travelnet_front",
    "travelnet_travelnet_front": (("mese", "steel"), "travelnet_front"),
    "travelnet_travelnet_side": (("glass", "steel"), "travelnet_side", "travelnet_side"),
}

overrides = {
    ("travelnet:travelnet", "back"): "_travelnet_travelnet_topbottom",
    ("travelnet:travelnet", "left"): "_travelnet_travelnet_topbottom",
}
