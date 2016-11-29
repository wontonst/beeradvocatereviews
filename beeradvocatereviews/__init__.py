"""
Beeradvocatereviews is a module that exports a user's beeradvocate reviews.
"""
from __future__ import print_function

import json

from pyquery import PyQuery
import requests

BASE_URL = 'https://www.beeradvocate.com'


class Beer(object):
    """
    Object to store beer reviews.
    """
    def __init__(self, name, brewery, style, abv, date, url):
        self.name = name
        self.brewery = brewery
        self.style = style
        self.abv = abv
        self.date = date
        self.url = url
        self.get_beer_detail(url)

    @staticmethod
    def clean_xml(xml):
        return str(unicode(xml).encode('utf-8'))

    @staticmethod
    def build_from_xml(xml):
        """
        Given a tr HTMLElement, parse the table contents.
        """
        date = Beer.clean_xml(xml[0].text_content())
        a = [x for x in xml[1].getchildren() if x.tag == 'a']
        name = Beer.clean_xml(a[0].text_content())
        brewery = Beer.clean_xml(a[1].text_content())
        style = Beer.clean_xml(a[2].text_content())
        url = Beer.clean_xml(a[0].get('href'))
        abv = Beer.clean_xml(xml[2].text_content())
        return Beer(name, brewery, style, abv, date, url)

    def get_beer_detail(self, url):
        """
        Follow the link to beer page to get detailed review information.
        """
        r = requests.get(BASE_URL + url)
        pq = PyQuery(r.text)
        pq = pq('#rating_fullview_content_2:first')
        self.rating = self.clean_xml(pq('.BAscore_norm:first').text())
        self.comment = pq('.muted:first').text()
        pq.remove('br')
        pq.remove('.muted')
        pq.remove('.BAscore_norm')
        self.comment += "\n" + pq.text()


def get(username, start):
    """
    Second level function to pull up to 50 reviews.
    start - review number to start from
    """
    r = requests.get(
        '{}/user/beers/?start={}&&ba={}&order=dateD&view=R'.format(
            BASE_URL, start, username
        )
    )
    beers = []
    pq = PyQuery(r.text)
    pq = pq('#ba-content')
    pq = pq('table')
    pq = pq('tr')

    for p in pq[3:]:
        d = p.getchildren()[1:]
        beers.append(Beer.build_from_xml(d))
    return beers


def serialize(beers):
    """
    Serialize and print out the result.
    """
    print(json.dumps([b.__dict__ for b in beers]))


def run(username, num):
    """
    Top level function to call get() until all reviews are obtained, then print
    """
    result = []
    for a in range(0, int(num), 50):
        result += get(username, a)
    serialize(result)


def main():
    """
    Parse command line args and run app.
    """
    import argparse
    parser = argparse.ArgumentParser(description='Export BeerAdvocate ratings')
    parser.add_argument('username', help='Username to get reviews from')
    parser.add_argument('reviews', help='Number of reviews the user has')
    args = parser.parse_args()
    run(args.username, args.reviews)
