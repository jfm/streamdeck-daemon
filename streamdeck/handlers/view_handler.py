from streamdeck.handlers.key_handler import KeyHandler


class ViewHandler(object):
    def __init__(self, configuration, logger, streamdeck, ui_handler):
        self.ui_handler = ui_handler
        self.configuration = configuration
        self.logger = logger
        self.streamdeck = streamdeck

    def render_page(self, page_name):
        self.streamdeck.reset()
        self.ui_handler.render_page(self.streamdeck, page_name)
        key_handler = KeyHandler(self.configuration, self.logger, self)
        key_handler.set_page_name(page_name)
        self.streamdeck.set_key_callback(key_handler.handle_key)

    def set_brightness(self, brightness):
        self.streamdeck.set_brightness(brightness)
