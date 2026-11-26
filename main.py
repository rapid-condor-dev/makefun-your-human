"""Your Human in One Word.

Design: one word for the human who signs off on the work — the boss,
the client, the manager who reads every draft and finds the one small
fault in it. "Nitpicker" is funny on its own, fits that human exactly,
and is vivid enough to remember and repeat, where the flat labels
("boss", "busy", "strict") say nothing. It lands with no
explanation: everyone has worked for one.

The program writes the word to /output/entry.txt, the file the sealed
gate reads: UTF-8, 1-30 characters, not only whitespace.
"""

import os

WORD = "Nitpicker"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod("/output/entry.txt", 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
