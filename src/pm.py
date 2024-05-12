import sys
import os
from pathlib import Path

STORAGE_PATH = '.config/storage'


class RecordNotFoundError(Exception):
    pass


def add(name: str, url: str, username: str, password: str):
    record = {'name': name, 'url': url, 'username': username, 'password': password}
    write_on_storage(record)


def fetch(name):
    check_and_create_storage()
    try:
        result = find_record_by_name(name)
        print(generate_parsed_record(result))
    except RecordNotFoundError as e:
        print(f"No record found for: {name}", file=sys.stderr)


def write_on_storage(record_dict):
    parsed_record = generate_parsed_record(record_dict)
    with open(STORAGE_PATH, 'a') as f:
        f.write(parsed_record)


def generate_parsed_record(record_dict):
    return f"[{record_dict['name']}]\nurl={record_dict['url']}\nusername={record_dict['username']}\npassword={record_dict['password']}\n\n"


def find_record_by_name(name):
    records = find_all_records()
    for record in records:
        if record['name'] == name:
            return record
    raise RecordNotFoundError


def find_all_records():
    records = []
    with open(STORAGE_PATH, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            l = lines[i]
            if l.startswith('[') and l.endswith(']\n'):
                name = l.strip('[]\n')
                url = lines[i + 1].strip().replace("url=", "")
                username = lines[i + 2].strip().replace("username=", "")
                password = lines[i + 3].strip().replace("password=", "")
                records.append({'name': name, 'url': url, 'username': username, 'password': password})
                i += 4
            else:
                i += 1
    return records


def check_and_create_storage():
    storage_dir = os.path.dirname(STORAGE_PATH)
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    try:
        with open(STORAGE_PATH, 'x') as file:
            file.close()
    except FileExistsError:
        return
