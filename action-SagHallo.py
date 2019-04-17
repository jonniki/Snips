#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io


def subscribe_intent_callback(hermes, intentMessage):
    conf = None
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    result_sentence = "Herzlich Willkommen nach Hause, mein Herr Eugen. Ich stehe zu Deinen Dienste."
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)
    
def intent_callback_Tschuess(hermes, intentMessage, conf):
    result_sentence = "Auf Wiedersehen, mein Sir. Ich stehe zu Deine Dienste."
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)    


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("studger:SagHallo", subscribe_intent_callback)
        h.subscribe_intent("studger:SagTschuess", intent_callback_Tschuess)
        h.start()
