import os

# ToDo: Need to remove this file
def read_env_file(path, env_file):
    env = {}
    section = 'default'
    file_path = os.path.join(path, f'{env_file}.properties')
    if not os.path.isfile(os.path.abspath(file_path)):
        raise FileNotFoundError("Properties file not found: Please try again.")
    with open(file_path, "rt") as file:
        for line in file.readlines():
            try:
                value: object
                key, value = line.strip().split('=', 1)

                if '.' in key:
                    key_list = key.split('.')
                    if key_list[0] in env[section]:
                        env[section][key_list[0]][key_list[1].lower()] = value
                    else:
                        env[section][key_list[0]] = {key_list[1].lower(): value}
                elif '#' not in key:
                    env[section][key] = value
            except:
                section = line.strip()[1:]
                if section.isalpha():
                    env[section] = {}
    return env

