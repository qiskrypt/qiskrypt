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
Import required Libraries and Packages.
"""

from src.quantum_regime.networking_and_communications.endpoints.QiskryptEndpoint \
    import QiskryptEndpoint
"""
Import the Qiskrypt's Endpoint.
"""

from src.quantum_regime.networking_and_communications.endpoints.QiskryptEndpoint \
    import POSSIBLE_ENDPOINT_STATION_TYPES
"""
Import the possible station types of the Qiskrypt's Endpoint.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_SATELLITE_ORBITS = ["LOW-EARTH ORBIT (LEO)", "MEDIUM-EARTH ORBIT (MEO)",
                             "HIGH-EARTH ORBIT (HEO)", "GEOSTATIONARY ORBIT (GEO)"]
"""
The available Satellite Endpoint orbits for the Qiskrypt's Endpoint.
"""

MAX_ALTITUDE_SATELLITE_STATION_IN_KMS = 100000
"""
The maximum altitude in KMs (Kilometers) for a Qiskrypt's Satellite Station.
"""


class QiskryptSatelliteStationEndpoint(QiskryptEndpoint):
    """
    Object class for the Qiskrypt's Satellite Station Endpoint.
    """

    def __init__(self, num: int, name: str, context: str,
                 longitude: str, latitude: str, altitude_in_kms: str):
        """
        Constructor of the Qiskrypt's Satellite Station Endpoint.

        :param num: the number of the Qiskrypt's Endpoint.
        :param name: the name of the Qiskrypt's Endpoint.
        :param context: the context of the Qiskrypt's Endpoint.
        :param longitude: the longitude of the Qiskrypt's Endpoint.
        :param latitude: the latitude of the Qiskrypt's Endpoint.
        :param altitude_in_kms: the altitude in KMs (Kilometers) of the Qiskrypt's Endpoint.
        """

        if float(altitude_in_kms) <= MAX_ALTITUDE_SATELLITE_STATION_IN_KMS:
            """
            If the altitude of the Qiskrypt's Satellite Station Endpoint is valid,
            i.e., lower than or equal to 100,000 KMs (Kilometers).
            """

            super().__init__(num, name, POSSIBLE_ENDPOINT_STATION_TYPES[1],
                             context, longitude, latitude, altitude_in_kms)
            """
            Call of the constructor of the super-class Qiskrypt's Endpoint.
            """

        else:
            """
            If the altitude of hte Qiskrypt's Satellite Station Endpoint is not valid,
            i.e., higher than 100,000 KMs (Kilometers).
            """

            # TODO Throw - Exception

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Endpoint.

        :return super().get_num(): the number of the Qiskrypt's Endpoint.
        """

        """
        Return the number of the Qiskrypt's Endpoint.
        """
        return super().get_num()

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Endpoint.

        :return super().get_name(): the name of the Qiskrypt's Endpoint.
        """

        """
        Return the name of the Qiskrypt's Endpoint.
        """
        return super().get_name()

    def get_station_type(self) -> str:
        """
        Return the station type of the Qiskrypt's Endpoint.

        :return super().get_station_type(): the station type of the Qiskrypt's Endpoint.
        """

        """
        Return the station type of the Qiskrypt's Endpoint.
        """
        return super().get_station_type()

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Endpoint.

        :return super().get_context(): the context of the Qiskrypt's Endpoint.
        """

        """
        Return the context of the Qiskrypt's Endpoint.
        """
        return super().get_context()

    def get_longitude(self) -> str:
        """
        Return the longitude of the Qiskrypt's Endpoint.

        :return super().get_longitude(): the longitude of the Qiskrypt's Endpoint.
        """

        """
        Return the longitude of the Qiskrypt's Endpoint.
        """
        return super().get_longitude()

    def get_latitude(self) -> str:
        """
        Return the latitude of the Qiskrypt's Endpoint.

        :return super().get_latitude(): the latitude of the Qiskrypt's Endpoint.
        """

        """
        Return the latitude of the Qiskrypt's Endpoint.
        """
        return super().get_latitude()

    def get_altitude_in_kms(self) -> str:
        """
        Return the altitude in KMs (Kilometers) of the Qiskrypt's Endpoint.

        :return super().get_altitude_in_kms(): the altitude in KMs (Kilometers) of the Qiskrypt's Endpoint.
        """

        """
        Return the altitude in KMs (Kilometers) of the Qiskrypt's Endpoint.
        """
        return super().get_altitude_in_kms()

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Endpoint.

        :return super().__str__(): the string representation for the Qiskrypt's Endpoint.
        """

        """
        Return the string representation for the Qiskrypt's Endpoint.
        """
        return super().__str__()
