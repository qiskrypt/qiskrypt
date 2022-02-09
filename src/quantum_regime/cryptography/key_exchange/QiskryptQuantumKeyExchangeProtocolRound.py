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

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumKeyExchangeProtocolRound:
    """
    Object class for the Qiskrypt's Quantum Key Exchange Protocol Round.
    """

    def __init__(self, round_number: int, round_type: str, round_quantum_circuit: QiskryptQuantumCircuit):
        """
        Constructor of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :param round_number: the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_type: the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        :param round_quantum_circuit: the Qiskrypt's Quantum Circuit for
                                      the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        if round_number > 0:
            """
            If the given number of the Qiskrypt's Quantum Key Exchange Protocol Round is valid.
            """

            if round_type is not None:
                """
                If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is valid.
                """

                if round_quantum_circuit is not None:
                    """
                    If the Qiskrypt's Quantum Circuit for
                    the Qiskrypt's Quantum Key Exchange Protocol Round is valid.
                    """

                    self.round_number = round_number
                    """
                    Set the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
                    """

                    self.round_type = round_type
                    """
                    Set the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
                    """

                    self.round_quantum_circuit = round_quantum_circuit
                    """
                    Set the Qiskrypt's Quantum Circuit for the Qiskrypt's
                    Quantum Key Exchange Protocol Round.
                    """

                    self.round_discarded = False
                    """
                    Set the boolean flag to keep the information about if the Qiskrypt's
                    Quantum Key Exchange Protocol Round is discarded or not, initially, as False.
                    """

                else:
                    """
                    If the Qiskrypt's Quantum Circuit for
                    the Qiskrypt's Quantum Key Exchange Protocol Round is not valid.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the given number of the Qiskrypt's Quantum Key Exchange Protocol Round is not valid.
            """

            # TODO Throw - Exception

    def get_round_number(self) -> int:
        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return self.round_number: the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return self.round_number

    def get_round_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return self.round_type: the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return self.round_type

    def get_round_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return self.round_quantum_circuit: the Qiskrypt's Quantum Circuit of
                                            the Qiskrypt's Quantum Key Exchange Protocol Round.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return self.round_quantum_circuit

    def is_round_discarded(self) -> bool:
        """
        Return the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not.

        :return self.round_discarded: the boolean flag to keep the information about if the Qiskrypt's
                                      Quantum Key Exchange Protocol Round is discarded or not.
        """

        """
        Return the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not.
        """
        return self.round_discarded

    def set_round_discarded(self) -> None:
        """
        Set the boolean flag to keep the information about if the Qiskrypt's
        Quantum Key Exchange Protocol Round is discarded or not, as True.
        """

        if not self.is_round_discarded():
            """
            If the boolean flag to keep the information about if the Qiskrypt's
            Quantum Key Exchange Protocol Round is discarded or not, is still set as False.
            """

            """
            Set the boolean flag to keep the information about if the Qiskrypt's
            Quantum Key Exchange Protocol Round is discarded or not, as True.
            """
            self.round_discarded = True

        else:
            """
            If the boolean flag to keep the information about if the Qiskrypt's
            Quantum Key Exchange Protocol Round is discarded or not, is already set as True.
            """

            # TODO Throw - Exception
