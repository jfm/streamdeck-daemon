from streamdeck_daemon.handlers.view_handler import ViewHandler
from streamdeck_daemon.handlers.ui_handler import UIHandler

from tests.base import BaseTest


class TestViewHandler(BaseTest):
    def test_render_page(self, mocker):
        self.default_setup(mocker)
        self.build_mock_streamdeck(mocker)

        mocker.patch.object(UIHandler, 'render_page')
        mock_ui_handler = UIHandler(self.mock_logger, self.mock_configuration)

        view_handler = ViewHandler(self.mock_configuration, self.mock_logger, self.mock_streamdeck, mock_ui_handler)

        view_handler.render_page('testpage')

        mock_ui_handler.render_page.assert_called_once()
        self.mock_streamdeck.reset.assert_called_once()
        self.mock_streamdeck.set_key_callback.assert_called_once()

    def test_set_brightness(self, mocker):
        self.default_setup(mocker)
        self.build_mock_streamdeck(mocker)

        mocker.patch.object(UIHandler, 'render_page')
        mock_ui_handler = UIHandler(self.mock_logger, self.mock_configuration)

        view_handler = ViewHandler(self.mock_configuration, self.mock_logger, self.mock_streamdeck, mock_ui_handler)

        view_handler.set_brightness(5)

        self.mock_streamdeck.set_brightness.assert_called_once()
