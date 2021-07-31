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

from string import ascii_lowercase, ascii_uppercase, punctuation
"""
Import the ASCII's lowercase characters,
the ASCII's uppercase characters and punctuation from
the String Python's library.
"""

from math import ceil, log2
"""
Import the Logarithm of Base-2 and the  Ceil mathematical function from
the Math Python's library.
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

from src.true_random.random_generator.alphabetic.exception.QiskryptQuantumRandomAlphabeticGeneratorException \
    import QiskryptQuantumRandomAlphabeticGeneratorNoCharactersGroupChosenError
"""
Import the No Characters Group Chosen Error for
the Qiskrypt's Quantum Random Alphabetic Generator.
"""


class QiskryptQuantumRandomAlphabeticGenerator(QiskryptQuantumRandomGenerator):
    """
    Object class for the Qiskrypt's Quantum Random Alphabetic Generator.
    """

    def __init__(self, name: str, lowercase_flag=True, uppercase_flag=True, punctuation_flag=True):
        """
        Constructor of the Qiskrypt's Quantum Random Alphabetic Generator.

        :param name: the name of the Qiskrypt's Quantum Random Alphabetic Generator.
        :param lowercase_flag: the boolean flag to keep the information about if
                               it is pretended to use lowercase characters or not.
        :param uppercase_flag: the boolean flag to keep the information about if
                               it is pretended to use uppercase characters or not.
        :param punctuation_flag: the boolean flag to keep the information about if
                                 it is pretended to use punctuation or not.
        """

        super().__init__(name)
        """
        Calls the constructor of the super-class Qiskrypt's Quantum Random Generator.
        """

        self.lowercase_flag = lowercase_flag
        """
        Set the boolean flag to keep the information about if
        it is pretended to use lowercase characters or not. 
        """

        self.uppercase_flag = uppercase_flag
        """
        Set the boolean flag to keep the information about if
        it is pretended to use uppercase characters or not.
        """

        self.punctuation_flag = punctuation_flag
        """
        Set the boolean flag to keep the information about if
        it is pretended to use punctuation or not.
        """

        self.available_alphabet = ""
        """
        Initialise the available Alphabet, as an empty string.
        """

        if self.lowercase_flag:
            """
            If the boolean flag to keep the information about if
            it is pretended to use lowercase characters or not, is True.
            """

            self.available_alphabet += ascii_lowercase
            """
            Append the ASCII lowercase characters to the available Alphabet.
            """

        if self.uppercase_flag:
            """
            If the boolean flag to keep the information about if
            it is pretended to use uppercase characters or not, is True.
            """

            self.available_alphabet += ascii_uppercase
            """
            Append the ASCII uppercase characters to the available Alphabet.
            """

        if self.punctuation_flag:
            """
            If the boolean flag to keep the information about if
            it is pretended to use punctuation or not, is True.
            """

            self.available_alphabet += punctuation
            """
            Append the punctuation characters to the available Alphabet.
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

    def use_lowercase(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        it is pretended to use lowercase characters or not.

        :return self.lowercase_flag: the boolean flag to keep the information about if
                                     it is pretended to use lowercase characters or not.
        """

        """
        Return the boolean flag to keep the information about if
        it is pretended to use lowercase characters or not.
        """
        return self.lowercase_flag

    def use_uppercase(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        it is pretended to use uppercase characters or not.

        :return self.uppercase_flag: the boolean flag to keep the information about if
                                     it is pretended to use uppercase characters or not.
        """

        """
        Return the boolean flag to keep the information about if
        it is pretended to use uppercase characters or not.
        """
        return self.uppercase_flag

    def use_punctuation(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        it is pretended to use punctuation or not.

        :return self.punctuation_flag: the boolean flag to keep the information about if
                                       it is pretended to use punctuation or not.
        """

        """
        Return the boolean flag to keep the information about if
        it is pretended to use punctuation or not.
        """
        return self.punctuation_flag

    def get_available_alphabet(self) -> str:
        """
        Return the available Alphabet for
        the Qiskrypt's Quantum Random Alphabetic Generator.

        :return self.available_alphabet: the available Alphabet for
                                         the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Return the available Alphabet for
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """
        return self.available_alphabet

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

        length_binary_string_for_choices = ceil(log2(len(self.available_alphabet)))
        """
        Set the length of the binary string,
        representing the possible choices for the available Alphabet.
        """

        super().configure((size * length_binary_string_for_choices))
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

    def generate_alphabetic_string(self) -> str:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Alphabetic Generator,
        in a string format (i.e., a sequence of characters and punctuation).

        :return alphabetic_string: a alphabetic string from the Qiskrypt's
                                   Quantum Random Alphabetic Generator, in a string format
                                   (i.e., a sequence of characters and punctuation).
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Alphabetic Generator is already configured.
            """

            if self.lowercase_flag or self.uppercase_flag or self.punctuation_flag:
                """
                If, at least, some of the boolean flags to keep information about if
                it is pretended to use uppercase characters, lowercase characters or
                punctuation, or not, is set to True.
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
                        execute(qiskrypt_quantum_hadamard_transform.get_qiskrypt_quantum_circuit()
                                .get_qiskit_quantum_circuit(),
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

                binary_string_bits_size = len(binary_string_bits[2:])
                """
                Retrieve the length of the binary string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator,
                in a binary format (i.e., a sequence of bits). 
                """

                num_binary_alphabet_indexes = \
                    int(binary_string_bits_size / ceil(log2(len(self.available_alphabet))))
                """
                Compute the number of indexes of small integers of base-2 binary blocks for
                the sample choices of the Alphabet.
                """

                alphabetic_string = ""
                """
                Initialise the alphabetic string, as an empty string.
                """

                for num_binary_alphabet_index in range(num_binary_alphabet_indexes):
                    """
                    For each index of small integers of base-2 binary block for
                    the sample choices of the available Alphabet.
                    """

                    offset_binary_block_start = (num_binary_alphabet_index * ceil(log2(len(self.available_alphabet))))
                    """
                    Compute the Offset of the start of the current binary block from the binary string generated.
                    """

                    offset_binary_block_end = ((num_binary_alphabet_index + 1) * ceil(log2(len(self.available_alphabet))))
                    """
                    Compute the Offset of the end of the current binary block from the binary string generated.
                    """

                    alphabet_binary_block = \
                        binary_string[(2 + offset_binary_block_start):(2 + offset_binary_block_end)]
                    """
                    Retrieve the current binary block from the binary string generated.
                    """

                    alphabet_index = int(((int(alphabet_binary_block, base=2)) *
                                          (len(self.available_alphabet)) - 1) /
                                         (2 ** (ceil(log2(len(self.available_alphabet)))) - 1))
                    """
                    Compute and re-scale the computed binary block for
                    the current sample choice of the available Alphabet.
                    """

                    alphabetic_string += self.available_alphabet[alphabet_index]
                    """
                    Retrieve the current sample choice of the available Alphabet and append it to
                    the alphabetic string being generated.
                    """

                """
                Return the alphabetic string generated from
                the Qiskrypt's Quantum Random Alphabetic Generator,
                in an alphabetic format (i.e., a sequence of characters).
                """
                return alphabetic_string

            else:
                """
                If none of the boolean flags to keep information about if
                it is pretended to use uppercase characters, lowercase characters or
                punctuation, or not, is set to True.
                """

                """
                Return/Raise a No Characters Group Chosen Error for
                the Qiskrypt's Quantum Random Alphabetic Generator.
                """
                self.raise_no_characters_group_chosen_error()

        else:
            """
            If the Qiskrypt's Quantum Random Alphabetic Generator is not configured yet.
            """

            """
            Return/Raise a Quantum Random Generator Not Configured Yet Error for
            the Qiskrypt's Quantum Random Generator.
            """
            super().raise_quantum_random_generator_not_configured_yet_error()

    @staticmethod
    def raise_no_characters_group_chosen_error() -> None:
        """
        Return/Raise a No Characters Group Chosen Error for
        the Qiskrypt's Quantum Random Alphabetic Generator.

        :raise no_characters_group_chosen_error: a No Characters Group Chosen Error for
                                                 the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        no_characters_group_chosen_error = \
            QiskryptQuantumRandomAlphabeticGeneratorNoCharactersGroupChosenError()
        """
        Retrieve the No Characters Group Chosen Error for
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """

        """
        Raise the No Characters Group Chosen Error for
        the Qiskrypt's Quantum Random Alphabetic Generator.
        """
        raise no_characters_group_chosen_error
