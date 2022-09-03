from dataclasses import dataclass


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
    summary: list[str] = None

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


class Mechs:
    EVEREST = Mech(
        name="everest",
        corp=Corps.GMS,
        summary=["Your first summit", "Balanced for most situations", "Safe fallback"],
    )
    SAGARMATHA = Mech(
        name="sagarmatha",
        corp=Corps.GMS,
        source=Sources.WALLFLOWER,
        summary=["Fat Everest", "All-round defender"],
    )
    BLACKBEARD = Mech(
        name="blackbeard",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/a/a1/Blackbeard.jpg/revision/latest?cb=20200509100622",
        summary=[
            "Berserker pattern melee",
            "Agile",
            "Grappling",
            "Teamkilling",
            "Chain Axe",
        ],
    )
    CALIBAN = Mech(
        "caliban",
        corp=Corps.IPSN,
        source=Sources.LONG_RIM,
        image_path="https://external-preview.redd.it/uiHVNTr51s5O7LdbPLLwI-BkRrvRmbPZx_XW4m2jH1U.jpg?auto=webp&s=51e7c6a99d745f9c9a5e213a848219cfc2682382",
        summary=[
            "Boarding and Asset Reclamation",
            "Enormous Shotgun",
            "Doomguy",
            "Chase people twice your size around the map",
        ],
    )
    DRAKE = Mech(
        name="drake",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/6/62/Drake.jpg/revision/latest?cb=20200509100716",
        summary=["Heavy Assault/Fire Support", "Stationary bunker turret", "minigun"],
    )
    LANCASTER = Mech(
        name="lancaster",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/2/2c/Lancaster.jpg/revision/latest?cb=20200509101034",
        summary=[
            "Field Support/Repair",
            "Space Horse - Battle Bus",
            "The only healer",
            "Neat utilities",
            "Fireproof",
        ],
    )
    KIDD = Mech(
        name="kidd",
        corp=Corps.IPSN,
        source=Sources.WALLFLOWER,
        image_path="https://pbs.twimg.com/media/EfE34JxXoAEWdnT.jpg:large",
        summary=[
            "Lancaster Variant",
            "Frontline Rapid Support",
            "Drones",
            "Orbital Strike",
            "Low tech pirate aesthetic arrr yo ho",
        ],
    )
    NELSON = Mech(
        name="nelson",
        corp=Corps.IPSN,
        image_path="https://pbs.twimg.com/media/D0da5CUWwAAwpO0.jpg:large",
        summary=[
            "Rapid Assault",
            "Fast Knight with a Spear the Explodes",
            "Hit and Run",
        ],
    )
    RALEIGH = Mech(
        name="raleigh",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/6/69/Raleigh.jpg/revision/latest?cb=20200509101441",
        summary=[
            "Frontline Assault",
            "Reloading Gun Platform",
            "Too many guns",
            "Cowboy - Fan the Hammer",
            "Chest Cannon",
        ],
    )
    TORTUGA = Mech(
        name="tortuga",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/0/03/Tortuga.jpg/revision/latest?cb=20200509101655",
        summary=[
            "Overwatch/Zone Defense",
            "Ship defense and boarding",
            "Auto-Shotgun",
            "Controls close range",
            "Smash through walls",
        ],
    )
    VLAD = Mech(
        name="vlad",
        corp=Corps.IPSN,
        image_path="https://static.wikia.nocookie.net/lancer/images/d/d1/Vlad.jpg/revision/latest?cb=20200509101717",
        summary=[
            "Nail people to the ground",
            "Damage attackers because covered in spikes",
            "Massive drill",
            "Sadistic Porcupine",
        ],
    )
    ZHENG = Mech(
        name="zheng",
        corp=Corps.IPSN,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D4xiHSrW4AA7IM5.jpg:large",
        summary=[
            "Unarmed Melee",
            "Terrain destruction",
            "Use the environment as a weapon",
            "Throw people like a bowling ball",
        ],
    )

    ATLAS = Mech(
        name="atlas",
        corp=Corps.SSC,
        source=Sources.LONG_RIM,
        image_path=[
            "https://pbs.twimg.com/media/D55kqK-WwAAMyND?format=jpg&name=large",
            "https://pbs.twimg.com/media/EMXOad_WwAMMkZM?format=jpg&name=large",
        ],
        summary=[
            "Human sized kaiju hunter",
            "Cybernetic ninja suit",
            "'Draws on the profiles of past pilots to power current action'",
            "Attack on Titan / Revengeance",
        ],
    )
    BLACK_WITCH = Mech(
        name="black_witch",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/4/47/Blackwitch1.jpeg/revision/latest?cb=20210510124208",
        summary=[
            "Magnetic Control",
            "Catch Bullets",
            "Antimagic",
            "Throw people around",
            "Mech-Magneto",
        ],
    )
    DEATHS_HEAD = Mech(
        name="death's head",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D3AyF5pXgAIM3t_.jpg:large",
        summary=[
            "Mobile Artillery",
            "The Snipiest Sniper",
            "Maximum Accuracy",
            "One shot - one kill",
            "Railgun",
            "Wall climbing",
        ],
    )
    DUSK_WING = Mech(
        name="dusk_wing",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D28PCW3WsAIGZuU.jpg:large",
        summary=[
            "Sustained Aerial Harassment",
            "Super mobile flying",
            "Mess with their heads",
            "Annoying fairy",
            "Create confusing duplicates",
        ],
    )
    EMPEROR = Mech(
        name="emperor",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://external-preview.redd.it/YVWXiFNpCBcuyvcvPzX3Y1tjOnEQ_2XX2e2W1kueA0Y.jpg?auto=webp&s=f71b0a8c1ccb329dd0b0523260c8c18c88ec97a8",
        summary=[
            "Long Range Support Archer",
            "Tonnes of overshields for everyone",
            "Armor piercing",
        ],
    )
    METALMARK = Mech(
        name="metalmark",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/b/ba/Metalmark.jpeg/revision/latest?cb=20210510130854",
        summary=[
            "Tactical Superiority/Stealth",
            "Speed, invisibility, flashbangs, hiding",
            "The sneakiest",
        ],
    )
    MONARCH = Mech(
        name="monarch",
        corp=Corps.SSC,
        image_path="https://pbs.twimg.com/media/D0SvXINX4AEcN1Z.jpg:large",
        summary=[
            "Missile Platform",
            "Lock on + Barrage",
            "Too many missiles",
            "Homing attacks",
            "Small quick missiles",
            "Big slow missiles",
            "Missiles for every situation",
        ],
    )
    MOURNING_CLOAK = Mech(
        name="mourning_cloak",
        corp=Corps.SSC,
        image_path="https://static.wikia.nocookie.net/lancer/images/1/15/MourningCloak.jpg/revision/latest?cb=20200509101339",
        summary=[
            "Agile, Teleporting Melee Assassin",
            "Nothing personnel",
            "Big crits",
            "Counter lone targets" "Teleporting hit and run",
        ],
    )
    SWALLOWTAIL = Mech(
        name="swallowtail",
        corp=Corps.SSC,
        image_path="https://external-preview.redd.it/4ts71UdtaOTzZJOYApRc6U-m5G_CgzyTx9PGVqAKvn8.jpg?auto=webp&s=f54bcc86818f54f4e3008ceee2c50842201e93fa",
        summary=[
            "Stealth Scout",
            "Invisible while not moving",
            "Scanning, sees everything",
            "Shut down defenses",
            "Extremely fast",
            "You can't see me because I'm invisible, and I can see you even though you're invisible",
        ],
    )
    SWALLOWTAIL_RANGER = Mech(
        name="swallowtail_ranger",
        corp=Corps.SSC,
        image_path="https://cdnb.artstation.com/p/assets/images/images/035/138/645/large/theotime-gm-ranger-variant-web.jpg?1614191125",
        summary=[
            "Set up the map",
            "Terrain usage mastery" "Tactical movement",
        ],
    )
    WHITE_WITCH = Mech(
        name="white_witch",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://pbs.twimg.com/media/EM6PMpPW4AAn668.jpg:large",
        summary=[],
    )

    ORCHIS = Mech(
        name="orchis",
        corp=Corps.SSC,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://preview.redd.it/7ulbcgdnafn81.jpg?auto=webp&s=2af07f9391443e756c07e3f94108e0c7ca94f965",
        summary=[
            "Black Witch Variant",
            "Mobile Bodyguard",
            "Throwable shield",
        ],
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
