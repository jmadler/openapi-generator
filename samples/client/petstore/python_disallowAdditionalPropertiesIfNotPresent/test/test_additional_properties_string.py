# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
from petstore_api.model.additional_properties_string import AdditionalPropertiesString


class TestAdditionalPropertiesString(unittest.TestCase):
    """AdditionalPropertiesString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdditionalPropertiesString(self):
        """Test AdditionalPropertiesString"""
        # can make model without additional properties
        model = AdditionalPropertiesString()

        # can make one with additional properties
        model = AdditionalPropertiesString(some_key='some_val')
        assert model['some_key'] == 'some_val'

        # type checking works on additional properties
        with self.assertRaises(petstore_api.ApiTypeError) as exc:
            model = AdditionalPropertiesString(some_key=True)


if __name__ == '__main__':
    unittest.main()