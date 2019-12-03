import uuid
from datetime import datetime
from ..utils.constants import ApiLogConstants as alc
import requests
import socket
import json
import pkgutil


class LoggingBDI:

    def __init__(self, env):
        self.id = str(uuid.uuid4())
        self.time_format = '%Y-%m-%dT%H:%M:%SZ'
        api_log_address = pkgutil.get_data('src', 'config/api-log-{}.json'.format(env)).decode()
        self.countries_equivalences = json.loads(pkgutil.get_data('src', 'config/countries_equivalences.json').decode())
        self.api_log_endpoint = create_endpoint(json.loads(api_log_address))

    def create_session(self, app, service, country, type_execution):
        endpoint = self.api_log_endpoint + '/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        user_execution = s.getsockname()[0]
        s.close()

        headers = {'Content-type': 'application/json'}

        data = {
            "app": app,
            "servicio": service,
            "codigoPais": self.countries_equivalences[country],
            "estadoEjecucion": alc.PENDING,
            "tipoEjecucion": type_execution,
            "usuarioEjecucion": user_execution,
            "fechaInicio": timestamp,
            "input": {"TiempoEspera": "2000"},
            "output": {}
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def update_session(self):
        endpoint = self.api_log_endpoint + '/' + self.id

        headers = {'Content-type': 'application/json'}

        data = {
            "estadoEjecucion": alc.STARTED
        }

        response = requests.put(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def done_session(self):
        endpoint = self.api_log_endpoint + '/done/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaFin": timestamp
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def failed_session(self, message):
        endpoint = self.api_log_endpoint + '/error/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaFin": timestamp,
            "mensaje": message
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def add_event(self, type_event, event, initial_datetime, final_datetime, message):
        endpoint = self.api_log_endpoint + '/add/' + self.id

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaEjecucion": initial_datetime.strftime(self.time_format),
            "fechaInicio": final_datetime.strftime(self.time_format),
            "tipoEvento": type_event,
            "evento": event,
            "duracion": str(round((final_datetime - initial_datetime).total_seconds()*1000)),
            "mensaje": message
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response


def create_endpoint(api_log):
    return 'http://{}:{}'.format(api_log['API-LOG-ADDRESS']['IP'], api_log['API-LOG-ADDRESS']['PORT'])
