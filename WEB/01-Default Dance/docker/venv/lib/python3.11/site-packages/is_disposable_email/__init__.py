from ._domains import domains as domain_list

__all__ = ['domain_list', 'check']


def check(email_address):
    """
    Check if the given email address belongs to a disaposable email service
    provider.

    :returns: boolean
    """
    data = email_address.split('@')
    result = False
    if data[1] in domain_list:
        result = True

    return result
