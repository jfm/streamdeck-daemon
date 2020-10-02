def handle_action(logger, streamdeck, action_config):
    brightness = action_config['value']
    logger.debug("Brightness: {}".format(brightness))
    streamdeck.set_brightness(brightness)
