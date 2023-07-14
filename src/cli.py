# Convert a string to its unicode representation.
# Accept piped input or a series of arguments.
# Ref:
# - https://stackoverflow.com/questions/58942873/convert-a-string-into-a-unicode-escape-sequence#58943018

import sys

from esc import string_to_unicode
from esc import wordlist_to_unicode


SPACES = False
usage = f"Usage:\n\t{sys.argv[0]} STRING\n\techo \"STRING\" | {sys.argv[0]}"
output = "\\u0053\\u0054\\u0052\\u0049\\u004e\\u0047"
help = "Convert a string to its unicode representation; accepts piped input or a series of arguments."
args = sys.argv[1:]

if '-h' in args or '--help' in args:
    print(usage)
    print(f"Output:\n\t{output}\n")
    print(help)
    exit()
for o in ['-s', '--spaces']:
    if o in args:
        SPACES = True
        args.remove(o)
        break

if not sys.stdin.isatty():
    for line in sys.stdin:
        output = wordlist_to_unicode(line.rstrip().split())
        break
elif len(args) > 0:
    output = wordlist_to_unicode(args)

if SPACES:
    output = output.replace(' ', rf'\u0020')
print(output)
