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

from src.quantum.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""

from src.quantum.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum.transforms.hadamard.QiskryptQuantumHadamardTransform \
    import QiskryptQuantumHadamardTransform
"""
Import the Qiskrypt's Quantum Hadamard Transform.
"""

from datetime import datetime
"""
Import the DateTime Module from the DateTime Python's Library.
"""

"""
Definition of Constants and Enumerations.
"""

from src.quantum.common.utils.QiskryptLibraryParameters \
    import QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS
"""
Import the maximum number of Qubits for
the QASM (Quantum Assembly) Simulator of the IBM's Qiskit.
"""

from src.quantum.true_random.random_generator.exception.QiskryptQuantumRandomGeneratorException \
    import QiskryptQuantumRandomGeneratorNotConfiguredYetError
"""
Import the Quantum Random Generator Not Configured Yet Error for
the Qiskrypt's Quantum Random Generator.
"""

from src.quantum.true_random.random_generator.exception.QiskryptQuantumRandomGeneratorException \
    import QiskryptQuantumRandomGeneratorAlreadyConfiguredError
"""
Import the Quantum Random Generator Already Configured Error for
the Qiskrypt's Quantum Random Generator.
"""


class QiskryptQuantumRandomGenerator:
    """
    Object class for the Qiskrypt's Quantum Random Generator.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Quantum Random Generator.

        :param name: the name of the Qiskrypt's Quantum Random Generator.
        """

        self.name = name
        """
        Set the name for the Qiskrypt's Quantum Random Generator.
        """

        self.qiskrypt_quantum_hadamard_transforms = None
        """
        Set the Qiskrypt's Quantum Hadamard Transforms, as None.
        """

        self.size = 0
        """
        Set the size of the Qiskrypt's Quantum Random Generator,
        regarding the number of qubits and bits being used, as zero.
        """

        self.configured = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Generator is configured or not, as False.
        """

        self.creation_timestamp = datetime.now().timestamp()
        """
        Set the current DateTime format for the timestamp of
        the creation of the Qiskrypt's Quantum Random Generator.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Random Generator.

        :return self.name: the name of the Qiskrypt's Quantum Random Generator.
        """

        """
        Return the name of the Qiskrypt's Quantum Random Generator.
        """
        return self.name

    def get_qiskrypt_quantum_hadamard_transforms(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Generator.

        :return self.qiskrypt_quantum_hadamard_transforms: the list of the Qiskrypt's Quantum Hadamard Transforms of
                                                           the Qiskrypt's Quantum Random Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Generator.
        """
        return self.qiskrypt_quantum_hadamard_transforms

    def get_size(self) -> int:
        """
        Return the size of the Qiskrypt's Quantum Random Generator,
        regarding the number of qubits and bits being used.

        :return self.size: the size of the Qiskrypt's Quantum Random Generator,
                           regarding the number of qubits and bits being used.
        """

        """
        Return the size of the Qiskrypt's Quantum Random Generator,
        regarding the number of qubits and bits being used.
        """
        return self.size

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Generator is configured or not.

        :return self.configured: the boolean flag to keep the information about if
                                 the Qiskrypt's Quantum Random Generator is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Generator is configured or not.
        """
        return self.configured

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Generator.

        :return self.creation_timestamp: the current DateTime format for the timestamp of
                                         the Qiskrypt's Quantum Random Generator.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Generator.
        """
        return self.creation_timestamp

    def configure(self, size: int) -> None:
        """
        Configure the Qiskrypt's Quantum Random Generator,
        given a size for the Qiskrypt's Quantum Random Generator.

        :param size: the size of the Qiskrypt's Quantum Random Generator.
        """

        if not self.is_configured():
            """
            If the Qiskrypt's Quantum Random Generator is not configured yet.
            """

            self.size = size
            """
            Set the size of the Qiskrypt's Quantum Random Generator,
            regarding the number of qubits and bits being used, from the size given.
            """

            self.qiskrypt_quantum_hadamard_transforms = []
            """
            Set the Qiskrypt's Quantum Hadamard Transforms, as an empty list.
            """

            if (self.size % QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS) > 0:
                """
                If the size of the Qiskrypt's Quantum Random Generator is not multiple of
                the maximum number of qubits that can be simulated in
                the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                """

                num_qiskrypt_quantum_hadamard_transforms = (int(self.size / QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS) + 1)
                """
                Set the number of Qiskrypt's Quantum Hadamard Transforms,
                as being both the size of the Qiskrypt's Quantum Random Generator divided by
                the maximum number of qubits that can be simulated in
                the IBM Qiskit's QASM (Quantum Assembly) Simulator,
                plus one more Qiskrypt's Quantum Hadamard Transform for the remaining qubits.
                """

            else:
                """
                If the size of the Qiskrypt's Quantum Random Generator is multiple of
                the maximum number of qubits that can be simulated in the QASM (Quantum Assembly) Simulator.
                """

                num_qiskrypt_quantum_hadamard_transforms = int(self.size / QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS)
                """
                Set the number of Qiskrypt's Quantum Hadamard Transforms,
                as being only the size of the Qiskrypt's Quantum Random Generator divided by
                the maximum number of qubits that can be simulated in
                the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                """

            for current_num_qiskrypt_quantum_hadamard_transform in range(num_qiskrypt_quantum_hadamard_transforms):
                """
                For each Qiskrypt's Quantum Hadamard Transform to be created.
                """

                if current_num_qiskrypt_quantum_hadamard_transform != (num_qiskrypt_quantum_hadamard_transforms - 1):
                    """
                    If the current Qiskrypt's Quantum Hadamard Transform to be created is not the last one yet.
                    """

                    qiskrypt_quantum_register_quantum_hadamard_transform_size = QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS
                    """
                    Set the size of the current Qiskrypt's Quantum Hadamard Transform to be created,
                    as the maximum number of qubits that can be simulated in
                    the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                    """

                else:
                    """
                    If the current Qiskrypt's Quantum Hadamard Transform to be created is already the last one.
                    """

                    if (self.size % QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS) == 0:
                        """
                        If the number of qubits for the last Qiskrypt's Quantum Hadamard Transform,
                        is equal to the maximum number of qubits that can be simulated in
                        the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                        """

                        qiskrypt_quantum_register_quantum_hadamard_transform_size = \
                            QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS
                        """
                        Set the size of the current Qiskrypt's Quantum Hadamard Transform to be created,
                        as the remainder of the division of the size given initially by
                        the maximum number of qubits that can be simulated in
                        the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                        """

                    else:
                        """
                        If the number of qubits for the last Qiskrypt's Quantum Hadamard Transform,
                        is not equal to the maximum number of qubits that can be simulated in
                        the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                        """

                        qiskrypt_quantum_register_quantum_hadamard_transform_size = \
                            int(self.size % QISKIT_QASM_SIMULATOR_MAX_NUM_QUBITS)
                        """
                        Set the size of the current Qiskrypt's Quantum Hadamard Transform to be created,
                        as the remainder of the division of the size given initially by
                        the maximum number of qubits that can be simulated in
                        the IBM Qiskit's QASM (Quantum Assembly) Simulator.
                        """

                qiskrypt_quantum_register_quantum_hadamard_transform = \
                    QiskryptQuantumRegister(f"qu_reg_qrg_{(current_num_qiskrypt_quantum_hadamard_transform + 1)}",
                                            qiskrypt_quantum_register_quantum_hadamard_transform_size)
                """
                Create a Qiskrypt's Quantum Register for the current Qiskrypt's Quantum Hadamard Transform,
                with a number of qubits corresponding to its previously computed size.
                """

                qiskrypt_classical_register_quantum_hadamard_transform = \
                    QiskryptClassicalRegister(f"cl_reg_qrg_{(current_num_qiskrypt_quantum_hadamard_transform + 1)}",
                                              qiskrypt_quantum_register_quantum_hadamard_transform_size)
                """
                Create a Qiskrypt's Classical Register for the current Qiskrypt's Quantum Hadamard Transform,
                with a number of bits corresponding to its previously computed size.
                """

                qiskrypt_quantum_circuit = \
                    QiskryptQuantumCircuit(f"qu_circ_qrg_{(current_num_qiskrypt_quantum_hadamard_transform + 1)}",
                                           qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform],
                                           qiskrypt_fully_quantum_registers=None,
                                           qiskrypt_semi_quantum_registers=None,
                                           qiskrypt_ancilla_quantum_registers=None,
                                           qiskrypt_ancilla_fully_quantum_registers=None,
                                           qiskrypt_ancilla_semi_quantum_registers=None,
                                           qiskrypt_classical_registers=[qiskrypt_classical_register_quantum_hadamard_transform],
                                           global_phase=0, qiskit_quantum_circuit=None)
                """
                Create a Qiskrypt's Quantum Circuit with the both previously created
                Qiskrypt's Quantum Register and Qiskrypt's Classical Register.
                """

                qiskrypt_quantum_hadamard_transform = \
                    QiskryptQuantumHadamardTransform("quantum_hadamard_transform_qrg",
                                                     qiskrypt_quantum_circuit,
                                                     ([0] * qiskrypt_quantum_register_quantum_hadamard_transform_size),
                                                     [*range(qiskrypt_quantum_register_quantum_hadamard_transform_size)])
                """
                Setup the currently created Qiskrypt's Quantum Hadamard Transform for
                the Qiskrypt's Quantum Random Generator.
                """

                qiskrypt_quantum_hadamard_transform.apply_transform()
                """
                Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved
                in the current Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Random Generator.
                """

                qiskrypt_quantum_hadamard_transform\
                    .qiskrypt_quantum_circuit.measure_all_qubits_in_qiskit_quantum_register(0, 0)
                """
                Measure all the qubits in the IBM Qiskit's Quantum Register to
                the IBM Qiskit's Classical Register, in the Qiskrypt's Quantum Circuit of
                the current Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Random Generator.
                """

                self.qiskrypt_quantum_hadamard_transforms.append(qiskrypt_quantum_hadamard_transform)
                """
                Append the current created Qiskrypt's Quantum Hadamard Transform for
                the Qiskrypt's Quantum Random Generator.
                """

            self.configured = True
            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Quantum Random Generator is configured or not, as True.
            """

        else:
            """
            If the Qiskrypt's Quantum Random Generator is already configured.
            """

            """
            Return/Raise a Quantum Random Generator Already Configured Error for
            the Qiskrypt's Quantum Random Generator.
            """
            self.raise_quantum_random_generator_already_configured_error()

    def reset(self):
        """
        Reset the Qiskrypt's Quantum Random Generator.
        """

        self.size = 0
        """
        Set the size of the Qiskrypt's Quantum Random Generator, as zero.
        """

        self.configured = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Generator is configured or not, as False.
        """

    @staticmethod
    def raise_quantum_random_generator_not_configured_yet_error() -> None:
        """
        Return/Raise a Quantum Random Generator Not Configured Yet Error for
        the Qiskrypt's Quantum Random Generator.

        :raise quantum_random_generator_not_configured_yet_error: a Quantum Random Generator Not Configured Yet Error for
                                                                  the Qiskrypt's Quantum Random Generator.
        """

        quantum_random_generator_not_configured_yet_error = \
            QiskryptQuantumRandomGeneratorNotConfiguredYetError()
        """
        Retrieve the Quantum Random Generator Not Configured Yet Error for
        the Qiskrypt's Quantum Random Generator.
        """

        """
        Raise the Quantum Random Generator Not Configured Yet Error for
        the Qiskrypt's Quantum Random Generator.
        """
        raise quantum_random_generator_not_configured_yet_error

    @staticmethod
    def raise_quantum_random_generator_already_configured_error() -> None:
        """
        Return/Raise a Quantum Random Generator Already Configured Error for
        the Qiskrypt's Quantum Random Generator.

        :raise quantum_random_generator_already_configured_error: a Quantum Random Generator Already Configured Error for
                                                                  the Qiskrypt's Quantum Random Generator.
        """

        quantum_random_generator_already_configured_error = \
            QiskryptQuantumRandomGeneratorAlreadyConfiguredError()
        """
        Retrieve the Quantum Random Generator Already Configured Error for
        the Qiskrypt's Quantum Random Generator.
        """

        """
        Raise the Quantum Random Generator Already Configured Error for
        the Qiskrypt's Quantum Random Generator.
        """
        raise quantum_random_generator_already_configured_error
