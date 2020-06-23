textures = {
    "_travelnet_elevator_topbottom": (("glass", "steel"), "elevator_topbottom", "elevator_topbottom"),
    "_travelnet_travelnet_topbottom": ("steel", "travelnet_topbottom"),
    "travelnet_elevator_front": (("steel", "steel"), "travelnet_front"),
    "travelnet_elevator_inside_ceiling": (("glass", "steel"), "elevator_topbottom", "elevator_topbottom_inside"),
    "travelnet_elevator_inside_controls": "travelnet_elevator_front",
    "travelnet_elevator_inside_floor": "travelnet_elevator_inside_ceiling",
    "travelnet_elevator_sides_outside": "travelnet_elevator_front",
    "travelnet_travelnet_back": "travelnet_travelnet_front",
    "travelnet_travelnet_front": (("mese", "steel"), "travelnet_front"),
    "travelnet_travelnet_side": (("glass", "steel"), "travelnet_side", "travelnet_side"),
}

overrides = {
    ("travelnet:elevator", "front"): "_travelnet_elevator_topbottom",
    ("travelnet:travelnet", "back"): "_travelnet_travelnet_topbottom",
    ("travelnet:travelnet", "left"): "_travelnet_travelnet_topbottom",
}
