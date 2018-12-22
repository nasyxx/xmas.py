#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              '
    |         =\  -  /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

* author: Nasy
* date: Dec 22, 2017
* update: Dec 22, 2018
* email: nasyxx@gmail.com
* file: xmasx.py
* license: GPL-3.0+

A cat, sitting on a wall, near a Xmas tree, is gazing starry picturesque night.

Copyright © 2018 by Nasy. All Rights Reserved.
"""
# Standard Library
import sys
import random
from typing import Tuple

COLORS = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")


def colorprint(string: str, color: str = "", blink: bool = False) -> str:
    """Print twinkle and colorful string."""
    if not color:
        color = random.choice(COLORS)
    return (
        "\x1b["
        + ";".join([str(30 + COLORS.index(color)), "5" if blink else ""])
        + "m"
        + str(string)
        + "\x1b[0m"
    )


def star(
    x: str, density: float = 0, marker: Tuple[str, str] = (".", "*")
) -> str:
    """Generate a star."""
    if not density:
        density = random.random() / 10
    if x == " ":
        if random.random() < density:
            return marker[0]
        elif random.random() > (1 - density):
            return marker[1]
    return x


def translate(x: str) -> str:
    """Translate a string to a twinkle colorful string."""
    if x == ".":
        return colorprint(x, "", True if random.random() < 0.2 else False)
    elif x == "*":
        return colorprint(x, "", True if random.random() < 0.1 else False)
    elif x in {"@", "&"}:
        return colorprint(
            x,
            random.choice(("cyan", "blue")),
            True if random.random() < 0.1 else False,
        )
    elif x in {",", "`", ";", "'", "#", "⁂"}:
        return colorprint(x, "", True if random.random() < 0.05 else False)
    elif x in {"/", "\\", "^", "|", "_"}:
        return colorprint(x, "green", False)
    elif x == "★":
        return colorprint(x, "yellow", False)
    return x


def main() -> None:
    """Yooo, here is the main function."""
    name = sys.argv[1].upper() if len(sys.argv) > 1 else "NASY"
    cat = ["| "] * 21 + [
        "|   .     |\\___/|   ",
        "|     .   )    -(   ",
        "|  *     =\\  -  /=  ",
        "|   .      )===(    ",
        "|      *  /   - \\   ",
        "|    .    |-    |   ",
        "|        /   -   \\  ",
        f"| {name[:6]:_<6}_\\__( (__/__",
        "| ______|____) )|___",
        "| ___|______( (_____",
        "|_______|____\\_|____",
    ]
    tree = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "★",
        "/⁂\\",
        "/ \\",
        "@/.;'\\&",
        "&/_   _\\@",
        "@ / ,.;'\\ &",
        "/,.;'   \\",
        "@/;'      ,\\&",
        "@/_      ,.;_\\&",
        "/     ,.;'  \\",
        "&/   ,.;'      \\@",
        "@/  ,.;'`      ,.;'\\&",
        "@/,.;'       ,.;'    \\&",
        "////////////^\\\\\\\\\\\\\\\\\\\\\\\\",
        "| |",
        "| |",
        "|_|".center(53, "_"),
    ]
    print(colorprint("." + "_".center(72, "_") + ".", "green"))
    for i, (ct, e) in enumerate(zip(cat, tree)):
        tree[i] = e.center(53)
        cat[i] = ct.ljust(20)
        if not e:
            tree[i] = "".join(map(translate, map(star, cat[i] + tree[i])))
        else:
            inside = False
            nt = [""]
            if i < 21:
                nt.extend(map(star, cat[i]))
            else:
                nt.extend(cat[i])
            for c in tree[i]:
                if c == "/":
                    inside = True
                elif c == "\\":
                    inside = False
                if inside:
                    nt.append(star(c, 0.05, ("#", "⁂")))
                    continue
                nt.append(star(c))
            tree[i] = "".join(map(translate, nt))
        print(tree[i] + colorprint("|", "green"), sep="\n")


if __name__ == "__main__":
    main()
