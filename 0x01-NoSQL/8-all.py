#!/usr/bin/env python3
"""
8. List all documents in Python
"""

import pymongo


def list_all(mongo_collection):
    """
    List all documents.
    """

    docs = mongo_collection.find()
    return [x for x in docs]
