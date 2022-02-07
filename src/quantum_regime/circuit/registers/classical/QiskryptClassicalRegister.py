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
- NOVA LINCS, Portugal.
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

from qiskit import ClassicalRegister
"""
Import Classical Register from IBM's Qiskit.
"""

from src.quantum_regime.circuit.registers.classical.exception.QiskryptClassicalRegisterException \
    import QiskryptNotClassicalRegisterError
"""
Import the Not a Classical Register Error for the Qiskrypt's Classical Register.
"""

from src.quantum_regime.circuit.registers.classical.exception.QiskryptClassicalRegisterException \
    import QiskryptNotValidClassicalRegisterIndexError
"""
Import the Not a Valid Classical Register Index Error for the Qiskrypt's Classical Register.
"""

from src.quantum_regime.circuit.registers.classical.exception.QiskryptClassicalRegisterException \
    import QiskryptClassicalRegisterInvalidBitIndexGivenError
"""
Import the Invalid Bit Index Given Error for the Qiskrypt's Classical Register.
"""


class QiskryptClassicalRegister:
    """
    Object Class of the Qiskrypt's Classical Register.
    """

    def __init__(self, name="cl_reg", num_bits=1, qiskit_classical_register=None):
        """
        Constructor for the Qiskrypt's Classical Register.

        :param name: the name of the Qiskrypt's Classical Register.
        :param num_bits: the number of bits of the Qiskrypt's Classical Register.
        :param qiskit_classical_register: an IBM Qiskit's Classical Register.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        self.num_bits = num_bits
        """
        Set the number of the bits of the Qiskrypt's Classical Register.
        """

        self.bits = [0] * num_bits
        """
        Set the bits of the Qiskrypt's Classical Register.
        """

        if qiskit_classical_register is None:
            """
            If the IBM Qiskit's Classical Register is None.
            """

            self.qiskit_classical_register = ClassicalRegister(name=name, size=num_bits)
            """
            Set the IBM Qiskit's Classical Register of the Qiskrypt's Classical Register.
            """

        else:
            """
            If the IBM Qiskit's Classical Register is not None.
            """

            if isinstance(qiskit_classical_register, ClassicalRegister):
                """
                If the IBM Qiskit's Classical Register is really an IBM Qiskit's Classical Register.
                """

                if qiskit_classical_register.size == num_bits:
                    """
                    If the number of bits of the Qiskrypt's Classical Register
                    is equal to the given number of bits.
                    """

                    self.qiskit_classical_register = qiskit_classical_register
                    """
                    Set the IBM Qiskit's Classical Register of the Qiskrypt's Classical Register.
                    """

                else:
                    """
                    If the number of bits of the Qiskrypt's Classical Register
                    is not equal to the given number of bits.
                    """

                    # TODO Throw - Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Classical Register.

        :return self.name: the name of the Qiskrypt's Classical Register.
        """

        """
        Return the name of the Qiskrypt's Classical Register.
        """
        return self.name

    def get_num_bits(self) -> int:
        """
        Return the number of bits of the Qiskrypt's Classical Register.

        :return self.num_bits: the number of bits of the Qiskrypt's Classical Register.
        """

        """
        Return the number of bits of the Qiskrypt's Classical Register.
        """
        return self.num_bits

    def get_bits(self) -> list:
        """
        Return the bits of the Qiskrypt's Classical Register.

        :return self.bits: the bits of the Qiskrypt's Classical Register.
        """

        """
        Return the bits of the Qiskrypt's Classical Register.
        """
        return self.bits

    def get_bit(self, bit_index: int) -> int:
        """
        Return the bit in the Qiskrypt's Classical Register,
        for a given index.

        :param bit_index: the given index of the bit in
                          the Qiskrypt's Classical Register.

        :return self.bits[bit_index]: the bit in the Qiskrypt's Classical Register,
                                      for a given index.
        """

        if bit_index < self.get_num_bits():
            """
            If the given index of the bit is valid for
            the Qiskrypt's Classical Register.
            """

            """
            Return the pretended bit in
            the Qiskrypt's Classical Register.
            """
            return self.bits[bit_index]

        else:
            """
            If the given index of the bit is not valid for
            the Qiskrypt's Classical Register.
            """

            """
            Return/Raise an Invalid Bit Index Given Error.
            """
            self.raise_invalid_bit_index_given_error()

    def buffer_bit(self, bit_index: int):
        """
        Buffer the bit in the Qiskrypt's Classical Register,
        for a given index.

        :param bit_index: the given index of the bit in
                          the Qiskrypt's Classical Register.
        """

        if bit_index < self.get_num_bits():
            """
            If the given index of the bit is valid for
            the Qiskrypt's Classical Register.
            """

            """
            Buffer the pretended bit in
            the Qiskrypt's Classical Register.
            """
            self.bits[bit_index] = self.bits[bit_index]

        else:
            """
            If the given index of the bit is not valid for
            the Qiskrypt's Classical Register.
            """

            """
            Return/Raise an Invalid Bit Index Given Error.
            """
            self.raise_invalid_bit_index_given_error()

    def invert_bit(self, bit_index: int):
        """
        Invert the bit in the Qiskrypt's Classical Register,
        for a given index.

        :param bit_index: the given index of the bit in
                          the Qiskrypt's Classical Register.
        """

        if bit_index < self.get_num_bits():
            """
            If the given index of the bit is valid for
            the Qiskrypt's Classical Register.
            """

            """
            Invert the pretended bit in
            the Qiskrypt's Classical Register.
            """
            self.bits[bit_index] = int(not self.bits[bit_index])

        else:
            """
            If the given index of the bit is not valid for
            the Qiskrypt's Classical Register.
            """

            """
            Return/Raise an Invalid Bit Index Given Error.
            """
            self.raise_invalid_bit_index_given_error()

    def get_qiskit_classical_register(self) -> ClassicalRegister:
        """
        Return the IBM Qiskit's Classical Register of the Qiskrypt's Classical Register.

        :return self.qiskit_classical_register: the IBM Qiskit's Classical Register of
                                                the Qiskrypt's Classical Register.
        """

        """
        Return the IBM Qiskit's Classical Register of the Qiskrypt's Classical Register.
        """
        return self.qiskit_classical_register

    @staticmethod
    def raise_not_classical_register_error() -> None:
        """
        Return/Raise a Not a Classical Register Error for the Qiskrypt's Classical Register.

        :raise not_classical_register_error: a Not a Classical Register Error for
                                             the Qiskrypt's Classical Register.
        """

        not_classical_register_error = QiskryptNotClassicalRegisterError()
        """
        Retrieve the Not a Classical Register Error for the Qiskrypt's Classical Register.
        """

        """
        Raise the Not a Classical Register Error for the Qiskrypt's Classical Register.
        """
        raise not_classical_register_error

    @staticmethod
    def raise_not_valid_qiskrypt_classical_register_index_error() -> None:
        """
        Return/Raise a Not a Valid Qiskrypt's Classical Register Index Error for the Qiskrypt's Classical Register.

        :raise not_valid_qiskrypt_classical_register_index_error: a Not a Valid Qiskrypt's Classical Register Index Error for
                                                                  the Qiskrypt's Classical Register.
        """

        not_valid_classical_register_index_error = QiskryptNotValidClassicalRegisterIndexError()
        """
        Retrieve the Not a Valid Qiskrypt's Classical Register Index Error for the Qiskrypt's Classical Register.
        """

        """
        Raise the Not a Valid Qiskrypt's Classical Register Index Error for the Qiskrypt's Classical Register.
        """
        raise not_valid_classical_register_index_error

    @staticmethod
    def raise_invalid_bit_index_given_error() -> None:
        """
        Return/Raise an Invalid Bit Index Given Error.

        :raise invalid_bit_index_given_error: an Invalid Bit Index Given Error.
        """

        invalid_bit_index_given_error = QiskryptClassicalRegisterInvalidBitIndexGivenError()
        """
        Retrieve the Invalid Bit Index Given Error for the Qiskrypt's Classical Register.
        """

        """
        Raise the Invalid Bit Index Given Error for the Qiskrypt's Classical Register.
        """
        raise invalid_bit_index_given_error
