# coding: utf-8

"""
    ChemOS Web Portal

    API entry point for ChemOS Web Portal. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Web Portal account. You can generate your `API KEY` on your [account information page](https://scientia.chemos.io/user).  # noqa: E501

    The version of the OpenAPI document: beta
    Contact: support@chemos.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ListFilesResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'request_id': 'str',
        'result': 'Result',
        'objects': 'list[ListFilesResponseObjects]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'result': 'result',
        'objects': 'objects'
    }

    def __init__(self, request_id=None, result=None, objects=None, local_vars_configuration=None):  # noqa: E501
        """ListFilesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_id = None
        self._result = None
        self._objects = None
        self.discriminator = None

        self.request_id = request_id
        self.result = result
        self.objects = objects

    @property
    def request_id(self):
        """Gets the request_id of this ListFilesResponse.  # noqa: E501

        Request Id.  # noqa: E501

        :return: The request_id of this ListFilesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListFilesResponse.

        Request Id.  # noqa: E501

        :param request_id: The request_id of this ListFilesResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and len(request_id) > 36):
            raise ValueError("Invalid value for `request_id`, length must be less than or equal to `36`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and len(request_id) < 36):
            raise ValueError("Invalid value for `request_id`, length must be greater than or equal to `36`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and not re.search(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$', request_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `request_id`, must be a follow pattern or equal to `/^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$/`")  # noqa: E501

        self._request_id = request_id

    @property
    def result(self):
        """Gets the result of this ListFilesResponse.  # noqa: E501


        :return: The result of this ListFilesResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListFilesResponse.


        :param result: The result of this ListFilesResponse.  # noqa: E501
        :type: Result
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def objects(self):
        """Gets the objects of this ListFilesResponse.  # noqa: E501


        :return: The objects of this ListFilesResponse.  # noqa: E501
        :rtype: list[ListFilesResponseObjects]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this ListFilesResponse.


        :param objects: The objects of this ListFilesResponse.  # noqa: E501
        :type: list[ListFilesResponseObjects]
        """
        if self.local_vars_configuration.client_side_validation and objects is None:  # noqa: E501
            raise ValueError("Invalid value for `objects`, must not be `None`")  # noqa: E501

        self._objects = objects

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFilesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListFilesResponse):
            return True

        return self.to_dict() != other.to_dict()
