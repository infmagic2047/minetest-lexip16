textures = {
    'travelnet_travelnet_back': 'travelnet_travelnet_front',
    'travelnet_travelnet_front': (('mese', 'steel'), 'travelnet_front'),
    'travelnet_travelnet_side': (('glass', 'steel'), 'travelnet_side', 'travelnet_side'),
}

override_textures = {
    'travelnet_travelnet_topbottom': ('steel', 'travelnet_topbottom'),
}

overrides = {
    ('travelnet:travelnet', 'back'): 'travelnet_travelnet_topbottom',
    ('travelnet:travelnet', 'left'): 'travelnet_travelnet_topbottom',
}
