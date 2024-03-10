from json import loads
from logging import info
from typing import Any

from django.conf import settings
from paho.mqtt.client import Client as MQTTClient
from paho.mqtt.client import ConnectFlags, MQTTMessage
from paho.mqtt.enums import CallbackAPIVersion
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCode

from .normaliser.map import NORMALISER_MAPPING
from .schemas import Message

BROKER_URL = settings.MQTT_BROKER_HOST
TOPIC = settings.MQTT_CENTRAL_TOPIC


def on_connect(
    client: MQTTClient,
    userdata: Any,
    flags: ConnectFlags,
    rc: ReasonCode,
    properties: Properties | None,
) -> None:
    info("Connect to MQTT broker with result code %s" % str(rc))
    client.subscribe(TOPIC)
    info("Django is connected to the topic %s" % TOPIC)


def on_message(client: MQTTClient, userdata: Any, message: MQTTMessage) -> None:
    payload = loads(message.payload.decode("utf-8"))
    validated_message = Message(
        message_type=payload["message_type"],
        device_id=payload["device_id"],
        value=payload.get("value", None),
    )

    normaliser = NORMALISER_MAPPING[validated_message.message_type](
        validated_message.device_id
    )
    normaliser.process(message)


client = MQTTClient(CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_URL, 1883, 60)
