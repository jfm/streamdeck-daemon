import os


def handle_action(logger, view_handler, action_config):
    logger.debug("Launching: {}".format(action_config['application']))
    os.system("gtk-launch {}".format(action_config['application']))
