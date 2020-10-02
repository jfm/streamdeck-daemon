#!/home/jfm/.local/share/virtualenvs/streamdeck-daemon-2GNwbxCc/bin/python
import sys
import time
import threading
from StreamDeck.DeviceManager import DeviceManager
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
                key_handler = KeyHandler(configuration, logger, streamdeck)
                ui_handler = UIHandler(configuration, logger)

                streamdeck.open()
                streamdeck.reset()

                logger.info("StreamDeck {} - {}".format(index, streamdeck.deck_type()))

                streamdeck.set_brightness(configuration.config['streamdeck']['brightness'])
                ui_handler.initialize_keys(streamdeck)
                streamdeck.set_key_callback(key_handler.handle_key)

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
