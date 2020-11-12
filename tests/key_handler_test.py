from streamdeck_daemon.handlers.view_handler import ViewHandler
from streamdeck_daemon.handlers.key_handler import KeyHandler
from streamdeck_daemon.handlers.action_handler import ActionHandler
from streamdeck_daemon.handlers.ui_handler import UIHandler
from tests.base import BaseTest


class TestKeyHandler(BaseTest):
    def test_set_page_name(self, mocker):
        self.default_setup(mocker)

        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        key_handler = KeyHandler(self.mock_configuration, self.mock_logger, mock_view_handler)

        key_handler.set_page_name('testpage')

        assert key_handler.page_name == 'testpage'

    def test_handle_key(self, mocker):
        self.default_setup(mocker)

        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        mocker.patch.object(KeyHandler, 'handle_key_pressed')
        mocker.patch.object(KeyHandler, 'handle_key_released')
        key_handler = KeyHandler(self.mock_configuration, self.mock_logger, mock_view_handler)

        key_handler.handle_key(None, 0, True)
        key_handler.handle_key_pressed.assert_called_once_with(0)

        key_handler.handle_key(None, 1, False)
        key_handler.handle_key_released.assert_called_once_with(1)

    def test_handle_key_pressed(self, mocker):
        pass

    def test_handle_key_released_button_type(self, mocker):
        key_config = self.get_key_config(0, 'button', 'TEST', 'TEST')
        self.default_setup(mocker, key_config=key_config)

        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        mocker.patch.object(ActionHandler, 'handle_actions')
        mock_action_handler = ActionHandler(self.mock_logger, mock_view_handler)
        mocker.patch.object(UIHandler, 'toggle_key')

        key_handler = KeyHandler(self.mock_configuration, self.mock_logger, mock_view_handler)
        key_handler.action_handler = mock_action_handler
        key_handler.set_page_name('testpage')

        key_handler.handle_key_released(0)

        mock_action_handler.handle_actions.assert_called_once()

    def test_handle_key_released_toggle_type(self, mocker):
        key_config = self.get_key_config(0, 'toggle', 'TEST', 'TEST')
        self.default_setup(mocker, key_config=key_config)

        mock_view_handler = ViewHandler(self.mock_configuration, self.mock_logger, None, None)

        mocker.patch.object(ActionHandler, 'handle_actions')
        mock_action_handler = ActionHandler(self.mock_logger, mock_view_handler)
        mocker.patch.object(UIHandler, 'toggle_key')
        mock_ui_handler = UIHandler(self.mock_logger, self.mock_configuration)

        key_handler = KeyHandler(self.mock_configuration, self.mock_logger, mock_view_handler)
        key_handler.action_handler = mock_action_handler
        key_handler.set_page_name('testpage')

        key_handler.handle_key_released(0)

        mock_action_handler.handle_actions.assert_called_once()
        mock_ui_handler.toggle_key.assert_called_once()
