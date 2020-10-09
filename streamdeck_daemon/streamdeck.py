import sys
import time
import threading
from StreamDeck.DeviceManager import DeviceManager
from streamdeck_daemon.handlers.view_handler import ViewHandler
from streamdeck_daemon.handlers.ui_handler import UIHandler
from streamdeck_daemon.config.configuration import Configuration
from streamdeck_daemon.logging.logger import Logger


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
            streamdeck.set_brightness(5)
            streamdeck.close()
            sys.exit()

        logger.debug("StreamDeck disconnected... Waiting for reconnection")
        time.sleep(3)
