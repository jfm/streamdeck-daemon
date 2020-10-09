from pyautogui import hotkey


def handle_action(logger, view_handler, action_config):
    shortcut = action_config['shortcut']
    logger.debug("Shortcut: {}".format(shortcut))
    shortcut_params = shortcut.split('+')
    hotkey(*shortcut_params)
