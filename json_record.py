import json as js
from os import path

def read_json_record(filename: str="records.json") -> list[dict[str:str]]:
    """Reads all recorded data from either a named JSON file or 'records.json' if no filename is provided."""
    record = []

    # Verify that provided filename can be found
    if path.isfile(filename):
        # Verify that provided file is a .json file
        if not filename.endswith(".json"):
            raise ValueError("Incorrect file type provided [Must use JSON file]")
        
        with open(filename) as f:
            record = js.loads(f.read())

    return record

def write_json_record(record_data: list[dict[str:str]], filename: str="records.json") -> None:
    """Writes all provided data to either a named JSON file or 'records.json' if no filename is provided."""
    with open(filename, "w", encoding="utf-8") as f:
        js.dump(record_data, f, indent=2)