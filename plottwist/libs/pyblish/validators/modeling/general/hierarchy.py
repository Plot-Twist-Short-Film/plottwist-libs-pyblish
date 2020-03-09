#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Plot Twist hierarchy validator implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import pyblish.api


class ValidatePlotTwistHierarchy(pyblish.api.InstancePlugin):
    """
    Checks if a geometry node has clean history
    """

    label = 'General - Check Hierarchy'
    order = pyblish.api.ValidatorOrder
    hosts = ['maya']
    families = ['geometry']
    optional = False

    def process(self, context, plugin):
        print('GOGOGOGOGOGOGOGO')
