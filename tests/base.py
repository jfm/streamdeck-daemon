from streamdeck_daemon.config.configuration import Configuration
from streamdeck_daemon.logging.logger import Logger


class BaseTest():

    def default_setup(self, mocker, **kwargs):
        mocker.patch.object(Configuration, 'get_pages')
        if 'page_config' in kwargs:
            mocker.patch.object(Configuration, 'get_page', return_value=kwargs.get('page_config'))
        else:
            mocker.patch.object(Configuration, 'get_page')

        if 'keys_config' in kwargs:
            mocker.patch.object(Configuration, 'get_keys', return_value=kwargs.get('keys_config'))
        else:
            mocker.patch.object(Configuration, 'get_keys')

        if 'key_config' in kwargs:
            mocker.patch.object(Configuration, 'get_key', return_value=kwargs.get('key_config'))
        else:
            mocker.patch.object(Configuration, 'get_key')

        if 'actions_config' in kwargs:
            mocker.patch.object(Configuration, 'get_actions', return_value=kwargs.get('actions_config'))
        else:
            mocker.patch.object(Configuration, 'get_actions')
        mocker.patch.object(Logger, 'debug')
        self.mock_configuration = Configuration()
        self.mock_logger = Logger(self.mock_configuration)

    def get_action_config(self, plugin, plugin_key, plugin_value):
        return {'plugin': plugin, plugin_key: plugin_value}

    def get_key_config(self, index, key_type, text, icon):
        return {'index': index, 'type': key_type, 'text': text, 'icon': icon}
