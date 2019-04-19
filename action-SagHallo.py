#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.publish as publish
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

SITE = "default"

def subscribe_intent_callback(hermes, intentMessage):
    conf = None
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    SITE = "default"
    SOUNDFILE = "./Herzlich_willkommen.wav"
    binaryFile = open(SOUNDFILE, mode='rb')
    wav = bytearray(binaryFile.read())
    result_sentence = "Herzlich Willkommen nach Hause Sir. Ich stehe zu Deinen Dienste."
    current_session_id = intentMessage.session_id
    publish.single("hermes/audioServer/{}/playBytes/whateverId".format(SITE),payload=wav, hostname="localhost", client_id="")
    #hermes.publish_end_session(current_session_id, result_sentence)
    
def intent_callback_Tschuess(hermes, intentMessage):
    result_sentence = "Auf Wiedersehen Sir. Ich stehe zu Deine Dienste."
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)    


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("studger:SagHallo", subscribe_intent_callback)
        h.subscribe_intent("studger:SagTschuess", intent_callback_Tschuess)
        h.start()
