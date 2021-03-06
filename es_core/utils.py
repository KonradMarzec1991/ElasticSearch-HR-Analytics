"""
Helper functions for filters and aggregations
"""

from django.conf import settings
from es_core.es_search import get_client


allowed = ['Age', 'Designation', 'Gender', 'MaritalStatus', 'Salary']


def execute_query(func):
    """
    Basic decorator for executing query
    :param func: search instance
    :return: dict results
    """
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute().hits.hits
    return wrapper


def execute_aggs(func):
    """
    Basic decorator for executing aggregation
    :param func: search instance
    :return: dict results
    """
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute()['aggregations']
    return wrapper


def check_term_field(func):
    """
    Decorator checks if function arg is in allowed list
    :param func: decorated function
    :return: raise Exception if arg is invalid else returns function
    """
    def wrapper(arg):
        """Decorator wrapper"""
        if arg not in allowed:
            raise ArgumentException
        return func(arg)
    return wrapper


class ArgumentException(Exception):
    """
    Exception raised when arg not in allowed list
    """


def create_range_buckets(start, end, step):
    """
    Simple helper function for creating ES-able range buckets
    :param start: start of range
    :param end: end of range
    :param step: length of bucket
    :return: list with given ranges
    """
    ranges = []
    for _ in range(start, end, step):
        ranges.append(
            {'from': start, 'to': start + step}
        )
    ranges.insert(0, {'to': start})
    ranges.append({'from': end})
    return ranges


def upsert(employee_model):
    """
    Creates for employee instance ES-dict and save it
    :param employee_model: employee instance
    :return: ES response
    """
    client = get_client()
    employee_dict = employee_model.as_elasticsearch_dict()

    response = client.update(
        index=settings.ES_INDEX,
        doc_type='_doc',
        id=employee_model.id,
        body={
            'doc': employee_dict,
            'doc_as_upsert': True
        }
    )
    return response


def delete_from_es(employee_id):
    """
    Deletes employee instance from ElasticSearch
    :param employee_id: employee id
    :return: ES delete response
    """
    client = get_client()
    response = client.delete(
        index=settings.ES_INDEX,
        doc_type='_doc',
        id=employee_id
    )
    return response
