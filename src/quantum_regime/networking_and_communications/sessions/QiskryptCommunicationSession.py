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

from typing import final
"""
Import the 'final' decorator from the Typing module
from the Python's Library.
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

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
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

        self.timeout_in_secs = 0
        """
        Set the timeout in Secs. (Seconds) for the
        Qiskrypt's Communication Session to expire, initially, as zero.
        """

        self.started = False
        """
        Set the boolean flag to keep information about if the
        Qiskrypt's Communication Session is started or not.
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

    def set_started(self, started):
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Communication Session is started or not, with a new boolean value.

        :param started: the new boolean flag to keep the information about if
                        the Qiskrypt's Communication Session is started or not.
        """

        if started != self.is_started():
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Communication Session is started or not is equal to the current one.
            """

            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Communication Session is started or not, with a new boolean value.
            """
            self.started = started

        else:
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Communication Session is started or not is equal to the current one.
            """

            if self.is_started():
                """
                If the Qiskrypt's Communication Session is already started.
                """

                # TODO Throw - Exception

            else:
                """
                If the Qiskrypt's Communication Session is not started yet.
                """

                # TODO Throw - Exception

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

        if not self.is_started():
            """
            If the Qiskrypt's Communication Session is not started yet
            between a list of sender Qiskrypt's Party Clients and
            a list of receiver Qiskrypt's Party Clients, through a Qiskrypt's Link.
            """

            num_sender_party_clients = len(sender_party_clients)
            """
            Retrieve the number of sender Qiskrypt's Party Clients.
            """

            for current_sender_party_client_index in range(num_sender_party_clients):
                """
                For each object's index in the given list of possible sender Qiskrypt's Party Clients.
                """

                current_sender_party_client = \
                    sender_party_clients[current_sender_party_client_index]
                """
                Retrieve the current object for a possible sender Qiskrypt's Party Client.
                """

                if not isinstance(current_sender_party_client, QiskryptPartyClient):
                    """
                    Check if the current object is not a Qiskrypt's Party Client.
                    """

                    # TODO Throw - Exception

            num_receiver_party_clients = len(receiver_party_clients)
            """
            Retrieve the number of receiver Qiskrypt's Party Clients.
            """

            for current_receiver_party_client_index in range(num_receiver_party_clients):
                """
                For each object's index in the given list of possible receiver Qiskrypt's Party Clients.
                """

                current_receiver_party_client = \
                    receiver_party_clients[current_receiver_party_client_index]
                """
                Retrieve the current object for a possible receiver Qiskrypt's Party Client.
                """

                if not isinstance(current_receiver_party_client, QiskryptPartyClient):
                    """
                    Check if the current object is not a Qiskrypt's Party Client.
                    """

                    # TODO Throw - Exception

            self.sender_party_clients = sender_party_clients
            """
            Set the list of sender Qiskrypt's Party Clients with
            the given list of sender Qiskrypt's Party Clients.
            """

            self.link = link
            """
            Set the Qiskrypt's Link with the given Qiskrypt's Link.
            """

            self.receiver_party_clients = receiver_party_clients
            """
            Set the list of receiver Qiskrypt's Party Clients with
            the given list of receiver Qiskrypt's Party Clients.
            """

            self.timeout_in_secs = timeout_in_secs
            """
            Set the timeout in Secs. (Seconds) for the
            Qiskrypt's Communication Session to expire, with
            the given timeout in Secs. (Seconds).
            """

        else:
            """
            If the Qiskrypt's Communication Session is already started
            between a list of sender Qiskrypt's Party Clients and
            a list of receiver Qiskrypt's Party Clients, through a Qiskrypt's Link.
            """

            # TODO Throw - Exception

    @final
    def generate_base_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Generate the base Qiskrypt's Quantum Circuit for each round of
        the Qiskrypt's Communication Session, from the Qiskrypt's Registers
        retrieved of the sender and receiver Qiskrypt's Party Clients,
        and respective associated Qiskrypt's Link connecting them.

        :return quantum_circuit:
        """

        if self.is_started():
            """
            If the Qiskrypt's Communication Session is already started.
            """

            quantum_registers_list = list()
            """
            Create an empty list for the Qiskrypt's Quantum Registers
            to be used for the generation of the base Qiskrypt's Quantum Circuit for
            each round of the Qiskrypt's Communication Session.
            """

            fully_quantum_registers_list = list()
            """
            Create an empty list for the Qiskrypt's Fully-Quantum Registers
            to be used for the generation of the base Qiskrypt's Quantum Circuit for
            each round of the Qiskrypt's Communication Session.
            """

            semi_quantum_registers_list = list()
            """
            Create an empty list for the Qiskrypt's Semi-Quantum Registers
            to be used for the generation of the base Qiskrypt's Quantum Circuit for
            each round of the Qiskrypt's Communication Session.
            """

            classical_registers_list = list()
            """
            Create an empty list for the Qiskrypt's Classical Registers
            to be used for the generation of the base Qiskrypt's Quantum Circuit for
            each round of the Qiskrypt's Communication Session.
            """

            sender_party_clients = self.get_sender_party_clients()
            """
            Retrieve the list of the sender Qiskrypt's Party Clients.
            """

            num_sender_party_clients = len(sender_party_clients)
            """
            Retrieve the number of the sender Qiskrypt's Party Clients.
            """

            for current_sender_party_client_index in range(num_sender_party_clients):
                """
                For each sender Qiskrypt's Party Client's index in
                the given list of possible sender Qiskrypt's Party Clients.
                """

                current_sender_party_client = \
                    sender_party_clients[current_sender_party_client_index]
                """
                Retrieve the current sender Qiskrypt's Party Client in
                the given list of possible sender Qiskrypt's Party Clients.
                """

                if isinstance(current_sender_party_client, QiskryptPartyClient):
                    """
                    If the current sender Qiskrypt's Party Client is
                    really a Qiskrypt's Party Client.
                    """

                    current_sender_party_client.get_registers()

            quantum_circuit = QiskryptQuantumCircuit(name="qu_circ_{}".format(self.get_name()))
            """
            Create the base Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers
            retrieved of the sender and receiver Qiskrypt's Party Clients,
            and respective associated Qiskrypt's Link connecting them.
            """

            """
            Return the base Qiskrypt's Quantum Circuit for each round of
            the Qiskrypt's Communication Session, from the Qiskrypt's Registers
            retrieved of the sender and receiver Qiskrypt's Party Clients,
            and respective associated Qiskrypt's Link connecting them.
            """
            return quantum_circuit

        else:
            """
            If the Qiskrypt's Communication Session is not started yet.
            """

            # TODO Throw - Exception
