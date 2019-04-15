import requests
import re
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def get_game_title(soup):
    return (soup.find('div', attrs = {'class': 'profile_header shadow_text'})
            .get_text()
            .strip('\n')
            .strip(' $'))


def text_from_tag(tag):
    return tag.get_text().strip('\n').strip(' $')


def get_average_time(times):
    return text_from_tag(times[1])

def get_median_time(times):
    return text_from_tag(times[2])

def get_rushed_time(times):
    return text_from_tag(times[3])

def get_leisure_time(times):
    return text_from_tag(times[4])

def get_poll_count(times):
    return text_from_tag(times[0])

def get_main_story_times(soup):
    return soup.find("td", text="Main Story").find_next_siblings("td")

def get_main_story_extras_times(soup):
    return soup.find("td", text="Main + Extras").find_next_siblings("td")

def get_completionist_times(soup):
    return soup.find("td", text="Completionists").find_next_siblings("td")

def get_all_playstyles_times(soup):
    return soup.find("td", text="All PlayStyles").find_next_siblings("td")

def generate_row(tag, soup, play_title, id_no):
    return pd.DataFrame(data = [[get_game_title(soup),
                                 id_no,
                                 play_title,
                                 get_poll_count(tag),
                                 get_average_time(tag),
                                 get_median_time(tag),
                                 get_rushed_time(tag),
                                 get_leisure_time(tag)]],
                       columns = ['Title', 'ID', 'Playstyle', 'Polled',
                                  'Average', 'Median', 'Rushed', 'Leisure'])


def cook_soup(id_no):
    return BeautifulSoup(requests.get(str('https://howlongtobeat.com/game.php?id=' + id_no)).content, "lxml")


def create_game_entry(id_no):
    soup = cook_soup(id_no)
    valid_page = [soup.find("td", text="Main Story"),
                  soup.find("td", text="Main + Extras"),
                  soup.find("td", text="Completionists"),
                  soup.find("td", text="All PlayStyles")]

    if None in valid_page:
        return pd.DataFrame()
    else:
        if soup.findAll('tr'):
            main = generate_row(get_main_story_times(soup), soup, "Main", id_no)
            main_extra = (generate_row(get_main_story_extras_times(soup),
                                       soup,
                                       "Main + Extras",
                                       id_no))
            completionist = (generate_row(get_completionist_times(soup),
                                          soup,
                                          "Completionist",
                                          id_no))
            all_playstyles = (generate_row(get_all_playstyles_times(soup),
                                           soup,
                                           "All Playstyles",
                                           id_no))
            return (main.append(main_extra)
                    .append(completionist)
                    .append(all_playstyles)
                    .set_index(['ID', 'Title','Playstyle']))
        else:
            return pd.DataFrame()


n = 0


for i in np.arange(1, 10): #99999
    data = create_game_entry(str(i))
    if not data.empty:
        n = n + 1
        data.to_csv("hl2b.csv", mode='a', header=False)


print("Added", n, "games")
