def handle_action(logger, view_handler, action_config):
    logger.debug("Changing Page to: {}".format(action_config['page']))
    view_handler.render_page(action_config['page'])
