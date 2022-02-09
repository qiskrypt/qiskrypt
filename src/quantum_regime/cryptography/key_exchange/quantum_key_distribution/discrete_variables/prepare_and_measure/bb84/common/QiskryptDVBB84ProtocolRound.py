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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistributionRound \
    import QiskryptQuantumKeyDistributionRound
"""
Import the Qiskrypt's Quantum Key Distribution (QKD) Round.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES = ["Z-BASIS ROUND", "X-BASIS ROUND",
                                         "CLASSICAL POST-PROCESSING ROUND"]
"""
The available DV (Discrete Variables) BB84 Protocol Round types for
the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""


class QiskryptDVBB84ProtocolRound(QiskryptQuantumKeyDistributionRound):
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.
    """

    def __init__(self, round_number: int, round_type: str,
                 round_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.

        :param round_number: the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_type: the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_quantum_circuit: the Qiskrypt's Quantum Circuit for
                                      the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        if round_type in POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is
            one of the available (and thus, valid) BB84 Protocol Round types for
            the Qiskrypt's BB84 Protocol with Discrete Variables (DVs).
            """

            super().__init__(round_number, round_type, round_quantum_circuit)
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Distribution (QKD) Round.
            """

            self.round_basis_sender_choice = None
            """
            Set the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, initially, as None.
            """

            self.round_basis_receiver_choice = None
            """
            Set the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, initially, as None.
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is
            not one of the available (and thus, not valid) BB84 Protocol Round types for
            the Qiskrypt's BB84 Protocol with Discrete Variables (DVs).
            """

            # TODO Throw - Exception

    def get_round_number(self) -> int:
        """
        Return the number of the Qiskrypt's Quantum Key Distribution (QKD) Round.

        :return super().get_round_number(): the number of the Qiskrypt's Quantum Key Distribution Round.
        """

        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_round_number()

    def get_round_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_round_type(): the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_round_type()

    def get_round_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_round_quantum_circuit(): the Qiskrypt's Quantum Circuit of
                                                     the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_round_quantum_circuit()

    def is_round_discarded(self) -> bool:
        """
        Return the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not.

        :return super().is_round_discarded(): the boolean flag to keep the information about if the Qiskrypt's
                                              Quantum Key Exchange Protocol Round is discarded or not.
        """

        """
        Return the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not.
        """
        return super().is_round_discarded()

    def set_round_discarded(self) -> None:
        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not, as True.
        """

        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not, as True.
        """
        super().set_round_discarded()

    def is_round_basis_sender_choice_made(self) -> bool:
        """
        Return the verification for if the basis choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.

        :return self.round_basis_sender_choice is not None: if the basis choice made by the sender in
                                                            the Qiskrypt's DV (Discrete Variables)
                                                            BB84 Protocol Round is already set.
        """

        """
        Return the verification for if the basis choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.
        """
        return self.round_basis_sender_choice is not None

    def set_round_basis_sender_choice(self, round_basis_sender_choice: str) -> None:
        """
        Set the basis choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is not set yet.

        :param round_basis_sender_choice: the basis choice made by the sender in
                                          the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.
        """

        if not self.is_round_basis_sender_choice_made():
            """
            If the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            """
            Set the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is not set yet.
            """
            self.round_basis_sender_choice = round_basis_sender_choice

        else:
            """
            If the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            # TODO Throw - Exception

    def get_round_basis_sender_choice(self) -> str:
        """
        Return the basis choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is already set.

        :return self.round_basis_sender_choice: the basis choice made by the sender in
                                                the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round,
                                                if it is already set.
        """

        if self.is_round_basis_sender_choice_made():
            """
            If the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.
            """

            """
            Return the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is already set.
            """
            return self.round_basis_sender_choice

        else:
            """
            If the basis choice made by the sender in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            # TODO Throw - Exception

    def is_round_basis_receiver_choice_made(self) -> bool:
        """
        Return the verification for if the basis choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.

        :return self.round_basis_receiver_choice is not None: if the basis choice made by the receiver in
                                                              the Qiskrypt's DV (Discrete Variables)
                                                              BB84 Protocol Round is already set.
        """

        """
        Return the verification for if the basis choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.
        """
        return self.round_basis_receiver_choice is not None

    def set_round_basis_receiver_choice(self, round_basis_receiver_choice: str) -> None:
        """
        Set the basis choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is not set yet.

        :param round_basis_receiver_choice: the basis choice made by the receiver in
                                            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.
        """

        if not self.is_round_basis_receiver_choice_made():
            """
            If the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            """
            Set the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is not set yet.
            """
            self.round_basis_receiver_choice = round_basis_receiver_choice

        else:
            """
            If the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            # TODO Throw - Exception

    def get_round_basis_receiver_choice(self) -> str:
        """
        Return the basis choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is already set.

        :return self.round_basis_receiver_choice: the basis choice made by the receiver in
                                                  the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round,
                                                  if it is already set.
        """

        if self.is_round_basis_receiver_choice_made():
            """
            If the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is already set.
            """

            """
            Return the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round, if it is already set.
            """
            return self.round_basis_receiver_choice

        else:
            """
            If the basis choice made by the receiver in
            the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round is not set yet.
            """

            # TODO Throw - Exception
