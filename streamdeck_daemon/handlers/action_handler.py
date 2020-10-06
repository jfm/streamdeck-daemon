from pluginbase import PluginBase


class ActionHandler(object):
    def __init__(self, logger, view_handler):
        self.logger = logger
        self.view_handler = view_handler
        plugin_base = PluginBase(package='streamdeck_daemon.plugins')
        self.plugin_source = plugin_base.make_plugin_source(searchpath=['./actions'])

    def handle_actions(self, actions):
        for action in actions:
            self.handle_action(action)

    def handle_action(self, action):
        action_plugin = self.plugin_source.load_plugin(action['plugin'])
        action_plugin.handle_action(self.logger, self.view_handler, action)
