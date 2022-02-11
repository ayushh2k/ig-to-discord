import json
import requests
import os


INSTAGRAM_USERNAME = os.environ.get('IG_USERNAME')

def get_last_publication_url(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"][
        "edges"][0]["node"]["shortcode"]


def get_description_photo(html):
    return html.json(
    )["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"][
        "edge_media_to_caption"]["edges"][0]["node"]["text"]


def get_last_thumb_url(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"][
        "edges"][0]["node"]["display_url"]
    
def get_profile_pic_url(html):
  return html.json()["graphql"]["user"]["profile_pic_url"]

def get_username(html):
  return html.json()["graphql"]["user"]["username"]


def webhook(webhook_url, html):
    data = {}
    data["embeds"] = []
    embed = {}
    embed["color"] = 3467325
    embed["thumbnail"] = {'url':get_profile_pic_url(html)}
    embed["title"] = f"{get_username(html)} - Link to post!" + ""
    embed["url"] = "https://www.instagram.com/p/" + \
        get_last_publication_url(html)+"/"
    embed["description"] = get_description_photo(html)
    embed["image"] = {"url":get_last_thumb_url(html)}
    data["embeds"].append(embed)
    result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Image successfully posted in Discord, code {}.".format(result.status_code))


def get_instagram_html(INSTAGRAM_USERNAME):
    headers = {
        "Host":
        "www.instagram.com",
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    html = requests.get("https://www.instagram.com/" + INSTAGRAM_USERNAME +
                        "/feed/?__a=1",
                        headers=headers)
    return html
