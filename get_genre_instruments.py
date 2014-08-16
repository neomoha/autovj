# -*- coding: utf-8 -*-

# This file is part of AutoVJ.
#
# AutoVJ is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AutoVJ is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AutoVJ.  If not, see <http://www.gnu.org/licenses/>.

# Written by Mohamed Sordo (@neomoha)
# Email: mohamed ^dot^ sordo ^at^ gmail ^dot^ com
# Website: http://msordo.weebly.com

import codecs, argparse
import wikipedia
from rdflib import Graph, URIRef

dbpedia_ontology = {
    "dbpedia-owl": URIRef("http://dbpedia.org/ontology/instrument"),
    "dbprop": URIRef("http://dbpedia.org/property/instruments"),
    "label": URIRef("http://www.w3.org/2000/01/rdf-schema#label")
}

def _clean_genre(genre):
    return genre.lower().replace("-", "").replace(" ", "")

def _get_instrument_name_from_url(instrument):
    instrument = instrument[instrument.rfind("/")+1:]
    if instrument.find("(") > -1:
        instrument = instrument[:instrument.rfind("(")]
    instrument = instrument.replace("_", " ").strip()
    return instrument

def _get_genre_url(genre):
    res = wikipedia.search(genre+" music")
    if len(res) == 0:
        return None
    page = wikipedia.page(res[0])
    dbpedia_url = "http://dbpedia.org/resource/" + page.url[page.url.rfind("/")+1:]
    print dbpedia_url
    return dbpedia_url

def get_genre_instruments(genre):
    g = Graph()
    g.parse(_get_genre_url(genre))
    instruments = set()
    for prop in ("dbpedia-owl", "dbprop"):
        for stmt in g.subject_objects(dbpedia_ontology[prop]):
            instrument = _get_instrument_name_from_url(stmt[1])
            instruments.add(instrument)
    return instruments
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the most representative instruments of a genre')
    parser.add_argument('genre', help='Genre (use quotes for genres with more than one word)')
    args = parser.parse_args()
    instruments = get_genre_instruments(args.genre)
    print instruments