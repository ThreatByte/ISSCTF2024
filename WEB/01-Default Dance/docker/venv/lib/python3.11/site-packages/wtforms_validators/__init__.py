from wtforms.validators import ValidationError, URL, Regexp, Email
import re
from dns.resolver import query
import json
from abc import ABC, abstractmethod
from is_disposable_email import check

__all__ = [
    'Accepted',
    'ActiveUrl',
    'AbstractText',
    'Alpha',
    'AlphaDash',
    'AlphaSpace',
    'AlphaNumeric',
    'NotEqualTo',
    'Integer',
    'IsJson',
    'DisposableEmail'
]


class Accepted:
    """
    Validates if the field is either yes, on, 1, true or True.

    :param message:
        Error message to raise in case of a validation error.
    """

    def __init__(self, message=None):
        self.message = message
        self.values = ['yes', 'on', '1', 'true', True]

    def __call__(self, form, field):
        if field.data not in self.values:
            message = self.message
            if message is None:
                message = field.gettext("This field must be accepted.")

            raise ValidationError(message)


class ActiveUrl:
    """
    Validates if the url is active by checking A or AAAA dns records.

    :param message:
        Error message to raise in case of a validation error.
    """
    def __init__(self, message=None):
        self.message = message
        self.__is_url = URL()

        regex = r"^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$"
        self.__reg_test = Regexp(regex, re.IGNORECASE, message)

    def __call__(self, form, field):
        self.__is_url(form, field)
        match = self.__reg_test(form, field)

        message = self.message
        if message is None:
            message = field.gettext("URL does not exist.")

        result = False
        try:
            query(match.group("host"), 'A')[0].to_text()
            result = True
        except Exception:
            pass

        try:
            query(match.group("host"), 'AAAA')[0].to_text()
            result = True
        except Exception:
            pass

        if not result:
            raise ValidationError(message)


class AbstractText(ABC):
    """
    Abstract Class to match a regex pattern on strings.
    """

    def __init__(self, message=None):
        self.custom_message = message
        self._regex = Regexp(self.pattern, message=message)

    @property
    @abstractmethod
    def pattern(self):
        """
        Regex Pattern
        """
        pass

    @property
    @abstractmethod
    def message(self):
        """
        Default Error Message
        """
        return "Invalid Text"

    def __call__(self, form, field):
        if self.custom_message is None:
            message = self.message
        else:
            message = self.custom_message

        self._regex(form, field, field.gettext(message))


class Alpha(AbstractText):
    """
    The field under validation must be entirely alphabets.

    :param message:
        Error message to raise in case of a validation error.
    """

    @property
    def pattern(self):
        return r"^[a-zA-Z]+$"

    @property
    def message(self):
        return "Must only contain alphabets."


class AlphaDash(AbstractText):
    """
    The field under validation must be of alphabets with dash(-).

    :param message:
        Error message to raise in case of a validation error.
    """

    @property
    def pattern(self):
        return r"^[a-zA-Z-]+$"

    @property
    def message(self):
        return "Must only contain alphabets and dashes."


class AlphaSpace(AbstractText):
    """
    The field under validation must be of alphabets with spaces.

    :param message:
        Error message to raise in case of a validation error.
    """

    @property
    def pattern(self):
        return r"^[a-zA-Z\s]+$"

    @property
    def message(self):
        return "Must only contain alphabets and dashes."


class AlphaNumeric(AbstractText):
    """
    The field under validation can be of alphabets with integers.

    :param message:
        Error message to raise in case of a validation error.
    """

    @property
    def pattern(self):
        return r"^[a-zA-Z0-9]+$"

    @property
    def message(self):
        return "Must only contain alphabets and Numbers."


class NotEqualTo:
    """
    Validates if the values of two fields are not equal.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """

    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(
                field.gettext("Invalid field name '%s'.") % self.fieldname
            )
        if field.data == other.data:
            d = {
                "other_label": hasattr(other, "label")
                and other.label.text
                or self.fieldname,
                "other_name": self.fieldname,
            }
            message = self.message
            if message is None:
                message = field.gettext("Field must not be equal \
                to %(other_name)s.")

            raise ValidationError(message % d)


class Integer(AbstractText):
    """
    Validates if the given field is integer.

    :param message:
        Error message to raise in case of a validation error.
    """

    @property
    def pattern(self):
        return r"^[0-9]+$"

    @property
    def message(self):
        return "Should only contain numbers."


class IsJson:
    """
    The field under validation must be a json string.

    :param message:
        Error message to raise in case of a validation error.
    """

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        message = self.message
        if message is None:
            message = field.gettext("Not a valid json")

        try:
            json.loads(field.data)
        except Exception:
            raise ValidationError(message)


class DisposableEmail(Email):
    """
    Validates if the email address is not offered by
    disposable email service provider.
    By design, this validator also validates if the given
    email address is a valid ones.

    :param message:
        Error message to raise if the email address is a disposable ones.

    :param invalid_message:
        Error message to raise if the email address is invalid.
    """
    def __init__(self, message=None, invalid_message=None):
        super().__init__(message=invalid_message)
        self.d_message = message

    def __call__(self, form, field):
        super().__call__(form, field)

        message = self.d_message
        if message is None:
            message = field.gettext("Invalid Email Address.")

        if check(field.data):
            raise ValidationError(message)
