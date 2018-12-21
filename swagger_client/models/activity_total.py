# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActivityTotal(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count': 'int',
        'distance': 'float',
        'moving_time': 'int',
        'elapsed_time': 'int',
        'elevation_gain': 'float',
        'achievement_count': 'int'
    }

    attribute_map = {
        'count': 'count',
        'distance': 'distance',
        'moving_time': 'moving_time',
        'elapsed_time': 'elapsed_time',
        'elevation_gain': 'elevation_gain',
        'achievement_count': 'achievement_count'
    }

    def __init__(self, count=None, distance=None, moving_time=None, elapsed_time=None, elevation_gain=None, achievement_count=None):  # noqa: E501
        """ActivityTotal - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._distance = None
        self._moving_time = None
        self._elapsed_time = None
        self._elevation_gain = None
        self._achievement_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if distance is not None:
            self.distance = distance
        if moving_time is not None:
            self.moving_time = moving_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if elevation_gain is not None:
            self.elevation_gain = elevation_gain
        if achievement_count is not None:
            self.achievement_count = achievement_count

    @property
    def count(self):
        """Gets the count of this ActivityTotal.  # noqa: E501

        The number of activities considered in this total.  # noqa: E501

        :return: The count of this ActivityTotal.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ActivityTotal.

        The number of activities considered in this total.  # noqa: E501

        :param count: The count of this ActivityTotal.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def distance(self):
        """Gets the distance of this ActivityTotal.  # noqa: E501

        The total distance covered by the considered activities.  # noqa: E501

        :return: The distance of this ActivityTotal.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this ActivityTotal.

        The total distance covered by the considered activities.  # noqa: E501

        :param distance: The distance of this ActivityTotal.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def moving_time(self):
        """Gets the moving_time of this ActivityTotal.  # noqa: E501

        The total moving time of the considered activities.  # noqa: E501

        :return: The moving_time of this ActivityTotal.  # noqa: E501
        :rtype: int
        """
        return self._moving_time

    @moving_time.setter
    def moving_time(self, moving_time):
        """Sets the moving_time of this ActivityTotal.

        The total moving time of the considered activities.  # noqa: E501

        :param moving_time: The moving_time of this ActivityTotal.  # noqa: E501
        :type: int
        """

        self._moving_time = moving_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this ActivityTotal.  # noqa: E501

        The total elapsed time of the considered activities.  # noqa: E501

        :return: The elapsed_time of this ActivityTotal.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this ActivityTotal.

        The total elapsed time of the considered activities.  # noqa: E501

        :param elapsed_time: The elapsed_time of this ActivityTotal.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def elevation_gain(self):
        """Gets the elevation_gain of this ActivityTotal.  # noqa: E501

        The total elevation gain of the considered activities.  # noqa: E501

        :return: The elevation_gain of this ActivityTotal.  # noqa: E501
        :rtype: float
        """
        return self._elevation_gain

    @elevation_gain.setter
    def elevation_gain(self, elevation_gain):
        """Sets the elevation_gain of this ActivityTotal.

        The total elevation gain of the considered activities.  # noqa: E501

        :param elevation_gain: The elevation_gain of this ActivityTotal.  # noqa: E501
        :type: float
        """

        self._elevation_gain = elevation_gain

    @property
    def achievement_count(self):
        """Gets the achievement_count of this ActivityTotal.  # noqa: E501

        The total number of achievements of the considered activities.  # noqa: E501

        :return: The achievement_count of this ActivityTotal.  # noqa: E501
        :rtype: int
        """
        return self._achievement_count

    @achievement_count.setter
    def achievement_count(self, achievement_count):
        """Sets the achievement_count of this ActivityTotal.

        The total number of achievements of the considered activities.  # noqa: E501

        :param achievement_count: The achievement_count of this ActivityTotal.  # noqa: E501
        :type: int
        """

        self._achievement_count = achievement_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ActivityTotal, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActivityTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
