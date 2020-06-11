_pipeworks_tube_override_map = {
    'pipeworks:accelerator_tube': ('pipeworks_accelerator_tube_plain', '_pipeworks_accelerator_tube_plain_right_overlay'),
    'pipeworks:conductor_tube_off': ('pipeworks_conductor_tube_plain', '_pipeworks_conductor_tube_plain_right_overlay'),
    'pipeworks:conductor_tube_on': ('pipeworks_conductor_tube_on_plain', '_pipeworks_conductor_tube_on_plain_right_overlay'),
    'pipeworks:crossing_tube': ('pipeworks_crossing_tube_plain', '_pipeworks_crossing_tube_plain_right_overlay'),
    'pipeworks:detector_tube_off': ('pipeworks_detector_tube_plain', '_pipeworks_detector_tube_plain_right_overlay'),
    'pipeworks:detector_tube_on': ('_pipeworks_detector_tube_on_plain', '_pipeworks_detector_tube_plain_right_overlay'),
    'pipeworks:mese_sand_tube': ('pipeworks_mese_sand_tube_plain', '_pipeworks_mese_sand_tube_plain_right_overlay'),
    'pipeworks:priority_tube': ('_pipeworks_priority_tube_plain', '_pipeworks_priority_tube_plain_right_overlay'),
    'pipeworks:sand_tube': ('pipeworks_sand_tube_plain', '_pipeworks_sand_tube_plain_right_overlay'),
    'pipeworks:teleport_tube': ('pipeworks_teleport_tube_plain', '_pipeworks_teleport_tube_plain_right_overlay'),
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

_pipeworks_mese_tube_overrides_left = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'left'):
    ('pipeworks_mese_tube_plain_1',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not front and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not top and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not back and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not bottom and (front or back) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not left and not (bottom == top == front == back)
}

_pipeworks_mese_tube_overrides_right = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'right'):
    ('pipeworks_mese_tube_plain_2',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not back and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not top and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not front and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not bottom and (front or back) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not right and not (bottom == top == front == back)
}

_pipeworks_mese_tube_overrides_bottom = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'bottom'):
    ('pipeworks_mese_tube_plain_3',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not right and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not front and (left or right) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not left and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not back and (left or right) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not bottom and not (left == right == front == back)
}

_pipeworks_mese_tube_overrides_top = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'top'):
    ('pipeworks_mese_tube_plain_4',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not right and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not back and (left or right) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not left and (front or back) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not front and (left or right) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not top and not (left == right == front == back)
}

_pipeworks_mese_tube_overrides_front = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'front'):
    ('pipeworks_mese_tube_plain_5',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not right and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not top and (left or right) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not left and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not bottom and (left or right) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not front and not (left == right == bottom == top)
}

_pipeworks_mese_tube_overrides_back = {
    ('pipeworks:mese_tube_{:d}{:d}{:d}{:d}{:d}{:d}'.format(
        left, right, bottom, top, front, back), 'back'):
    ('pipeworks_mese_tube_plain_6',) +
    (('_pipeworks_mese_tube_plain_right_overlay',)
     if not left and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR90'),)
     if not top and (left or right) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR180'),)
     if not right and (bottom or top) else ()) +
    ((('_pipeworks_mese_tube_plain_right_overlay', '[transformR270'),)
     if not bottom and (left or right) else ())
    for left in (False, True)
    for right in (False, True)
    for bottom in (False, True)
    for top in (False, True)
    for front in (False, True)
    for back in (False, True)
    if not back and not (left == right == bottom == top)
}

