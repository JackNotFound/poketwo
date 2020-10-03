"""
This is a one-shot script used to add timestamp fields to all pokemon.
17 September 2020
"""

import os

import config
from pymongo import MongoClient

client = MongoClient(config.DATABASE_URI)
db = client[config.DATABASE_NAME]

result = db["new_pokemon"].aggregate(
    [
        {
            "$merge": {
                "into": "pokemon",
                "on": "_id",
            }
        },
    ],
    allowDiskUse=True,
)

for i in result:
    print(i)
