
"""

JSONUTILITIES IS A OPENSOURCE LIBRAIRIE FOR PYTHON, IT'S BASE ON PY 3.12.5
THE OBJECTIF IS TO HAVE A BETTER EXPERIENCE WITH JSON FILES, THE LIBRAIRIE IS THE PERFECT OPTION TO HAVE GOOD EXPERIENCE 
WITH JSON FILES

DEV BY RAPIDO, ALL RIGHT RESERVED
"""

def is_file_exist(file):
    try:
        with open(file, "r"):
            return True
    except (FileNotFoundError, SyntaxError, ValueError):
        print("The file doesn't exist, Please check the file name or location")
        return False


def dict_to_json_string(data, indent=4):
    items = []
    for key, value in data.items():
        if isinstance(value, str):
            value_str = f'"{value}"'
        elif isinstance(value, dict):
            value_str = dict_to_json_string(value, indent)
        else:
            value_str = str(value)
        items.append(f'"{key}": {value_str}')
    items_str = ",\n".join(items)
    return "{\n" + " " * indent + items_str.replace("\n", "\n" + " " * indent) + "\n}"


def get_data_of_file(file):
    if is_file_exist(file):
        try:
            with open(file, "r") as open_file:
                content = open_file.read()
                data = eval(content)
                return data
        except (SyntaxError, ValueError):
            print("Error decoding JSON from the file")
            return None
    return None


def get_all_key(file):
    data = get_data_of_file(file)
    if data and "config" in data:
        list_of_data = data["config"]
        primary_keys = list(list_of_data.keys())
        return primary_keys, list_of_data
    return None, None


def get_value_of_key(file):
    primary_keys, list_of_data = get_all_key(file)
    if primary_keys and list_of_data:
        values = []
        for key in primary_keys:
            values.append(list_of_data[key])
        return values
    return None


def get_value_of_one_key(file, val):
    value = get_value_of_key(file)
    if value:
        for v in value:
            if val == v:
                print(f"'{val}' exist in the config file")
                return v
    return f"The value '{val}' doesn't exist in the config file"
        

def get_one_key(file, key):
    data = get_data_of_file(file)
    if data and "config" in data:
        one_key = list(data["config"].keys())
        if key in one_key:
            print(f"'{key}' exist in the config file")
            return key
        return f"The key '{key}' doesn't exist in the config file"


def change_value_of_key(file, key, new_val):
    data = get_data_of_file(file)
    if data and "config" in data:
        if key in data["config"]:
            data["config"][key] = new_val
            updated_content = dict_to_json_string(data)
            with open(file, "w") as open_file:
                open_file.write(updated_content)
            print(f"The value of the key '{key}' has been successfully updated by '{new_val}'.")
        else:
            print(f"The key '{key}' does not exist in the configuration file.")


