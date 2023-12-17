"""Support for EZVIZ camera."""
import logging

from pyezviz.client import EzvizClient
from pyezviz.mqtt import MQTTClient
from pyezviz.exceptions import (
    EzvizAuthTokenExpired,
    EzvizAuthVerificationCode,
    HTTPError,
    InvalidURL,
    PyEzvizError,
)
from typing import Any
import json
import paho.mqtt.client as mqtt

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

ezviz_client = EzvizClient(account="xxxxxx", password="xxxxxxx")

try:
    token = ezviz_client.login()

except (EzvizAuthTokenExpired, EzvizAuthVerificationCode) as error:
    logging.CRITICAL({error})

except (InvalidURL, HTTPError, PyEzvizError) as error:
    logging.CRITICAL({error})



mymqtt = mqtt.Client()
mymqtt.connect(host="192.168.1.15")


class MQTTClientCustom(MQTTClient):

    pass

    def on_message(self, client: Any, userdata: Any, msg: Any) -> None:
        """On MQTT message receive."""
        # pylint: disable=unused-argument
        try:
            mqtt_message = json.loads(msg.payload)

        except ValueError as err:
            self.stop()
            raise PyEzvizError(
                "Impossible to decode mqtt message: " + str(err)
            ) from err

        mqtt_message["ext"] = mqtt_message["ext"].split(",")

        # Format payload message and keep latest device message.
        self.rcv_message[mqtt_message["ext"][2]] = {
            "id": mqtt_message["id"],
            "alert": mqtt_message["alert"],
            "time": mqtt_message["ext"][1],
            "alert type": mqtt_message["ext"][4],
            "image": mqtt_message["ext"][16] if len(mqtt_message["ext"]) > 16 else None,
        }

        msg2publish = json.dumps(self.rcv_message)

        mymqtt.publish(topic="ezviz/mensaje",payload=msg2publish)

        logging.error(self.rcv_message, exc_info=True)

mqtt = MQTTClientCustom(token)
mqtt.start()
