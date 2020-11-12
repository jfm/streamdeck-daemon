import os
from phue import Bridge


def handle_action(logger, view_handler, action_config):
    config_path = view_handler.configuration.config_path
    key_file = os.path.join(config_path, "python_hue.key")
#    bridge = Bridge('10.0.0.72', config_file_path=key_file)
    bridge = Bridge('10.0.0.72')
    bridge.connect()
    bridge.run_scene(action_config['group'], action_config['scene'])
