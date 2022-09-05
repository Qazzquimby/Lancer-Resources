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
    GMS = "GMS - General Massive Systems"
    IPSN = "IPSN - Interplanetary Shipping Northstar"
    SSC = "SSC - Smith Shimano Corpro"
    HORUS = "HORUS"
    HA = "HA - Harisson Armory"
    MFECANE = "MFECANE"
    GRIMM = "G&S - Grimm & Sons"
    C_H = "C&H - Chandrasekhar & Herschel Ltd."
    INTERCORP = "Intercorp"


CORPS: list[str] = list_content(Corps)


class Authors:
    MASSIF = "Massif Press"
    NHP_SHAKA = "NHP-SHAKA"
    DELILAH = "Delilah Worthy"
    KAI_TAVE = "Kai Tave"
    ITERPOINT = "Interpoint Station"


AUTHORS: list[str] = list_content(Authors)


@dataclass
class Source:
    name: str
    author: str
    url: str


class Sources:
    CORE = Source(
        name="Core Book",
        author=Authors.MASSIF,
        url="https://massif-press.itch.io/corebook-pdf-free",
    )
    WALLFLOWER = Source(
        name="No Room for a Wallflower",
        author=Authors.MASSIF,
        url="https://massif-press.itch.io/no-room-for-a-wallflower-act-1",
    )
    LONG_RIM = Source(
        name="Long Rim",
        author=Authors.MASSIF,
        url="https://massif-press.itch.io/the-long-rim",
    )
    KARRAKIN_TRADE_BARONIES = Source(
        name="Field Guide: The Karrakin Trade Baronies",
        author=Authors.MASSIF,
        url="https://massif-press.itch.io/field-guide-the-karrakin-trade-baronies",
    )
    MFECANE = Source(
        name="Field Guide to Mfecane",
        author=Authors.NHP_SHAKA,
        url="https://nhp-shaka.itch.io/mfecane-field-guide",
    )
    GRIMM = Source(
        name="Grimm & Sons",
        author=Authors.DELILAH,
        url="https://nightmareworks.itch.io/grimmandsons",
    )
    SULDAN = Source(
        name="Field Guide to Suldan",
        author=Authors.KAI_TAVE,
        url="https://kaitave.itch.io/field-guide-to-suldan",
    )
    INTERCORP = Source(
        name="Intercorp",
        author=Authors.ITERPOINT,
        url="https://interpoint-station.itch.io/intercorp",
    )


SOURCES: list[str] = list_content(Sources)


