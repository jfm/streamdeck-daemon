from streamdeck_daemon.handlers.action_handler import ActionHandler
from streamdeck_daemon.handlers.ui_handler import UIHandler


class KeyHandler(object):
    def __init__(self, config, logger, view_handler):
        self.config = config
        self.logger = logger
        self.view_handler = view_handler
        self.action_handler = ActionHandler(logger, view_handler)
        self.ui_handler = UIHandler(config, logger)

    def set_page_name(self, page_name):
        self.page_name = page_name

    def handle_key(self, streamdeck, key, state):
        if state is True:
            self.handle_key_pressed(key)
        else:
            self.handle_key_released(key)

    def handle_key_pressed(self, key):
        pass

    def handle_key_released(self, key):
        pages_config = self.config.get_pages()
        page_config = self.config.get_page(pages_config, self.page_name)
        keys_config = self.config.get_keys(page_config)
        key_config = self.config.get_key(keys_config, key)
        actions_config = self.config.get_actions(key_config)
        self.action_handler.handle_actions(actions_config)
        if key_config['type'] == 'toggle':
            self.ui_handler.toggle_key(self.view_handler.streamdeck, key)
