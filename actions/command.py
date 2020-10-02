import os


def handle_action(logger, streamdeck, action_config):
    command = action_config['command']
    logger.debug("Executing: {}".format(command))
    os.system(command)
