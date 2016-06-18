from importlib import import_module
from pkgutil import iter_modules


textures = {}
overrides = {}


for _, name, _ in iter_modules(__path__):
    mod = import_module('rules.' + name)
    textures.update(getattr(mod, 'textures', {}))
    overrides.update(getattr(mod, 'overrides', {}))
