"""
Automatically add all OpenSquirrel Python modules to docs/reference.md whenever the mkdocs documentation is built.
"""

from pathlib import Path

import mkdocs_gen_files

repo = Path(__file__).parent.parent
opensquirrel = repo / "opensquirrel"
reference_file = repo / "docs" / "reference.md"

reference_md_content = "<!--- This file was automatically generated by scripts/gen_reference_page.py --->\n\n"
for path in sorted(opensquirrel.rglob("*.py")):
    module_path = path.relative_to(repo).with_suffix("")

    parts = list(module_path.parts)

    if parts[-1] == "__init__":
        continue
    elif parts[-1] == "__main__":
        continue

    identifier = ".".join(parts)
    reference_md_content += "::: " + identifier + "\n"

with mkdocs_gen_files.open(reference_file, "w") as fd:
    print(reference_md_content, file=fd)