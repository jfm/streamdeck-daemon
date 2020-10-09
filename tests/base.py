from streamdeck_daemon.config.configuration import Configuration
from streamdeck_daemon.logging.logger import Logger


class BaseTest():

    def default_setup(self, mocker):
        mocker.patch.object(Configuration, 'get_action')
        mocker.patch.object(Logger, 'debug')
        self.mock_configuration = Configuration()
        self.mock_logger = Logger(self.mock_configuration)

    def get_action_config(self, plugin, plugin_key, plugin_value):
        return {'plugin': plugin, plugin_key: plugin_value}
