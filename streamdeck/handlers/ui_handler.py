from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper


class UIHandler(object):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.toggle_map = {}

    def render_page(self, streamdeck, page_name):
        pages_config = self.config.get_pages()
        page_config = self.config.get_page(pages_config, page_name)
        for key_config in self.config.get_keys(page_config):
            index = key_config['index']
            text = key_config['text']
            icon = key_config['icon']
            self.render_key_image(streamdeck, page_name, index, icon, text)

    def render_key_image(self, streamdeck, page_name, key_number, icon_path, text):
        pages_config = self.config.get_pages()
        page_config = self.config.get_page(pages_config, page_name)
        icon = Image.open(icon_path)
        image = PILHelper.create_scaled_image(streamdeck, icon, margins=[0, 0, 20, 0])
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(page_config['font'], page_config['font-size'])
        label_w, label_h = draw.textsize(text, font=font)
        label_pos = ((image.width - label_w) // 2, image.height - 20)
        draw.text(label_pos, text=text, font=font, fill="white")
        rendered_image = PILHelper.to_native_format(streamdeck, image)
        with streamdeck:
            streamdeck.set_key_image(key_number, rendered_image)

    def toggle_key(self, streamdeck, index):
        pages = self.config.get_pages()
        page = self.config.get_page(pages, 0)
        keys = self.config.get_keys(page)
        key = self.config.get_key(keys, index)

        if index not in self.toggle_map.keys():
            self.toggle_map[index] = False

        if self.toggle_map[index] is False:
            self.toggle_map[index] = True
            self.render_key_image(streamdeck, index, key['toggled_icon'], key['toggled_text'])
        else:
            self.toggle_map[index] = False
            self.render_key_image(streamdeck, index, key['icon'], key['text'])
