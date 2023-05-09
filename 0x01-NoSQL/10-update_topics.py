#!/usr/bin/env python3
"""
10. Change school topics
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document base on the name.
    """

    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
