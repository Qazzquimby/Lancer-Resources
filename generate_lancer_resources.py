from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


def list_content(enum_class):
    all_contents = [
        item
        for item in dir(enum_class)
        if not callable(getattr(enum_class, item)) and not item.startswith("__")
    ]
    useful_contents = [getattr(enum_class, item) for item in all_contents]
    sorted_contents = sorted(useful_contents, key=lambda item: str(item))
    return sorted_contents


class Corps:
    GMS = "GMS"
    IPSN = "IPSN"
    SSC = "SSC"
    HORUS = "HORUS"
    HA = "HA"
    MFECANE = "MFECANE"


CORPS: list[str] = list_content(Corps)


class Sources:
    CORE = "Core Book"
    WALLFLOWER = "No Room for a Wallflower"
    LONG_RIM = "Long Rim"
    KARRAKIN_TRADE_BARONIES = "Field Guide: The Karrakin Trade Baronies"
    MFECANE = "Field Guide: Mfecane"


SOURCES: list[str] = list_content(Sources)


class Authors:
    MASSIF = "Massif Press"
    NHP_SHAKA = "NHP-SHAKA"


AUTHORS: list[str] = list_content(Authors)


@dataclass
class Mech:
    name: str
    corp: str
    source: str = Sources.CORE
    author: str = Authors.MASSIF
    image_path: str | list[str] = None

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


