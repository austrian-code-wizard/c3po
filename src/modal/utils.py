import os


def copy_json_files_recursively(volume: str, path: str):
    os.system(f"modal volume get {volume} \"{path}/*\" --force")