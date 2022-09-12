from objects import Mechs
from resources import ResourceGroup, Image

IMAGES_DUMP = (
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
                ),
                Image(
                    path="https://64.media.tumblr.com/1096ac33af42eff7c5e0aea54cf10730/098fe549157297c7-a3/s2048x3072/56d210b3f8e54d1e4dbd57a92fba81fd333309a2.pnj",
                    source="https://shadefish.tumblr.com/post/686057517989642241/a-commission-off-of-twitter-of-a-ktbdom-inspired",
                ),
            ],
            Mechs.GENGHIS: [
                Image(
                    path="https://64.media.tumblr.com/70803b21c7c72b6eff9903cb0b470b9d/3aa4ab0d75812a20-00/s2048x3072/f044a5f8bd0b75baf7b57bb98f9c1da09db127ae.pnj",
                    source="https://shadefish.tumblr.com/post/684754091862278144/a-horus-themed-genghis-i-am-calling-agni-kind",
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
            Mechs.SALADIN: [
                Image(
                    path="https://cdna.artstation.com/p/assets/images/images/026/824/932/large/jan-kruner-lancer-saladin-fortress1d.jpg?1589831446",
                    source="https://www.artstation.com/artwork/lVga4a",
                )
            ],
            Mechs.SHERMAN: [
                Image(
                    path="https://64.media.tumblr.com/eea9efef04e818b95c0db83cb1f9399b/f3d3bd283de8101d-ba/s1280x1920/2697a8781a42c4d8a667360a7a21303c8928db0b.png",
                    source="https://shadefish.tumblr.com/post/683083791970025472/a-pair-of-commissions-for-an-upcoming-lancer?is_related_post=1",
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
)
