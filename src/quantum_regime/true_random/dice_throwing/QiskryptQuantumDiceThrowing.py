"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum_regime cryptography, quantum_regime communication and
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

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum_regime.transforms.hadamard.QiskryptQuantumHadamardTransform \
    import QiskryptQuantumHadamardTransform
"""
Import the Qiskrypt's Quantum Hadamard Transform.
"""

from math import ceil, log2
"""
Import the Logarithm of Base-2 and the  Ceil mathematical function from
the Math Python's library.
"""

from datetime import datetime
"""
Import the DateTime Module from the DateTime Python's Library.
"""

from src.quantum_regime.true_random.dice_throwing.exception.QiskryptQuantumDiceThrowingException \
    import QiskryptQuantumDiceThrowingDiceTypeNotValidError
"""
Import the Dice Type Not Valid Error for
the Qiskrypt's Quantum Dice Throwing.
"""

from src.quantum_regime.true_random.dice_throwing.exception.QiskryptQuantumDiceThrowingException \
    import QiskryptQuantumDiceThrowingDiceNotConfiguredYetError
"""
Import the Dice Not Configured Yet Error for
the Qiskrypt's Quantum Dice Throwing.
"""

from src.quantum_regime.true_random.dice_throwing.exception.QiskryptQuantumDiceThrowingException \
    import QiskryptQuantumDiceThrowingDiceAlreadyConfiguredError
"""
Import the Dice Already Configured Error for
the Qiskrypt's Quantum Dice Throwing.
"""

from src.quantum_regime.true_random.dice_throwing.exception.QiskryptQuantumDiceThrowingException \
    import QiskryptQuantumDiceThrowingDiceNotThrownYetError
"""
Import the Dice Not Thrown Yet Error for
the Qiskrypt's Quantum Dice Throwing.
"""

from src.quantum_regime.true_random.dice_throwing.exception.QiskryptQuantumDiceThrowingException \
    import QiskryptQuantumDiceThrowingDiceAlreadyThrownError
"""
Import the Dice Already Thrown Error for
the Qiskrypt's Quantum Dice Throwing.
"""


"""
Definition of Constants and Enumerations.
"""

DICE_TETRAHEDRON_NUM_SIDES = 4
"""
The number of sides of a Dice, in a form of a Tetrahedron.
"""

DICE_CUBE_NUM_SIDES = 6
"""
The number of sides of a Dice, in a form of a Cube.
"""

DICE_OCTAHEDRON_NUM_SIDES = 8
"""
The number of sides of a Dice, in a form of an Octahedron.
"""

DICE_PENTAGONAL_TRAPEZOHEDRON_NUM_SIDES = 10
"""
The number of sides of a Dice, in a form of a Pentagonal Trapezohedron.
"""

DICE_DODECAHEDRON_NUM_SIDES = 12
"""
The number of sides of a Dice, in a form of a Dodecahedron.
"""

DICE_ICOSAHEDRON_NUM_SIDES = 20
"""
The number of sides of a Dice, in a form of an Icosahedron.
"""

DICE_TYPES = ["tetrahedron", "cube", "octahedron",
              "pentagonal_trapezohedron", "dodecahedron", "icosahedron"]
"""
The Dice types for all the configurations available for
the Qiskrypt's Quantum Dice Throwing.
"""

NUM_SIDES_FOR_DICE_TYPES = {     DICE_TYPES[0]: DICE_TETRAHEDRON_NUM_SIDES,
                                 DICE_TYPES[1]: DICE_CUBE_NUM_SIDES,
                                 DICE_TYPES[2]: DICE_OCTAHEDRON_NUM_SIDES,
                                 DICE_TYPES[3]: DICE_PENTAGONAL_TRAPEZOHEDRON_NUM_SIDES,
                                 DICE_TYPES[4]: DICE_DODECAHEDRON_NUM_SIDES,
                                 DICE_TYPES[5]: DICE_ICOSAHEDRON_NUM_SIDES                  }
"""
The number of sides of the Dice for
the Qiskrypt's Quantum Dice Throwing,
for each configuration of Dice Type available.
"""


