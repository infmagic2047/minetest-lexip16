textures = {
    'pipeworks_tube_connection_metallic': (('steel', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_stony': (('stone', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_wooden': (('wood', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_end': ('plastic', 'simple_block_64', 'tube_end'),
    'pipeworks_tube_noctr': ('plastic', 'simple_block_64', 'tube_noctr'),
    'pipeworks_tube_plain': ('plastic', 'simple_block_64', 'tube_plain'),
    'pipeworks_tube_short': ('plastic', 'simple_block_64', 'tube_short'),
}

override_textures = {
    'pipeworks_tube_plain_right_overlay': ('plastic', 'simple_block_64', 'tube_plain_right_overlay'),
}

overrides = {
    ('pipeworks:tube_2', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_2', 'bottom'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_2', 'front'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_2', 'top'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_3', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_3', 'bottom'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_3', 'front'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_3', 'top'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_4', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR180')),
    ('pipeworks:tube_4', 'front'): ('pipeworks_tube_plain', '_pipeworks_tube_plain_right_overlay', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_4', 'right'): ('pipeworks_tube_plain', '_pipeworks_tube_plain_right_overlay', ('_pipeworks_tube_plain_right_overlay', '[transformR180')),
    ('pipeworks:tube_4', 'top'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_5', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR180')),
    ('pipeworks:tube_5', 'right'): ('pipeworks_tube_plain', '_pipeworks_tube_plain_right_overlay', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_5', 'top'): ('pipeworks_tube_plain', '_pipeworks_tube_plain_right_overlay', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_6', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_6', 'front'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_6', 'top'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90'), ('_pipeworks_tube_plain_right_overlay', '[transformR270')),
    ('pipeworks:tube_7', 'back'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
    ('pipeworks:tube_7', 'top'): ('pipeworks_tube_plain', ('_pipeworks_tube_plain_right_overlay', '[transformR90')),
}
