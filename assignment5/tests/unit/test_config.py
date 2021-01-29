#!/usr/bin/env python3

from assignment5 import config
import pytest
TEST = {"bos taurus": "Bos_tarus", "cow": "Bos_tarus", "cows": "Bos_tarus", "bos_tarus": "Bos_tarus", "homo sapiens": "Homo_sapiens", "human": "Homo_sapiens", "humans": "Homo_sapiens", "homo_sapiens": "Homo_sapiens",  "equus caballus": "Equus_caballus", "horse": "Equus_caballus", "horses": "Equus_caballus", "equus_caballus": "Equus_caballus", "mus muculus": "Mus_musculus", "mouse": "Mus_musculus", "mice": "Mus_musculus", "mus_musculus": "Mus_musculus", "ovis aries": "Ovis_aries", "sheep": "Ovis_aries", "sheeps": "Ovis_aries", "ovis_aries": "Ovis_aries", "rattus norvegicus": "Rattus_norvegicus", "rat": "Rattus_norvegicus", "rats": "Rattus_norvegicus", "rattus_norvegicus": "Rattus_norvegicus"}


KEYWORDS = config.get_host_keywords()
def test_host_keywords_type():
    assert (KEYWORDS == TEST) is True

test = []
def test_host_keywords_type():
    assert (KEYWORDS == test) is False

def test_dict_attr():
    assert hasattr(KEYWORDS, "keys")


def test_val_attr():
    assert hasattr(KEYWORDS, "values")


def test_dict_attr_keys():
    key = list(KEYWORDS.keys())[0]
    assert (type(key) == type("<class 'str'>")) is True


def test_dict_attr_keys():
    key = list(KEYWORDS.keys())[0]
    assert (type(key) == ("<class 'dict'>")) is False
VALS = list(KEYWORDS.values())
USED = list()
UNIQUE_VALUES = []
for c in VALS:
    if c not in UNIQUE_VALUES:
        UNIQUE_VALUES.append(c)


ANIMALS = ['Bos_taurus', 'Homo_sapiens', 'Rattus_norvegicus', 'Ovis_aries']
def test_lists():
    assert (ANIMALS.sort() == UNIQUE_VALUES.sort()) is True

def test_dir_upper():
    assert (UNIQUE_VALUES[0][0].isupper() is True)


def test_dir_lower():
    assert (UNIQUE_VALUES[0][1:].islower() is True)


COWS = ['bos taurus', 'cow', 'cows', 'bos_tarus']
def test_cows():
    for cow in COWS:
        for key, value in KEYWORDS.items():    
             if cow == key:
                 assert value == "Bos_tarus"


HUMANS = ['homo_sapiens', 'humans', 'human', 'homo sapiens']
def test_humans():
    for human in HUMANS:
        for key, value in KEYWORDS.items():
             if human == key:
                 assert value == "Homo_sapiens"


KEYS = list(KEYWORDS.keys())
def test_keys_lower():
    for key in KEYS:
        assert(key.islower() is True)


HUMANS = ['homo_sapiens', 'humans', 'human', 'homo sapiens']
def test_humans():
    for human in HUMANS:
        for key, value in KEYWORDS.items():
             if human == key:
                 assert value == "Homo_sapiens"
KEYS = list(KEYWORDS.keys())

HORSES = ['equus_caballus', 'horse', 'horses', 'equus caballus']
def test_horses():
    for horse in HORSES:
        for key, value in KEYWORDS.items():
             if horse == key:
                 assert value == "Equus_caballus"

RATS = ['rattus_norvegicus', 'rat', 'rats', 'rattus norvegicus']
def test_horses():
    for rat in RATS:
        for key, value in KEYWORDS.items():
             if rat == key:
                 assert value == "Rattus_norvegicus"

host = 'does_not_exist'
def test_gene_name():
    assert (host not in KEYWORDS) is True
