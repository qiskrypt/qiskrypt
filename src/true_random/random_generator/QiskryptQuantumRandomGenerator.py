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

"""

"""
Import required Libraries and Packages.
"""


from src.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
from src.circuit.registers.classical.QiskryptClassicalRegister import QiskryptClassicalRegister
from src.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
from src.true_random.transforms.QiskryptQuantumHadamardTransform import QiskryptQuantumHadamardTransform


from datetime import datetime
"""

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

        self.qiskrypt_quantum_hadamard_transform = None
        """
        Set the Qiskrypt's Quantum Hadamard Transform, as None.
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

    def get_qiskrypt_quantum_hadamard_transform(self) -> QiskryptQuantumHadamardTransform:
        """
        Return the Qiskrypt's Quantum Hadamard Transform.

        :return self.qiskrypt_quantum_hadamard_transform: the Qiskrypt's Quantum Hadamard Transform.
        """

        """
        Return the Qiskrypt's Quantum Hadamard Transform.
        """
        return self.qiskrypt_quantum_hadamard_transform

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

            qiskrypt_quantum_register_quantum_hadamard_transform = \
                QiskryptQuantumRegister("qu_reg_qrg", self.size)
            """
            Create a Qiskrypt's Quantum Register for the Qiskrypt's Quantum Hadamard Transform,
            with a number of qubits corresponding to the size of the Qiskrypt's Quantum Random Generator.
            """

            qiskrypt_classical_register_quantum_hadamard_transform = \
                QiskryptClassicalRegister("cl_reg_qrg", self.size)
            """
            Create a Qiskrypt's Classical Register for the Qiskrypt's Quantum Hadamard Transform,
            with a number of bits corresponding to the size of the Qiskrypt's Quantum Random Generator.
            """

            qiskrypt_quantum_circuit = \
                QiskryptQuantumCircuit("qu_circ_qrg",
                                       qiskrypt_quantum_registers=[qiskrypt_quantum_register_quantum_hadamard_transform],
                                       qiskrypt_fully_quantum_registers=None,
                                       qiskrypt_semi_quantum_registers=None,
                                       qiskrypt_ancilla_quantum_registers=None,
                                       qiskrypt_ancilla_fully_quantum_registers=None,
                                       qiskrypt_ancilla_semi_quantum_registers=None,
                                       qiskrypt_classical_registers=[qiskrypt_classical_register_quantum_hadamard_transform],
                                       global_phase=0, qiskit_quantum_circuit=None)
            """
            Create a Qiskrypt's Quantum Circuit with the previously created Qiskrypt's Quantum Register.
            """

            self.qiskrypt_quantum_hadamard_transform = \
                QiskryptQuantumHadamardTransform("quantum_hadamard_transform_qrg",
                                                 qiskrypt_quantum_circuit,
                                                 ([0] * self.size), [*range(self.size)])
            """
            Setup the Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Random Generator.
            """

            self.qiskrypt_quantum_hadamard_transform.apply_transform()
            """
            Apply the Quantum Hadamard Transform to the Qiskrypt's Quantum Registers and qubits involved
            in the Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Random Generator.
            """

            self.qiskrypt_quantum_hadamard_transform\
                .qiskrypt_quantum_circuit.measure_all_qubits_in_qiskit_quantum_register(0, 0)
            """
            Measure all the qubits in the IBM Qiskit's Quantum Register to
            the IBM Qiskit's Classical Register, in the Qiskrypt's Quantum Circuit of
            the Qiskrypt's Quantum Hadamard Transform for the Qiskrypt's Quantum Random Generator.
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

            # TODO Throw Exception

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
