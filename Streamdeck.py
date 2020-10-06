#!/home/jfm/.local/share/virtualenvs/streamdeck-daemon-2GNwbxCc/bin/python
import sys
import time
import threading
from StreamDeck.DeviceManager import DeviceManager
from streamdeck.handlers.view_handler import ViewHandler
from streamdeck.handlers.key_handler import KeyHandler
from streamdeck.handlers.ui_handler import UIHandler
from streamdeck.config.configuration import Configuration
from streamdeck.logging.logger import Logger


def run_streamdeck():
    configuration = Configuration()
    logger = Logger(configuration)

    while True:
        try:
            try:
                streamdecks = DeviceManager().enumerate()
            except DeviceManager.ProbeError:
                logger.error("No connected devices found")

            for index, streamdeck in enumerate(streamdecks):
                initial_page = configuration.config['streamdeck']['initial_page']
                ui_handler = UIHandler(configuration, logger)
                view_handler = ViewHandler(configuration, logger, streamdeck, ui_handler)

                streamdeck.open()
                streamdeck.reset()

                logger.info("StreamDeck {} - {}".format(index, streamdeck.deck_type()))

                streamdeck.set_brightness(configuration.config['streamdeck']['brightness'])

                view_handler.render_page(initial_page)

                for t in threading.enumerate():
                    if t is threading.currentThread():
                        continue

                    if t.is_alive():
                        t.join()

        except KeyboardInterrupt:
            logger.info("Closing StreamDeck daemon")
            streamdeck.reset()
            streamdeck.close()
            sys.exit()

        logger.debug("StreamDeck disconnected... Waiting for reconnection")
        time.sleep(3)


if __name__ == "__main__":
    run_streamdeck()
