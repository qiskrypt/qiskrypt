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

from string import ascii_lowercase, ascii_uppercase, punctuation, digits
"""
Import the ASCII's lowercase characters,
the ASCII's uppercase characters, punctuation and digits from
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

from src.quantum_regime.true_random.random_generator.QiskryptQuantumRandomGenerator \
    import QiskryptQuantumRandomGenerator
"""
Import the Qiskrypt's Quantum Random Generator.
"""


class QiskryptQuantumRandomPasswordGenerator(QiskryptQuantumRandomGenerator):
    """
    Object class for the Qiskrypt's Quantum Random Password Generator.
    """

    def __init__(self, name: str, characters_exceptions=""):
        """
        Constructor of the Qiskrypt's Quantum Random Password Generator.

        :param name: the name of the Qiskrypt's Quantum Random Password Generator.
        :param characters_exceptions: the exceptions specified to the characters to not be
                                      used in the Quantum Random Password Generator,
                                      separated by the ' ' character.
        """

        super().__init__(name)
        """
        Calls the constructor of the super-class Qiskrypt's Quantum Random Generator.
        """

        available_alphabet = ascii_lowercase + ascii_uppercase + punctuation + digits
        """
        Initialise the available Alphabet, as a Password string,
        composed by ASCII lowercase characters, ASCII uppercase characters,
        punctuation and numbers.
        """

        characters_exceptions_list = characters_exceptions.split(" ")
        """
        Retrieve the list of the exceptions specified to
        the characters to not be used in the Quantum Random Password Generator,
        after the given string for the exceptions specified to the characters be split.
        """

        for current_character_exception in range(len(characters_exceptions_list)):
            """
            For each exception specified to
            the characters to not be used in the Quantum Random Password Generator.
            """

            character_exception = characters_exceptions_list[current_character_exception]
            """
            Retrieve the current exception of character to not be used in
            the Quantum Random Password Generator.
            """

            available_alphabet = available_alphabet.replace(character_exception, "")
            """
            Remove the current exception of character to not be used in
            the Quantum Random Password Generator, from the available Alphabet.
            """

        self.available_alphabet = available_alphabet
        """
        Set the final available Alphabet to be used in
        the Quantum Random Password Generator.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Random Password Generator.

        :return super().get_name(): the name of the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Return the name of the Qiskrypt's Quantum Random Password Generator.
        """
        return super().get_name()

    def get_available_alphabet(self) -> str:
        """
        Return the available Alphabet for
        the Qiskrypt's Quantum Random Password Generator.

        :return self.available_alphabet: the available Alphabet for
                                         the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Return the available Alphabet for
        the Qiskrypt's Quantum Random Password Generator.
        """
        return self.available_alphabet

    def get_qiskrypt_quantum_hadamard_transforms(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Password Generator.

        :return super().get_qiskrypt_quantum_hadamard_transform(): the list of the Qiskrypt's
                                                                   Quantum Hadamard Transform of
                                                                   the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Password Generator.
        """
        return super().get_qiskrypt_quantum_hadamard_transforms()

    def get_size(self) -> int:
        """
        Return the size of the Qiskrypt's Quantum Random Password Generator,
        regarding the number of qubits and bits being used.

        :return super().get_size(): the size of the Qiskrypt's Quantum Random Password Generator,
                                    regarding the number of qubits and bits being used.
        """

        """
        Return the size of the Qiskrypt's Quantum Random Password Generator,
        regarding the number of qubits and bits being used.
        """
        return super().get_size()

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Password Generator is configured or not.

        :return super().is_configured(): the boolean flag to keep the information about if
                                         the Qiskrypt's Quantum Random Password Generator is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Password Generator is configured or not.
        """
        return super().is_configured()

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Password Generator.

        :return super().get_creation_timestamp(): the current DateTime format for the timestamp of
                                                  the Qiskrypt's Quantum Random Password Generator.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Password Generator.
        """
        return super().get_creation_timestamp()

    def initiate(self, size: int) -> None:
        """
        Configure the Qiskrypt's Quantum Random Password Generator,
        given a size for the Qiskrypt's Quantum Random Password Generator.

        :param size: the size of the Qiskrypt's Quantum Random Password Generator.
        """

        length_binary_string_for_choices = ceil(log2(len(self.available_alphabet)))
        """
        Set the length of the binary string,
        representing the possible choices for the available Alphabet.
        """

        super().configure((size * length_binary_string_for_choices))
        """
        Configure the Qiskrypt's Quantum Random Password Generator, given its size.
        """

    def reset(self) -> None:
        """
        Reset the Qiskrypt's Quantum Random Password Generator.
        """

        super().reset()
        """
        Reset the Qiskrypt's Quantum Random Password Generator.
        """

    def generate_password_string(self) -> str:
        """
        Generate and return a binary string from
        the Qiskrypt's Quantum Random Password Generator,
        in a string format (i.e., a sequence of characters, punctuation and numbers).

        :return password_string: a password string from the Qiskrypt's
                                 Quantum Random Password Generator, in a string format
                                 (i.e., a sequence of characters, punctuation and numbers).
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Password Generator is already configured.
            """

            qiskrypt_quantum_hadamard_transforms = \
                self.get_qiskrypt_quantum_hadamard_transforms()
            """
            Retrieve the list of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Password Generator.
            """

            num_qiskrypt_quantum_hadamard_transforms = \
                len(qiskrypt_quantum_hadamard_transforms)
            """
            Retrieve the number of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Password Generator.
            """

            binary_string = ""
            """
            Initialise the binary string generated from
            the Qiskrypt's Quantum Random Password Generator.
            """

            for current_num_qiskrypt_quantum_hadamard_transform \
                in range(num_qiskrypt_quantum_hadamard_transforms):
                """
                For each Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Password Generator.
                """

                qiskrypt_quantum_hadamard_transform = \
                    qiskrypt_quantum_hadamard_transforms[current_num_qiskrypt_quantum_hadamard_transform]
                """
                Retrieve the current Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Password Generator.
                """

                qiskit_qasm_backend = Aer.get_backend("qasm_simulator")
                """
                Getting the Aer Simulator Backend for the QASM (Quantum Assembly) Simulation
                (i.e., the classical_regime simulation of an IBM Qiskit's Quantum Circuit).
                """

                final_results_frequency_counting = \
                    execute(qiskrypt_quantum_hadamard_transform.get_qiskrypt_quantum_circuit()
                            .get_qiskit_quantum_circuit(),
                            qiskit_qasm_backend, shots=1).result().get_counts()
                """
                Execute the IBM Qiskit's Quantum Circuit of the Qiskrypt's Quantum Circuit
                and store the resulted measurement of its final quantum_regime state.
                """

                binary_string += final_results_frequency_counting.most_frequent()
                """
                Append the resulted outcome to the binary string generated from
                the Qiskrypt's Quantum Random Password Generator.
                """

            binary_string_bits = format(int(binary_string, base=2), f"#0{(self.get_size() + 2)}b")
            """
            Convert the binary string generated from
            the Qiskrypt's Quantum Random Password Generator,
            in a binary format (i.e., a sequence of bits).
            """

            binary_string_bits_size = len(binary_string_bits[2:])
            """
            Retrieve the length of the binary string generated from
            the Qiskrypt's Quantum Random Password Generator,
            in a binary format (i.e., a sequence of bits). 
            """

            num_binary_alphabet_indexes = \
                int(binary_string_bits_size / ceil(log2(len(self.available_alphabet))))
            """
            Compute the number of indexes of small integers of base-2 binary blocks for
            the sample choices of the Alphabet.
            """

            password_string = ""
            """
            Initialise the password string, as an empty string.
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

                password_string += self.available_alphabet[alphabet_index]
                """
                Retrieve the current sample choice of the available Alphabet and append it to
                the password string being generated.
                """

            """
            Return the password string generated from
            the Qiskrypt's Quantum Random Password Generator,
            in an alphanumeric format (i.e., a sequence of characters).
            """
            return password_string

        else:
            """
            If the Qiskrypt's Quantum Random Password Generator is not configured yet.
            """

            """
            Return/Raise a Quantum Random Generator Not Configured Yet Error for
            the Qiskrypt's Quantum Random Generator.
            """
            super().raise_quantum_random_generator_not_configured_yet_error()
