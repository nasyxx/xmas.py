#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
Python ♡ Nasy.

    |             *         *
    |                  .                .
    |           .                              登
    |     *                      ,
    |                   .                      至
    |
    |                               *          恖
    |          |\___/|
    |          )    -(             .           聖 ·
    |         =\ -   /=
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

author   : Nasy https://nasy.moe
date     : Dec 22, 2017
update   : Dec 24, 2022
email    : Nasy <nasyxx+python@gmail.com>
filename : xmas.py
project  : xmas.py
license  : GPL-3.0+
url      : https://github.com/nasyxx/xmas.py

A cat, sitting on a wall, near a Xmas tree, is gazing starry
picturesque night.
"""
__version__ = "2022.1"

# Standard Library
import random
import sys

# Types
from typing import Tuple, Optional
from unicodedata import east_asian_width as ew

COLORS = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
)

SNOW = {"❅", "❆"}


def colorprint(
    string: str, color: Optional[str] = None, blink: bool = False
) -> str:
    """Print twinkle and colorful string."""
    color = color or random.choice(COLORS)
    return (
        f"\x1b[{str(30 + COLORS.index(color))};"
        f"{blink and 5 or ''}m{string}\x1b[0m"
    )


def star(
    x: str, density: float = 0, markers: Tuple[str, ...] = (".", "*", *SNOW)
) -> str:
    """Generate a star."""
    density = density or random.random() / 10
    if x == " ":
        if random.random() < density:
            return markers[0]
        elif random.random() > (1 - density):
            return random.choice(markers[1:])
    return x


def translate(x: str) -> str:
    """Translate a string to a twinkle colorful string."""
    if x == ".":
        return colorprint(x, "", random.random() < 0.2)
    elif x == "*":
        return colorprint(x, "", random.random() < 0.1)
    elif x in SNOW:
        return colorprint(x, "white", False)
    elif x in {"@", "&"}:
        return colorprint(
            x, random.choice(("cyan", "blue")), random.random() < 0.1
        )
    elif x in {",", "`", ";", "'", "#", "⁂"}:
        return colorprint(x, "", random.random() < 0.05)
    elif x in {"/", "\\", "^", "|", "_"}:
        return colorprint(x, "green", False)
    elif x == "★":
        return colorprint(x, "yellow", False)
    return x


def main() -> None:
    """Yooo, here is the main function."""
    name = sys.argv[1].upper() if len(sys.argv) > 1 else "NASY"
    nl = sum(map(lambda r: r == "W" and 2 or 1, map(ew, name)))
    mc = "MERRY CHRISTMAS "
    cat = ["| "] * 21 + [
        "|   .     |\\___/|   ",
        "|     .   )    -(   ",
        "|  *     =\\  -  /=  ",
        "|   .      )===(    ",
        "|      *  /   - \\   ",
        "|    .    |-    |   ",
        "|        /   -   \\  ",
        "| _______\\__( (__/__",
        "| ______|____) )|___",
        "| ___|______( /_____",
        "|_______|____∀_|____",
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
        "| |".center(53)[: -len(mc)] + mc,
        "| |".center(53)[: -nl - 1] + f"{name} ",
        "|_|".center(53, "_"),
    ]
    print(colorprint("." + "_".center(72, "_") + ".", "green"))
    for i, (ct, e) in enumerate(zip(cat, tree)):
        if i < len(tree) - 2:
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
                    nt.append(star(c, 0.05, ("#", "⁂", *SNOW)))
                    continue
                nt.append(star(c))
            tree[i] = "".join(map(translate, nt))
        print(tree[i] + colorprint("|", "green"), sep="\n")


if __name__ == "__main__":
    if "-v" in sys.argv:
        print("2022.1 -- https://github.com/nasyxx/xmas.py -- Nasy")
    else:
        main()
