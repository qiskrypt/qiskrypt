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

from qiskit import Aer, execute
"""
Import Aer Simulator and the Execute function from IBM's Qiskit.
"""

from struct import unpack, pack
"""
Import the Unpack and Pack functions from
the Struct Module of the Python's Library.
"""

from decimal import Decimal
"""
Import the Decimal function from
the Decimal Module of the Python's Library.
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

NUM_BYTES_INTEGER = 4
"""
The number of bytes for an Integer.
"""

NUM_BYTES_LONG_INTEGER = 4
"""
The number of bytes for a Long Integer.
"""

NUM_BYTES_LONG_LONG_INTEGER = 8
"""
The number of bytes for a Long Long Integer.
"""

NUM_BYTES_FLOAT = 4
"""
The number of bytes for a Float with Single Precision.
"""

NUM_BYTES_DOUBLE = 8
"""
The number of bytes for a Double.
"""

NUM_BYTES_LONG_DOUBLE = 10
"""
The number of bytes for a Long Double.
"""

DATA_TYPES = ["signed_short_int", "unsigned_short_int",
              "signed_int", "unsigned_int",
              "signed_long_int", "unsigned_long_int",
              "signed_long_long_int", "unsigned_long_long_int",
              "signed_float", "unsigned_float",
              "signed_double", "unsigned_double",
              "signed_long_double", "unsigned_long_double"]
"""
The Data Types for all the numbers that can be possibly generated.
"""

SIZE_OF_NUMERIC_DATA_TYPES = {      DATA_TYPES[0]: (NUM_BYTES_SHORT_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[1]: (NUM_BYTES_SHORT_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[2]: (NUM_BYTES_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[3]: (NUM_BYTES_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[4]: (NUM_BYTES_LONG_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[5]: (NUM_BYTES_LONG_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[6]: (NUM_BYTES_LONG_LONG_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[7]: (NUM_BYTES_LONG_LONG_INTEGER * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[8]: (NUM_BYTES_FLOAT * NUM_BITS_FOR_ONE_BYTE),
                                    DATA_TYPES[9]: (NUM_BYTES_FLOAT * NUM_BITS_FOR_ONE_BYTE),
                                   DATA_TYPES[10]: (NUM_BYTES_DOUBLE * NUM_BITS_FOR_ONE_BYTE),
                                   DATA_TYPES[11]: (NUM_BYTES_DOUBLE * NUM_BITS_FOR_ONE_BYTE),
                                   DATA_TYPES[12]: (NUM_BYTES_LONG_DOUBLE * NUM_BITS_FOR_ONE_BYTE),
                                   DATA_TYPES[13]: (NUM_BYTES_LONG_DOUBLE * NUM_BITS_FOR_ONE_BYTE)      }
"""
The sizes of the Data Types for all the numbers that can be possibly generated.
"""


class QiskryptQuantumRandomNumericGenerator(QiskryptQuantumRandomGenerator):
    """
    Object class for the Qiskrypt's Quantum Random Numeric Generator.
    """

    def __init__(self, name: str, data_type: str):
        """
        Constructor of the Qiskrypt's Quantum Random Numeric Generator.

        :param name: the name of the Qiskrypt's Quantum Random Numeric Generator.
        :param data_type: the data type of the numbers to be generated from
                          the Qiskrypt's Quantum Random Numeric Generator.
        """

        super().__init__(name)
        """
        Calls the constructor of the super-class Qiskrypt's Quantum Random Generator.
        """

        if data_type in DATA_TYPES:
            """
            If the data type of the numbers to be generated from
            the Qiskrypt's Quantum Random Numeric Generator is valid.
            """

            self.data_type = data_type
            """
            Set the data type of the numbers to be generated from
            the Qiskrypt's Quantum Random Numeric Generator.
            """

        else:
            """
            If the data type of the numbers to be generated from
            the Qiskrypt's Quantum Random Numeric Generator is not valid.
            """

            # TODO - Throw Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Random Numeric Generator.

        :return super().get_name(): the name of the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Return the name of the Qiskrypt's Quantum Random Numeric Generator.
        """
        return super().get_name()

    def get_qiskrypt_quantum_hadamard_transforms(self) -> list:
        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Numeric Generator.

        :return super().get_qiskrypt_quantum_hadamard_transform(): the list of the Qiskrypt's
                                                                   Quantum Hadamard Transform of
                                                                   the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Return the list of the Qiskrypt's Quantum Hadamard Transforms of
        the Qiskrypt's Quantum Random Numeric Generator.
        """
        return super().get_qiskrypt_quantum_hadamard_transforms()

    def get_data_type(self):
        """
        Return the data type of the numbers to be generated from
        the Qiskrypt's Quantum Random Numeric Generator.

        :return self.data_type: the data type of the numbers to be generated from
                                the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Return the data type of the numbers to be generated from
        the Qiskrypt's Quantum Random Numeric Generator.
        """
        return self.data_type

    def get_size(self) -> int:
        """
        Return the size of the Qiskrypt's Quantum Random Numeric Generator,
        regarding the number of qubits and bits being used for the specified data type.

        :return super().get_size(): the size of the Qiskrypt's Quantum Random Numeric Generator,
                                    regarding the number of qubits and bits being used for
                                    the specified data type.
        """

        """
        Return the size of the Qiskrypt's Quantum Random Numeric Generator,
        regarding the number of qubits and bits being used for
        the specified data type.
        """
        return SIZE_OF_NUMERIC_DATA_TYPES[self.data_type]

    def is_configured(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Numeric Generator is configured or not.

        :return super().is_configured(): the boolean flag to keep the information about if
                                         the Qiskrypt's Quantum Random Numeric Generator is configured or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Quantum Random Numeric Generator is configured or not.
        """
        return super().is_configured()

    def get_creation_timestamp(self):
        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Numeric Generator.

        :return super().get_creation_timestamp(): the current DateTime format for the timestamp of
                                                  the Qiskrypt's Quantum Random Numeric Generator.
        """

        """
        Return the current DateTime format for the timestamp of
        the Qiskrypt's Quantum Random Numeric Generator.
        """
        return super().get_creation_timestamp()

    def initiate(self) -> None:
        """
        Configure the Qiskrypt's Quantum Random Numeric Generator,
        given a size for the Qiskrypt's Quantum Random Numeric Generator.
        """

        super().configure(SIZE_OF_NUMERIC_DATA_TYPES[self.data_type])
        """        
        Configure the Qiskrypt's Quantum Random Numeric Generator, given its size.
        """

    def reset(self) -> None:
        """
        Reset the Qiskrypt's Quantum Random Numeric Generator.
        """

        super().reset()
        """
        Reset the Qiskrypt's Quantum Random Numeric Generator.
        """

    def generate_number(self) -> object:
        """
        Generate and return a number generated from
        the Qiskrypt's Quantum Random Numeric Generator,
        in a numeric decimal format (i.e., a short inter number).

        :return number: a number generated from
                        the Qiskrypt's Quantum Random Numeric Generator,
                        in a numerical decimal format.
        """

        if super().is_configured():
            """
            If the Qiskrypt's Quantum Random Numeric Generator is already configured.
            """

            qiskrypt_quantum_hadamard_transforms = \
                self.get_qiskrypt_quantum_hadamard_transforms()
            """
            Retrieve the list of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Numeric Generator.
            """

            num_qiskrypt_quantum_hadamard_transforms = \
                len(qiskrypt_quantum_hadamard_transforms)
            """
            Retrieve the number of the Qiskrypt's Quantum Hadamard Transforms of
            the Qiskrypt's Quantum Random Numeric Generator.
            """

            binary_string = ""
            """
            Initialise the binary string generated from
            the Qiskrypt's Quantum Random Numeric Generator.
            """

            for current_num_qiskrypt_quantum_hadamard_transform \
                in range(num_qiskrypt_quantum_hadamard_transforms):
                """
                For each Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Numeric Generator.
                """

                qiskrypt_quantum_hadamard_transform = \
                    qiskrypt_quantum_hadamard_transforms[current_num_qiskrypt_quantum_hadamard_transform]
                """
                Retrieve the current Qiskrypt's Quantum Hadamard Transform of
                the Qiskrypt's Quantum Random Numeric Generator.
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
                the Qiskrypt's Quantum Random Numeric Generator.
                """

            binary_string_bits = format(int(binary_string, base=2), f"#0{(self.get_size() + 2)}b")
            """
            Convert the initial binary string generated from
            the Qiskrypt's Quantum Random Numeric Generator,
            in a binary format (i.e., a sequence of bits).
            """

            random_number = None
            """
            Set the random number generated initially as, None.
            """

            if self.data_type == DATA_TYPES[0]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Short Integer.
                """

                random_number = unpack("h", pack("H", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Signed Short Integer.
                """

            elif self.data_type == DATA_TYPES[1]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Unsigned Short Integer.
                """

                random_number = unpack("H", pack("H", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Unsigned Short Integer.
                """

            elif self.data_type == DATA_TYPES[2]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Integer.
                """

                random_number = unpack("i", pack("I", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Signed Integer.
                """

            elif self.data_type == DATA_TYPES[3]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Unsigned Integer.
                """

                random_number = unpack("I", pack("I", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Unsigned Integer.
                """

            elif self.data_type == DATA_TYPES[4]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Long Integer.
                """

                random_number = unpack("l", pack("L", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Signed Long Integer.
                """

            elif self.data_type == DATA_TYPES[5]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Unsigned Long Integer.
                """

                random_number = unpack("L", pack("L", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Unsigned Long Integer.
                """

            elif self.data_type == DATA_TYPES[6]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Long Long Integer.
                """

                random_number = unpack("q", pack("Q", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Signed Long Long Integer.
                """

            elif self.data_type == DATA_TYPES[7]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Unsigned Long Long Integer.
                """

                random_number = unpack("Q", pack("Q", int(binary_string_bits, 2)))[0]
                """
                Convert the initial binary string generated from
                the Qiskrypt's Quantum Random Numeric Generator,
                in a final Unsigned Long Long Integer.
                """

            elif self.data_type == DATA_TYPES[8]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Float.
                """

                sign_ieee_32_float = binary_string_bits[2]
                """
                Retrieve the bit for the Sign for the Float with
                a Signed IEEE 32-bit Single Precision Floating-Point format.
                """

                single_precision_floating_point_sign = pow(-1, int(sign_ieee_32_float))
                """
                Compute the Sign of the Float with
                a Signed IEEE 32-bit Single Precision Floating-Point format.
                """

                exponent_biased_ieee_32_float = int(binary_string_bits[3:11], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Float with
                a Signed IEEE 32-bit Single Precision Floating-Point format.
                """

                exponent_unbiased_ieee_32_float = (exponent_biased_ieee_32_float - 127)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 127.
                """

                single_precision_floating_point_exponent = pow(2, exponent_unbiased_ieee_32_float)
                """
                Compute the Exponent of the Float with
                a Signed IEEE 32-bit Single Precision Floating-Point format.
                """

                mantissa_ieee_32_float = binary_string_bits[12:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Float with
                a Signed IEEE 32-bit Single Precision Floating-Point format.
                """

                single_precision_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Signed IEEE 32-bit Single Precision Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_32_float:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Float with
                    a Signed IEEE 32-bit Single Precision Floating-Point format.
                    """

                    single_precision_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Float Mantissa,
                    to the fraction part of the Signed IEEE 32-bit Single Precision Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (single_precision_floating_point_sign *
                                 single_precision_floating_point_exponent *
                                 single_precision_floating_point_fraction)
                """
                Compute the final number in the Signed IEEE 32-bit Single Precision Floating-Point format,
                considering its sign, exponent and fraction parts.
                """

            elif self.data_type == DATA_TYPES[9]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is an Unsigned Float.
                """

                exponent_biased_ieee_32_float = int(binary_string_bits[2:11], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Float with
                an Unsigned IEEE 32-bit Single Precision Floating-Point format.
                """

                exponent_unbiased_ieee_32_float = (exponent_biased_ieee_32_float - 255)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 255.
                """

                single_precision_floating_point_exponent = pow(2, exponent_unbiased_ieee_32_float)
                """
                Compute the Exponent of the Float with
                an Unsigned IEEE 32-bit Single Precision Floating-Point format.
                """

                mantissa_ieee_32_float = binary_string_bits[12:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Float with
                an Unsigned IEEE 32-bit Single Precision Floating-Point format.
                """

                single_precision_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Unsigned IEEE 32-bit Single Precision Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_32_float:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Float with
                    an Unsigned IEEE 32-bit Single Precision Floating-Point format.
                    """

                    single_precision_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Float Mantissa,
                    to the fraction part of the Unsigned IEEE 32-bit
                    Single Precision Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (single_precision_floating_point_exponent *
                                 single_precision_floating_point_fraction)
                """
                Compute the final number in the Unsigned IEEE 32-bit Single Precision Floating-Point format,
                considering only its exponent and fraction parts.
                """

            elif self.data_type == DATA_TYPES[10]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Double.
                """

                sign_ieee_64_double = binary_string_bits[2]
                """
                Retrieve the bit for the Sign for the Double with
                a Signed IEEE 64-bit Double Precision Floating-Point format.
                """

                double_precision_floating_point_sign = pow(-1, int(sign_ieee_64_double))
                """
                Compute the Sign of the Double with
                a Signed IEEE 64-bit Double Precision Floating-Point format.
                """

                exponent_biased_ieee_64_double = int(binary_string_bits[3:14], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Double with
                a Double IEEE 64-bit Single Precision Floating-Point format.
                """

                exponent_unbiased_ieee_64_double = (exponent_biased_ieee_64_double - 1023)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 1023.
                """

                double_precision_floating_point_exponent = pow(2, exponent_unbiased_ieee_64_double)
                """
                Compute the Exponent of the Double with
                a Double IEEE 64-bit Single Precision Floating-Point format.
                """

                mantissa_ieee_64_double = binary_string_bits[15:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Double with
                a Signed IEEE 64-bit Double Precision Floating-Point format.
                """

                double_precision_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Signed IEEE 64-bit Double Precision Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_64_double:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Double with
                    a Signed IEEE 64-bit Double Precision Floating-Point format.
                    """

                    double_precision_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Double Mantissa,
                    to the fraction part of the Signed IEEE 64-bit Double Precision Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (Decimal(double_precision_floating_point_sign) *
                                 Decimal(double_precision_floating_point_exponent) *
                                 Decimal(double_precision_floating_point_fraction))
                """
                Compute the final number in the Signed IEEE 64-bit Double Precision Floating-Point format,
                considering its sign, exponent and fraction parts.
                """

            elif self.data_type == DATA_TYPES[11]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is an Unsigned Double.
                """

                exponent_biased_ieee_64_double = int(binary_string_bits[2:14], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Double with
                an Unsigned IEEE 64-bit Double Precision Floating-Point format.
                """

                exponent_unbiased_ieee_64_double = (exponent_biased_ieee_64_double - 2047)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 2047.
                """

                double_precision_floating_point_exponent = pow(2, exponent_unbiased_ieee_64_double)
                """
                Compute the Exponent of the Double with
                an Unsigned IEEE 64-bit Double Precision Floating-Point format.
                """

                mantissa_ieee_64_double = binary_string_bits[15:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Double with
                an Unsigned IEEE 64-bit Double Precision Floating-Point format.
                """

                double_precision_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Unsigned IEEE 64-bit Double Precision Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_64_double:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Double with
                    an Unsigned IEEE 64-bit Double Precision Floating-Point format.
                    """

                    double_precision_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Double Mantissa,
                    to the fraction part of the Unsigned IEEE 64-bit
                    Double Precision Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (Decimal(double_precision_floating_point_exponent) *
                                 Decimal(double_precision_floating_point_fraction))
                """
                Compute the final number in the Unsigned IEEE 64-bit Double Precision Floating-Point format,
                considering only its exponent and fraction parts.
                """

            elif self.data_type == DATA_TYPES[12]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Signed Long Double.
                """

                sign_ieee_x86_extended_80_long_double = binary_string_bits[2]
                """
                Retrieve the bit for the Sign for the Long Double with
                a Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                extended_precision_x86_floating_point_sign = pow(-1, int(sign_ieee_x86_extended_80_long_double))
                """
                Compute the Sign of the Long Double with
                a Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                exponent_biased_ieee_x86_extended_80_long_double = int(binary_string_bits[3:18], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Long Double with
                an IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                exponent_unbiased_ieee_x86_extended_80_long_double = (exponent_biased_ieee_x86_extended_80_long_double - 16383)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 16383.
                """

                extended_precision_x86_floating_point_exponent = pow(2, exponent_unbiased_ieee_x86_extended_80_long_double)
                """
                Compute the Exponent of the Long Double with
                a Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                mantissa_ieee_x86_extended_80_long_double = binary_string_bits[19:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Long Double with
                a Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                extended_precision_x86_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Signed IEEE 80-bit Extended Precision x86 Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_x86_extended_80_long_double:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Long Double with
                    a Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                    """

                    extended_precision_x86_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Long Double Mantissa,
                    to the fraction part of the Signed IEEE 80-bit Extended Precision x86 Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (Decimal(extended_precision_x86_floating_point_sign) *
                                 Decimal(extended_precision_x86_floating_point_exponent) *
                                 Decimal(extended_precision_x86_floating_point_fraction))
                """
                Compute the final number in the Signed IEEE 80-bit Extended Precision x86 Floating-Point format,
                considering its sign, exponent and fraction parts.
                """

            elif self.data_type == DATA_TYPES[13]:
                """
                If the data type of the numbers to be generated from
                the Qiskrypt's Quantum Random Numeric Generator is a Unsigned Long Double.
                """

                exponent_biased_ieee_x86_extended_80_long_double = int(binary_string_bits[2:18], base=2)
                """
                Retrieve the Exponent Biased in a Decimal Integer format from
                the respective bits for the Long Double with
                an Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                exponent_unbiased_ieee_x86_extended_80_long_double = (exponent_biased_ieee_x86_extended_80_long_double - 32767)
                """
                Compute the Exponent Unbiased from the Exponent Biased, subtracting it 32767.
                """

                extended_precision_x86_floating_point_exponent = pow(2, exponent_unbiased_ieee_x86_extended_80_long_double)
                """
                Compute the Exponent of the Long Double with
                an Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                mantissa_ieee_x86_extended_80_long_double = binary_string_bits[19:]
                """
                Retrieve the Mantissa format from
                the respective bits for the Long Double with
                an Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format.
                """

                extended_precision_x86_floating_point_fraction = 1
                """
                Initialise the fraction part of
                the Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format, as 1.
                """

                negative_exponent_power_counter = -1
                """
                Initialise the Negative Exponent Power counter, as -1.
                """

                for mantissa_bit in mantissa_ieee_x86_extended_80_long_double:
                    """
                    For each bit of the Mantissa format from
                    the respective bits for the Long Double with
                    an Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format.
                    """

                    extended_precision_x86_floating_point_fraction += \
                        (int(mantissa_bit) * pow(2, negative_exponent_power_counter))
                    """
                    Adds the converted value of the current bit to a Long Double Mantissa,
                    to the fraction part of the Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format.
                    """

                    negative_exponent_power_counter -= 1
                    """
                    Decrement the the Negative Exponent Power counter.
                    """

                random_number = (Decimal(extended_precision_x86_floating_point_exponent) *
                                 Decimal(extended_precision_x86_floating_point_fraction))
                """
                Compute the final number in the Unsigned IEEE 80-bit Extended Precision x86 Floating-Point format,
                considering only its exponent and fraction parts.
                """

            """
            Return the number generated from
            the Qiskrypt's Quantum Random Numeric Generator,
            in a decimal format (i.e., digits of a numeric representation).
            """
            return random_number

        else:
            """
            If the Qiskrypt's Quantum Random Numeric Generator is not configured yet.
            """

            # TODO - Throw exception
