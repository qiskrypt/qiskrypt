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

from src.true_random.random_generator.QiskryptQuantumRandomGenerator \
    import QiskryptQuantumRandomGenerator
"""

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
        Calls the constructor of the super-class Qiskrypt's Quantum Random Generator.
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
        Return the list of the Qiskrypt's Quantum Hadamard Transform of
        the Qiskrypt's Quantum Random Binary Generator.

        :return super().get_qiskrypt_quantum_hadamard_transform(): the list of the Qiskrypt's Quantum Hadamard Transform of
                                                                   the Qiskrypt's Quantum Random Binary Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transform of
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

    def configure(self, size: int) -> None:
        """
        Configure the Qiskrypt's Quantum Random Binary Generator,
        given a size for the Qiskrypt's Quantum Random Binary Generator.

        :param size: the size of the Qiskrypt's Quantum Random Binary Generator.
        """

        super().configure(size)
        """
        Configure the Qiskrypt's Quantum Random Binary Generator,
        given a size for the Qiskrypt's Quantum Random Binary Generator.
        """

    def reset(self):
        """
        Reset the Qiskrypt's Quantum Random Binary Generator.
        """

        super().reset()
        """
        Reset the Qiskrypt's Quantum Random Binary Generator.
        """

    def generate_binary_string(self) -> str:
        """
        Return a generated binary string

        :return:
        """

    def generate_binary_string_as_int_base_2(self) -> int:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Binary Generator,
        in an integer base-2 format (i.e., an integer representation of a bit).

        :return: a binary string from
                 the Qiskrypt's Quantum Random Binary Generator,
                 in an integer base-2 format (i.e., an integer representation of a bit)
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

            # TODO - Throw exception