class QiskryptQuantumDiceThrowing:
    """
    Object class for the Qiskrypt's Quantum Dice Throwing.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Quantum Dice Throwing.

        :param name: the name of the Qiskrypt's Quantum Dice Throwing.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Dice Throwing.
        """

        self.dice_type = None
        """
        Set the dice type of the configuration to be used on
        the Qiskrypt's Quantum Dice Throwing, as None.
        """

        self.num_dice_sides = 0
        """
        Set the number of sides of the Dice configured for
        the Qiskrypt's Quantum Dice Throwing, as 0.
        """

        self.qiskrypt_quantum_hadamard_transform = None
        """
        Set the Qiskrypt's Quantum Hadamard Transform, as None.
        """

        self.already_thrown = False
        """
        Set the boolean flag to keep information about if
        the Dice was already thrown or not, as False.
        """

        self.configured = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Quantum Dice Throwing is configured or not, as False.
        """

        self.creation_timestamp = datetime.now().timestamp()
        """
        Set the current DateTime format for the timestamp of
        the creation of the Qiskrypt's Quantum Dice Throwing.
        """

        self.dice_throwing_outcome_bits = None
        """
        Set the bits' outcome for the Dice Throwing,
        from the measurement of the Qiskrypt's Quantum Circuit for
        the Qiskrypt's Quantum Dice Throwing, as None.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Dice Throwing.

        :return self.name: the name of the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Return the name of the Qiskrypt's Quantum Dice Throwing.
        """
        return self.name

    def get_qiskrypt_quantum_hadamard_transform(self) -> list:
        """
        Return the Qiskrypt's Quantum Hadamard Transform of
        the Qiskrypt's Quantum Dice Throwing.

        :return self.qiskrypt_quantum_hadamard_transforms: the Qiskrypt's Quantum Hadamard Transform of
                                                           the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Return the Qiskrypt's Quantum Hadamard Transform of
        the Qiskrypt's Quantum Dice Throwing.
        """
        return self.qiskrypt_quantum_hadamard_transform

    def get_num_dice_sides(self) -> int:
        """
        Return the number of sides of the Dice configured for
        the Qiskrypt's Quantum Dice Throwing,
        regarding the number of qubits and bits being used.

        :return self.num_dice_sides: the number of sides of the Dice configured for
                                     the Qiskrypt's Quantum Dice Throwing,
                                     regarding the number of qubits and bits being used.
        """

        """
        Return the number of sides of the Dice configured for
        the Qiskrypt's Quantum Dice Throwing,
        regarding the number of qubits and bits being used.
        """
        return self.num_dice_sides

    def is_already_thrown(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Dice was already thrown or not.

        :return self.already_thrown: the boolean flag to keep information about if
                                     the Dice was already thrown or not.
        """

        """
        Return the boolean flag to keep information about if
        the Dice was already thrown or not.
        """
        return self.already_thrown

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Dice Throwing is configured or not.

        :return self.configured: the boolean flag to keep the information about if
                                 the Qiskrypt's Quantum Dice Throwing is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Dice Throwing is configured or not.
        """
        return self.configured

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Dice Throwing.

        :return self.creation_timestamp: the current DateTime format for the timestamp of
                                         the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Dice Throwing.
        """
        return self.creation_timestamp

    def get_dice_throwing_outcome_bits(self) -> str:
        """
        Return the classical_regime outcome (i.e., the observation) from the Dice Throwing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in binary digits format (i.e., a sequence of bits).

        :return self.dice_throwing_outcome_bits: the classical_regime outcome (i.e., the observation) from the Dice Throwing,
                                                 through the execution of the respective Qiskrypt's Quantum Circuit,
                                                 in binary digits format (i.e., a sequence of bits).
        """

        if self.is_already_thrown():
            """
            If the Dice was already thrown.          
            """

            """
            Return the classical_regime outcome (i.e., the observation) from the Dice Throwing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in binary digits format (i.e., a sequence of bits).
            """
            return self.dice_throwing_outcome_bits

        else:
            """
            If the Dice was not thrown yet.          
            """

            """
            Return/Raise a Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
            """
            self.raise_dice_not_thrown_yet_error()

    def get_dice_throwing_outcome_bits_as_int_base_2(self) -> int:
        """
        Return the classical_regime outcome (i.e., the observation) from the Dice Throwing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in an integer base-2 format (i.e., an integer representation of bits).

        :return int(self.dice_throwing_outcome_bits, base=2): the classical_regime outcome (i.e., the observation) from
                                                              the Dice Throwing, through the execution of
                                                              the respective Qiskrypt's Quantum Circuit,
                                                              in an integer base-2 format
                                                              (i.e., an integer representation of bits).
        """

        if self.is_already_thrown():
            """
            If the Dice was already thrown.          
            """

            """
            Return the classical_regime outcome (i.e., the observation) from the Dice Throwing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in an integer base-2 format (i.e., an integer representation of a bit).
            """
            return int(self.dice_throwing_outcome_bits, base=2)

        else:
            """
            If the Dice was not thrown yet.          
            """

            """
            Return/Raise a Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
            """
            self.raise_dice_not_thrown_yet_error()

    def get_dice_throwing_num_points(self) -> int:
        """
        Return the number of points corresponding to
        the classical_regime outcome (i.e., the observation) from the Dice Throwing,
        through the execution of the respective Qiskrypt's Quantum Circuit,
        in an integer base-2 format (i.e., an integer representation of bits).

        :return self.get_dice_throwing_outcome_bits_as_int_base_2() + 1: the number of points corresponding to
                                                                         the classical_regime outcome (i.e., the observation) from
                                                                         the Dice Throwing, through the execution of
                                                                         the respective Qiskrypt's Quantum Circuit,
                                                                         in an integer base-2 format
                                                                         (i.e., an integer representation of bits).
        """

        if self.is_already_thrown():
            """
            If the Dice was already thrown.          
            """

            """
            Return the number of points corresponding to
            the classical_regime outcome (i.e., the observation) from the Dice Throwing,
            through the execution of the respective Qiskrypt's Quantum Circuit,
            in an integer base-2 format (i.e., an integer representation of a bit).
            """
            return int(self.dice_throwing_outcome_bits, base=2) + 1

        else:
            """
            If the Dice was not thrown yet.          
            """

            """
            Return/Raise a Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
            """
            self.raise_dice_not_thrown_yet_error()

    def configure(self, dice_type: str) -> None:
        """
        Configure the Qiskrypt's Quantum Dice Throwing,
        given the type of Dice for its configuration.

        :param dice_type: the type of the Dice for
                          the Qiskrypt's Quantum Dice Throwing.
        """

        if not self.is_configured():
            """
            If the Qiskrypt's Quantum Dice Throwing is not configured yet.
            """

            if dice_type in DICE_TYPES:
                """
                If the given type of the Dice for
                the Qiskrypt's Quantum Dice Throwing is valid.
                """

                self.dice_type = dice_type
                """
                Set the Dice type of the configuration to be used on
                the Qiskrypt's Quantum Dice Throwing,
                according to the given Dice type.
                """

                self.num_dice_sides = NUM_SIDES_FOR_DICE_TYPES[dice_type]
                """
                Set the number of sides of the Dice configured for
                the Qiskrypt's Quantum Dice Throwing, from the size given.
                """

                num_qubits = num_bits = ceil(log2(self.num_dice_sides))
                """
                Set the number of qubits and bits, according to
                the respective number of sides of the Dice configured.
                """

                qiskrypt_quantum_register_quantum_dice_throwing = \
                    QiskryptQuantumRegister("qu_reg_dice_throw", num_qubits)
                """
                Create a Qiskrypt's Quantum Register for the current Qiskrypt's Quantum Dice Throwing,
                with a number of qubits corresponding to the respective number of sides of the Dice configured.
                """

                qiskrypt_classical_register_quantum_dice_throwing = \
                    QiskryptClassicalRegister("cl_reg_dice_throw", num_bits)
                """
                Create a Qiskrypt's Classical Register for the current Qiskrypt's Quantum Dice Throwing,
                with a number of bits corresponding to the respective number of sides of the Dice configured.
                """

                qiskrypt_quantum_circuit = \
                    QiskryptQuantumCircuit("qu_circ_dice_throw",
                                           qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_dice_throwing],
                                           qiskrypt_fully_quantum_registers=None,
                                           qiskrypt_semi_quantum_registers=None,
                                           qiskrypt_ancilla_quantum_registers=None,
                                           qiskrypt_ancilla_fully_quantum_registers=None,
                                           qiskrypt_ancilla_semi_quantum_registers=None,
                                           qiskrypt_classical_registers=[qiskrypt_classical_register_quantum_dice_throwing],
                                           global_phase=0, qiskit_quantum_circuit=None)
                """
                Create a Qiskrypt's Quantum Circuit with the both previously created
                Qiskrypt's Quantum Register and Qiskrypt's Classical Register.
                """

                self.qiskrypt_quantum_hadamard_transform = \
                    QiskryptQuantumHadamardTransform("quantum_hadamard_transform_qrg",
                                                     qiskrypt_quantum_circuit,
                                                     ([0] * num_qubits),
                                                     [*range(num_qubits)])
                """
                Setup the currently created Qiskrypt's Quantum Hadamard Transform for
                the Qiskrypt's Quantum Dice Throwing.
                """

                self.qiskrypt_quantum_hadamard_transform.apply_transform()
                """
                Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved
                in the current Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Dice Throwing.
                """

                self.qiskrypt_quantum_hadamard_transform \
                    .qiskrypt_quantum_circuit.measure_all_qubits_in_qiskit_quantum_register(0, 0)
                """
                Measure all the qubits in the IBM Qiskit's Quantum Register to
                the IBM Qiskit's Classical Register, in the Qiskrypt's Quantum Circuit of
                the current Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Dice Throwing.
                """

            else:
                """
                If the given type of the Dice for
                the Qiskrypt's Quantum Dice Throwing is not valid.
                """

                """
                Return/Raise a Dice Type Not Valid Error for
                the Qiskrypt's Quantum Dice Throwing.
                """
                self.raise_dice_type_not_valid_error()

            self.configured = True
            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Quantum Dice Throwing is configured or not, as True.
            """

        else:
            """
            If the Qiskrypt's Quantum Dice Throwing is already configured.
            """

            """
            Return/Raise a Dice Already Configured Error for
            the Qiskrypt's Quantum Dice Throwing.
            """
            self.raise_dice_already_configured_error()

    def reset(self):
        """
        Reset the Qiskrypt's Quantum Dice Throwing.
        """

        self.dice_type = None
        """
        Set the dice type of the configuration to be used on
        the Qiskrypt's Quantum Dice Throwing, as None.
        """

        self.num_dice_sides = 0
        """
        Set the size of the Qiskrypt's Quantum Dice Throwing, as zero.
        """

        self.configured = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Quantum Dice Throwing is configured or not, as False.
        """

    def throw_dice(self):
        """
        Throw the Dice related to the Qiskrypt's Quantum Dice Throwing,
        through the application of the Quantum Hadamard Transformation
        to the respective qubits, execution of the respective Qiskrypt's Quantum Circuit
        and the measurement of all that qubits representing the Dice in an equally and distributed
        Quantum Superposition all over their possible classical_regime results/outcomes (observations),
        storing, the final classical_regime result/outcome from the observation of it, in a sequence of bits.
        """

        if not self.is_already_thrown() and self.is_configured():
            """
            If the Dice is not already thrown and
            the Qiskrypt's Quantum Dice Throwing is already configured.
            """

            qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
            """
            Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
            (i.e., the classical_regime simulation of an IBM Qiskit's Quantum Circuit).
            """

            final_results_frequency_counting = \
                execute(self.qiskrypt_quantum_hadamard_transform
                        .qiskrypt_quantum_circuit.get_qiskit_quantum_circuit(),
                        qiskit_qasm_backend, shots=1).result().get_counts()
            """
            Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
            and store the resulted measurement of its final quantum_regime state.
            """

            self.dice_throwing_outcome_bits = \
                bin(int(final_results_frequency_counting.most_frequent(), base=2))
            """
            Set the bit outcome for the Dice Throwing,
            from the measurement of the Qiskrypt's Quantum Circuit for
            the Qiskrypt's Quantum Coin Tossing, as the resulted outcome
            from the measurement of the IBM Qiskit's Quantum Circuit,
            in an binary format (i.e., the Python's representation for a bit).
            """

            self.already_thrown = True
            """
            Set the boolean flag to keep information about if
            the Dice was already thrown or not, as True.
            """

            while (self.get_dice_throwing_num_points() is None) \
                or (self.get_dice_throwing_num_points() > self.num_dice_sides):
                """
                                
                """

                final_results_frequency_counting = \
                    execute(self.qiskrypt_quantum_hadamard_transform
                            .qiskrypt_quantum_circuit.get_qiskit_quantum_circuit(),
                            qiskit_qasm_backend, shots=1).result().get_counts()
                """
                Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
                and store the resulted measurement of its final quantum_regime state.
                """

                self.dice_throwing_outcome_bits = \
                    bin(int(final_results_frequency_counting.most_frequent(), base=2))
                """
                Set the bit outcome for the Dice Throwing,
                from the measurement of the Qiskrypt's Quantum Circuit for
                the Qiskrypt's Quantum Coin Tossing, as the resulted outcome
                from the measurement of the IBM Qiskit's Quantum Circuit,
                in an binary format (i.e., the Python's representation for a bit).
                """

        else:
            """
            If the Dice is already thrown and/or
            the Qiskrypt's Quantum Circuit for the Qiskrypt's Quantum Dice Throwing is not configured yet.
            """

            if not self.is_configured():
                """
                If the Qiskrypt's Quantum Dice Throwing is not configured yet.
                """

                """
                Return/Raise a Dice Not Configured Yet Error for
                the Qiskrypt's Quantum Dice Throwing.
                """
                self.raise_dice_already_configured_error()

            if self.is_already_thrown():
                """
                If the Dice was already thrown.
                """

                """
                Return/Raise a Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
                """
                self.raise_dice_already_thrown_error()

    @staticmethod
    def raise_dice_type_not_valid_error() -> None:
        """
        Return/Raise a Dice Type Not Valid Error for the Qiskrypt's Quantum Dice Throwing.

        :raise dice_type_not_valid_error: a Dice Type Not Valid Error for
                                          the Qiskrypt's Quantum Dice Throwing.
        """

        dice_type_not_valid_error = QiskryptQuantumDiceThrowingDiceTypeNotValidError()
        """
        Retrieve the Dice Type Not Valid Error for the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Raise the Dice Type Not Valid Error for the Qiskrypt's Quantum Dice Throwing.
        """
        raise dice_type_not_valid_error

    @staticmethod
    def raise_dice_not_configured_yet_error() -> None:
        """
        Return/Raise a Dice Not Configured Yet Error for the Qiskrypt's Quantum Dice Throwing.

        :raise dice_not_configured_yet_error: a Dice Not Configured Yet Error for
                                              the Qiskrypt's Quantum Dice Throwing.
        """

        dice_not_configured_yet_error = QiskryptQuantumDiceThrowingDiceNotConfiguredYetError()
        """
        Retrieve the Dice Not Configured Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Raise the Dice Not Configured Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """
        raise dice_not_configured_yet_error

    @staticmethod
    def raise_dice_already_configured_error() -> None:
        """
        Return/Raise a Dice Already Configured Error for the Qiskrypt's Quantum Dice Throwing.

        :raise dice_already_configured_error: a Dice Already Configured Error for
                                              the Qiskrypt's Quantum Dice Throwing.
        """

        dice_already_configured_error = QiskryptQuantumDiceThrowingDiceAlreadyConfiguredError()
        """
        Retrieve the Dice Already Configured Error for the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Raise the Dice Already Configured Error for the Qiskrypt's Quantum Dice Throwing.
        """
        raise dice_already_configured_error

    @staticmethod
    def raise_dice_not_thrown_yet_error() -> None:
        """
        Return/Raise a Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.

        :raise dice_not_thrown_yet_error: a Dice Not Thrown Yet Error for
                                          the Qiskrypt's Quantum Dice Throwing.
        """

        dice_not_thrown_yet_error = QiskryptQuantumDiceThrowingDiceNotThrownYetError()
        """
        Retrieve the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Raise the Dice Not Thrown Yet Error for the Qiskrypt's Quantum Dice Throwing.
        """
        raise dice_not_thrown_yet_error

    @staticmethod
    def raise_dice_already_thrown_error() -> None:
        """
        Return/Raise a Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.

        :raise dice_already_thrown_error: a Dice Already Thrown Error for
                                          the Qiskrypt's Quantum Dice Throwing.
        """

        dice_already_thrown_error = QiskryptQuantumDiceThrowingDiceAlreadyThrownError()
        """
        Retrieve the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
        """

        """
        Raise the Dice Already Thrown Error for the Qiskrypt's Quantum Dice Throwing.
        """
        raise dice_already_thrown_error
