#!/usr/bin/env python3

import base64
import logging
import argparse
import glob
import webbrowser

import yaml

from os.path import relpath
from copy import deepcopy
from collections import defaultdict


def generate_stack_filename(filename):
    # relpath mainly used here to strip out multiple occurrences of `/` for aesthetics
    return relpath(f'{args.stack_dir}/{filename}.yaml')


def gen_short_name(name, id_num, seen):
    if not name in seen.keys():
        id_num += 1
        ident = f'i{id_num}'
        seen[name] = ident
        return f'{ident}["{name}"]', id_num, seen
    return seen[name], id_num, seen


def walk_imports(filename, parents=[], output=[], mermaid=defaultdict(list)):
    parents.append(filename)
    with open(filename) as f:
        body = f.read()
        data = yaml.safe_load(body)

    parents_chain = ' > '.join(parents)
    output.append(f'''---
###
### stack: {filename}
### chain: {parents_chain}
###


{body}
''')
    
    for f in data.get('import', []):
        import_filename = generate_stack_filename(f)
        short_import_filename = import_filename.replace(args.stack_dir, '')
        short_filename = filename.replace(args.stack_dir, '')
        mermaid[short_filename].append(short_import_filename)
        logger.debug(f'import: {f}')
        logger.debug(f'parents: {parents}')
        walk_imports(import_filename, deepcopy(parents), output, mermaid)
    
    return output, mermaid

    
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("stack", help="stack file to read imports from")
parser.add_argument("-d", "--stack-dir", help="base stack directory name", default="stacks/")
parser.add_argument("-f", "--flowchart", help="https://mermaid-js.github.io/mermaid/#/flowchart?id=flowchart-orientation", default="LR")
parser.add_argument("-l", "--logging-level", help="execution logging level", default="info")
parser.add_argument("-m", "--mermaid", help="output mermaid graph", action=argparse.BooleanOptionalAction, default=False)
parser.add_argument("-o", "--open-mermaid", help="open mermaid graph in browser", action=argparse.BooleanOptionalAction, default=False)

args = parser.parse_args()

logging.basicConfig(level=args.logging_level.upper())
logger = logging.getLogger(__name__)

logger.debug(f'args: {args}')


def main():
    output, mermaid = walk_imports(args.stack)

    mermaid_diagram = f'flowchart {args.flowchart}\n'
    id_num = 0
    seen = {}
    for parent, children in mermaid.items():
        for child in children:
            c, id_num, seen = gen_short_name(parent, id_num, seen)
            i, id_num, seen = gen_short_name(child, id_num, seen)
            mermaid_diagram += f'  {c} --> {i}\n'

    if args.mermaid:
        print(mermaid_diagram)
    else:
        print('\n'.join(output))

    if args.open_mermaid:
        b64_mermaid = base64.b64encode(mermaid_diagram.encode("ascii")).decode("ascii")
        webbrowser.open(f'https://mermaid.ink/img/{b64_mermaid}')


if __name__ == "__main__":
    main()