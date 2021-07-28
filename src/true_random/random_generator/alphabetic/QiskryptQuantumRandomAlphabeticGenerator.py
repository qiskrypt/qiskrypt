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
import string

"""
Import required Libraries and Packages.
"""

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
"""

from src.true_random.random_generator.QiskryptQuantumRandomGenerator \
    import QiskryptQuantumRandomGenerator
"""
Import the Qiskrypt's Quantum Random Generator.
"""

"""
Definition of Constants and Enumerations.
"""

NUM_BITS_FOR_ONE_BYTE = 8
"""
The number of bits of a byte.
"""

NUM_BYTES_SHORT_INTEGER = 2
"""
The number of bytes for a Short Integer.
"""


class QiskryptQuantumRandomAlphabeticGenerator(QiskryptQuantumRandomGenerator):
    """
    Object class for the Qiskrypt's Quantum Random Alphabetic Generator.
    """

    def __init__(self, name: str):
        """
        Constructor of the Qiskrypt's Quantum Random Alphabetic Generator.

        :param name: the name of the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        super().__init__(name)
        """
        Calls the constructor of the super-class Qiskrypt's Quantum Random Generator.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Random Alphabetic Generator.

        :return super().get_name(): the name of the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Return the name of the Qiskrypt's Quantum Random Alphabetic Generator.
        """
        return super().get_name()

    def get_qiskrypt_quantum_hadamard_transforms(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Alphabetic Generator.

        :return super().get_qiskrypt_quantum_hadamard_transform(): the list of the Qiskrypt's
                                                                   Quantum Hadamard Transform of
                                                                   the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """
        return super().get_qiskrypt_quantum_hadamard_transforms()

    def get_size(self) -> int:
        """
        Return the size of the Qiskrypt's Quantum Random Alphabetic Generator,
        regarding the number of qubits and bits being used.

        :return super().get_size(): the size of the Qiskrypt's Quantum Random Alphabetic Generator,
                                    regarding the number of qubits and bits being used.
        """

        """
        Return the size of the Qiskrypt's Quantum Random Alphabetic Generator,
        regarding the number of qubits and bits being used.
        """
        return super().get_size()

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Alphabetic Generator is configured or not.

        :return super().is_configured(): the boolean flag to keep the information about if
                                         the Qiskrypt's Quantum Random Alphabetic Generator is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Alphabetic Generator is configured or not.
        """
        return super().is_configured()

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Alphabetic Generator.

        :return super().get_creation_timestamp(): the current DateTime format for the timestamp of
                                                  the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """
        return super().get_creation_timestamp()

    def initiate(self, size: int) -> None:
        """
        Configure the Qiskrypt's Quantum Random Alphabetic Generator,
        given a size for the Qiskrypt's Quantum Random Alphabetic Generator.

        :param size: the size of the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        super().configure((size * NUM_BITS_FOR_ONE_BYTE * NUM_BYTES_SHORT_INTEGER))
        """
        Configure the Qiskrypt's Quantum Random Alphabetic Generator, given its size.
        """

    def reset(self) -> None:
        """
        Reset the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        super().reset()
        """
        Reset the Qiskrypt's Quantum Random Alphabetic Generator.
        """

    def generate_alphabetic_string(self, use_lowercase=True, use_uppercase=True, use_punctuation=True) -> str:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        in a binary format (i.e., a sequence of bits).

        :param use_lowercase: the boolean flag to keep the information about if
                              it is pretended to use lowercase characters or not.
        :param use_uppercase: the boolean flag to keep the information about if
                              it is pretended to use uppercase characters or not.
        :param use_punctuation: the boolean flag to keep the information about if
                                it is pretended to use punctuation or not.

        :return alphabetic_string: a alphabetic string from
                                   the Qiskrypt's Quantum Random Alphabetic Generator,
                                   in a string format (i.e., a sequence of characters).
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Alphabetic Generator is already configured.
            """

            if use_lowercase or use_uppercase or use_punctuation:
                """
                If, at least, some of the boolean flags to keep information about if
                it is pretended to use uppercase characters, lowercase characters or
                punctuation or not, is set to True.
                """

                qiskrypt_quantum_hadamard_transforms = \
                    self.get_qiskrypt_quantum_hadamard_transforms()
                """
                Retrieve the list of the Qiskrypt's Quantum Hadamard Transforms of
                the Qiskrypt's Quantum Random Alphabetic Generator.
                """

                num_qiskrypt_quantum_hadamard_transforms = \
                    len(qiskrypt_quantum_hadamard_transforms)
                """
                Retrieve the number of the Qiskrypt's Quantum Hadamard Transforms of
                the Qiskrypt's Quantum Random Alphabetic Generator.
                """

                binary_string = ""
                """
                Initialise the binary string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator.
                """

                for current_num_qiskrypt_quantum_hadamard_transform \
                    in range(num_qiskrypt_quantum_hadamard_transforms):
                    """
                    For each Qiskrypt's Quantum Hadamard Transform of
                    the Qiskrypt's Quantum Random Alphabetic Generator.
                    """

                    qiskrypt_quantum_hadamard_transform = \
                        qiskrypt_quantum_hadamard_transforms[current_num_qiskrypt_quantum_hadamard_transform]
                    """
                    Retrieve the current Qiskrypt's Quantum Hadamard Transform of
                    the Qiskrypt's Quantum Random Alphabetic Generator.
                    """

                    qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
                    """
                    Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
                    (i.e., the classical simulation of an IBM Qiskit's Quantum Circuit).
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
                    the Qiskrypt's Quantum Random Alphabetic Generator.
                    """

                binary_string_bits = format(int(binary_string, base=2), f"#0{(self.get_size() + 2)}b")
                """
                Convert the binary string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator,
                in a binary format (i.e., a sequence of bits).
                """

                available_alphabet = ""
                """
                Initialise the available Alphabet, as an empty string.
                """

                if use_lowercase:
                    """
                    If the boolean flag to keep the information about if
                    it is pretended to use lowercase characters or not, is True.
                    """

                    available_alphabet += string.ascii_lowercase
                    """
                    Append the ASCII lowercase characters to the available Alphabet.
                    """

                if use_uppercase:
                    """
                    If the boolean flag to keep the information about if
                    it is pretended to use uppercase characters or not, is True.
                    """

                    available_alphabet += string.ascii_uppercase
                    """
                    Append the ASCII uppercase characters to the available Alphabet.
                    """

                if use_punctuation:
                    """
                    If the boolean flag to keep the information about if
                    it is pretended to use punctuation or not, is True.
                    """

                    available_alphabet += string.punctuation
                    """
                    Append the punctuation characters to the available Alphabet.
                    """

                binary_string_bits_size = len(binary_string_bits[2:])
                """
                Retrieve the length of the binary string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator,
                in a binary format (i.e., a sequence of bits). 
                """

                num_short_integer_binary_blocks_for_alphabet_indexes = \
                    int(binary_string_bits_size / (NUM_BITS_FOR_ONE_BYTE * NUM_BYTES_SHORT_INTEGER))
                """
                Compute the number of indexes of Short Integer Binary Blocks for the sample choices of the Alphabet.
                """

                alphabetic_string = ""
                """
                Initialise the alphabetic string, as an empty string.
                """

                for short_integer_binary_block_for_alphabet_index \
                        in range(num_short_integer_binary_blocks_for_alphabet_indexes):
                    """
                    For each index of Short Integer binary block for
                    the sample choices of the available Alphabet.
                    """

                    offset_binary_block_start = (short_integer_binary_block_for_alphabet_index *
                                                 NUM_BITS_FOR_ONE_BYTE * NUM_BYTES_SHORT_INTEGER)
                    """
                    Compute the Offset of the start of the current binary block from the binary string generated.
                    """

                    offset_binary_block_end = ((short_integer_binary_block_for_alphabet_index + 1) *
                                                NUM_BITS_FOR_ONE_BYTE * NUM_BYTES_SHORT_INTEGER)
                    """
                    Compute the Offset of the end of the current binary block from the binary string generated.
                    """

                    short_integer_binary_block = binary_string[(2 + offset_binary_block_start):(2 + offset_binary_block_end)]
                    """
                    Retrieve the current binary block from the binary string generated.
                    """

                    alphabet_index = int(((int(short_integer_binary_block, base=2)) *
                                          len(available_alphabet)) / (2**16 - 1))
                    """
                    Compute and re-scale the computed binary block for
                    the current sample choice of the available Alphabet.
                    """

                    alphabetic_string += available_alphabet[alphabet_index]
                    """
                    Retrieve the current sample choice of the available Alphabet and append it to
                    the alphabetic string being generated.
                    """

                """
                Return the alphabetic string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator,
                in a alphabetic format (i.e., a sequence of characters).
                """
                return alphabetic_string

            else:
                """
                If none of the boolean flags to keep information about if
                it is pretended to use uppercase characters, lowercase characters or
                punctuation or not, is set to True.
                """

                # TODO - Throw Exception

        else:
            """
            If the Qiskrypt's Quantum Random Binary Generator is not configured yet.
            """

            # TODO - Throw exception
