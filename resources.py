from objects import Mechs
from resource_classes import (
    Image,
    MechResource,
    ResourceGroup,
    get_image_resources_with_source,
)
from resources_image_dump import IMAGES_DUMP

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
        name="Mechanic Brewery, Lancer Homebrew",
        resources={
            Mechs.SCHEHERAZADE: "https://www.youtube.com/watch?v=h6YoTaG8Srs&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=4",
            Mechs.CHARIOTEER: "https://www.youtube.com/watch?v=J0xi_T7ohRs&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=6&t=18s",
            # Mechs.LEMONGRASS: "https://www.youtube.com/watch?v=MKBIoCwHI14&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=8&t=2s",
            # Mechs.CIMMERIA: "https://www.youtube.com/watch?v=RuzTuUv0DRg&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=9&t=1s",
            # Mechs.ORCA: "https://www.youtube.com/watch?v=BGPOz7u0n3I&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=11",
            # Mechs.RASPUTIN: "https://www.youtube.com/watch?v=1ML79x4vo1s&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=16",
            Mechs.PESILAT: "https://www.youtube.com/watch?v=exwhZsMK560&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=23",
            Mechs.KALISTA: "https://www.youtube.com/watch?v=YLXJ8N_qdpQ&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=27",
            Mechs.KALLARANI: "https://www.youtube.com/watch?v=M5_i9IAnmTs&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=28",
            Mechs.SAGITTARIUS: "https://www.youtube.com/watch?v=kZ6agtQUb_o&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=29",
            Mechs.EFREET: "https://www.youtube.com/watch?v=sTwBED0DYPQ&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=30",
            Mechs.WORDEN: "https://www.youtube.com/watch?v=K_VJq45CtYo&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=31",
            Mechs.COMET: "https://www.youtube.com/watch?v=8dA0uplxt8U&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=32",
            Mechs.AGRIPPA: "https://www.youtube.com/watch?v=1q0SN67d8qI&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=34",
            Mechs.SABREUR: "https://www.youtube.com/watch?v=mRSvyIgh89k&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=35",
            Mechs.MATADOR: "https://www.youtube.com/watch?v=vktGjzAlUyM&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=36",
            Mechs.RETIARIUS: "https://www.youtube.com/watch?v=JXR19Q02RnE&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=37",
            Mechs.IBUTHO: "https://www.youtube.com/watch?v=nXI-9ThUNCs&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=38&t=200s",
            Mechs.GROOTSLANG: "https://www.youtube.com/watch?v=QqMeB7cy_FI&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=39&t=35s",
            Mechs.AMADLOZI: "https://www.youtube.com/watch?v=S0KDE1AMmXk&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=40&t=13s",
            Mechs.CETSHWAYO: "https://www.youtube.com/watch?v=dK83-PRbmn4&list=PLOnXWQrYlGSAp3ElGgduDHtkh2lTTileB&index=41",
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
        resources=get_image_resources_with_source(
            source="https://shadefish.tumblr.com/post/683554906831028224/a-commission-from-twitter-of-the-clients-players",
            mechs_to_paths={
                Mechs.RALEIGH: [
                    "https://64.media.tumblr.com/facbc6c631f7f9250228dcfa7044ea73/ec76d959dbf1d4eb-b4/s1280x1920/df0d94a145561af32e68cd3fd55c03e0f80879d0.png",
                    "https://64.media.tumblr.com/9d874bd2f120588e0840e86bf9cb0ed9/ec76d959dbf1d4eb-5d/s1280x1920/1677517da98f30a5ddaecd78e670592ba7429f3d.png",
                ],
                Mechs.ENKIDU: "https://64.media.tumblr.com/d1431d115f025023a5f42413fc35f835/ec76d959dbf1d4eb-25/s1280x1920/cf35aefc558d3dbc57fdd927c97feaab426e4033.png",
                Mechs.METALMARK: "https://64.media.tumblr.com/ae85668512b65047ab781131f371a1d2/ec76d959dbf1d4eb-39/s1280x1920/f227b31710071d06b17a8fa8c614fd6d401efe23.png",
                Mechs.SWALLOWTAIL: "https://64.media.tumblr.com/b44c9c83f1cf26247644905f955e5999/ec76d959dbf1d4eb-11/s1280x1920/e76777247d7aa10c1ea6e245c7c1d4d52fcfa891.png    ",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://shadefish.tumblr.com/post/680013756630171649/a-commission-for-negativevalence-of-a-pair-of?is_related_post=1#notes",
            mechs_to_paths={
                Mechs.VLAD: "https://64.media.tumblr.com/79790b6113078004e8f15b18954cedb4/d45c623ae12ee7b4-60/s400x600/99b3a03d5c7d715326ff636bca35796357253876.png",
                Mechs.BALOR: "https://64.media.tumblr.com/4afa2f4919490c1cc4e9436d5ca808f6/d45c623ae12ee7b4-e5/s1280x1920/07007a499ac507de58b71e197d9ed104b08cff09.png",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://shadefish.tumblr.com/post/686057909575090176/all-of-the-player-mechs-for-my-current-lancer-game#notes",
            mechs_to_paths={
                Mechs.DRAKE: "https://64.media.tumblr.com/fb4487566c8cfbd0ef170d9b47b8155f/83ae21a13fea1bf1-5f/s1280x1920/9b0963568b1b7a4514e9c7b82965af1ce6ec40ae.png",
                Mechs.BARBAROSSA: "https://64.media.tumblr.com/2261b2b61a2b602e90aff4792e148df4/83ae21a13fea1bf1-73/s1280x1920/4a844381a6d9811cbf367d3d155f7c182c22d1aa.png",
                Mechs.MONARCH: "https://64.media.tumblr.com/6d576f39fcad391abeab012688cc7a13/83ae21a13fea1bf1-1a/s1280x1920/6cdd2e3f9564ddfe263a186a3823bd66f7738bae.png",
                Mechs.ATLAS: "https://64.media.tumblr.com/d086492d8a516f3f68feb872c2ce26cc/83ae21a13fea1bf1-2a/s1280x1920/9017a7c930cca9f3b089b6591c37109d2f7f8f0a.png",
                Mechs.ORCHIS: "https://64.media.tumblr.com/d0c80cb1386be058bffcf3c59c5ede10/83ae21a13fea1bf1-29/s1280x1920/b9321e0ed10a4163ec27a7a160cd5fd30f429180.png",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://theogm.artstation.com/projects/N51P5d?album_id=5224111",
            mechs_to_paths={
                Mechs.NELSON: "https://cdnb.artstation.com/p/assets/images/images/026/564/691/large/theotime-galmiche-marchofrobots-22.jpg?1589126440",
                Mechs.TOKUGAWA: "https://cdnb.artstation.com/p/assets/images/images/026/565/041/large/theotime-galmiche-marchofrobots-19.jpg?1589127024",
            },
        )
    ),
    ResourceGroup(
        resources=get_image_resources_with_source(
            source="https://gentrigger.tumblr.com/post/634066953889333248/lancerrpg-commission-for-zombiemike-for-their",
            mechs_to_paths={
                Mechs.RALEIGH: "https://64.media.tumblr.com/c4acc6f710020a8042bc3d8d2fdca6d7/533efeceb3f1e35b-94/s1280x1920/ae660c6e1567579e77b9333b0ade4e360bcc901e.pnj",
                Mechs.PEGASUS: "https://64.media.tumblr.com/c4acc6f710020a8042bc3d8d2fdca6d7/533efeceb3f1e35b-94/s1280x1920/ae660c6e1567579e77b9333b0ade4e360bcc901e.pnj",
            },
        )
    ),
    IMAGES_DUMP,
]


def _is_image_group(group: list[MechResource]) -> bool:
    if not group:
        return False
    if not isinstance(group, list):
        group = [group]
    return isinstance(group[0], Image)
