from objects import Mechs
from resource_classes import Image, ResourceGroup

IMAGES_DUMP = ResourceGroup(
    resources={
        Mechs.ATLAS: [
            Image(
                path="https://64.media.tumblr.com/bd9238b9d4ed94209d4469ad7486428b/f80aef141460641a-fb/s500x750/5f75b3fca5ae0443550debc85b1982566a185c43.png",
                source="https://gentrigger.tumblr.com/post/190526552790/callsign-banchou-mech-mac-the-knife",
            ),
            Image(
                path="https://64.media.tumblr.com/ff2cb827135bc3552942c8cbff4d1a64/79f4605774502c9e-ac/s400x600/177ed4dfa0e1f2a314af0ea1ee45534e9e71a25d.png",
                source="https://gentrigger.tumblr.com/post/188510099195/graya-the-runic-commission-for-xiakha-for-a",
            ),
        ],
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
            ),
            Image(
                path="https://64.media.tumblr.com/a2ee60341a781abe43004cd89bfd2dd1/fadf2f75e0611d22-76/s640x960/382cc903aad1b76c1aa3b193b78fc03d9ca8ed74.pnj",
                source="https://gentrigger.tumblr.com/post/633880005884116992/commission-for-sleepyshaman-for-their-players",
            ),
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
            ),
            Image(
                path="https://64.media.tumblr.com/ca1594f2c70f634d200752986e28bb6a/5366032220d7eb4c-9e/s1280x1920/fbed762b977752fdac1e2bca2bdb6b591c9bb234.pnj",
                source="https://gentrigger.tumblr.com/post/615476498745458688/fenris-a-commission-for-a-pilots-blackbeard-for",
            ),
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
            Image(
                path="https://64.media.tumblr.com/2750bdb23bbc6a8efaceae82317162e9/09f8ca5dcf96a206-82/s1280x1920/d71c122ed015f0c5a3f83b9d38ffd91a1deb71ef.png",
                source="https://gentrigger.tumblr.com/post/683151100751364096/avi-callsign-dilettante-ips-n-drake-lancer",
            ),
            Image(
                path="https://64.media.tumblr.com/dafe3b6e9d5eb2cae596238188ae941f/157dee283aafe314-f2/s500x750/7f74252b765b6ca3cf86345764c68b4f5984e1d2.png",
                source="https://gentrigger.tumblr.com/post/615542193491427329/sup-gamers-finally-got-the-designs-for-the-pilots",
            ),
        ],
        Mechs.DUSK_WING: [
            Image(
                path="https://64.media.tumblr.com/9d5f6cf2dc2f1755f7c7126f8d79b79a/c148271a052055b7-b0/s500x750/07174c7c5a41a3986f1489466705d9032b567e87.png",
                source="https://gentrigger.tumblr.com/post/189695369565/hazel-star-hunter-modified-ssc-dusk-wing",
            )
        ],
        Mechs.GENGHIS: [
            Image(
                path="https://64.media.tumblr.com/70803b21c7c72b6eff9903cb0b470b9d/3aa4ab0d75812a20-00/s2048x3072/f044a5f8bd0b75baf7b57bb98f9c1da09db127ae.pnj",
                source="https://shadefish.tumblr.com/post/684754091862278144/a-horus-themed-genghis-i-am-calling-agni-kind",
            )
        ],
        Mechs.GOBLIN: [
            Image(
                path="https://64.media.tumblr.com/e1d553e5e7353adb991e631cdfb388a4/tumblr_plhm1xf8ts1qgwtzgo1_500.png",
                source="https://gentrigger.tumblr.com/post/182088864995/modified-goblin-commission-for-a-players",
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
            Image(
                path="https://64.media.tumblr.com/157a013650bbff8b070e8397873696de/9f78a9e705e8157a-76/s1280x1920/ebe03a804189898c234d34b31f7ba2ccdebf80a9.pnj",
                source="https://gentrigger.tumblr.com/post/611885787161755648/call-sign-one-love-pilot-1l-0v-3-mech-illegal",
            ),
        ],
        Mechs.HYDRA: [
            Image(
                path="https://64.media.tumblr.com/0c9ab7e15b32936285033229ff18f5d8/678735dcf678e3b0-0e/s500x750/fbf2c1dbde3df4cd262c77707f588a096b66533d.png",
                source="https://gentrigger.tumblr.com/post/189380326335/callsign-salvage-horus-hydra-ransomware",
            ),
            Image(
                path="https://64.media.tumblr.com/7192cd26adf98cce49cb15967bc939a6/cd54c799356ed9d5-cf/s500x750/28aab2189b3f934ebd5d728f712c5db2fb3a5454.png",
                source="https://gentrigger.tumblr.com/post/189159854415/pilot-sanzang-mech-i-am-not-a-demon-mech",
            ),
        ],
        Mechs.ISKANDER: [
            Image(
                path="https://64.media.tumblr.com/0e4fa19d2944a40ab4c54208b33c8944/9886819bb8d0e9ef-76/s500x750/dc2c2df3716009bb57b9b00822dfa3efe975f4c2.png",
                source="https://gentrigger.tumblr.com/post/189695382260/pilot-hairpin-mech-clerical-error-a",
            ),
            Image(
                path="https://64.media.tumblr.com/aea9ed6740b570bb826ca82e2864556b/fa8d156b50700275-7b/s500x750/b2cfc0602e8f230848759357d51efdfd4ae332f3.png",
                source="https://64.media.tumblr.com/aea9ed6740b570bb826ca82e2864556b/fa8d156b50700275-7b/s500x750/b2cfc0602e8f230848759357d51efdfd4ae332f3.png",
            ),
        ],
        Mechs.KOBOLD: [
            Image(
                path="https://64.media.tumblr.com/4b583325a224c81ec2f2032ac3201bb0/tumblr_pyre9zYsNH1qgwtzgo1_500.png",
                source="https://gentrigger.tumblr.com/post/188089450790/pugnacious-photon-gnoll-commission-for",
            )
        ],
        Mechs.NELSON: [
            Image(
                path="https://cdna.artstation.com/p/assets/images/images/027/409/116/large/theotime-gm-commission-b-s-colored-web.jpg?1591454260",
                source="https://theogm.artstation.com/projects/q9L9ky?album_id=5224111",
            ),
            Image(
                path="https://64.media.tumblr.com/0390c491c7f413b83717b2c810b27641/cefce4d98bc655fe-68/s500x750/d9d6ac55cc93ffc6e933650dee9c3c5300ead161.png",
                source="https://gentrigger.tumblr.com/post/617410189660913664/lancerrpg-mech-commission-for-meckamecha-a",
            ),
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
            ),
            Image(
                path="https://64.media.tumblr.com/9e2b505d2e1e3fbaa66ca6b1940250d0/9d6107ff0e09a276-73/s500x750/009b14324e72f9e76022df400c7d4900c39bc8e9.png",
                source="https://gentrigger.tumblr.com/post/611161087352651776/ira-morne-and-one-hot-friend-commission-for",
            ),
        ],
        Mechs.SWALLOWTAIL: [
            Image(
                path="https://cdna.artstation.com/p/assets/images/images/029/678/810/large/theotime-gm-athena-swallowtail-web.jpg?1598315334",
                source="https://theogm.artstation.com/projects/Xna6Vy?album_id=5224111",
            ),
            Image(
                path="https://64.media.tumblr.com/688f17a43ce2a4349118f584f0829cb4/cb73197f91c09b2d-94/s1280x1920/09836deac253703bee7a84656b27a6156178f383.png  ",
                source="https://gentrigger.tumblr.com/post/665559271285686272/commish-fo-discountatlatl-for-their-lancer-ttrpg",
            ),
            Image(
                path="https://64.media.tumblr.com/82fd86f2aacc0806deaad1b80d28b507/6a8c2779d35581ea-ec/s500x750/1e664e2369f210443f0f24704168a5bc42bc2062.png",
                source="https://gentrigger.tumblr.com/post/189714316120/pilot-aurora-mech-cosmic-filter-commission",
            ),
        ],
        Mechs.SUNZI: [
            Image(
                path="https://64.media.tumblr.com/aea9ed6740b570bb826ca82e2864556b/fa8d156b50700275-7b/s500x750/b2cfc0602e8f230848759357d51efdfd4ae332f3.png",
                source="https://gentrigger.tumblr.com/post/188907770970/caravela-8ball-lancer-mech-commission-for-an",
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
        Mechs.LANCASTER: [
            Image(
                path="https://64.media.tumblr.com/8d2c4e42f06392506f4fe07e62b05ef9/f05f6f983f722d5d-26/s500x750/6d44e167d3fb6a47d236d857c57a2c82a9887a87.png",
                source="https://gentrigger.tumblr.com/post/189695342080/pilot-apollo-j-nox-callsign-chief-chief",
            )
        ],
        Mechs.MONARCH: [
            Image(
                path="https://64.media.tumblr.com/601ab106836d0e4ceab62064c04f975a/62f0792dc9833caa-fe/s500x750/51bac71fac6a4874a4e291ff345b01414bd58cd4.png",
                source="https://gentrigger.tumblr.com/post/618035208486322176/lancerrpg-mech-commission-for-xiakha-for-their",
            )
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
        Mechs.VOLK: [
            Image(
                path="https://64.media.tumblr.com/ca1594f2c70f634d200752986e28bb6a/5366032220d7eb4c-9e/s1280x1920/fbed762b977752fdac1e2bca2bdb6b591c9bb234.pnj",
                source="https://gentrigger.tumblr.com/post/615476498745458688/fenris-a-commission-for-a-pilots-blackbeard-for",
            ),
            Image(
                path="https://64.media.tumblr.com/859aaca210fd99d92fbd86db585d1d22/bad869ca9ff041ad-96/s500x750/b30fddbd7ab8f77beb3df40fbc9bc636bfd3df2d.png",
                source="https://gentrigger.tumblr.com/post/189695356025/mech-hheldrin-pilot-rota-commission-for",
            ),
        ],
        Mechs.ZHENG: [
            Image(
                path="https://64.media.tumblr.com/cb1f48b2986bf24fb5a7dd68233fc4a9/b46255c18bd3d7ab-66/s500x750/2ec78edcbbf9c6cd5e34164ce233f2e04073c4eb.png",
                source="https://gentrigger.tumblr.com/post/615487815382401024/another-finished-commission-for-a-lancerrpg-mech",
            )
        ],
    },
)
