from pathlib import Path

import bs4

# html_name = "lancer_custom_werks_playlist.html"
# html_name = "trashtalk_on_lancer_playlist.html"
html_name = "mechanics_brewery_playlist.html"

html = (Path("in") / html_name).read_text(errors="ignore")

soup = bs4.BeautifulSoup(html, "html.parser")
links = soup.select("a#video-title")

root_url = "https://www.youtube.com"

# for link in links:
#     href = root_url + link.get("href")
#     text = link.text
#     mech_name = text.split(": ")[1]
#     sanitized_name = mech_name.upper().strip().replace(" ", "_").replace("'", "")
#     print(f"{sanitized_name}: '{href}',")

all_links = links  # for debug
links = [
    link for link in links if link.text.startswith("\n")
]  # idk why this is necessary

for link in links:
    href = root_url + link.get("href")
    text = link.text
    try:
        mech_name_corp = text.split(": ")[1]
        mech_name = mech_name_corp.split(" (")[0]
        corp = mech_name_corp.split(" (")[1].split(")")[0]

        sanitized_name = mech_name.upper().strip().replace(" ", "_").replace("'", "")
        print(f"{sanitized_name}: '{href}',")
    except IndexError:
        pass


print("done")
