from streamdeck_daemon.plugins.brightness import handle_action as brightness_action
from streamdeck_daemon.plugins.shortcut import handle_action as shortcut_action
from streamdeck_daemon.handlers.view_handler import ViewHandler
from tests.base import BaseTest
import pyautogui


class TestDefaultActions(BaseTest):

    def test_brightness_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch.object(ViewHandler, 'set_brightness')
        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        action_config = self.get_action_config('brightness', 'brightness', '1')

        brightness_action(self.mock_logger, mock_view_handler, action_config)

        mock_view_handler.set_brightness.assert_called_once_with('1')

    def test_shortcut_action(self, mocker):
        self.default_setup(mocker)

        mocker.patch('pyautogui.hotkey')

        action_config = self.get_action_config('shortcut', 'shortcut', 'shift+t')

        shortcut_action(self.mock_logger, None, action_config)

        assert pyautogui.hotkey.called_once_with('shift+t')
