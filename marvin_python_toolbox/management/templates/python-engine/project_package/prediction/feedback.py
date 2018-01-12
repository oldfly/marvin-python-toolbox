#!/usr/bin/env python
# coding=utf-8

"""Feedback engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBasePrediction

__all__ = ['Feedback']


logger = get_logger('feedback')


class Feedback(EngineBasePrediction):

    def __init__(self, **kwargs):
        super(Feedback, self).__init__(**kwargs)

    def execute(self, input_message, **kwargs):
        """
        Receive feedback message, user can manipulate this message for any use.
        Return "Done" to signal that the message is received and processed.
        """
        return {"message": "Done"}
