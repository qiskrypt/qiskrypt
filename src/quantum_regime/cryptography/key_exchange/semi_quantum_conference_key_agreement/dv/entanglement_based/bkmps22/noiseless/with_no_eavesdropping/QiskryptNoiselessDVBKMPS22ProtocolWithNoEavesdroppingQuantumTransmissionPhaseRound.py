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

from src.quantum_regime.cryptography.key_exchange.semi_quantum_conference_key_agreement.dv \
    .entanglement_based.bkmps22.common.QiskryptDVBKMPS22ProtocolRound \
    import QiskryptDVBKMPS22ProtocolRound
"""
Import the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptNoiselessDVBKMPS22ProtocolWithNoEavesdroppingQuantumTransmissionPhaseRound \
            (QiskryptDVBKMPS22ProtocolRound):
    """
    Object class for the Qiskrypt's Noiseless DV (Discrete Variables)
    BKMPS22 Protocol with No Eavesdropping Quantum Transmission Phase Round.
    """

    def __init__(self, round_number: int, round_type: str,
                 round_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's Noiseless DV (Discrete Variables)
        BKMPS22 Protocol with No Eavesdropping Quantum Transmission Phase Round.

        :param round_number: the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_type: the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_quantum_circuit: the Qiskrypt's Quantum Circuit for
                                      the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        super().__init__(round_number, round_type, round_quantum_circuit)
        """
        Call of the constructor of the super-class Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round.
        """

    def get_quantum_key_exchange_protocol_round_number(self) -> int:
        """
        Return the number of the Qiskrypt's Quantum Key Distribution (QKD) Round.

        :return super().get_round_number(): the number of the Qiskrypt's Quantum Key Distribution Round.
        """

        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_round_number()

    def get_quantum_key_exchange_protocol_round_type(self) -> str:
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

    def is_round_discarded_from_key_sifting(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Key Exchange Protocol Round is discarded from
        the Key Sifting or not.

        :return super().is_round_discarded_from_key_sifting(): the boolean flag to keep the information about if
                                                               the Qiskrypt's Quantum Key Exchange Protocol Round
                                                               is discarded from the Key Sifting or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Key Exchange Protocol Round is discarded from
        the Key Sifting or not.
        """
        return super().is_round_discarded_from_key_sifting()

    def is_round_discarded_from_parameter_estimation(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Key Exchange Protocol Round is discarded from
        the Parameter Estimation or not.

        :return super().is_round_discarded_from_parameter_estimation(): the boolean flag to keep the information
                                                                        about if the Qiskrypt's Quantum Key Exchange
                                                                        Protocol Round is discarded from
                                                                        the Parameter Estimation or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Key Exchange Protocol Round is discarded from
        the Parameter Estimation or not.
        """
        return super().is_round_discarded_from_parameter_estimation()

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

    def set_round_discarded_from_key_sifting(self) -> None:
        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded from
        the Key Sifting or not, as True.
        """

        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded from
        the Key Sifting or not, as True.
        """
        super().set_round_discarded_from_key_sifting()

    def set_round_discarded_from_parameter_estimation(self) -> None:
        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded from
        the Parameter Estimation or not, as True.
        """

        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded from
        the Parameter Estimation or not, as True.
        """
        super().set_round_discarded_from_parameter_estimation()

    def is_round_operation_sender_choice_made(self) -> bool:
        """
        Return the verification for if the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.

        :return super().is_round_operation_sender_choice_made(): if the operation choice made by the sender in
                                                                 the Qiskrypt's DV (Discrete Variables)
                                                                 BKMPS22 Protocol Round is already set.
        """

        """
        Return the verification for if the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
        """
        return super().is_round_operation_sender_choice_made()

    def set_round_operation_sender_choice(self, round_operation_sender_choice: str) -> None:
        """
        Set the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is not set yet.

        :param round_operation_sender_choice: the operation choice made by the sender in
                                              the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round.
        """

        """
        Set the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is not set yet.
        """
        super().set_round_operation_sender_choice(round_operation_sender_choice)

    def get_round_operation_sender_choice(self) -> str:
        """
        Return the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is already set.

        :return super().get_round_operation_sender_choice(): the operation choice made by the sender in
                                                             the Qiskrypt's DV (Discrete Variables)
                                                             BKMPS22 Protocol Round, if it is already set.
        """

        """
        Return the operation choice made by the sender in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is already set.
        """
        return super().get_round_operation_sender_choice()

    def is_round_operation_receiver_choice_made(self) -> bool:
        """
        Return the verification for if the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.

        :return super().is_round_operation_receiver_choice_made(): if the operation choice made by the receiver in
                                                                   the Qiskrypt's DV (Discrete Variables)
                                                                   BKMPS22 Protocol Round is already set.
        """

        """
        Return the verification for if the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round is already set.
        """
        return super().is_round_operation_receiver_choice_made()

    def set_round_operation_receiver_choice(self, round_operation_receiver_choice: str) -> None:
        """
        Set the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is not set yet.

        :param round_operation_receiver_choice: the operation choice made by the receiver in
                                                the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round.
        """

        """
        Set the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is not set yet.
        """
        super().set_round_operation_receiver_choice(round_operation_receiver_choice)

    def get_round_operation_receiver_choice(self) -> str:
        """
        Return the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is already set.

        :return super().get_round_operation_receiver_choice(): the operation choice made by the receiver in
                                                               the Qiskrypt's DV (Discrete Variables)
                                                               BKMPS22 Protocol Round, if it is already set.
        """

        """
        Return the operation choice made by the receiver in
        the Qiskrypt's DV (Discrete Variables) BKMPS22 Protocol Round, if it is already set.
        """
        return super().get_round_operation_receiver_choice()
