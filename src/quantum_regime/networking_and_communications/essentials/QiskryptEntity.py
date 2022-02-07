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
- NOVA LINCS, Portugal.
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


class QiskryptEntity:
    """
    Object class for the Qiskrypt's Entity.
    """

    def __init__(self, name: str, longitude: float, latitude: float, altitude_in_kms: float):
        """
        Constructor of the Qiskrypt's Entity.

        :param name: the name of the Qiskrypt's Entity.
        :param longitude: the longitude of the Qiskrypt's Entity.
        :param latitude: the latitude of the Qiskrypt's Entity.
        :param altitude_in_kms: the altitude in KMs (Kilometers) of the Qiskrypt's Entity.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Entity.
        """

        self.longitude = longitude
        """
        Set the longitude of the Qiskrypt's Entity.
        """

        self.latitude = latitude
        """
        Set the latitude of the Qiskrypt's Entity.
        """

        self.altitude_in_kms = altitude_in_kms
        """
        Set the altitude in KMs (Kilometers) of the Qiskrypt's Entity.
        """

    def get_name(self):
        """
        Return the name of the Qiskrypt's Entity.

        :return self.name: the name of the Qiskrypt's Entity.
        """

        """
        Return the name of the Qiskrypt's Entity.
        """
        return self.name

    def get_latitude(self) -> float:
        """
        Return the latitude of the Qiskrypt's Entity.

        :return self.latitude: the latitude of the Qiskrypt's Entity.
        """

        """
        Return the latitude of the Qiskrypt's Entity.
        """
        return self.latitude

    def get_longitude(self) -> float:
        """
        Return the latitude of the Qiskrypt's Entity.

        :return self.longitude: the longitude of the Qiskrypt's Entity.
        """

        """
        Return the longitude of the Qiskrypt's Entity.
        """
        return self.longitude

    def get_altitude_in_kms(self) -> float:
        """
        Return the altitude in KMs (Kilometers) of the Qiskrypt's Entity.

        :return self.altitude_in_kms: the altitude in KMs (Kilometers) of
                                      the Qiskrypt's Entity.
        """

        """
        Return the altitude in KMs (Kilometers) of the Qiskrypt's Entity.
        """
        return self.altitude_in_kms
