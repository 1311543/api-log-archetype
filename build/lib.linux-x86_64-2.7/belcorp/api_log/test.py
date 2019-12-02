import uuid
from datetime import datetime
from ..utils_aws.constants import ApiLogConstants as alc
import socket
import json


class TestImport:

    def __init__(self, env):
        self.id = str(uuid.uuid4())
        self.time_format = '%Y-%m-%dT%H:%M:%SZ'
        self.test = 0

    def create_session(self, app, service, country, type_execution):
        return self.id+"123454"