@dataclass
class Mech:
    name: str
    corp: str
    source: Source = Sources.CORE
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
    # region massif IPSN
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
    # endregion

    # region massif SSC
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
        summary=[
            "Point Defense/Duelist",
            "Aggressive Tank",
            "Ramping Armor - wants to be hit",
        ],
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
    # endregion

    # region massif HORUS
    BALOR = Mech(
        name="balor",
        corp=Corps.HORUS,
        image_path="https://external-preview.redd.it/NfhQ53rmZpR7nZs7Giymy0QVlKnV_3KMS4hmuXEsIRU.jpg?auto=webp&s=6f5af6c3cb517bfa26be2535c89ab9b540a49043",
        summary=[
            "Nanobot Swarm Host/Frontline Assault",
            "Big cloud of death",
            "Grapple people and disintegrate them",
        ],
    )
    CALENDULA = Mech(
        name="calendula",
        corp=Corps.HORUS,
        source=Sources.KARRAKIN_TRADE_BARONIES,
        image_path="https://pbs.twimg.com/media/FNXBM8JXIAsBmrc.jpg:large",
        summary=[
            "Minotaur Variant",
            "Be a ghost",
            "Make ghost duplicates",
            "Turn people into ghosts",
            "Also slow everyone",
        ],
    )
    GOBLIN = Mech(
        name="goblin",
        corp=Corps.HORUS,
        image_path="https://static.wikia.nocookie.net/lancer/images/e/ef/Goblin.jpg/revision/latest?cb=20200509100851",
        summary=[
            "Technical/Enlightenment/Hacking",
            "Irritate the hell out of your enemies",
            "Make them insane",
            "Ride around on your bigger friends",
            "Wizard",
        ],
    )
    GORGON = Mech(
        name="gorgon",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/DhCxXZtWsAEa0HH.jpg",
        summary=[
            "Overwatch/Electronic Defense",
            "Punish people for attacking your allies",
            "So ugly it literally hurts to look",
        ],
    )
    HYDRA = Mech(
        name="hydra",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D3ZsrznWkAEDfHl.jpg:large",
        summary=[
            "Drone warfare/Tactical Dismemberment",
            "Everything is drone related",
            "Smart weapons",
            "Summoner",
        ],
    )
    KOBOLD = Mech(
        name="kobold",
        corp=Corps.HORUS,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D4M6nGAWkAEmIQB.jpg:large",
        summary=[
            "Offensive Terraforming",
            "Camouflage invisibility",
            "Build your own terrain",
        ],
    )
    LICH = Mech(
        name="lich",
        corp=Corps.HORUS,
        source=Sources.LONG_RIM,
        image_path="https://pbs.twimg.com/media/D6dRYIeW0AEhBg2.jpg:large",
        summary=[
            "Time manipulation",
            "Paradoxically immortal via time loops",
            "Suicidally tank hits",
        ],
    )
    MANTICORE = Mech(
        name="manticore",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D15ojOZW0AAcdQn.jpg:large",
        summary=[
            "Direct Energy Assault",
            "Bomb with legs",
            "Self destructive",
            "Divine punishment",
            "CASTIGATE THE ENEMIES OF THE GODHEAD",
        ],
    )
    MINOTAUR = Mech(
        name="minotaur",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/D0NqbpiXgAE6WLs.jpg:large",
        summary=[
            "Interdictor/area control",
            "Make people not move via metaphorical mazes",
            "Lots of hacking utilities",
            "Bigger on the inside - you can live in there",
        ],
    )
    PEGASUS = Mech(
        name="pegasus",
        corp=Corps.HORUS,
        image_path="https://pbs.twimg.com/media/Dm7Lwc1XsAElCJj.jpg:large",
        summary=[
            "Esoteric Firepower",
            "Has a gun which doesn't exist and hits before it fires",
            "Manipulate dice directly - tell them what to roll",
        ],
    )
    # endregion

    # region massif HA
    BARBAROSSA = Mech(
        name="barbarossa",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/Ds471y1WsAAjpwJ.jpg",
        summary=[
            "Siege/Anti-Air",
            "Walking siege engine" "The biggest mech",
            "Ship-grade slow charging laser",
            "Everyone stand behind you",
        ],
    )
    ENKIDU = Mech(
        name="enkidu",
        corp=Corps.HA,
        source=Sources.WALLFLOWER,
        image_path="https://preview.redd.it/5ev5xcyprab81.jpg?auto=webp&s=768fba2788fc4d9c61d3bce3ffe1e8b32aa12905",
        summary=[
            "Tokugawa Variant",
            "Melee glass cannon",
            "Plasma whip fingers",
            "Go werewolf when in danger",
            "Rip your enemies in half",
        ],
    )
    GENGHIS = Mech(
        name="genghis",
        corp=Corps.HA,
        image_path="https://external-preview.redd.it/HnEsHvovvilWcBUdooCiFLgd99EzEMlwjMgzHIihSZA.jpg?auto=webp&s=10a5adb10e31c2fcba4936dec7b2b39731ec14b0",
        summary=[
            "Total Biome Kill",
            "Fire everywhere",
            "Low health, high armor",
            "Heat management",
            "Canonically the first mech, created for genocide",
        ],
    )
    GENGHIS_WORLDKILLER = Mech(
        name="genghis worldkiller",
        corp=Corps.HA,
        source=Sources.WALLFLOWER,
        image_path="https://cdn-animation.artstation.com/p/thumbnails/000/265/518/thumb.jpg",
        summary=[
            "Genghis Variant - The original Genghis design",
            "Less restrained, less safe to pilot",
            "Aura of fire",
        ],
    )
    ISKANDER = Mech(
        name="iskander",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/D3V3iiaXkAEO29u.jpg:large",
        summary=[
            "Gravity Manipulation/Area Denial",
            "Make everything an explosive",
            "Minefield",
            "Gravity gun",
        ],
    )
    NAPOLEON = Mech(
        name="napoleon",
        corp=Corps.HA,
        image_path="https://external-preview.redd.it/flbCTCmqhnLOoWTzF6lRtYZPgpKtf9duWoLOqF6Zxiw.jpg?auto=webp&s=d968822a1fffa257adc347b4f59eadcdf1699ffe",
        summary=[
            "Experimental Stasis/Battlefield Control",
            "Tiny tank",
            "Put people in stasis",
            "Become nigh immortal while doing nothing",
            "'I reduce the damage to 1'",
            "Gun that deletes people from existence",
        ],
    )
    SALADIN = Mech(
        name="saladin",
        corp=Corps.HA,
        image_path="https://pbs.twimg.com/media/D3HXdK3XcAEkLxk.jpg:large",
        summary=[
            "Shield Support",
            "All sorts of force fields",
            "Damage reflection",
            "Block for your squishy friends",
            "A defender who actually defends",
        ],
    )
    SHERMAN = Mech(
        name="sherman",
        corp=Corps.HA,
        image_path=[
            "https://pbs.twimg.com/media/D3w3yZ-XoAAGo_x?format=jpg&name=large",
            "https://pbs.twimg.com/media/Df3RCD7XcAAws0N.jpg:large",
        ],
        summary=[
            "Frontline Assault",
            "lots of lasers with heat costs",
            "excellent heat management",
            "stabilize without losing a full action",
        ],
    )
    SUNZI = Mech(
        name="sunzi",
        corp=Corps.HA,
        source=Sources.LONG_RIM,
        image_path="https://ksr-ugc.imgix.net/assets/024/944/488/16ffd6f132e4ecd32ee139293b129442_original.jpg?ixlib=rb-4.0.2&w=700&fit=max&v=1556548469&gif-q=50&q=92&s=9f83682094aafa03d5a39cb69e4760e0",
        summary=[
            "Space Manipulation/Tactics",
            "Teleportation controller",
            "Put your allies and enemies wherever you want",
        ],
    )
    TOKUGAWA = Mech(
        name="tokugawa",
        corp=Corps.HA,
        image_path="https://64.media.tumblr.com/8642aa32ea7e7fde660a6d5daa833a8e/tumblr_pgedezbTgB1qlxan5o1_1280.jpg",
        summary=[
            "Superheated Melee",
            "High risk high reward",
            "Play as close to destruction as possible",
            "Benefits while vulnerable and near death",
            "Die in a blaze of glory",
        ],
    )
    # endregion

    # region MFECANE
    IBUTHO = Mech(
        name="ibutho",
        corp=Corps.MFECANE,
        source=Sources.MFECANE,
        image_path=[
            "https://preview.redd.it/dgnj8y0n51q61.png?width=512&format=png&auto=webp&s=db1d0ba19fa81acd625a801898c1a4f48fab279d",
            "https://preview.redd.it/fga3361n51q61.png?width=512&format=png&auto=webp&s=f25b79691edd1b70dabf504f33612ff2cfe1d754",
        ],
        summary=[
            "Berserk when close to death",
            "Loves ramming and knocking people prone",
            "Tactical flexibility",
            "Can't take other NHPs",
        ],
    )
    GROOTSLANG = Mech(
        name="grootslang",
        corp=Corps.MFECANE,
        source=Sources.MFECANE,
        image_path="https://img.itch.zone/aW1hZ2UvOTc0Njk0LzgzNzE4MjAucG5n/original/n64DbK.png",
        summary=[
            "Enormous slow team support",
            "Guard and buff firepower of nearby allies",
        ],
    )
    AMADLOZI = Mech(
        name="amadlozi",
        corp=Corps.MFECANE,
        source=Sources.MFECANE,
        image_path="https://img.itch.zone/aW1hZ2UvOTc0Njk0LzgzNzE4MTgucG5n/original/%2FV4kya.png",
        summary=[
            "Terrain Architect Defender/Controller",
            "Protect team from terrain",
            "Frustrate the GM by redrawing their map",
        ],
    )
    CETSHWAYO = Mech(
        name="cetshwayo",
        corp=Corps.MFECANE,
        source=Sources.MFECANE,
        image_path="https://img.itch.zone/aW1hZ2UvOTc0Njk0LzgzNzE4MTkucG5n/original/3nbT3l.png",
        summary=[
            "Artillery/Controller",
            "Tiny fragile speedster",
            "Launcher weapons and repositioning",
            "Buffed from taking heat",
        ],
    )
    # endregion

    # region Grimm
    JOHN_HENRY = Mech(
        name="john henry",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTcuanBn/original/K73D9j.jpg",
        summary=[
            "A Mighty Woman",
            "Heavy melee - Built-in giant hammer",
            "Huge blows, knock prone",
            "Overheat in the process",
        ],
    )
    VOLK = Mech(
        name="volk",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTQuanBn/original/W4D8f9.jpg",
        summary=[
            "Wolven Hunter" "Knockoff Blackbeard",
            "Speedy Brawler",
            "Hot-rod engine powering chainsaws",
        ],
    )
    BUNYAN = Mech(
        name="bunyan",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTEuanBn/original/nDZtN4.jpg",
        summary=["Utterly massive defender", "Very slow", "BABE forcefield drone"],
    )
    JACK = Mech(
        name="jack",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTUuanBn/original/2DwTvs.jpg",
        summary=[
            "Giant Killer",
            "Agile all-rounder",
            "Scout and Skirmish",
            "Plasma weapons - Can be buffed with limited ammo",
        ],
    )
    DOROTHY = Mech(
        name="dorothy",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTIuanBn/original/Tw%2BCnV.jpg",
        summary=[
            "Combat support",
            "Search and rescue",
            "Immune to environment damage",
            "Nanite healing",
        ],
    )
    MAGARAC = Mech(
        name="magarac",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTYuanBn/original/V7B071.jpg",
        summary=[
            "Walking fortress-factory",
            "Repair allies, even after their death",
            "Slow, limited resources",
        ],
    )
    ORLANDO = Mech(
        name="orlando",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://i.pinimg.com/originals/e4/72/93/e47293978e2956008ea5f642721b63a9.jpg",
        summary=[
            "Linebreaker",
            "Knight in shining armor",
            "Charge through people",
            "Uncontrolled wild movement",
        ],
    )
    ANANSI = Mech(
        name="anansi",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ1MDcuanBn/original/npwuJJ.jpg",
        summary=[
            "Control Sniper",
            "Cling on walls",
            "Good at hiding and using terrain",
            "Spread spiderweb traps and fire on people who touch them",
        ],
    )
    MAX = Mech(
        name="max",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        summary=[
            "Ram people around",
            "Automatically destroy low health targets",
            "Counterattack reactions",
            "'A dirge for the Fall of mankind'",
        ],
    )
    SCHEHERAZADE = Mech(
        name="scheherazade",
        corp=Corps.GRIMM,
        source=Sources.GRIMM,
        image_path="https://img.itch.zone/aW1hZ2UvODc1MzAwLzQ5MjQ0OTMuanBn/original/lwgDu6.jpg",
        summary=[
            "Battlefield Control",
            "Terribly fragile, but with dodge chance",
            "Place mines for free at start of battle",
            "Weird control abilities, like reversing accuracy and disadvantage",
        ],
    )
    # endregion

    # region Suldan
    CHARIOTEER = Mech(
        name="charioteer",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://img.itch.zone/aW1hZ2UvODc3NzY1LzQ5Mzk4MjYucG5n/original/mkCaE7.png",
        summary=[
            "Mach-speed Reconnaissance",
            "High-speed daredevil",
            "Close range targeting",
            "Unmatched mobility",
            "Support",
        ],
    )
    KALISTA = Mech(
        name="kalista",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://img.itch.zone/aW1hZ2UvODc3NzY1LzQ5Mzk4MjcucG5n/original/7GMvGa.png",
        summary=[
            "Frontline Assault",
            "Unstoppable Juggernaut",
            "Brute force, huge hits",
        ],
    )
    KALLARANI = Mech(
        name="kallarani",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/a5a936e6ff701aaa7fad65183be314f0.png",
        summary=[
            "CQB Armsmaster",
            "Versatile Striker",
            "Multifunction tools",
        ],
    )
    MATADOR = Mech(
        name="matador",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/19500408a7311c3930fa51a0e1759ede.jpg",
        summary=[
            "Electronic Defense/Superiority" "Anti-electronic Defender",
            "Malware",
        ],
    )
    PESILAT = Mech(
        name="pesilat",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://img.itch.zone/aW1hZ2UvODc3NzY1LzQ5Mzk4MjgucG5n/original/sPsxRY.png",
        summary=[
            "Cyber-space Martial Arts",
            "Striker/Controller",
            "Melee hacker",
        ],
    )
    RETIARIUS = Mech(
        name="retiarius",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/756354db5c49ee126d03c441c6e8e4e6.png",
        summary=[
            "Mid-Range Suppression/Support" "Sturdy Controller",
            "entangle enemies",
        ],
    )
    SABREUR = Mech(
        name="sabreur",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/eaebe26830cb2a491ff74bb15504b122.png",
        summary=[
            "Enrapturing Duelist",
            "Precision melee striker",
            "High single target damage",
        ],
    )
    SAGITTARIUS = Mech(
        name="sagittarius",
        corp=Corps.C_H,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/0c63ca0b5e2549f41dc7f461bcff473f.png",
        summary=[
            "Inflitration/Elimination",
            "Elusive midrange archer",
            "Assassinate from stealth",
        ],
    )
    WORDEN = Mech(
        name="worden",
        corp=Corps.IPSN,
        source=Sources.SULDAN,
        image_path="https://i.gyazo.com/9972ca9bfe7a0e40d2f789526ff128f2.png",
        summary=[
            "Overwhelming Fire-support Artillery",
            "Long range suppression fire",
            "The best defense",
            "Stupid number of bullets",
        ],
    )
    COMET = Mech(
        name="comet",
        corp=Corps.SSC,
        source=Sources.SULDAN,
        image_path="https://img.itch.zone/aW1hZ2UvODc3NzY1LzQ5Mzk4MjkucG5n/original/%2FD8UyO.png",
        summary=[
            "High SPeed Air Intercept/Support",
            "Aerial gunship",
            "Smart weapons",
            "Lock on to everything",
        ],
    )
    EFREET = Mech(
        name="efreet",
        corp=Corps.HORUS,
        image_path="https://i.gyazo.com/5622a14616fd0bea8126cf6f110e0df4.jpg",
        summary=[
            "Hypermobile close-protection/Rapid response",
            "Close range teleporting defender",
            "Space manipulation",
        ],
    )
    AGRIPPA = Mech(
        name="agrippa",
        corp=Corps.HA,
        image_path="https://i.gyazo.com/cc891096eedab824f8116776d1bc2081.png",
        summary=[
            "Defensive Construction/Support",
            "Combat engineer - Build structures like bridges and traps",
            "Repair allies",
            "Be a crane",
            "Extremely versatile helper drone",
        ],
    )
    # endregion

    # region Interpoint
    ACASTUS = Mech(
        name="acastus",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3Lzk1Mzk2MjYucG5n/original/g%2Bjg7F.png",
        summary=[
            "Vicious close combat",
            "Destroy and regenerate your weapons for profit",
            "So many blades",
        ],
    )
    ARGUS = Mech(
        name="argus",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3LzU1NTY3NDIucG5n/original/boifhT.png",
        summary=[
            "Sniper with a 'Bloodhound' drone",
            "Pet class teamwork",
            "Walk around on stilts",
        ],
    )
    ATLANTA = Mech(
        name="atlanta",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3Lzk1Mzk1MDAucG5n/original/%2FoL3ZF.png",
        summary=[
            "Time manipulation",
            "Be in multiple places at once",
            "Replay actions you took",
            "Rewind people",
        ],
    )
    CORONUS = Mech(
        name="coronus",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3Lzk1Mzk1ODMucG5n/original/ydzH6g.png",
        summary=[
            "Luck manipulation",
            "Play casino mini-games in combat",
            "Pushing your luck and making risky plays",
        ],
    )
    HERACLES = Mech(
        name="heracles",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3Lzk1Mzk0NzIucG5n/original/n%2FLHAw.png",
        summary=[
            "Highly flexible, toggling powerful systems on and off",
            "Each turn, pick one stat to be good at",
            "Heat attacks",
        ],
    )
    NESTOR = Mech(
        name="nestor",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3LzU0MzYzNjQucG5n/original/tm2TA0.png",
        summary=[
            "Durable frontline all-rounder",
            "Many small tactical options",
        ],
    )
    POLLUX = Mech(
        name="pollux",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3LzU0MzYzNjMucG5n/original/nSeIyl.png",
        summary=[
            "Melt everything around you",
            "Tank heat",
            "Powered by a tiny star",
        ],
    )
    ORPHEUS = Mech(
        name="orpheus",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3LzYxNjk5NjkucG5n/original/5h%2BexB.png",
        summary=[
            "Jockey other mechs and buff/debuff them",
        ],
    )
    THESEUS = Mech(
        name="theseus",
        corp=Corps.INTERCORP,
        image_path="https://img.itch.zone/aW1hZ2UvOTU4NjM3Lzk1Mzk0ODAucG5n/original/huJi17.png",
        summary=[
            "Area denial and support",
            "Spread hard cover crystals",
            "Detonate crystals to damage enemies and shield allies",
        ],
    )

    # endregion


MECHS: list[Mech] = list_content(Mechs)
