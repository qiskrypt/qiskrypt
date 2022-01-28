"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):\n
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):\n
- Instituto de Telecomunicacoes, Portugal.
- SQIG, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):\n
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):\n
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_ENDPOINT_STATION_TYPES = ["GROUND-STATION", "SATELLITE-STATION"]
"""
The available Endpoint station types for the Qiskrypt's Endpoint.
"""

POSSIBLE_ENDPOINT_CONTEXTS = ["QUANTUM", "FULLY-QUANTUM", "SEMI-QUANTUM", "CLASSICAL"]
"""
The available Endpoint contexts for the Qiskrypt's Endpoint.
"""


class QiskryptEndpoint:
    """
    Object class for the Qiskrypt's Endpoint.
    """

    def __init__(self, num: int, name: str, station_type: str, context: str,
                 longitude: str, latitude: str):
        """
        Constructor of the Qiskrypt's Endpoint.

        :param num: the number of the Qiskrypt's Endpoint.
        :param name: the name of the Qiskrypt's Endpoint.
        :param station_type: the station type of the Qiskrypt's Endpoint.
        :param context: the context of the Qiskrypt's Endpoint.
        :param longitude: the longitude of the Qiskrypt's Endpoint.
        :param latitude: the latitude of the Qiskrypt's Endpoint.
        """

        self.num = num
        """
        Set the number of the Qiskrypt's Endpoint.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Endpoint.
        """

        self.station_type = station_type
        """
        Set the station type of the Qiskrypt'sEndpoint.
        """

        self.context = context
        """
        Set the context of the Qiskrypt's Endpoint.
        """

        self.longitude = longitude
        """
        Set the longitude of the Qiskrypt's Endpoint.
        """

        self.latitude = latitude
        """
        Set the latitude of the Qiskrypt's Endpoint.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Endpoint.

        :return self.num: the number of the Qiskrypt's Endpoint.
        """

        """
        Return the number of the Qiskrypt's Endpoint.
        """
        return self.num

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Endpoint.

        :return self.name: the name of the Qiskrypt's Endpoint.
        """

        """
        Return the name of the Qiskrypt's Endpoint.
        """
        return self.name

    def get_station_type(self) -> str:
        """
        Return the station type of the Qiskrypt's Endpoint.

        :return self.station_type: the station type of the Qiskrypt's Endpoint.
        """

        """
        Return the station type of the Qiskrypt's Endpoint.
        """
        return self.station_type

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Endpoint.

        :return self.context: the context of the Qiskrypt's Endpoint.
        """

        """
        Return the context of the Qiskrypt's Endpoint.
        """
        return self.context

    def get_longitude(self) -> str:
        """
        Return the longitude of the Qiskrypt's Endpoint.

        :return self.longitude: the longitude of the Qiskrypt's Endpoint.
        """

        """
        Return the longitude of the Qiskrypt's Endpoint.
        """
        return self.longitude

    def get_latitude(self) -> str:
        """
        Return the latitude of the Qiskrypt's Endpoint.

        :return self.latitude: the latitude of the Qiskrypt's Endpoint.
        """

        """
        Return the latitude of the Qiskrypt's Endpoint.
        """
        return self.latitude

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Endpoint.

        :return qiskrypt_endpoint_string_representation: the string representation for the Qiskrypt's Endpoint.
        """

        qiskrypt_endpoint_string_representation = "Endpoint #{}:\n- Name: {}\n- Context: {}"\
            .format(self.num, self.name, self.context)
        """
        Set the string representation for the Qiskrypt's Endpoint.
        """

        """
        Return the string representation for the Qiskrypt's Endpoint.
        """
        return qiskrypt_endpoint_string_representation
