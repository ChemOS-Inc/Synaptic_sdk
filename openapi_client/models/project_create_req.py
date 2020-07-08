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


class ProjectCreateReq(object):
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
        'project_name': 'str',
        'project_description': 'str'
    }

    attribute_map = {
        'project_name': 'project_name',
        'project_description': 'project_description'
    }

    def __init__(self, project_name=None, project_description='', local_vars_configuration=None):  # noqa: E501
        """ProjectCreateReq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_name = None
        self._project_description = None
        self.discriminator = None

        self.project_name = project_name
        if project_description is not None:
            self.project_description = project_description

    @property
    def project_name(self):
        """Gets the project_name of this ProjectCreateReq.  # noqa: E501

        Name assigned to the project  # noqa: E501

        :return: The project_name of this ProjectCreateReq.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectCreateReq.

        Name assigned to the project  # noqa: E501

        :param project_name: The project_name of this ProjectCreateReq.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project_name is None:  # noqa: E501
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_name is not None and len(project_name) > 50):
            raise ValueError("Invalid value for `project_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_name is not None and len(project_name) < 1):
            raise ValueError("Invalid value for `project_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_name is not None and not re.search(r'^[ -~]+$', project_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `project_name`, must be a follow pattern or equal to `/^[ -~]+$/`")  # noqa: E501

        self._project_name = project_name

    @property
    def project_description(self):
        """Gets the project_description of this ProjectCreateReq.  # noqa: E501

        Description of the project.  # noqa: E501

        :return: The project_description of this ProjectCreateReq.  # noqa: E501
        :rtype: str
        """
        return self._project_description

    @project_description.setter
    def project_description(self, project_description):
        """Sets the project_description of this ProjectCreateReq.

        Description of the project.  # noqa: E501

        :param project_description: The project_description of this ProjectCreateReq.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                project_description is not None and len(project_description) > 255):
            raise ValueError("Invalid value for `project_description`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_description is not None and not re.search(r'^[ -~]*$', project_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `project_description`, must be a follow pattern or equal to `/^[ -~]*$/`")  # noqa: E501

        self._project_description = project_description

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
        if not isinstance(other, ProjectCreateReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCreateReq):
            return True

        return self.to_dict() != other.to_dict()
