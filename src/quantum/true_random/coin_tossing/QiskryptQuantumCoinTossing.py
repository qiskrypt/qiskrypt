"""

Copyrights:\n
- © Qiskrypt, 2021 - All rights reserved.\n

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

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
"""

from src.quantum.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitNotInitialisedYetError
"""
Import the Quantum Circuit Not Initialised Yet Error for
the Qiskrypt's Quantum Circuit.
"""

from src.quantum.circuit.exception.QiskryptQuantumCircuitException \
    import QiskryptQuantumCircuitAlreadyInitialisedError
"""
Import the Quantum Circuit Already Initialised Error for
the Qiskrypt's Quantum Circuit.
"""

from src.quantum.true_random.coin_tossing.exception.QiskryptQuantumCoinTossingException \
    import QiskryptQuantumCoinTossingCoinNotTossedYetError
"""
Import the Coin Not Tossed Yet Error for
the Qiskrypt's Quantum Coin Tossing.
"""

from src.quantum.true_random.coin_tossing.exception.QiskryptQuantumCoinTossingException \
    import QiskryptQuantumCoinTossingCoinAlreadyTossedError
"""
Import the Coin Already Tossed Error for
the Qiskrypt's Quantum Coin Tossing.
"""

"""
Definition of Constants and Enumerations.
"""

NUM_QUBITS_FOR_COIN = NUM_BITS_FOR_COIN = 1
"""
The number of qubits and bits needed, for a Coin (just 1 qubit/bit).
"""

PHYSICAL_ANATOMIC_PARTS_OF_A_COIN = {"0b0": "HEADS", "0b1": "TAILS"}
"""
The dictionary for the physical anatomic parts of a Coin. 
"""


