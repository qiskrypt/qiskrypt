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

from src.quantum_regime.true_random.random_generator.QiskryptQuantumRandomGenerator \
    import QiskryptQuantumRandomGenerator
"""
Import the Qiskrypt's Quantum Random Generator.
"""


class QiskryptQuantumRandomBinaryGenerator(QiskryptQuantumRandomGenerator):
    """
    Object class for the Qiskrypt's Quantum Random Binary Generator.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Quantum Random Binary Generator.

        :param name: the name of the Qiskrypt's Quantum Random Binary Generator.
        """

        super().__init__(name)
        """
        Call of the constructor of the super-class Qiskrypt's Quantum Random Generator.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Random Binary Generator.

        :return super().get_name(): the name of the Qiskrypt's Quantum Random Binary Generator.
        """

        """
        Return the name of the Qiskrypt's Quantum Random Binary Generator.
        """
        return super().get_name()

    def get_qiskrypt_quantum_hadamard_transforms(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Binary Generator.

        :return super().get_qiskrypt_quantum_hadamard_transform(): the list of the Qiskrypt's
                                                                   Quantum Hadamard Transform of
                                                                   the Qiskrypt's Quantum Random Binary Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Binary Generator.
        """
        return super().get_qiskrypt_quantum_hadamard_transforms()

    def get_size(self) -> int:
        """
        Return the size of the Qiskrypt's Quantum Random Binary Generator,
        regarding the number of qubits and bits being used.

        :return super().get_size(): the size of the Qiskrypt's Quantum Random Binary Generator,
                                    regarding the number of qubits and bits being used.
        """

        """
        Return the size of the Qiskrypt's Quantum Random Binary Generator,
        regarding the number of qubits and bits being used.
        """
        return super().get_size()

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Binary Generator is configured or not.

        :return super().is_configured(): the boolean flag to keep the information about if
                                         the Qiskrypt's Quantum Random Binary Generator is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Binary Generator is configured or not.
        """
        return super().is_configured()

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Binary Generator.

        :return super().get_creation_timestamp(): the current DateTime format for the timestamp of
                                                  the Qiskrypt's Quantum Random Binary Generator.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Binary Generator.
        """
        return super().get_creation_timestamp()

    def initiate(self, size: int) -> None:
        """
        Configure the Qiskrypt's Quantum Random Binary Generator,
        given a size for the Qiskrypt's Quantum Random Binary Generator.

        :param size: the size of the Qiskrypt's Quantum Random Binary Generator.
        """

        super().configure(size)
        """
        Configure the Qiskrypt's Quantum Random Binary Generator, given its size.
        """

    def reset(self) -> None:
        """
        Reset the Qiskrypt's Quantum Random Binary Generator.
        """

        super().reset()
        """
        Reset the Qiskrypt's Quantum Random Binary Generator.
        """

    def generate_binary_string(self) -> str:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Binary Generator,
        in a binary format (i.e., a sequence of bits).

        :return binary_string_bits: a binary string from
                                    the Qiskrypt's Quantum Random Binary Generator,
                                    in a binary format (i.e., a sequence of bits).
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Binary Generator is already configured.
            """

            qiskrypt_quantum_hadamard_transforms = \
                self.get_qiskrypt_quantum_hadamard_transforms()
            """
            Retrieve the list of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Binary Generator.
            """

            num_qiskrypt_quantum_hadamard_transforms = \
                len(qiskrypt_quantum_hadamard_transforms)
            """
            Retrieve the number of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Binary Generator.
            """

            binary_string = ""
            """
            Initialise the binary string generated from
            the Qiskrypt's Quantum Random Binary Generator.
            """

            for current_num_qiskrypt_quantum_hadamard_transform \
                in range(num_qiskrypt_quantum_hadamard_transforms):
                """
                For each Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Binary Generator.
                """

                qiskrypt_quantum_hadamard_transform = \
                    qiskrypt_quantum_hadamard_transforms[current_num_qiskrypt_quantum_hadamard_transform]
                """
                Retrieve the current Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Binary Generator.
                """

                qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
                """
                Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
                (i.e., the classical_regime simulation of an IBM Qiskit's Quantum Circuit).
                """

                final_results_frequency_counting = \
                    execute(qiskrypt_quantum_hadamard_transform.get_qiskrypt_quantum_circuit().get_qiskit_quantum_circuit(),
                            qiskit_qasm_backend, shots=1).result().get_counts()
                """
                Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
                and store the resulted measurement of its final quantum state.
                """

                binary_string += final_results_frequency_counting.most_frequent()
                """
                Append the resulted outcome to the binary string generated from
                the Qiskrypt's Quantum Random Binary Generator.
                """

            binary_string_bits = format(int(binary_string, base=2), f"#0{(self.get_size() + 2)}b")
            """
            Convert the binary string generated from
            the Qiskrypt's Quantum Random Binary Generator,
            in a binary format (i.e., a sequence of bits).
            """

            """
            Return the binary string generated from
            the Qiskrypt's Quantum Random Binary Generator,
            in a binary format (i.e., a sequence of bits).
            """
            return binary_string_bits

        else:
            """
            If the Qiskrypt's Quantum Random Binary Generator is not configured yet.
            """

            """
            Return/Raise a Quantum Random Generator Not Configured Yet Error for
            the Qiskrypt's Quantum Random Generator.
            """
            super().raise_quantum_random_generator_not_configured_yet_error()

    def generate_binary_string_as_int_base_2(self) -> int:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Binary Generator,
        in an integer base-2 format (i.e., an integer representation of a bit).

        :return int(self.generate_binary_string(), base=2): a binary string from
                                                            the Qiskrypt's Quantum Random Binary Generator,
                                                            in an integer base-2 format
                                                            (i.e., an integer representation of a bit)
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Binary Generator is already configured.
            """

            """
            Generate a binary string and convert it to an integer base-2 format.            
            """
            return int(self.generate_binary_string(), base=2)

        else:
            """
            If the Qiskrypt's Quantum Random Binary Generator is not configured yet.
            """

            """
            Return/Raise a Quantum Random Generator Not Configured Yet Error for
            the Qiskrypt's Quantum Random Generator.
            """
            super().raise_quantum_random_generator_not_configured_yet_error()
