from streamdeck_daemon.plugins.brightness import handle_action as brightness_action
from streamdeck_daemon.plugins.command import handle_action as command_action
from streamdeck_daemon.plugins.launch import handle_action as launch_action
from streamdeck_daemon.plugins.page import handle_action as page_action
from streamdeck_daemon.handlers.view_handler import ViewHandler
from tests.base import BaseTest
import os


class TestDefaultActions(BaseTest):

    def test_brightness_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch.object(ViewHandler, 'set_brightness')
        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        action_config = self.get_action_config('brightness', 'brightness', '1')

        brightness_action(self.mock_logger, mock_view_handler, action_config)

        mock_view_handler.set_brightness.assert_called_once_with('1')

    def test_command_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch('os.system')

        action_config = self.get_action_config('command', 'command', 'ls')

        command_action(self.mock_logger, None, action_config)

        assert os.system.called_once_with('ls')

    def test_launch_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch('os.system')

        action_config = self.get_action_config('launch', 'application', 'twitter')

        launch_action(self.mock_logger, None, action_config)

        assert os.system.called_once_with('gtk-launch twitter')

    def test_page_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch.object(ViewHandler, 'render_page')
        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        action_config = self.get_action_config('page', 'page', 'testpage')

        page_action(self.mock_logger, mock_view_handler, action_config)

        mock_view_handler.render_page.assert_called_once_with('testpage')
