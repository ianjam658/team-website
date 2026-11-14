#!/usr/bin/env python3
"""Create a ZIP archive of this repository, excluding Git internals and the archive itself."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "team-website.zip"
EXCLUDED_DIRS = {".git", "__pycache__"}


def main() -> None:
    files = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != ARCHIVE
        and not any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)
    )

    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT))

    print(f"Created {ARCHIVE.name} with {len(files)} files.")


if __name__ == "__main__":
    main()
