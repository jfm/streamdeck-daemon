from pyautogui import hotkey


def handle_action(logger, streamdeck, action_config):
    shortcut = action_config['shortcut']
    logger.debug("Shortcut: {}".format(shortcut))
    shortcut_params = shortcut.split('+')
    hotkey(*shortcut_params)
