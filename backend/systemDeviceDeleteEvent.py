#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.event import Event

class SystemDeviceDeleteEvent(Event):
    """
    System.device.delete event
    """

    EVENT_NAME = u'system.device.delete'
    EVENT_SYSTEM = True
    EVENT_PARAMS = []

    def __init__(self, bus, formatters_broker, events_broker):
        """ 
        Constructor

        Args:
            bus (MessageBus): message bus instance
            formatters_broker (FormattersBroker): formatters broker instance
            events_broker (EventsBroker): events broker instance
        """
        Event.__init__(self, bus, formatters_broker, events_broker)
