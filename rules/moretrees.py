textures = {
    'moretrees_apple_tree_leaves': ('apple_tree_leaves', 'simple_block', 'leaves'),
    'moretrees_apple_tree_sapling': (('apple_tree_tree', 'apple_tree_leaves'), 'sapling', 'sapling'),
    'moretrees_apple_tree_trunk': ('apple_tree_tree', 'tree'),
    'moretrees_apple_tree_trunk_top': (('apple_tree_tree', 'apple_tree_wood'), 'tree_top'),
    'moretrees_apple_tree_wood': ('apple_tree_wood', 'wood'),
    'moretrees_beech_leaves': ('beech_leaves', 'simple_block', 'leaves'),
    'moretrees_beech_sapling': (('beech_tree', 'beech_leaves'), 'sapling', 'sapling'),
    'moretrees_beech_trunk': ('beech_tree', 'tree'),
    'moretrees_beech_trunk_top': (('beech_tree', 'beech_wood'), 'tree_top'),
    'moretrees_beech_wood': ('beech_wood', 'wood'),
    'moretrees_birch_leaves': ('birch_leaves', 'simple_block', 'leaves'),
    'moretrees_birch_sapling': (('birch_tree', 'birch_leaves'), 'sapling', 'sapling'),
    'moretrees_birch_trunk': ('birch_tree', 'aspen_tree'),
    'moretrees_birch_trunk_top': (('birch_tree', 'birch_wood'), 'aspen_tree_top'),
    'moretrees_birch_wood': ('birch_wood', 'wood'),
    'moretrees_cedar_leaves': ('cedar_leaves', 'simple_block', 'pine_needles'),
    'moretrees_cedar_sapling': (('cedar_tree', 'cedar_leaves'), 'sapling', 'sapling'),
    'moretrees_cedar_trunk': ('cedar_tree', 'tree'),
    'moretrees_cedar_trunk_top': (('cedar_tree', 'cedar_wood'), 'tree_top'),
    'moretrees_cedar_wood': ('cedar_wood', 'wood'),
    'moretrees_fir_leaves': ('fir_leaves', 'simple_block', 'pine_needles'),
    'moretrees_fir_leaves_bright': ('fir_leaves_bright', 'simple_block', 'pine_needles'),
    'moretrees_fir_sapling': (('fir_tree', 'fir_leaves'), 'sapling', 'sapling'),
    'moretrees_fir_trunk': ('fir_tree', 'tree'),
    'moretrees_fir_trunk_top': (('fir_tree', 'fir_wood'), 'tree_top'),
    'moretrees_fir_wood': ('fir_wood', 'wood'),
    'moretrees_jungletree_leaves_red': ('jungle_leaves_red', 'simple_block', 'leaves'),
    'moretrees_jungletree_leaves_yellow': ('jungle_leaves_yellow', 'simple_block', 'leaves'),
    'moretrees_oak_leaves': ('oak_leaves', 'simple_block', 'leaves'),
    'moretrees_oak_sapling': (('oak_tree', 'oak_leaves'), 'sapling', 'sapling'),
    'moretrees_oak_trunk': ('oak_tree', 'tree'),
    'moretrees_oak_trunk_top': (('oak_tree', 'oak_wood'), 'tree_top'),
    'moretrees_oak_wood': ('oak_wood', 'wood'),
    'moretrees_palm_leaves': ('palm_leaves', 'simple_block', 'palm_leaves'),
    'moretrees_palm_sapling': (('palm_tree', 'palm_leaves'), 'sapling', 'sapling'),
    'moretrees_palm_trunk': ('palm_tree', 'palm_tree'),
    'moretrees_palm_trunk_top': (('palm_tree', 'palm_wood'), 'palm_tree_top'),
    'moretrees_palm_wood': ('palm_wood', 'wood'),
    'moretrees_rubber_tree_leaves': ('rubber_tree_leaves', 'simple_block', 'leaves'),
    'moretrees_rubber_tree_sapling': (('rubber_tree_tree', 'rubber_tree_leaves'), 'sapling', 'sapling'),
    'moretrees_rubber_tree_trunk': (('rubber_tree_tree', 'latex'), 'rubber_tree_tree'),
    'moretrees_rubber_tree_trunk_empty': ('rubber_tree_tree', 'tree'),
    'moretrees_rubber_tree_trunk_top': (('rubber_tree_tree', 'rubber_tree_wood', 'latex'), 'rubber_tree_tree_top'),
    'moretrees_rubber_tree_wood': ('rubber_tree_wood', 'wood'),
    'moretrees_sequoia_leaves': ('sequoia_leaves', 'simple_block', 'pine_needles'),
    'moretrees_sequoia_sapling': (('sequoia_tree', 'sequoia_leaves'), 'sapling', 'sapling'),
    'moretrees_sequoia_trunk': ('sequoia_tree', 'tree'),
    'moretrees_sequoia_trunk_top': (('sequoia_tree', 'sequoia_wood'), 'tree_top'),
    'moretrees_sequoia_wood': ('sequoia_wood', 'wood'),
    'moretrees_spruce_leaves': ('spruce_leaves', 'simple_block', 'pine_needles'),
    'moretrees_spruce_sapling': (('spruce_tree', 'spruce_leaves'), 'sapling', 'sapling'),
    'moretrees_spruce_trunk': ('spruce_tree', 'tree'),
    'moretrees_spruce_trunk_top': (('spruce_tree', 'spruce_wood'), 'tree_top'),
    'moretrees_spruce_wood': ('spruce_wood', 'wood'),
}

override_textures = {
    'moretrees_rubber_tree_trunk_top_empty': (('rubber_tree_tree', 'rubber_tree_wood'), 'tree_top'),
}

overrides = {
    ('moretrees:rubber_tree_trunk_empty', 'bottom'): 'moretrees_rubber_tree_trunk_top_empty',
    ('moretrees:rubber_tree_trunk_empty', 'top'): 'moretrees_rubber_tree_trunk_top_empty',
}
