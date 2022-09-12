from collections import defaultdict
from pathlib import Path

from objects import CORPS, SOURCES, AUTHORS, Mech, MECHS
from resources import RESOURCE_GROUPS, _is_image_group
from resource_classes import Image, MechResource


def _generate_mech_readme_from_group_name_to_content(
    mech: Mech, groups_to_content: dict[str, list[MechResource]]
) -> str:
    content_groups = {}
    image_groups = {}
    for name, content in groups_to_content.items():
        if _is_image_group(content):
            image_groups[name] = content
        else:
            content_groups[name] = content

    lines = [
        f"### {mech.name.capitalize().replace('_', ' ')}\n",
        f"Corp: {mech.corp}\n",
        f"Source: [{mech.source.name}]({mech.source.url}), by {mech.source.author} \n",
    ]
    if mech.summary:
        for line in mech.summary:
            lines.append(f"- {line}\n")

    if mech.image_path:
        if not isinstance(mech.image_path, list):
            mech.image_path = [mech.image_path]
        for image_path in mech.image_path:
            lines.append(
                f'<img src="{image_path}" width="500"/>\n',
            )

    for name, content in content_groups.items():
        if not name or not content:
            continue  # This assumes non-image resources always have a name
        lines.append(f"#### {name}")
        if not isinstance(content, list):
            content = [content]
        for item in content:
            lines.append(f"- {item}")

    if image_groups:
        lines.append("<details>")
        lines.append("<summary>Images</summary>\n")
        named_image_groups = {
            name: content for name, content in image_groups.items() if name
        }
        unnamed_image_groups = {
            name: content for name, content in image_groups.items() if not name
        }
        for name, content in named_image_groups.items():
            lines.append(f"##### {name}")
            if not isinstance(content, list):
                content = [content]
            for item in content:
                assert isinstance(item, Image)
                lines.append(item.get_readme())

        if unnamed_image_groups:
            lines.append(f"##### miscellaneous")
            for name, content in unnamed_image_groups.items():
                if name:
                    continue
                if not isinstance(content, list):
                    content = [content]
                for item in content:
                    assert isinstance(item, Image)
                    lines.append(item.get_readme())

    lines.append("</details>")

    text = "\n".join(lines)
    return text


def generate_mech_readme(mech: Mech) -> str:
    group_names_to_content: dict[str, list[MechResource]] = defaultdict(list)
    for resource_group in RESOURCE_GROUPS:
        contents = resource_group.resources.get(mech, [])
        if not isinstance(contents, list):
            contents = [contents]
        group_names_to_content[resource_group.name] += contents

    mech_readme = _generate_mech_readme_from_group_name_to_content(
        mech, group_names_to_content
    )
    return mech_readme


def get_mech_toc_line(mech: Mech) -> str:
    header_link = mech.name.replace(" ", "-").replace("'", "")
    return f"- [{mech.name.capitalize()}](#{header_link})"


def generate_all_mechs_toc() -> str:
    toc_lines = ["<details>\n", "<summary>All Mechs</summary>\n"]
    for mech in MECHS:
        toc_lines.append(get_mech_toc_line(mech))
    toc_lines.append("</details>")
    toc = "\n".join(toc_lines)
    return toc


def generate_toc_by_corp() -> str:
    toc_lines = ["<details>\n", "<summary>Mechs by Corp</summary>\n"]
    for corp in CORPS:
        toc_lines.append("<details>")
        toc_lines.append(f"<summary>{corp}</summary>\n")
        for mech in MECHS:
            if mech.corp == corp:
                toc_lines.append(get_mech_toc_line(mech))
        toc_lines.append("</details>")
    toc_lines.append("</details>")
    toc = "\n".join(toc_lines)
    return toc


def generate_toc_by_source() -> str:
    toc_lines = ["<details>\n", "<summary>Mechs by Source</summary>\n"]
    for source in SOURCES:
        toc_lines.append("<details>")
        toc_lines.append(f"<summary>{source}</summary>\n")
        for mech in MECHS:
            if mech.source == source:
                toc_lines.append(get_mech_toc_line(mech))
        toc_lines.append("</details>")
    toc_lines.append("</details>")
    toc = "\n".join(toc_lines)
    return toc


def generate_toc_by_author() -> str:
    toc_lines = ["<details>\n", "<summary>Mechs by Author</summary>\n"]
    for author in AUTHORS:
        toc_lines.append("<details>")
        toc_lines.append(f"<summary>{author}</summary>\n")
        for mech in MECHS:
            if mech.source.author == author:
                toc_lines.append(get_mech_toc_line(mech))
        toc_lines.append("</details>")
    toc_lines.append("</details>")
    toc = "\n".join(toc_lines)
    return toc


def generate_tocs():
    all_toc = generate_all_mechs_toc()
    corp_toc = generate_toc_by_corp()
    source_toc = generate_toc_by_source()
    author_toc = generate_toc_by_author()

    full_text = "\n\n---\n\n".join([all_toc, corp_toc, source_toc, author_toc])
    return full_text


def generate_readme():
    mech_readmes = []

    toc = generate_tocs()

    for mech in MECHS:
        mech_readme = generate_mech_readme(mech)
        mech_readmes.append(mech_readme)

    readme = "\n\n-------\n".join([toc] + mech_readmes)
    return readme


if __name__ == "__main__":
    readme = generate_readme()
    Path("README.md").write_text(readme)
    print("done")
