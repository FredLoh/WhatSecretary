from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = []