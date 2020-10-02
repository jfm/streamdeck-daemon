import yaml


class Configuration(object):
    def __init__(self):
        with open("Streamdeck.yaml") as config_file:
            self.config = yaml.load(config_file, Loader=yaml.FullLoader)

    def get_pages(self):
        return self.config['streamdeck']['pages']

    def get_page(self, pages, page_index):
        return pages[page_index]

    def get_keys(self, page):
        return page['keys']

    def get_key(self, keys, key_index):
        for key in keys:
            if key['index'] == key_index:
                return key

    def get_actions(self, key):
        return key['actions']

    def get_action(self, actions, action_index):
        return actions[action_index]
