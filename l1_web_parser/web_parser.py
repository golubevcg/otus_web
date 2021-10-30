import requests
from bs4 import BeautifulSoup
import json
import os


def get_all_links(address: str, links_dict: dict, add_children_links: bool = True, filename: str = None):

    """
    Returns all links, founded in html page of given site address.

    :param address: address to html page
    :param links_dict: dictionary to write results to
    :param add_children_links: if true function will search for links inside each founded link
    :param filename: filename to write searched data to
    """

    if not address:
        print("Given address is empty, please provide correct address.")
        return

    html = requests.get(address)
    soup = BeautifulSoup(html.text, "html.parser")

    for link in soup.findAll("a"):
        current_link = link.get("href")
        if not current_link or not current_link.startswith("http"):
            links_dict[current_link] = "Wrong address, children not checked."
            continue

        links_dict[current_link] = dict()
        if add_children_links:
            children_links = dict()
            get_all_links(current_link, children_links, add_children_links=False)
            links_dict[current_link] = children_links

    if not filename:
        return

    if not os.path.exists(filename):
        print("Path not exists, file will be written in module folder.")

    with open(filename, 'w') as f:
        json.dump(links_dict, f, indent=4, ensure_ascii=False)


site_address = "https://mail.ru/"
file_path = "mail_ru_links.json"
result_dict = dict()
get_all_links(site_address, result_dict, filename=file_path)

for lnk in result_dict:
    print(lnk)
    child_links = result_dict[lnk]
    for child in child_links:
        print(f"\t{child}")
