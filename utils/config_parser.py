import re
from base_path import CONFIG_PATH


def get_config_list(path: str = CONFIG_PATH) -> list:
    """
    :param path: относительный путь к файлу конфигурации
    :return: список, конфигурационных настроек браузера

    приводит список конфигураций браузера к формату list,
    игнорируя пустые строки
    """
    with open(path, 'r') as f:
        config = f.readlines()
        config = ([conf.rstrip() for conf in config if re.search(r'\S', conf)])
    return config if config else []


if __name__ == "__main__":
    print(get_config_list())
