#!/usr/bin/env python3
"""The Internet in One Word.

The bounty asks for a single word that sums up the whole internet, and a
model judge compares entries two at a time on the brief sealed with the
bounty. The brief weighs, in order: the entry is one word; it earns a
laugh on its own; it says something true about the internet as a whole;
it surprises instead of reaching for the first obvious word; it lands in
one beat, short and instantly readable. The best word makes a reader
laugh first and then nod.

The word this program writes is "circus".

Why circus and not the first words anyone reaches for: "everything" is
true but flat, "connection" is a brochure word, "noise" is only a mood.
Circus is the whole show at once. Clowns, acrobats, strongmen and
spectators, everyone performing at the same time, nobody quite in
charge, the tent always one tent-peg from coming down. That is the
internet as a whole: a spectacle, a mess, and a crowd that cannot look
away. It is funny by itself, it is true of the whole thing rather than
one app, it is not the obvious pick, and at six letters it lands before
the reader has time to think.

The program does one thing and does it the same way every run: it writes
exactly that word, and nothing else, to /output/entry.txt.
"""

import os

WORD = "circus"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)
    os.chmod("/output/entry.txt", 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
