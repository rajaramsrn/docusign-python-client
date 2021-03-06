# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BillingInvoicesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billing_invoices=None, next_uri=None, previous_uri=None):
        """
        BillingInvoicesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'billing_invoices': 'list[BillingInvoice]',
            'next_uri': 'str',
            'previous_uri': 'str'
        }

        self.attribute_map = {
            'billing_invoices': 'billingInvoices',
            'next_uri': 'nextUri',
            'previous_uri': 'previousUri'
        }

        self._billing_invoices = billing_invoices
        self._next_uri = next_uri
        self._previous_uri = previous_uri

    @property
    def billing_invoices(self):
        """
        Gets the billing_invoices of this BillingInvoicesResponse.
        Reserved: TBD

        :return: The billing_invoices of this BillingInvoicesResponse.
        :rtype: list[BillingInvoice]
        """
        return self._billing_invoices

    @billing_invoices.setter
    def billing_invoices(self, billing_invoices):
        """
        Sets the billing_invoices of this BillingInvoicesResponse.
        Reserved: TBD

        :param billing_invoices: The billing_invoices of this BillingInvoicesResponse.
        :type: list[BillingInvoice]
        """

        self._billing_invoices = billing_invoices

    @property
    def next_uri(self):
        """
        Gets the next_uri of this BillingInvoicesResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :return: The next_uri of this BillingInvoicesResponse.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this BillingInvoicesResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :param next_uri: The next_uri of this BillingInvoicesResponse.
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this BillingInvoicesResponse.
        The postal code for the billing address.

        :return: The previous_uri of this BillingInvoicesResponse.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this BillingInvoicesResponse.
        The postal code for the billing address.

        :param previous_uri: The previous_uri of this BillingInvoicesResponse.
        :type: str
        """

        self._previous_uri = previous_uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
