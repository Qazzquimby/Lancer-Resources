from dataclasses import dataclass

from objects import Mech


@dataclass
class Image:
    path: str
    source: str = None

    def get_readme(self) -> str:
        lines = [
            f"<img src='{self.path}' width='400'>\n",
        ]
        if self.source:
            if self.source.startswith("http"):
                lines.append(f"[Source]({self.source})\n")
            else:
                lines.append(f"Source: {self.source}\n")
        else:
            lines.append("Source: Unknown.\n")
        return "\n".join(lines)


MechResource = str | list[str] | Image
MechResources = dict[Mech, MechResource]


@dataclass
class ResourceGroup:
    resources: MechResources
    name: str = None


def get_image_resources_with_source(source: str, mechs_to_paths) -> MechResources:
    all_images = {}
    for mech in mechs_to_paths.keys():
        paths = mechs_to_paths[mech]
        if isinstance(paths, list):
            images_at_path = [Image(source=source, path=path) for path in paths]
        else:
            path = paths  # just one
            images_at_path = Image(source=source, path=path)
        all_images[mech] = images_at_path
    return all_images
