import os
import zipfile

import rules


PROJECT_NAME = 'lexip16'

OPTIMIZE = int(ARGUMENTS.get('OPTIMIZE', 1))
SYMLINK = int(ARGUMENTS.get('SYMLINK', 1))
NOINVWIELD = int(ARGUMENTS.get('NOINVWIELD', 0))


env = Environment()


def palette_actions(source, target, env, for_signature):
    if not source:
        return 'false no sources for ${TARGET}'
    return 'pnmcat -leftright ${SOURCES} > ${TARGET}'


def rgb_actions(source, target, env, for_signature):
    if len(source) != 2:
        return 'false wrong number of sources for ${TARGET}'
    return 'pgmtoppm -map ${SOURCES[1]} ${SOURCE} > ${TARGET}'


def png_actions(source, target, env, for_signature):
    if len(source) != 1 and len(source) != 2:
        return 'false wrong number of sources for ${TARGET}'
    if len(source) == 1:
        return 'pnmtopng ${SOURCE} > ${TARGET}'
    else:
        return 'pnmtopng -alpha ${SOURCES[1]} ${SOURCE} > ${TARGET}'


def optimize_actions(source, target, env, for_signature):
    if OPTIMIZE:
        return 'optipng -quiet -o7 -zm1-9 -i0 -strip all -out ${TARGET} ${SOURCE}'
    else:
        return 'cp ${SOURCE} ${TARGET}'


def copyfile_actions(source, target, env, for_signature):
    if SYMLINK:
        return 'ln -srf ${SOURCE} ${TARGET}'
    else:
        return 'cp ${SOURCE} ${TARGET}'


def zipoutput(target, source, env):
    zf = zipfile.ZipFile(str(target[0]), 'w', zipfile.ZIP_DEFLATED)
    srcnames = [str(src) for src in source]
    for srcname in sorted(srcnames):
        outname = os.path.join(PROJECT_NAME, os.path.basename(srcname))
        zf.write(srcname, outname)
    zf.close()


env.Append(BUILDERS={
    'Palette': Builder(generator=palette_actions),
    'RGB': Builder(generator=rgb_actions),
    'PNG': Builder(generator=png_actions),
    'Optimize': Builder(generator=optimize_actions),
    'CopyFile': Builder(generator=copyfile_actions),
    'ZipOutput': Builder(action=zipoutput, multi=True),
})


def add_output(name):
    env.ZipOutput(PROJECT_NAME + '.zip', 'output/' + name)


def add(name, colors, index, alpha=None):
    if isinstance(colors, str):
        colors = (colors,)
    env.Palette('build/palette/{}.ppm'.format(name),
                ['color/{}.ppm'.format(color) for color in colors])
    env.RGB('build/rgb/{}.ppm'.format(name),
            ['index/{}.pgm'.format(index),
             'build/palette/{}.ppm'.format(name)])
    if alpha is None:
        env.PNG('build/png/{}.png'.format(name),
                'build/rgb/{}.ppm'.format(name))
    else:
        env.PNG('build/png/{}.png'.format(name),
                ['build/rgb/{}.ppm'.format(name),
                 'alpha/{}.pgm'.format(alpha)])
    env.Optimize('output/{}.png'.format(name),
                 'build/png/{}.png'.format(name))
    add_output('{}.png'.format(name))


def copy(name, othername):
    env.CopyFile('output/{}.png'.format(name),
                 'output/{}.png'.format(othername))
    add_output('{}.png'.format(name))


def get_texture_name(texture):
    return ('{}_override{}'.format(PROJECT_NAME, texture)
            if texture[0] == '_' else texture)


def add_all(textures):
    for k, v in textures.items():
        name = get_texture_name(k)
        if isinstance(v, str):
            copy(name, get_texture_name(v))
        else:
            add(name, *v)


def get_texture_string(parts):
    return '^'.join((get_texture_name(part) + '.png'
                     if part[0] != '[' else part)
                    if isinstance(part, str)
                    else '({})'.format(get_texture_string(part))
                    for part in parts)


def add_overrides(overrides):
    lines = []
    for (nodename, face), texture in sorted(overrides.items()):
        if NOINVWIELD and (face == 'inventory' or face == 'wield'):
            continue
        lines.append('{} {} {}'.format(
            nodename, face, get_texture_string(
                (texture,) if isinstance(texture, str) else texture)))

    def write_overrides(target, source, env):
        with open(str(target[0]), 'w') as fout:
            fout.write(''.join(l + '\n' for l in lines))

    env.Command('output/override.txt', '', action=write_overrides)
    add_output('override.txt')


add_all(rules.textures)
add_overrides(rules.overrides)
env.Default('output')
env.Alias('zip', PROJECT_NAME + '.zip')
if env.GetOption('clean'):
    env.Default('zip')
