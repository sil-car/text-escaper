# Convert a string to its unicode representation.
# Accept piped input or a series of arguments.
# Ref:
# - https://stackoverflow.com/questions/58942873/convert-a-string-into-a-unicode-escape-sequence#58943018

import argparse
import sys

from .esc import wordlist_to_unicode_list


def setup_parser():
    usage = f"\n  {sys.argv[0]} STRING\n  echo \"STRING\" | {sys.argv[0]}"
    output = "  \\u0053\\u0054\\u0052\\u0049\\u004e\\u0047"
    description = "Convert a string to its unicode representation; accepts piped input or a series of arguments."

    parser = argparse.ArgumentParser(
        description=description,
        usage=f"{usage}\n\n{output}",
        )
    parser.add_argument(
        '--gui-debug', action='store_true',
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        '-s', '--escape-spaces', action='store_true',
        help=r"Output spaces as escaped value '\u0020' instead of ' '.",
        )
    parser.add_argument(
        '-w', '--with-text', action='store_true',
        help=r"Output original text before its escaped values: 'hôtel \u0068\u006f\u0302\u0074\u0065\u006c'.",
        )
    parser.add_argument(
        'STRING',
        nargs="*",
    )

    return parser.parse_args()

def main():
    args = setup_parser()

    # Make list of input words.
    text_words = []
    if not sys.stdin.isatty(): # accept piped input
        for line in sys.stdin:
            text_words.extend(line.rstrip().split())
            break
    if len(args.STRING) > 0: # accept args input
        text_words.extend(args.STRING)

    # Make list of uniscaped words.
    uniscaped_words = wordlist_to_unicode_list(text_words)

    # Prepare output string.
    if args.with_text:
        # Merge text_words with uniscaped_words.
        output_words = []
        min_len = min(len(text_words), len(uniscaped_words))
        for i in range(min_len):
            output_words.append(text_words[i])
            output_words.append(uniscaped_words[i])
        # Add any extra items if one list is longer (shouldn't happen).
        # output_words += text_words[min_len:] + uniscaped_words[min_len:]
    else:
        output_words =  uniscaped_words
    output_string = ' '.join(output_words)

    # Convert spaces if requested.
    if args.escape_spaces:
        output_string = output_string.replace(' ', r'\u0020')

    print(output_string)

if __name__ == '__main__':
    main()
