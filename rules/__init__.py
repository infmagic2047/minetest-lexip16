from importlib import import_module
from pkgutil import iter_modules


textures = {}
override_textures = {}
overrides = {}
overrides_noprefix = {}


for _, name, _ in iter_modules(__path__):
    mod = import_module('rules.' + name)
    textures.update(getattr(mod, 'textures', {}))
    override_textures.update(getattr(mod, 'override_textures', {}))
    overrides.update(getattr(mod, 'overrides', {}))
    overrides_noprefix.update(getattr(mod, 'overrides_noprefix', {}))
