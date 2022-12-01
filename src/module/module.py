"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from kafka import KafkaConsumer
from json import loads
from os import getenv

log = getLogger("module")

def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    try:
        consumer = KafkaConsumer(
            topics=getenv("TOPIC"),
            bootstrap_servers=[server.strip() for server in getenv("BOOTSTRAP_SERVERS").split(',')],
            client_id=getenv("CLIENT_ID"),
            group_id=getenv("GROUP_ID"),
            auto_offset_reset=getenv("AUTO_OFFSET_RESET"), # 'earliest' or 'latest'
            enable_auto_commit=bool(getenv("ENABLE_AUTO_COMMIT")),
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

        for message in consumer:
            log.debug(f"Input data: {message.value}")

            # send data to the next module
            send_error = send_data(message.value)

            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent successfully.")

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