class QiskryptQuantumCoinTossing:
    """
    Object class for the Qiskrypt's Quantum Coin Tossing.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Quantum Coin Tossing.

        :param name: the name of the Qiskrypt's Quantum Coin Tossing.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Coin Tossing.
        """

        self.qiskrypt_quantum_circuit = None
        """
        Set the Qiskrypt's Quantum Circuit, as None.
        """

        self.qiskrypt_quantum_circuit_initialised = False
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing
        was already initialised or not, as False.
        """

        self.already_tossed = False
        """
        Set the boolean flag to keep information about if
        the Coin was already tossed or not, as False.
        """

        self.coin_tossing_outcome_bit = None
        """
        Set the bit outcome for the Coin Tossing,
        from the measurement of the Qiskrypt's Quantum Circuit for
        the Qiskrypt's Quantum Coin Tossing, as None.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Coin Tossing.

        :return self.name: the name of the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Return the name of the Qiskrypt's Quantum Coin Tossing.
        """
        return self.name

    def get_qiskrypt_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing.

        :return self.qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit for
                                               the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Return the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing.
        """
        return self.qiskrypt_quantum_circuit

    def is_qiskrypt_quantum_circuit_initialised(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing
        was already initialised or not.

        :return self.qiskrypt_quantum_circuit_initialised: the boolean flag to keep information about if
                                                           the Qiskrypt's Quantum Circuit for
                                                           the Qiskrypt's Quantum Coin Tossing
                                                           was already initialised or not.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing
        was already initialised or not.
        """
        return self.qiskrypt_quantum_circuit_initialised

    def is_already_tossed(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Coin was already tossed or not.

        :return self.already_tossed: the boolean flag to keep information about if
                                     the Coin was already tossed or not.
        """

        """
        Return the boolean flag to keep information about if
        the Coin was already tossed or not.
        """
        return self.already_tossed

    def get_coin_tossing_outcome_bit(self) -> str:
        """
        Return the classical outcome (i.e., the observation) from the Coin Tossing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in a binary digit format (i.e., a bit).

        :return self.coin_tossing_outcome_bit: the classical outcome (i.e., the observation) from the Coin Tossing,
                                               through the execution of the respective Qiskrypt's Quantum Circuit,
                                               in a binary digit format (i.e., a bit).
        """

        if self.is_already_tossed():
            """
            If the Coin was already tossed.          
            """

            """
            Return the classical outcome (i.e., the observation) from the Coin Tossing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in a binary digit format (i.e., a bit).
            """
            return self.coin_tossing_outcome_bit

        else:
            """
            If the Coin was not tossed yet.          
            """

            """
            Return/Raise a Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
            """
            self.raise_coin_not_tossed_yet_error()

    def get_coin_tossing_outcome_bit_as_int_base_2(self) -> int:
        """
        Return the classical outcome (i.e., the observation) from the Coin Tossing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in an integer base-2 format (i.e., an integer representation of a bit).

        :return int(self.coin_tossing_outcome_bit, base=2): the classical outcome (i.e., the observation) from
                                                            the Coin Tossing, through the execution of
                                                            the respective Qiskrypt's Quantum Circuit,
                                                            in an integer base-2 format
                                                            (i.e., an integer representation of a bit).
        """

        if self.is_already_tossed():
            """
            If the Coin was already tossed.          
            """

            """
            Return the classical outcome (i.e., the observation) from the Coin Tossing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in an integer base-2 format (i.e., an integer representation of a bit).
            """
            return int(self.coin_tossing_outcome_bit, base=2)

        else:
            """
            If the Coin was not tossed yet.          
            """

            """
            Return/Raise a Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
            """
            self.raise_coin_not_tossed_yet_error()

    def get_coin_tossing_outcome_bit_as_head_or_tails(self) -> str:
        """
        Return the classical outcome (i.e., the observation) from the Coin Tossing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in an anatomic part format (i.e., 'Heads' for |0⟩ and 'Tails' for |1⟩).

        :return ANATOMIC_PARTS_OF_A_COIN[self.coin_tossing_outcome_bit]: the classical outcome
                                                                         (i.e., the observation) from
                                                                         the Coin Tossing, through the execution of
                                                                         the respective Qiskrypt's Quantum Circuit,
                                                                         in an anatomic part format
                                                                         (i.e., 'Heads' for |0⟩ and 'Tails' for |1⟩).
        """

        if self.is_already_tossed():
            """
            If the Coin was already tossed.          
            """

            """
            Return the classical outcome (i.e., the observation) from the Coin Tossing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in a physical anatomic part format (i.e., 'Heads' for |0⟩ and 'Tails' for |1⟩).
            """
            return PHYSICAL_ANATOMIC_PARTS_OF_A_COIN[self.coin_tossing_outcome_bit]

        else:
            """
            If the Coin was not tossed yet.          
            """

            """
            Return/Raise a Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
            """
            self.raise_coin_not_tossed_yet_error()

    def initialise_qiskrypt_quantum_circuit(self) -> None:
        """
        Initialise the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing.
        """

        if not self.is_qiskrypt_quantum_circuit_initialised() and not self.is_already_tossed():
            """
            If neither the Qiskrypt's Quantum Circuit for
            the Qiskrypt's Quantum Coin Tossing was initialised yet,
            nor the Coin was tossed yet.
            """

            quantum_register_name = "qu_reg_coin_toss"
            """
            Set the name of the Qiskrypt's Quantum Register.
            """

            qiskrypt_quantum_register_coin_tossing = \
                QiskryptQuantumRegister(name=quantum_register_name,
                                        num_qubits=NUM_QUBITS_FOR_COIN)
            """
            Create a Qiskrypt's Quantum Register, given its name and number of qubits.
            """

            classical_register_name = "cl_reg_coin_toss"
            """
            Set the name of the Qiskrypt's Classical Register.
            """

            qiskrypt_classical_register_coin_tossing = \
                QiskryptClassicalRegister(name=classical_register_name,
                                          num_bits=NUM_BITS_FOR_COIN)
            """
            Create a Qiskrypt's Classical Register, given its name and number of bits.
            """

            self.qiskrypt_quantum_circuit = \
                QiskryptQuantumCircuit("qu_circ_coin_toss",
                                       qiskrypt_quantum_registers=[qiskrypt_quantum_register_coin_tossing],
                                       qiskrypt_fully_quantum_registers=None,
                                       qiskrypt_semi_quantum_registers=None,
                                       qiskrypt_ancilla_quantum_registers=None,
                                       qiskrypt_ancilla_fully_quantum_registers=None,
                                       qiskrypt_ancilla_semi_quantum_registers=None,
                                       qiskrypt_classical_registers=[qiskrypt_classical_register_coin_tossing],
                                       global_phase=0, qiskit_quantum_circuit=None)
            """
            Set the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing with
            the previously created Qiskrypt's Quantum and Classical Registers.
            """

            self.qiskrypt_quantum_circuit_initialised = True
            """
            Set the boolean flag to keep information about if
            the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing
            was already initialised or not, as True.
            """

        else:
            """
            If the Qiskrypt's Quantum Circuit for
            the Qiskrypt's Quantum Coin Tossing was already initialised and/or
            the Coin was also already tossed.
            """

            if self.is_qiskrypt_quantum_circuit_initialised():
                """
                If the Qiskrypt's Quantum Circuit for
                the Qiskrypt's Quantum Coin Tossing was already initialised.
                """

                """
                Return/Raise a Quantum Circuit Already Initialised Error for
                the Qiskrypt's Quantum Coin Tossing.
                """
                self.raise_quantum_circuit_already_initialised_error()

            if self.is_already_tossed():
                """
                If the Coin was already tossed.
                """

                """
                Return/Raise a Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
                """
                self.raise_coin_already_tossed_error()

    def toss_coin(self):
        """
        Toss the Coin related to the Qiskrypt's Quantum Coin Tossing,
        through the application of the respective Quantum Gate/Operation
        (Hadamard Gate/Operation), execution of the respective Qiskrypt's Quantum Circuit
        and the measurement of the qubit representing the Coin in a 50/50 Quantum Superposition,
        storing, the classical result/outcome from the observation of it, in a bit.
        """

        if not self.is_already_tossed() and self.is_qiskrypt_quantum_circuit_initialised():
            """
            If the Coin is not already tossed and
            the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing is already initialised.
            """

            self.qiskrypt_quantum_circuit.apply_hadamard(0, 0)
            """
            Start the Coin Tossing, through the application of the Hadamard Gate/Operation to
            the 1st qubit, to create a Quantum Superposition of 50/50 for the possible outcomes
            (i.e., Head or Tails). 
            """

            self.qiskrypt_quantum_circuit.measure_single_qubit_in_qiskit_quantum_register(0, 0, 0, 0)
            """
            Finish the Coin Tossing, through the measurement of the 1st qubit representing the Coin,
            in a Quantum Superposition of 50/50 for the possible outcomes (i.e., Head or Tails) into
            the respective bit, representing the result from the observation of the experiment of
            the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit.
            """

            qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
            """
            Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
            (i.e., the classical simulation of an IBM Qiskit's Quantum Circuit).
            """

            final_results_frequency_counting = \
                execute(self.qiskrypt_quantum_circuit.get_qiskit_quantum_circuit(),
                        qiskit_qasm_backend, shots=1).result().get_counts()
            """
            Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
            and store the resulted measurement of its final quantum state.
            """

            self.coin_tossing_outcome_bit = \
                bin(int(final_results_frequency_counting.most_frequent(), base=2))
            """
            Set the bit outcome for the Coin Tossing,
            from the measurement of the Qiskrypt's Quantum Circuit for
            the Qiskrypt's Quantum Coin Tossing, as the resulted outcome
            from the measurement of the IBM Qiskit's Quantum Circuit,
            in an binary format (i.e., the Python's representation for a bit).
            """

            self.already_tossed = True
            """
            Set the boolean flag to keep information about if
            the Coin was already tossed or not, as True.
            """

        else:
            """
            If the Coin is already tossed and/or
            the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Coin Tossing is not initialised yet.
            """

            if not self.is_qiskrypt_quantum_circuit_initialised():
                """
                If the Qiskrypt's Quantum Circuit for
                the Qiskrypt's Quantum Coin Tossing is not initialised yet.
                """

                """
                Return/Raise the Quantum Circuit Not Initialised Yet Error for
                the Qiskrypt's Quantum Coin Tossing.
                """
                self.raise_quantum_circuit_not_initialised_yet_error()

            if self.is_already_tossed():
                """
                If the Coin was already tossed.
                """

                """
                Return/Raise a Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
                """
                self.raise_coin_already_tossed_error()

    @staticmethod
    def raise_quantum_circuit_not_initialised_yet_error() -> None:
        """
        Return/Raise a Quantum Circuit Not Initialised Yet Error for the Qiskrypt's Quantum Coin Tossing.

        :raise quantum_circuit_not_initialised_yet_error: a Quantum Circuit Not Initialised Yet Error for
                                                          the Qiskrypt's Quantum Coin Tossing.
        """

        quantum_circuit_not_initialised_yet_error = \
            QiskryptQuantumCircuitNotInitialisedYetError(primitive="Qiskrypt's Quantum Coin Tossing")
        """
        Retrieve the Quantum Circuit Not Initialised Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Raise the Quantum Circuit Not Initialised Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """
        raise quantum_circuit_not_initialised_yet_error

    @staticmethod
    def raise_quantum_circuit_already_initialised_error() -> None:
        """
        Return/Raise a Quantum Circuit Already Initialised Error for the Qiskrypt's Quantum Coin Tossing.

        :raise quantum_circuit_already_initialised_error: a Quantum Circuit Already Initialised Error for
                                                          the Qiskrypt's Quantum Coin Tossing.
        """

        quantum_circuit_already_initialised_error = \
            QiskryptQuantumCircuitAlreadyInitialisedError(primitive="Qiskrypt's Quantum Coin Tossing")
        """
        Retrieve the Quantum Circuit Already Initialised Error for the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Raise the Quantum Circuit Already Initialised Error for the Qiskrypt's Quantum Coin Tossing.
        """
        raise quantum_circuit_already_initialised_error

    @staticmethod
    def raise_coin_not_tossed_yet_error() -> None:
        """
        Return/Raise a Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.

        :raise coin_not_tossed_yet_error: a Coin Not Tossed Yet Error for
                                          the Qiskrypt's Quantum Coin Tossing.
        """

        coin_not_tossed_yet_error = QiskryptQuantumCoinTossingCoinNotTossedYetError()
        """
        Retrieve the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Raise the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """
        raise coin_not_tossed_yet_error

    @staticmethod
    def raise_coin_already_tossed_error() -> None:
        """
        Return/Raise a Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.

        :raise coin_not_tossed_yet_error: a Coin Already Tossed Error for
                                          the Qiskrypt's Quantum Coin Tossing.
        """

        coin_already_tossed_error = QiskryptQuantumCoinTossingCoinAlreadyTossedError()
        """
        Retrieve the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
        """

        """
        Raise the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
        """
        raise coin_already_tossed_error
