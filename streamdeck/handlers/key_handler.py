from streamdeck.handlers.action_handler import ActionHandler
from streamdeck.handlers.ui_handler import UIHandler


class KeyHandler(object):
    def __init__(self, config, logger, streamdeck):
        self.config = config
        self.logger = logger
        self.streamdeck = streamdeck
        self.action_handler = ActionHandler(logger, streamdeck)
        self.ui_handler = UIHandler(config, logger)

    def handle_key(self, streamdeck, key, state):
        if state is True:
            self.handle_key_pressed(key)
        else:
            self.handle_key_released(key)

    def handle_key_pressed(self, key):
        pass

    def handle_key_released(self, key):
        pages_config = self.config.get_pages()
        page_config = self.config.get_page(pages_config, 0)
        keys_config = self.config.get_keys(page_config)
        key_config = self.config.get_key(keys_config, key)
        actions_config = self.config.get_actions(key_config)
        self.action_handler.handle_actions(actions_config)
        if key_config['type'] == 'toggle':
            self.ui_handler.toggle_key(self.streamdeck, key)
