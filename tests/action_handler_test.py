from streamdeck_daemon.handlers.action_handler import ActionHandler
from tests.base import BaseTest


class TestActionHandler(BaseTest):

    def test_handle_actions(self, mocker):
        self.default_setup(mocker)
        self.build_mock_viewhandler(mocker)

        mocker.patch.object(ActionHandler, 'handle_action')

        action_handler = ActionHandler(self.mock_logger, self.mock_view_handler)

        action_handler.handle_actions(self.get_actions_config())

        assert action_handler.handle_action.call_count == 2
