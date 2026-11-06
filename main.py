"""V Ray — A desktop helper that finds V Ray data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='v_ray_desktop',
        description='A desktop helper that finds V Ray data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('V Ray')
    print('Dated copies of V Ray data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# polish (2026-11-03)
# small fix (2026-11-03)
# update note (2026-11-05)
# refactor bit (2026-11-06)
# polish (2026-11-06)
