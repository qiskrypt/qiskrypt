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


"""
Import required Libraries and Packages.
"""

from src.quantum_regime.networking_and_communications\
    .clients.types.QiskryptPartyClient \
    import QiskryptPartyClient
"""
Import the Qiskrypt's Party Client.
"""

from src.quantum_regime.networking_and_communications.links.QiskryptLink \
    import QiskryptLink
"""
Import the Qiskrypt's Link.
"""


class QiskryptCommunicationSession:
    """
    Object class for the Qiskrypt's Communication Session.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Communication Session.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Communication Session.
        """

        self.sender_party_clients = list()
        """
        Set the list of sender Qiskrypt's Party Clients, initially,
        as an empty list.
        """

        self.link = None
        """
        Set the Qiskrypt's Link, initially, as None.
        """

        self.receiver_party_clients = list()
        """
        Set the list of receiver Qiskrypt's Party Clients, initially,
        as an empty list.
        """

        self.started = False
        """
        Set the boolean flag to keep information about if the
        Qiskrypt's Communication Session is started or not.
        """

        self.timeout_in_secs = 0
        """
        Set the timeout in Secs. (Seconds) for the
        Qiskrypt's Communication Session to expire.
        """

    def get_name(self):
        """
        Return the name of the Qiskrypt's Communication Session.

        :return self.name: the name of the Qiskrypt's Communication Session.
        """

        """
        Return the name of the Qiskrypt's Communication Session.
        """
        return self.name

    def get_sender_party_clients(self) -> list:
        """
        Return the list of sender Qiskrypt's Party Clients.

        :return self.sender_party_clients: the list of sender
                                           Qiskrypt's Party Clients.
        """

        """
        Return the list of sender Qiskrypt's Party Clients.
        """
        return self.sender_party_clients

    def get_link(self) -> QiskryptLink:
        """
        Return the Qiskrypt's Link of the Qiskrypt's Communication Session.

        :return self.link: the Qiskrypt's Link of the
                           Qiskrypt's Communication Session.
        """

        """
        Return the Qiskrypt's Link of the Qiskrypt's Communication Session.
        """
        return self.link

    def get_receiver_party_clients(self) -> list:
        """
        Return the list of receiver Qiskrypt's Party Clients.

        :return self.receiver_party_clients: the list of receiver
                                             Qiskrypt's Party Clients.
        """

        """
        Return the list of receiver Qiskrypt's Party Clients.
        """
        return self.receiver_party_clients

    def is_started(self) -> bool:
        """
        Return the boolean flag to keep information about if the
        Qiskrypt's Communication Session is started or not.

        :return self.started: the boolean flag to keep information about if the
                              Qiskrypt's Communication Session is started or not.
        """

        """
        Return the boolean flag to keep information about if the
        Qiskrypt's Communication Session is started or not.
        """
        return self.started

    def get_timeout_in_secs(self) -> int:
        """
        Return the timeout in Secs. (Seconds) for the
        Qiskrypt's Communication Session to expire.

        :return self.timeout_in_secs: the timeout in Secs. (Seconds) for the
                                      Qiskrypt's Communication Session to expire.
        """

        """
        Return the timeout in Secs. (Seconds) for the
        Qiskrypt's Communication Session to expire.
        """
        return self.timeout_in_secs

    def start(self, sender_party_clients: list, link: QiskryptLink,
              receiver_party_clients: list, timeout_in_secs: int):
        """
        Start the Qiskrypt's Communication Session from a list of
        possible sender Qiskrypt's Party Clients and a list of
        possible receiver Qiskrypt's Party Clients, through an existing Qiskrypt's Link.

        :param sender_party_clients: the list of possible sender Qiskrypt's Party Clients
                                     for the Qiskrypt's Communication Session.
        :param link: the Qiskrypt's Link for the Qiskrypt's Communication Session.
        :param receiver_party_clients: the list of possible receiver Qiskrypt's Party Clients
                                       for the Qiskrypt's Communication Session.
        :param timeout_in_secs: the timeout in Secs. (Seconds) for the
                                Qiskrypt's Communication Session to expire.
        """