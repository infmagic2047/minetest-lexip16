import itertools


_pipeworks_tube_override_map = {
    'pipeworks:priority_tube': ('_pipeworks_priority_tube_plain', '_pipeworks_priority_tube_plain_right_overlay'),
    'pipeworks:tube': ('pipeworks_tube_plain', '_pipeworks_tube_plain_right_overlay'),
}

_pipeworks_tube_override_rules = {
    ('2', 'back'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('2', 'bottom'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('2', 'front'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('2', 'top'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('3', 'back'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('3', 'bottom'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('3', 'front'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('3', 'top'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('4', 'back'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR180')),
    ('4', 'front'): lambda x, y: (x, y, (y, '[transformR90')),
    ('4', 'right'): lambda x, y: (x, y, (y, '[transformR180')),
    ('4', 'top'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('5', 'back'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR180')),
    ('5', 'right'): lambda x, y: (x, y, (y, '[transformR90')),
    ('5', 'top'): lambda x, y: (x, y, (y, '[transformR90')),
    ('6', 'back'): lambda x, y: (x, (y, '[transformR90')),
    ('6', 'front'): lambda x, y: (x, (y, '[transformR90')),
    ('6', 'top'): lambda x, y: (x, (y, '[transformR90'), (y, '[transformR270')),
    ('7', 'back'): lambda x, y: (x, (y, '[transformR90')),
    ('7', 'top'): lambda x, y: (x, (y, '[transformR90')),
}

_pipeworks_tube_overrides = {
    (name + '_' + rule[0], rule[1]): func(textures[0], textures[1])
    for name, textures in _pipeworks_tube_override_map.items()
    for rule, func in _pipeworks_tube_override_rules.items()
}

_pipeworks_tube_overrides_extra = {
    ('pipeworks:priority_tube_1', 'back'): '_pipeworks_priority_tube_short',
    ('pipeworks:priority_tube_1', 'bottom'): '_pipeworks_priority_tube_short',
    ('pipeworks:priority_tube_1', 'front'): '_pipeworks_priority_tube_short',
    ('pipeworks:priority_tube_1', 'inventory'): '_pipeworks_priority_tube_inv',
    ('pipeworks:priority_tube_1', 'left'): '_pipeworks_priority_tube_end',
    ('pipeworks:priority_tube_1', 'right'): '_pipeworks_priority_tube_end',
    ('pipeworks:priority_tube_1', 'top'): '_pipeworks_priority_tube_short',
    ('pipeworks:priority_tube_1', 'wield'): '_pipeworks_priority_tube_inv',
    ('pipeworks:priority_tube_10', 'back'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_10', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_10', 'front'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_10', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_10', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_10', 'top'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_2', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_2', 'right'): '_pipeworks_priority_tube_end',
    ('pipeworks:priority_tube_3', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_3', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_4', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_4', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_5', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_5', 'front'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_5', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_6', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_6', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_6', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_7', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_7', 'front'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_7', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_7', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_8', 'back'): '_pipeworks_priority_tube_plain',
    ('pipeworks:priority_tube_8', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_8', 'front'): '_pipeworks_priority_tube_plain',
    ('pipeworks:priority_tube_8', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_8', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_8', 'top'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_9', 'back'): '_pipeworks_priority_tube_plain',
    ('pipeworks:priority_tube_9', 'bottom'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_9', 'front'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_9', 'left'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_9', 'right'): '_pipeworks_priority_tube_noctr',
    ('pipeworks:priority_tube_9', 'top'): '_pipeworks_priority_tube_noctr',
}


textures = {
    '_pipeworks_priority_tube_end': ('priority_tube', 'simple_block_64', 'tube_end'),
    '_pipeworks_priority_tube_inv': ('priority_tube', 'simple_block', 'tube_inv'),
    '_pipeworks_priority_tube_noctr': ('priority_tube', 'simple_block_64', 'tube_noctr'),
    '_pipeworks_priority_tube_plain': ('priority_tube', 'simple_block_64', 'tube_plain'),
    '_pipeworks_priority_tube_plain_right_overlay': ('priority_tube', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_priority_tube_short': ('priority_tube', 'simple_block_64', 'tube_short'),
    '_pipeworks_tube_plain_right_overlay': ('plastic', 'simple_block_64', 'tube_plain_right_overlay'),
    'pipeworks_tube_connection_metallic': (('steel', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_stony': (('stone', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_wooden': (('wood', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_end': ('plastic', 'simple_block_64', 'tube_end'),
    'pipeworks_tube_inv': ('plastic', 'simple_block', 'tube_inv'),
    'pipeworks_tube_noctr': ('plastic', 'simple_block_64', 'tube_noctr'),
    'pipeworks_tube_plain': ('plastic', 'simple_block_64', 'tube_plain'),
    'pipeworks_tube_short': ('plastic', 'simple_block_64', 'tube_short'),
}

overrides = dict(itertools.chain(
    _pipeworks_tube_overrides.items(),
    _pipeworks_tube_overrides_extra.items(),
))
