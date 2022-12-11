from enum import Enum
from os.path import exists as file_exists
import requests

from .ListHelper import list_strip

PROBLEM_URI = 'https://adventofcode.com/{y}/day/{d}'
INPUT_URI = PROBLEM_URI + '/input'

RES_DIR = 'resources/'
COOKIE_FILE = RES_DIR + 'cookie.txt'
USER_AGENT_FILE = RES_DIR + 'user-agent.txt'

INPUT_FILE_NAME = 'day{d}.txt'
LIVE_INPUT_DIR = 'live-input/'
SAMPLE_INPUT_DIR = 'sample-input/'

INPUT_FILE = RES_DIR + LIVE_INPUT_DIR + INPUT_FILE_NAME
SAMPLE_FILE = RES_DIR + SAMPLE_INPUT_DIR + INPUT_FILE_NAME

class InputType(Enum):
    SAMPLE_DATA = 0,
    LIVE_DATA = 1

def read(year, day):
    __load_aoc_data(year,day)
    return __file_read(INPUT_FILE.format(d=day))

def readLines(year, day, stripped=True):
    __load_aoc_data(year,day)
    lines = __file_readlines(INPUT_FILE.format(d=day))
    return list_strip(lines) if stripped else lines
    
def get_sample_data(year, day, stripped=True):
    if not file_exists(SAMPLE_FILE.format(d=day)):
        session_id = __file_read(COOKIE_FILE).removeprefix('session=')
        user_agent = __file_read(USER_AGENT_FILE)

        uri = PROBLEM_URI.format(y=year, d=day)
        response = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': user_agent})

        start_index = response.text.find('<pre><code>') + 11
        end_index = response.text.find('</code></pre>')
        __file_create(SAMPLE_FILE.format(d=day), response.text[start_index:end_index])

    lines = __file_readlines(SAMPLE_FILE.format(d=day))
    return list_strip(lines) if stripped else lines
    

def __load_aoc_data(year, day):
    if not file_exists(INPUT_FILE.format(d=day)):
        session_id = __file_read(COOKIE_FILE).removeprefix('session=')
        user_agent = __file_read(USER_AGENT_FILE)

        uri = INPUT_URI.format(y=year, d=day)
        response = requests.get(uri, cookies={'session': session_id}, headers={'User-Agent': user_agent})

        __file_create(INPUT_FILE.format(d=day), response.text)

def __file_read(file_path):
    with open(file_path, 'r') as f:
        return f.read() 

def __file_readlines(file_path):
    with open(file_path, 'r') as f:
        return f.readlines() 

def __file_create(file_path, data):
    with open(file_path, 'x') as f:
        f.write(data)
