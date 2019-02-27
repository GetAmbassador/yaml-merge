#!/usr/bin/env python
import glob
import os
import re

def remove_prefix_and_suffix(yaml):
    prefix = '---\n'
    suffix = '\n---\n'

    return yaml[yaml.startswith(prefix) and len(prefix):\
                   (yaml.endswith(suffix) and len(suffix)) or None].rstrip() + '\n'

def main():
    tags = []
    raw_yaml = []
    pattern = r"\{([A-Za-z0-9_]+)\}"

    for f in glob.iglob("./definitions/**/*.yaml", recursive=True):
        with open(f, 'r+') as y:
            tmp = remove_prefix_and_suffix(y.read())
            tags += re.findall(pattern, tmp)
            raw_yaml.append(tmp)

    tag_values = {}
    for t in set(tags):
        tag_values[t] = os.getenv(t) or ''

    print('---\n'.join(raw_yaml).format(**tag_values))
