import yaml
from xdg import XDG_CONFIG_HOME
from os import path


class Configuration(object):
    def __init__(self):
        config_path = str(XDG_CONFIG_HOME) + "/streamdeck-daemon/streamdeck.yaml"
        if path.exists(config_path):
            with open(config_path) as config_file:
                self.config = yaml.load(config_file, Loader=yaml.FullLoader)
        else:
            with open("streamdeck.yaml") as config_file:
                self.config = yaml.load(config_file, Loader=yaml.FullLoader)
 
    def get_pages(self):
        return self.config['streamdeck']['pages']

    def get_page(self, pages, page_index):
        for page in pages:
            if page['name'] == page_index:
                return page

    def get_keys(self, page):
        return page['keys']

    def get_key(self, keys, key_index):
        for key in keys:
            if key['index'] == key_index:
                return key

    def get_actions(self, key):
        if key is not None:
            return key['actions']
        else:
            return None

    def get_action(self, actions, action_index):
        return actions[action_index]