class Mechs:
    EVEREST = Mech(name="everest", corp=Corps.GMS)
    SAGARMATHA = Mech(name="sagarmatha", corp=Corps.GMS, source=Sources.WALLFLOWER)

    BLACKBEARD = Mech(
        name="blackbeard",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/a/a1/Blackbeard.jpg/revision/latest?cb=20200509100622",
    )
    DRAKE = Mech(
        name="drake",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/6/62/Drake.jpg/revision/latest?cb=20200509100716",
    )
    LANCASTER = Mech(
        name="lancaster",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/2/2c/Lancaster.jpg/revision/latest?cb=20200509101034",
    )
    KIDD = Mech(
        name="kidd",
        corp=Corps.IPSN,
        source=Sources.WALLFLOWER,
        image_path="https://pbs.twimg.com/media/EfE34JxXoAEWdnT.jpg:large",
    )
    NELSON = Mech(
        name="nelson",
        corp=Corps.IPSN,
        image_path="https://pbs.twimg.com/media/D0da5CUWwAAwpO0.jpg:large",
    )
    RALEIGH = Mech(
        name="raleigh",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/6/69/Raleigh.jpg/revision/latest?cb=20200509101441",
    )
    TORTUGA = Mech(
        name="tortuga",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/0/03/Tortuga.jpg/revision/latest?cb=20200509101655",
    )
    VLAD = Mech(
        name="vlad",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/d/d1/Vlad.jpg/revision/latest?cb=20200509101717",
    )
    CALIBAN = Mech(
        "caliban",
        corp=Corps.IPSN,
        source=Sources.LONG_RIM,
        image_path="https://external-preview.redd.it/uiHVNTr51s5O7LdbPLLwI-BkRrvRmbPZx_XW4m2jH1U.jpg?auto=webp&s=51e7c6a99d745f9c9a5e213a848219cfc2682382",
    )

    BLACK_WITCH = Mech(
        name="black_witch",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/4/47/Blackwitch1.jpeg/revision/latest?cb=20210510124208",
    )
    DUSK_WING = Mech(
        name="dusk_wing",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D28PCW3WsAIGZuU.jpg:large",
    )
    MONARCH = Mech(
        name="monarch",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D0SvXINX4AEcN1Z.jpg:large",
    )
    DEATHS_HEAD = Mech(
        name="death's head",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D3AyF5pXgAIM3t_.jpg:large",
    )
    SWALLOWTAIL = Mech(
        name="swallowtail",
        corp=Corps.SSC,
        image_path="https://external-preview.redd.it/4ts71UdtaOTzZJOYApRc6U-m5G_CgzyTx9PGVqAKvn8.jpg?auto=webp&s=f54bcc86818f54f4e3008ceee2c50842201e93fa",
    )
    SWALLOWTAIL_RANGER = Mech(
        name="swallowtail_ranger",
        corp=Corps.SSC,
        image_path="https://cdnb.artstation.com/p/assets/images/images/035/138/645/large/theotime-gm-ranger-variant-web.jpg?1614191125",
    )
    METALMARK = Mech(
        name="metalmark",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/b/ba/Metalmark.jpeg/revision/latest?cb=20210510130854",
    )
    MOURNING_CLOAK = Mech(
        name="mourning_cloak",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/1/15/MourningCloak.jpg/revision/latest?cb=20200509101339",
    )

    ATLAS = Mech(
        name="atlas",
        corp=Corps.SSC,
        source=Sources.LONG_RIM,
        image_path=[
            "https://pbs.twimg.com/media/D55kqK-WwAAMyND?format=jpg&name=large",
            "https://pbs.twimg.com/media/EMXOad_WwAMMkZM?format=jpg&name=large",
        ],
    )
    WHITE_WITCH = Mech(
        name="white_witch",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://pbs.twimg.com/media/EM6PMpPW4AAn668.jpg:large",
    )
    EMPEROR = Mech(
        name="emperor",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://external-preview.redd.it/YVWXiFNpCBcuyvcvPzX3Y1tjOnEQ_2XX2e2W1kueA0Y.jpg?auto=webp&s=f71b0a8c1ccb329dd0b0523260c8c18c88ec97a8",
    )
    ORCHIS = Mech(
        name="orchis",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://preview.redd.it/7ulbcgdnafn81.jpg?auto=webp&s=2af07f9391443e756c07e3f94108e0c7ca94f965",
    )

    BALOR = Mech(
        name="balor",
        corp=Corps.HORUS,
        image_path="https://external-preview.redd.it/NfhQ53rmZpR7nZs7Giymy0QVlKnV_3KMS4hmuXEsIRU.jpg?auto=webp&s=6f5af6c3cb517bfa26be2535c89ab9b540a49043",
    )
    PEGASUS = Mech(
        name="pegasus",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/Dm7Lwc1XsAElCJj.jpg:large",
    )
    LICH = Mech(
        name="lich",
        corp=Corps.HORUS,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D6dRYIeW0AEhBg2.jpg:large",
    )
    MANTICORE = Mech(
        name="manticore",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D15ojOZW0AAcdQn.jpg:large",
    )
    HYDRA = Mech(
        name="hydra",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D3ZsrznWkAEDfHl.jpg:large",
    )
    GOBLIN = Mech(
        name="goblin",
        corp=Corps.HORUS,
        image_path="https://static.wikia.nocookie.net/lancer/images/e/ef/Goblin.jpg/revision/latest?cb=20200509100851",
    )
    GORGON = Mech(
        name="gorgon",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/DhCxXZtWsAEa0HH.jpg",
    )
    MINOTAUR = Mech(
        name="minotaur",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D0NqbpiXgAE6WLs.jpg:large",
    )
    KOBOLD = Mech(
        name="kobold",
        corp=Corps.HORUS,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D4M6nGAWkAEmIQB.jpg:large",
    )
    CALENDULA = Mech(
        name="calendula",
        corp=Corps.HORUS,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://pbs.twimg.com/media/FNXBM8JXIAsBmrc.jpg:large",
    )

    BARBAROSSA = Mech(
        name="barbarossa",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/Ds471y1WsAAjpwJ.jpg",
    )
    ENKIDU = Mech(
        name="enkidu",
        corp=Corps.HA,
        source=Sources.WALLFLOWER,
        image_path="https://preview.redd.it/5ev5xcyprab81.jpg?auto=webp&s=768fba2788fc4d9c61d3bce3ffe1e8b32aa12905",
    )
    GENGHIS = Mech(
        name="genghis",
        corp=Corps.HA,
        image_path="https://external-preview.redd.it/HnEsHvovvilWcBUdooCiFLgd99EzEMlwjMgzHIihSZA.jpg?auto=webp&s=10a5adb10e31c2fcba4936dec7b2b39731ec14b0",
    )
    GENGHIS_WORLDKILLER = Mech(
        name="genghis worldkiller",
        corp=Corps.HA,
        source=Sources.WALLFLOWER,
        image_path="https://cdn-animation.artstation.com/p/thumbnails/000/265/518/thumb.jpg",
    )
    ISKANDER = Mech(
        name="iskander",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/D3V3iiaXkAEO29u.jpg:large",
    )
    NAPOLEON = Mech(
        name="napoleon",
        corp=Corps.HA,
        image_path="https://external-preview.redd.it/flbCTCmqhnLOoWTzF6lRtYZPgpKtf9duWoLOqF6Zxiw.jpg?auto=webp&s=d968822a1fffa257adc347b4f59eadcdf1699ffe",
    )
    SALADIN = Mech(
        name="saladin",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/D3HXdK3XcAEkLxk.jpg:large",
    )
    SHERMAN = Mech(
        name="sherman",
        corp=Corps.HA,
        image_path=[
            "https://pbs.twimg.com/media/D3w3yZ-XoAAGo_x?format=jpg&name=large",
            "https://pbs.twimg.com/media/Df3RCD7XcAAws0N.jpg:large",
        ],
    )
    TOKUGAWA = Mech(
        name="tokugawa",
        corp=Corps.HA,
        image_path="https://64.media.tumblr.com/8642aa32ea7e7fde660a6d5daa833a8e/tumblr_pgedezbTgB1qlxan5o1_1280.jpg",
    )
    SUNZI = Mech(
        name="sunzi",
        corp=Corps.HA,
        source=Sources.LONG_RIM,
        image_path="https://ksr-ugc.imgix.net/assets/024/944/488/16ffd6f132e4ecd32ee139293b129442_original.jpg?ixlib=rb-4.0.2&w=700&fit=max&v=1556548469&gif-q=50&q=92&s=9f83682094aafa03d5a39cb69e4760e0",
    )
    ZHENG = Mech(
        name="zheng",
        corp=Corps.HA,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D4xiHSrW4AA7IM5.jpg:large",
    )

    IBUTHO = Mech(
        name="ibutho",
        corp=Corps.MFECANE,
        source=Sources.MFECANE,
        author=Authors.NHP_SHAKA,
        image_path=[
            "https://preview.redd.it/dgnj8y0n51q61.png?width=512&format=png&auto=webp&s=db1d0ba19fa81acd625a801898c1a4f48fab279d",
            "https://preview.redd.it/fga3361n51q61.png?width=512&format=png&auto=webp&s=f25b79691edd1b70dabf504f33612ff2cfe1d754",
        ],
    )


