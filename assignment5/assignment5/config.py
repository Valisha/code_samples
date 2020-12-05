#!/usr/bin/env python3

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    return _UNIGENE_DIR

def get_unigene_extension():
    return _UNIGENE_FILE_ENDING

def get_host_keywords():
    host_keywords = {"bos taurus": "Bos_tarus", "cow": "Bos_tarus", "cows": "Bos_tarus", "bos_tarus": "Bos_tarus", "homo sapiens": "Homo_sapiens", "human": "Homo_sapiens", "humans": "Homo_sapiens", "homo_sapiens": "Homo_sapiens",  "equus caballus": "Equus_caballus", "horse": "Equus_caballus", "horses": "Equus_caballus", "equus_caballus": "Equus_caballus", "mus muculus": "Mus_musculus", "mouse": "Mus_musculus", "mice": "Mus_musculus", "mus_musculus": "Mus_musculus", "ovis aries": "Ovis_aries", "sheep": "Ovis_aries", "sheeps": "Ovis_aries", "ovis_aries": "Ovis_aries", "rattus norvegicus": "Rattus_norvegicus", "rat": "Rattus_norvegicus", "rats": "Rattus_norvegicus", "rattus_norvegicus": "Rattus_norvegicus"}
    return host_keywords
def get_error_string_4_unable_to_open(file=None, mode=None):
    print("Could not open the file: {} for mode '{}'".format(file, mode))