_pipeworks_tube_overrides_extra = {
    ('pipeworks:conductor_tube_on_1', 'back'): '_pipeworks_conductor_tube_on_short',
    ('pipeworks:conductor_tube_on_1', 'bottom'): '_pipeworks_conductor_tube_on_short',
    ('pipeworks:conductor_tube_on_1', 'front'): '_pipeworks_conductor_tube_on_short',
    ('pipeworks:conductor_tube_on_1', 'top'): '_pipeworks_conductor_tube_on_short',
    ('pipeworks:detector_tube_off_1', 'back'): '_pipeworks_detector_tube_short',
    ('pipeworks:detector_tube_off_1', 'bottom'): '_pipeworks_detector_tube_short',
    ('pipeworks:detector_tube_off_1', 'front'): '_pipeworks_detector_tube_short',
    ('pipeworks:detector_tube_off_1', 'left'): '_pipeworks_detector_tube_end',
    ('pipeworks:detector_tube_off_1', 'right'): '_pipeworks_detector_tube_end',
    ('pipeworks:detector_tube_off_1', 'top'): '_pipeworks_detector_tube_short',
    ('pipeworks:detector_tube_off_10', 'back'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_10', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_10', 'front'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_10', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_10', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_10', 'top'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_2', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_2', 'right'): '_pipeworks_detector_tube_2_end',
    ('pipeworks:detector_tube_off_3', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_3', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_4', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_4', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_5', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_5', 'front'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_5', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_6', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_6', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_6', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_7', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_7', 'front'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_7', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_7', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_8', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_8', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_8', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_8', 'top'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_9', 'bottom'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_9', 'front'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_9', 'left'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_9', 'right'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_off_9', 'top'): '_pipeworks_detector_tube_noctr',
    ('pipeworks:detector_tube_on_1', 'back'): '_pipeworks_detector_tube_on_short',
    ('pipeworks:detector_tube_on_1', 'bottom'): '_pipeworks_detector_tube_on_short',
    ('pipeworks:detector_tube_on_1', 'front'): '_pipeworks_detector_tube_on_short',
    ('pipeworks:detector_tube_on_1', 'left'): '_pipeworks_detector_tube_on_end',
    ('pipeworks:detector_tube_on_1', 'right'): '_pipeworks_detector_tube_on_end',
    ('pipeworks:detector_tube_on_1', 'top'): '_pipeworks_detector_tube_on_short',
    ('pipeworks:detector_tube_on_10', 'back'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_10', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_10', 'front'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_10', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_10', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_10', 'top'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_2', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_2', 'right'): '_pipeworks_detector_tube_2_end',
    ('pipeworks:detector_tube_on_3', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_3', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_4', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_4', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_5', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_5', 'front'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_5', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_6', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_6', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_6', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_7', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_7', 'front'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_7', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_7', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_8', 'back'): '_pipeworks_detector_tube_on_plain',
    ('pipeworks:detector_tube_on_8', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_8', 'front'): '_pipeworks_detector_tube_on_plain',
    ('pipeworks:detector_tube_on_8', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_8', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_8', 'top'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_9', 'back'): '_pipeworks_detector_tube_on_plain',
    ('pipeworks:detector_tube_on_9', 'bottom'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_9', 'front'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_9', 'left'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_9', 'right'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:detector_tube_on_9', 'top'): '_pipeworks_detector_tube_on_noctr',
    ('pipeworks:mese_sand_tube_2', 'right'): '_pipeworks_mese_sand_tube_2_end',
    ('pipeworks:one_way_tube', 'inventory'): '_pipeworks_one_way_tube_inv',
    ('pipeworks:one_way_tube', 'wield'): '_pipeworks_one_way_tube_inv',
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
    '_pipeworks_accelerator_tube_plain_right_overlay': ('accelerator_tube', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_conductor_tube_on_plain_right_overlay': ('mesecons_on', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_conductor_tube_on_short': ('mesecons_on', 'simple_block_64', 'tube_short'),
    '_pipeworks_conductor_tube_plain_right_overlay': ('mesecons', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_crossing_tube_plain_right_overlay': ('plastic', 'crossing_tube_plain_right_overlay', 'tube_plain_right_overlay'),
    '_pipeworks_detector_tube_2_end': ('detector_tube', 'simple_block_64', 'tube_end'),
    '_pipeworks_detector_tube_end': ('mesecons', 'simple_block_64', 'tube_end'),
    '_pipeworks_detector_tube_noctr': ('mesecons', 'simple_block_64', 'tube_noctr'),
    '_pipeworks_detector_tube_on_end': ('mesecons_on', 'simple_block_64', 'tube_end'),
    '_pipeworks_detector_tube_on_noctr': ('mesecons_on', 'simple_block_64', 'tube_noctr'),
    '_pipeworks_detector_tube_on_plain': (('mesecons_on', 'detector_tube'), 'detector_tube_plain', 'tube_plain'),
    '_pipeworks_detector_tube_on_short': (('mesecons_on', 'detector_tube'), 'detector_tube_short', 'tube_short'),
    '_pipeworks_detector_tube_plain_right_overlay': ('detector_tube', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_detector_tube_short': (('mesecons', 'detector_tube'), 'detector_tube_short', 'tube_short'),
    '_pipeworks_mese_sand_tube_2_end': ('mese', 'simple_block_64', 'tube_end'),
    '_pipeworks_mese_sand_tube_plain_right_overlay': ('mese', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_mese_tube_plain_right_overlay': ('mese', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_one_way_tube_inv': (('plastic', 'one_way_tube_marker'), 'one_way_tube_inv', 'one_way_tube_inv'),
    '_pipeworks_priority_tube_end': ('priority_tube', 'simple_block_64', 'tube_end'),
    '_pipeworks_priority_tube_inv': ('priority_tube', 'simple_block', 'tube_inv'),
    '_pipeworks_priority_tube_noctr': ('priority_tube', 'simple_block_64', 'tube_noctr'),
    '_pipeworks_priority_tube_plain': ('priority_tube', 'simple_block_64', 'tube_plain'),
    '_pipeworks_priority_tube_plain_right_overlay': ('priority_tube', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_priority_tube_short': ('priority_tube', 'simple_block_64', 'tube_short'),
    '_pipeworks_sand_tube_plain_right_overlay': ('sand', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_teleport_tube_plain_right_overlay': ('teleport_tube', 'simple_block_64', 'tube_plain_right_overlay'),
    '_pipeworks_tube_plain_right_overlay': ('plastic', 'simple_block_64', 'tube_plain_right_overlay'),
    'pipeworks_accelerator_tube_end': ('accelerator_tube', 'simple_block_64', 'tube_end'),
    'pipeworks_accelerator_tube_inv': ('accelerator_tube', 'simple_block', 'tube_inv'),
    'pipeworks_accelerator_tube_noctr': ('accelerator_tube', 'simple_block_64', 'tube_noctr'),
    'pipeworks_accelerator_tube_plain': ('accelerator_tube', 'simple_block_64', 'tube_plain'),
    'pipeworks_accelerator_tube_short': ('accelerator_tube', 'simple_block_64', 'tube_short'),
    'pipeworks_black': ('color_black', 'simple_block'),
    'pipeworks_blue': ('color_blue', 'simple_block'),
    'pipeworks_conductor_tube_end': ('mesecons', 'simple_block_64', 'tube_end'),
    'pipeworks_conductor_tube_inv': ('mesecons', 'simple_block', 'tube_inv'),
    'pipeworks_conductor_tube_noctr': ('mesecons', 'simple_block_64', 'tube_noctr'),
    'pipeworks_conductor_tube_on_end': ('mesecons_on', 'simple_block_64', 'tube_end'),
    'pipeworks_conductor_tube_on_noctr': ('mesecons_on', 'simple_block_64', 'tube_noctr'),
    'pipeworks_conductor_tube_on_plain': ('mesecons_on', 'simple_block_64', 'tube_plain'),
    'pipeworks_conductor_tube_plain': ('mesecons', 'simple_block_64', 'tube_plain'),
    'pipeworks_conductor_tube_short': ('mesecons', 'simple_block_64', 'tube_short'),
    'pipeworks_crossing_tube_end': ('plastic', 'simple_block_64', 'tube_end'),
    'pipeworks_crossing_tube_inv': ('plastic', 'crossing_tube_inv', 'crossing_tube_inv'),
    'pipeworks_crossing_tube_noctr': ('plastic', 'crossing_tube_noctr', 'crossing_tube_noctr'),
    'pipeworks_crossing_tube_plain': ('plastic', 'crossing_tube_plain', 'crossing_tube_plain'),
    'pipeworks_crossing_tube_short': ('plastic', 'crossing_tube_short', 'crossing_tube_short'),
    'pipeworks_detector_tube_inv': (('mesecons', 'detector_tube'), 'detector_tube_inv', 'tube_inv'),
    'pipeworks_detector_tube_plain': (('mesecons', 'detector_tube'), 'detector_tube_plain', 'tube_plain'),
    'pipeworks_green': ('color_green', 'simple_block'),
    'pipeworks_mese_sand_tube_end': ('sand', 'simple_block_64', 'tube_end'),
    'pipeworks_mese_sand_tube_inv': (('sand', 'mese'), 'detector_tube_inv', 'tube_inv'),
    'pipeworks_mese_sand_tube_noctr': ('sand', 'simple_block_64', 'tube_noctr'),
    'pipeworks_mese_sand_tube_plain': (('sand', 'mese'), 'detector_tube_plain', 'tube_plain'),
    'pipeworks_mese_sand_tube_short': (('sand', 'mese'), 'detector_tube_short', 'tube_short'),
    'pipeworks_mese_tube_end': ('mese', 'simple_block_64', 'tube_end'),
    'pipeworks_mese_tube_inv': ('mese', 'simple_block', 'tube_inv'),
    'pipeworks_mese_tube_noctr_1': (('mese', 'color_black', 'color_green', 'color_white', 'color_yellow'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_noctr_2': (('mese', 'color_white', 'color_green', 'color_black', 'color_yellow'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_noctr_3': (('mese', 'color_blue', 'color_black', 'color_red', 'color_white'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_noctr_4': (('mese', 'color_blue', 'color_white', 'color_red', 'color_black'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_noctr_5': (('mese', 'color_blue', 'color_green', 'color_red', 'color_yellow'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_noctr_6': (('mese', 'color_red', 'color_green', 'color_blue', 'color_yellow'), 'mese_tube_noctr', 'mese_tube_noctr'),
    'pipeworks_mese_tube_plain_1': (('mese', 'color_black', 'color_green', 'color_white', 'color_yellow'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_plain_2': (('mese', 'color_white', 'color_green', 'color_black', 'color_yellow'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_plain_3': (('mese', 'color_blue', 'color_black', 'color_red', 'color_white'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_plain_4': (('mese', 'color_blue', 'color_white', 'color_red', 'color_black'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_plain_5': (('mese', 'color_blue', 'color_green', 'color_red', 'color_yellow'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_plain_6': (('mese', 'color_red', 'color_green', 'color_blue', 'color_yellow'), 'mese_tube_plain', 'mese_tube_plain'),
    'pipeworks_mese_tube_short': ('mese', 'simple_block_64', 'tube_short'),
    'pipeworks_one_way_tube_input': ('plastic', 'simple_block_64', 'tube_end'),
    'pipeworks_one_way_tube_output': 'pipeworks_one_way_tube_input',
    'pipeworks_one_way_tube_side': (('plastic', 'one_way_tube_marker'), 'one_way_tube_left', 'one_way_tube_left'),
    'pipeworks_one_way_tube_top': (('plastic', 'one_way_tube_marker'), 'one_way_tube_right', 'one_way_tube_right'),
    'pipeworks_red': ('color_red', 'simple_block'),
    'pipeworks_sand_tube_end': ('sand', 'simple_block_64', 'tube_end'),
    'pipeworks_sand_tube_inv': ('sand', 'simple_block', 'tube_inv'),
    'pipeworks_sand_tube_noctr': ('sand', 'simple_block_64', 'tube_noctr'),
    'pipeworks_sand_tube_plain': ('sand', 'simple_block_64', 'tube_plain'),
    'pipeworks_sand_tube_short': ('sand', 'simple_block_64', 'tube_short'),
    'pipeworks_teleport_tube_end': ('teleport_tube', 'simple_block_64', 'tube_end'),
    'pipeworks_teleport_tube_inv': ('teleport_tube', 'simple_block', 'tube_inv'),
    'pipeworks_teleport_tube_noctr': ('teleport_tube', 'simple_block_64', 'tube_noctr'),
    'pipeworks_teleport_tube_plain': ('teleport_tube', 'simple_block_64', 'tube_plain'),
    'pipeworks_teleport_tube_short': ('teleport_tube', 'simple_block_64', 'tube_short'),
    'pipeworks_tube_connection_metallic': (('steel', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_stony': (('stone', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_connection_wooden': (('wood', 'color_black'), 'tube_connection', 'tube_connection'),
    'pipeworks_tube_end': ('plastic', 'simple_block_64', 'tube_end'),
    'pipeworks_tube_inv': ('plastic', 'simple_block', 'tube_inv'),
    'pipeworks_tube_noctr': ('plastic', 'simple_block_64', 'tube_noctr'),
    'pipeworks_tube_plain': ('plastic', 'simple_block_64', 'tube_plain'),
    'pipeworks_tube_short': ('plastic', 'simple_block_64', 'tube_short'),
    'pipeworks_white': ('color_white', 'simple_block'),
    'pipeworks_yellow': ('color_yellow', 'simple_block'),
}

overrides = {
    **_pipeworks_tube_overrides,
    **_pipeworks_mese_tube_overrides_left,
    **_pipeworks_mese_tube_overrides_right,
    **_pipeworks_mese_tube_overrides_bottom,
    **_pipeworks_mese_tube_overrides_top,
    **_pipeworks_mese_tube_overrides_front,
    **_pipeworks_mese_tube_overrides_back,
    **_pipeworks_tube_overrides_extra,
}
