import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, src_lang, dst_lang):
    return text