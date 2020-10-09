def handle_action(logger, view_handler, action_config):
    brightness = action_config['value']
    logger.debug("Brightness: {}".format(brightness))
    view_handler.set_brightness(brightness)
