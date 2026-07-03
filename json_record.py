import json as js
from os import path

def read_json_record(filename="records.json"):
    record = []

    if path.isfile(filename):
        with open(filename) as f:
            record = js.loads(f.read())

    return record

def write_json_record(record_data, filename="records.json"):
    with open(filename, "w", encoding="utf-8") as f:
        js.dump(record_data, f, indent=2)