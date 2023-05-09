#!/usr/bin/env python3
"""
9. Insert a document in Python
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert  document(s).
    """

    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
