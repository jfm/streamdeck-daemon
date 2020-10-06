import os


def handle_action(logger, view_handler, action_config):
    command = action_config['command']
    logger.debug("Executing: {}".format(command))
    os.system(command)