MECHS: list[Mech] = list_content(Mechs)


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


RESOURCE_GROUPS: list[ResourceGroup] = [
    ResourceGroup(
        name="Trashtalk on Lancer, Mech Overviews",
        resources={
            Mechs.EVEREST: "https://www.youtube.com/watch?v=9qI1tP-RL7k&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=1",
            Mechs.BLACKBEARD: "https://www.youtube.com/watch?v=SUuM2sCVzZk&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=2",
            Mechs.BLACK_WITCH: "https://www.youtube.com/watch?v=rqVa7qQSY8s&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=3",
            Mechs.BALOR: "https://www.youtube.com/watch?v=xpMPQm60BV0&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=4",
            Mechs.BARBAROSSA: "https://www.youtube.com/watch?v=ZjN8Lrx0KYY&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=5",
            Mechs.MANTICORE: "https://www.youtube.com/watch?v=DhCPP32OlxY&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=6",
            Mechs.PEGASUS: "https://www.youtube.com/watch?v=KAYnUG83EB0&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=7",
            Mechs.RALEIGH: "https://www.youtube.com/watch?v=fXEFL8Mn8zc&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=8",
            Mechs.MONARCH: "https://www.youtube.com/watch?v=zxitMCtKC3E&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=9",
            Mechs.TOKUGAWA: "https://www.youtube.com/watch?v=kZBxbmxhaqM&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=10",
            Mechs.MINOTAUR: "https://www.youtube.com/watch?v=zV4TWjecIMU&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=11",
            Mechs.SWALLOWTAIL: "https://www.youtube.com/watch?v=lbiaGCdcClI&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=12&",
            Mechs.SWALLOWTAIL_RANGER: "https://www.youtube.com/watch?v=dPh19Z_jj8I&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=39&",
            Mechs.NAPOLEON: "https://www.youtube.com/watch?v=9vvWunzWp2w&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=13",
            Mechs.VLAD: "https://www.youtube.com/watch?v=AZUOtxbvyNI&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=14",
            Mechs.GOBLIN: "https://www.youtube.com/watch?v=5WuK1yrWGRY&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=15",
            Mechs.LANCASTER: "https://www.youtube.com/watch?v=5bhuWhT-B1I&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=16",
            Mechs.MOURNING_CLOAK: "https://www.youtube.com/watch?v=JBEWs7WCZ4E&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=17",
            Mechs.GENGHIS: "https://www.youtube.com/watch?v=lpI38hitHRs&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=18",
            Mechs.GORGON: "https://www.youtube.com/watch?v=1brSIB16AYU&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=19",
            Mechs.DRAKE: "https://www.youtube.com/watch?v=uUAaAbnssi0&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=20&",
            Mechs.DUSK_WING: "https://www.youtube.com/watch?v=Fo3peXAoC1M&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=21",
            Mechs.SHERMAN: "https://www.youtube.com/watch?v=eu2UE1sPRwk&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=22",
            Mechs.HYDRA: "https://www.youtube.com/watch?v=XUojhsHqsEw&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=23",
            Mechs.TORTUGA: "https://www.youtube.com/watch?v=386vWQOpCAg&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=24",
            Mechs.DEATHS_HEAD: "https://www.youtube.com/watch?v=3b2LcyaCEZE&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=25",
            Mechs.SALADIN: "https://www.youtube.com/watch?v=YhSfLeq8Ujg&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=26",
            Mechs.METALMARK: "https://www.youtube.com/watch?v=OpQzi9b8-os&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=27&",
            Mechs.ISKANDER: "https://www.youtube.com/watch?v=lpnWkWii274&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=28&",
            Mechs.CALIBAN: [
                "https://www.youtube.com/watch?v=X0Ll59VKy0I&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=29",
                "https://youtu.be/EcJUGtXKt0Q?t=56",
            ],
            Mechs.ATLAS: [
                "https://www.youtube.com/watch?v=P6ihnobmJqk&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=30",
                "https://youtu.be/EcJUGtXKt0Q?t=27",
            ],
            Mechs.ZHENG: "https://www.youtube.com/watch?v=NXSXEClUPVs&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=31",
            Mechs.SUNZI: [
                "https://www.youtube.com/watch?v=yDsTi83YklA&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=32",
                "https://youtu.be/EcJUGtXKt0Q",
            ],
            Mechs.KOBOLD: "https://www.youtube.com/watch?v=ylndROGoXXI&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=34",
            Mechs.LICH: "https://www.youtube.com/watch?v=H1DpWCKET34&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=35",
            Mechs.NELSON: "https://www.youtube.com/watch?v=3uXrwj7Ifro&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=37",
            Mechs.KIDD: "https://www.youtube.com/watch?v=HAH6erftukg&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=38",
            Mechs.SAGARMATHA: "https://www.youtube.com/watch?v=dPh19Z_jj8I&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=39&",
            Mechs.ENKIDU: "https://www.youtube.com/watch?v=nYZrPByvGcM&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=40&",
            Mechs.GENGHIS_WORLDKILLER: "https://www.youtube.com/watch?v=nYZrPByvGcM&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=40&",
            Mechs.WHITE_WITCH: "https://www.youtube.com/watch?v=UrekNv1vw74&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=41",
            Mechs.EMPEROR: "https://www.youtube.com/watch?v=ZwEQHK376as&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=42",
            Mechs.ORCHIS: "https://www.youtube.com/watch?v=OCME2FhXdLw&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=43",
            Mechs.CALENDULA: "https://www.youtube.com/watch?v=OCME2FhXdLw&list=PLOnXWQrYlGSDt2WL5TdRgfMEw9kzP_-XP&index=43",
        },
    ),
    ResourceGroup(
        name="Lancer Custom Werks, lancer builds",
        resources={
            Mechs.EVEREST: "https://www.youtube.com/watch?v=aYXwgsUNpcA&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=1",
            Mechs.BLACKBEARD: "https://www.youtube.com/watch?v=EHf7SRGP6J8&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=2",
            Mechs.ATLAS: "https://www.youtube.com/watch?v=0TkfEE7RHT8&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=3",
            Mechs.NAPOLEON: "https://www.youtube.com/watch?v=Ahq3tNyr0PM&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=4",
            Mechs.PEGASUS: "https://www.youtube.com/watch?v=7rMKgF_pvT0&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=5",
            Mechs.TORTUGA: "https://www.youtube.com/watch?v=5m9H-BQQ_SM&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=6",
            Mechs.MONARCH: "https://www.youtube.com/watch?v=PJLpl-74VA0&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=7",
            Mechs.LICH: "https://www.youtube.com/watch?v=WsmfKNGWKPU&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=8",
            Mechs.BARBAROSSA: "https://www.youtube.com/watch?v=PtmHWmVbb8I&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=9",
            Mechs.NELSON: "https://www.youtube.com/watch?v=6LfSTbNe3IY&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=10",
            Mechs.BLACK_WITCH: "https://www.youtube.com/watch?v=OPACqFvKCSQ&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=11",
            Mechs.BALOR: "https://www.youtube.com/watch?v=6xUhPPqb7jk&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=12",
            Mechs.ENKIDU: "https://www.youtube.com/watch?v=QQYPXWRbzLg&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=13",
            Mechs.KIDD: "https://www.youtube.com/watch?v=GFMFrxfYXKk&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=14",
            Mechs.DUSK_WING: "https://www.youtube.com/watch?v=Mhyle5yEFCs&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=15",
            Mechs.MANTICORE: "https://www.youtube.com/watch?v=wxSz13k35zo&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=16",
            Mechs.TOKUGAWA: "https://www.youtube.com/watch?v=mrZQvfbMYbs&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=17",
            Mechs.CALIBAN: "https://www.youtube.com/watch?v=IPHVBdTkZLA&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=18",
            Mechs.DEATHS_HEAD: "https://www.youtube.com/watch?v=qdyTbPnKA_4&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=19",
            Mechs.HYDRA: "https://www.youtube.com/watch?v=MMEOxU7HApk&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=20",
            Mechs.GENGHIS_WORLDKILLER: "https://www.youtube.com/watch?v=HeAIRn_ejUI&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=21",
            Mechs.LANCASTER: "https://www.youtube.com/watch?v=o8l6CSt6BaU&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=22",
            Mechs.MOURNING_CLOAK: "https://www.youtube.com/watch?v=0Vt7de3rAwU&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=23",
            Mechs.GOBLIN: "https://www.youtube.com/watch?v=i0k8IteO44E&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=24",
            Mechs.ISKANDER: "https://www.youtube.com/watch?v=YjlTfaiokyE&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=25",
            Mechs.RALEIGH: "https://www.youtube.com/watch?v=-g_uCb7iz3k&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=26",
            Mechs.SWALLOWTAIL: "https://www.youtube.com/watch?v=Lp9T3BLnAuA&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=27",
            Mechs.GORGON: "https://www.youtube.com/watch?v=8JauCUWQ8U4&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=28",
            Mechs.SUNZI: "https://www.youtube.com/watch?v=LVb9KfOLEQg&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=29",
            Mechs.ZHENG: "https://www.youtube.com/watch?v=jb3Bx_25dT8&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=30",
            Mechs.METALMARK: "https://www.youtube.com/watch?v=ns7WSKuOfLw&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=31",
            Mechs.MINOTAUR: "https://www.youtube.com/watch?v=5lwdEqrtJT0&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=32",
            Mechs.SHERMAN: "https://www.youtube.com/watch?v=Gccu9fyAeFU&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=33",
            Mechs.DRAKE: "https://www.youtube.com/watch?v=FPvy7UpU3K0&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=34",
            Mechs.EMPEROR: "https://www.youtube.com/watch?v=sbJMmJnVyPo&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=35",
            Mechs.KOBOLD: "https://www.youtube.com/watch?v=0THcOe5LwAE&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=36",
            Mechs.SALADIN: "https://www.youtube.com/watch?v=0m6YLA5VcWY&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=37",
            Mechs.VLAD: "https://www.youtube.com/watch?v=MnhJRc1IU9k&list=PLOnXWQrYlGSAgita8M5UU5oexBAh2C99L&index=38",
        },
    ),
    ResourceGroup(
        name="Stiq Atlas Guide",
        resources={
            Mechs.ATLAS: "https://docs.google.com/document/d/14LvDk5pLY1I5Y09EWvtPu2Q4LJl64SoibW0jNVEzHv8/edit#"
        },
    ),
    # IMAGES
    ResourceGroup(
        name="VEX memes",
        resources=get_image_resources_with_source(
            source="https://imgur.com/a/Ek5GSwa",
            mechs_to_paths={
                Mechs.ATLAS: "https://i.imgur.com/hCw5eEC.jpeg",
                Mechs.BALOR: "https://i.imgur.com/xZQWFC0.jpeg",
                Mechs.BARBAROSSA: "https://i.imgur.com/niZF56R.jpeg",
                Mechs.BLACKBEARD: "https://i.imgur.com/hkqtanS.jpeg",
                Mechs.CALENDULA: "https://i.imgur.com/0ZxlJsP.jpeg",
                Mechs.DUSK_WING: "https://i.imgur.com/3ViAeQ5.jpeg",
                Mechs.EVEREST: "https://i.imgur.com/yy6RaGk.jpeg",
                Mechs.GENGHIS: "https://i.imgur.com/3Yvu5mn.jpeg",
                Mechs.GORGON: "https://i.imgur.com/qeZnBWL.jpeg",
                Mechs.IBUTHO: "https://i.imgur.com/NVi5buX.jpeg",
                Mechs.ISKANDER: "https://i.imgur.com/7HVUvhe.jpeg",
                Mechs.KIDD: "https://i.imgur.com/iEHTSVi.png",
                Mechs.LANCASTER: "https://i.imgur.com/43kMUoM.jpeg",
                Mechs.MANTICORE: "https://i.imgur.com/uunGqoV.jpeg",
                Mechs.MONARCH: "https://i.imgur.com/6uEZ1aw.jpeg",
                Mechs.PEGASUS: "https://i.imgur.com/825EqVz.jpeg",
                Mechs.RALEIGH: "https://i.imgur.com/d7x3fkq.png",
                Mechs.SALADIN: "https://i.imgur.com/aQp4IEg.jpeg",
                Mechs.SHERMAN: "https://i.imgur.com/AwEj6HY.jpeg",
                Mechs.SUNZI: "https://i.imgur.com/oaCT8fL.jpeg",
                Mechs.SWALLOWTAIL: "https://i.imgur.com/75JzM1v.jpeg",
                Mechs.TOKUGAWA: [
                    "https://i.imgur.com/wGZojxU.jpeg",
                    "https://i.imgur.com/o0Tf73b.jpeg",
                ],
                Mechs.VLAD: "https://i.imgur.com/p4m7shF.jpeg",
                Mechs.ZHENG: "https://i.imgur.com/UZyIGbq.jpeg",
            },
        ),
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://twitter.com/ShadeFish1/status/1526362574350127104?s=20&t=3XgB7A50VHP-wPRwWshRrA",
            mechs_to_paths={
                Mechs.TOKUGAWA: "https://pbs.twimg.com/media/FS66E3iXEAMvGaB?format=jpg&name=4096x4096",
                Mechs.HYDRA: "https://pbs.twimg.com/media/FS66E4PWYAASMu_?format=jpg&name=4096x4096",
                Mechs.BLACKBEARD: "https://pbs.twimg.com/media/FS66Gq8WIAA_UDv?format=jpg&name=4096x4096",
                Mechs.BARBAROSSA: "https://pbs.twimg.com/media/FS66HOPWAAAGOZ7?format=jpg&name=4096x4096",
            },
        ),
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://twitter.com/ShadeFish1/status/1539776426886430720?s=20&t=ZM_19zR4z5xevMEoxCOPRg",
            mechs_to_paths={
                Mechs.EVEREST: "https://pbs.twimg.com/media/FV5iLF9XEAAzAhm?format=jpg&name=4096x4096",
                Mechs.MONARCH: "https://pbs.twimg.com/media/FV5iOurWAAMEY_o?format=jpg&name=4096x4096",
                Mechs.KIDD: "https://pbs.twimg.com/media/FV5iPw2XwAUZWSj?format=jpg&name=4096x4096",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://theogm.artstation.com/projects/DxrJnG",
            mechs_to_paths={
                Mechs.MOURNING_CLOAK: "https://cdna.artstation.com/p/assets/images/images/026/564/190/large/theotime-galmiche-marchofrobots-13.jpg?1589125642",
                Mechs.DRAKE: "https://cdna.artstation.com/p/assets/images/images/026/564/214/large/theotime-galmiche-marchofrobots-15.jpg?1589125715",
                Mechs.GORGON: "https://cdnb.artstation.com/p/assets/images/images/026/564/235/large/theotime-galmiche-marchofrobots-16.jpg?1589125740",
                Mechs.DEATHS_HEAD: "https://cdnb.artstation.com/p/assets/images/images/026/564/247/large/theotime-galmiche-marchofrobots-17.jpg?1589125765",
                Mechs.RALEIGH: "https://cdna.artstation.com/p/assets/images/images/026/564/266/large/theotime-galmiche-marchofrobots-18.jpg?1589125797",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://theogm.artstation.com/projects/A9ABe5?album_id=5224111",
            mechs_to_paths={
                Mechs.METALMARK: "https://cdna.artstation.com/p/assets/images/images/026/562/104/large/theotime-galmiche-marchofrobots-03.jpg?1589121322",
                Mechs.MANTICORE: "https://cdnb.artstation.com/p/assets/images/images/026/562/117/large/theotime-galmiche-marchofrobots-04.jpg?1589121355",
                Mechs.BLACK_WITCH: "https://cdna.artstation.com/p/assets/images/images/026/562/129/large/theotime-galmiche-marchofrobots-05.jpg?1589121387",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://theogm.artstation.com/projects/qAqzGD?album_id=5224111",
            mechs_to_paths={
                Mechs.TORTUGA: "https://cdna.artstation.com/p/assets/images/images/026/562/498/large/theotime-galmiche-marchofrobots-11.jpg?1589122243",
                Mechs.SALADIN: "https://cdnb.artstation.com/p/assets/images/images/026/562/515/large/theotime-galmiche-marchofrobots-12.jpg?1589122268",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://theogm.artstation.com/projects/8XqzGK?album_id=5224111",
            mechs_to_paths={
                Mechs.TOKUGAWA: "https://cdnb.artstation.com/p/assets/images/images/026/565/041/large/theotime-galmiche-marchofrobots-19.jpg?1589127024",
                Mechs.NELSON: "https://cdnb.artstation.com/p/assets/images/images/026/564/691/large/theotime-galmiche-marchofrobots-22.jpg?1589126440",
            },
        )
    ),
    ResourceGroup(
        resources={
            Mechs.EVEREST: [
                Image(
                    source="tfinnbarr",
                    path="https://media.discordapp.net/attachments/561000253608820737/1003517167683256391/image0.jpg?width=567&height=580",
                ),
                Image(
                    source="errent",
                    path="https://media.discordapp.net/attachments/645137498577698833/1002091640573394954/Form.png?width=557&height=580",
                ),
                Image(
                    source="No Man's Sky",
                    path="https://media.discordapp.net/attachments/566317602834743296/999502221232312430/20220721031822_1.jpg?width=1030&height=580",
                ),
                Image(
                    source="Pirate",
                    path="https://media.discordapp.net/attachments/561000253608820737/975588387731943424/Fast_Eddy.png?width=638&height=580",
                ),
                Image(
                    source="https://twitter.com/LymphOwned/status/1521525215305551874",
                    path="https://pbs.twimg.com/media/FR2KvMFXoAI89BT?format=png&name=900x900",
                ),
                Image(
                    source="13 Sentinels",
                    path="https://media.discordapp.net/attachments/430234654784749568/938943150972620820/2nd_Generation_Sentinel.jpg?width=535&height=580",
                ),
                *[
                    Image(
                        source="https://twitter.com/ShadeFish1/status/1487533768206389251?s=20&t=D6_Z8Ul8QhBqX5JDCmZn-A",
                        path=path,
                    )
                    for path in [
                        "https://pbs.twimg.com/media/FKTGt5VWYAUYEBv?format=jpg&name=4096x4096",
                        "https://pbs.twimg.com/media/FKTGw1oXIAUfiJz?format=jpg&name=4096x4096",
                        "https://pbs.twimg.com/media/FKTGw1sXwAQ_NXg?format=jpg&name=4096x4096",
                        "https://pbs.twimg.com/media/FKTGw1rWYAQcys8?format=jpg&name=4096x4096",
                    ]
                ],
                Image(
                    source="Oshlet",
                    path="https://media.discordapp.net/attachments/561000253608820737/928023915576569926/SSC_Everest.png?width=973&height=580",
                ),
                Image(
                    source="Oshlet",
                    path="https://media.discordapp.net/attachments/561000253608820737/928023915983437844/Baronies_Everest.png?width=639&height=580",
                ),
                *[
                    Image(
                        source="https://twitter.com/ShadeFish1/status/1478463660087468041?s=20",
                        path=path,
                    )
                    for path in [
                        "https://pbs.twimg.com/media/FISOUuBWUAARQUP?format=jpg&name=4096x4096",
                        "https://pbs.twimg.com/media/FISOYVyXsAEKYjt?format=jpg&name=4096x4096",
                        "https://pbs.twimg.com/media/FISOZ76X0AYaM8k?format=jpg&name=4096x4096",
                    ]
                ],
                Image(
                    source="JP",
                    path="https://media.discordapp.net/attachments/561000253608820737/902592109163479070/IMG_20211026_121625_184.jpg?width=580&height=580",
                ),
                Image(
                    source="https://twitter.com/artofjunn/status/1177912739366223872",
                    path="https://pbs.twimg.com/media/EFZQf9wXsAI8ltt?format=jpg&name=medium",
                ),
                Image(
                    source="https://twitter.com/SkyCrimeDraws/status/1450928540040503296",
                    path="https://pbs.twimg.com/media/FCK7fsJXEAM1Hg9?format=jpg&name=large",
                ),
                Image(
                    source="Sky Crime",
                    path="https://media.discordapp.net/attachments/561000253608820737/893718308904394802/unknown.png?width=580&height=580",
                ),
                Image(
                    source="https://twitter.com/ShadeFish1/status/1435734286439784449?s=20",
                    path="https://pbs.twimg.com/media/E-zAVHJXEAUUvSd?format=jpg&name=large",
                ),
                Image(
                    path="https://media.discordapp.net/attachments/561000253608820737/854595327889506304/unknown.png?width=417&height=580",
                ),
                Image(
                    source="https://twitter.com/LymphOwned/status/1401159860906037249",
                    path="https://pbs.twimg.com/media/E3HrJPnXwAErCC8?format=jpg&name=medium",
                ),
            ],
            Mechs.SAGARMATHA: [
                Image(
                    source="https://twitter.com/LymphOwned/status/1522259408029421568",
                    path="https://pbs.twimg.com/media/FSAmLJPXMAEiTpc?format=jpg&name=large",
                ),
                Image(
                    source="https://twitter.com/ShadeFish1/status/1478463660087468041?s=20",
                    path="https://pbs.twimg.com/media/FISOd4mX0AMp-kI?format=jpg&name=4096x4096",
                ),
                Image(
                    source="https://twitter.com/LymphOwned/status/1398992705456427009",
                    path="https://pbs.twimg.com/media/E2o35z5XIAAb9-e?format=jpg&name=medium",
                ),
                Image(
                    source="kaffeezombie",
                    path="https://media.discordapp.net/attachments/561000253608820737/842344434054070282/sketchbook_scribbles2c.png?width=571&height=580",
                ),
            ],
            Mechs.BALOR: [
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/042/590/651/large/theotime-gm-warlock-web-marked.jpg?1634913024",
                    source="https://theogm.artstation.com/projects/zO2N5w?album_id=5224111",
                )
            ],
            Mechs.BARBAROSSA: [
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/027/409/213/large/theotime-gm-t-boe-sigfried-color-web-02.jpg?1591454560",
                    source="https://theogm.artstation.com/projects/9mwmdR?album_id=5224111",
                )
            ],
            Mechs.BLACKBEARD: [
                Image(
                    path="https://cdna.artstation.com/p/assets/images/images/035/137/912/large/theotime-gm-honeyblood-web.jpg?1614189552",
                    source="https://theogm.artstation.com/projects/ZGZB8x?album_id=5224111",
                )
            ],
            Mechs.BLACK_WITCH: [
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/042/590/651/large/theotime-gm-warlock-web-marked.jpg?1634913024",
                    source="https://theogm.artstation.com/projects/zO2N5w?album_id=5224111",
                )
            ],
            Mechs.DRAKE: [
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/028/499/661/large/theotime-gm-bear-drake-bg-web.jpg?1594662162",
                    source="https://theogm.artstation.com/projects/3dq10o?album_id=5224111",
                )
            ],
            Mechs.GORGON: [
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/028/191/345/large/theotime-gm-preacher-web.jpg?1593725386",
                    source="https://theogm.artstation.com/projects/R33XXA?album_id=5224111",
                ),
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/042/591/061/large/theotime-gm-witheringgaze-web-watermark.jpg?1634913932",
                    source="https://theogm.artstation.com/projects/rAbY05?album_id=5224111",
                ),
            ],
            Mechs.NELSON: [
                Image(
                    path="https://cdna.artstation.com/p/assets/images/images/027/409/116/large/theotime-gm-commission-b-s-colored-web.jpg?1591454260",
                    source="https://theogm.artstation.com/projects/q9L9ky?album_id=5224111",
                )
            ],
            Mechs.SWALLOWTAIL: [
                Image(
                    path="https://cdna.artstation.com/p/assets/images/images/029/678/810/large/theotime-gm-athena-swallowtail-web.jpg?1598315334",
                    source="https://theogm.artstation.com/projects/Xna6Vy?album_id=5224111",
                )
            ],
            Mechs.TOKUGAWA: [
                Image(
                    source="https://twitter.com/EMFields_Art/status/1512528795080671233?s=20&t=RY4_6qI9V2Vk1NuT0wlWBg",
                    path="https://pbs.twimg.com/media/FP2UlOyWYAAHiEf?format=jpg&name=large",
                ),
                Image(
                    source="https://twitter.com/ShadeFish1/status/1549188245770178560?s=20&t=eJWLumciYJeQQdLn7ToTWw",
                    path="https://pbs.twimg.com/media/FX_R5SwXgAIhRdw?format=jpg&name=4096x4096",
                ),
                Image(path="https://pbs.twimg.com/media/EUEw6RTWsAENuUt.jpg:large"),
                Image(path="https://pbs.twimg.com/media/EdEHbFEXoAMYNJz.jpg:large"),
                Image(
                    path="https://cdn.discordapp.com/attachments/561000253608820737/768162242797371452/ha_Tokugawa.png"
                ),
                Image(
                    path="https://cdn.discordapp.com/attachments/561000253608820737/830512277572419584/toku_kait.png"
                ),
                Image(
                    path="https://cdn.discordapp.com/attachments/561000253608820737/831894740714258482/toku4.jpg"
                ),
                Image(
                    path="https://cdn.discordapp.com/attachments/645137498577698833/838970049175355433/hellhounbd1.png"
                ),
                Image(
                    path="https://cdn.discordapp.com/attachments/561000253608820737/845398230950477864/TOKUGAWA_REColoR.png"
                ),
            ],
            Mechs.MOURNING_CLOAK: [
                Image(
                    path="https://cdn.discordapp.com/attachments/561000253608820737/831894740714258482/toku4.jpg"
                ),
                Image(
                    path="https://cdnb.artstation.com/p/assets/images/images/042/589/797/large/theotime-gm-custom-mc-web-watermark.jpg?1634911204",
                    source="https://theogm.artstation.com/projects/w6DwJX?album_id=5224111",
                ),
            ],
            Mechs.CALIBAN: [
                Image(
                    source="https://twitter.com/LymphOwned/status/1564342981804670981",
                    path="https://pbs.twimg.com/media/FbWouPTWAAIB6ZJ?format=jpg&name=large",
                )
            ],
            Mechs.IBUTHO: [
                Image(
                    source="https://www.reddit.com/r/LancerRPG/comments/jdi3hy/the_mfecane_ibutho_the_frontier_pattern_in_the/",
                    path="https://preview.redd.it/qvv1mol8fvt51.jpg?width=640&crop=smart&auto=webp&s=eaabf675ab5b4048c8fc073dc2e9c667a7fa9a98",
                ),
                Image(
                    source="NHP-SHAKA",
                    path="https://pbs.twimg.com/media/E2wFcCVXwAM7KVk?format=jpg&name=4096x4096",
                ),
            ],
        },
    ),
]


def _is_image_group(group: list[MechResource]) -> bool:
    if not group:
        return False
    if not isinstance(group, list):
        group = [group]
    return isinstance(group[0], Image)


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
        f"Source: {mech.source}\n",
        f"Author: {mech.author}\n",
    ]
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
            if mech.author == author:
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
