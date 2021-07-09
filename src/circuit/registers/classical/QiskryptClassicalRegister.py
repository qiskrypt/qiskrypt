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

from qiskit import ClassicalRegister
"""
Import Classical Register from IBM's Qiskit.
"""

from src.circuit.registers.classical.exception.QiskryptClassicalRegisterException \
    import QiskryptNotClassicalRegisterError
"""
Import the Not Classical Register Error for the Qiskrypt's Classical Register.
"""


class QiskryptClassicalRegister:
    """
    Object Class of the Qiskrypt's Classical Register.
    """

    def __init__(self, name="cl_reg", num_bits=1, classical_register=None):
        """
        Constructor for the Qiskrypt's Classical Register.

        :param name: The name of the Qiskrypt's Classical Register.
        :param num_bits: The number of bits of the Qiskrypt's Classical Register.
        :param classical_register: A built-in classical register object of
                                   the IBM's Qiskit Classical Register.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Classical Register.
        """

        self.num_bits = num_bits
        """
        Set the number of the bits of the Qiskrypt's Classical Register.
        """

        if classical_register is None:
            """
            If the Classical Register is None.
            """

            self.classical_register = ClassicalRegister(name=name, size=num_bits)
            """
            Set the built-in classical register of the Qiskrypt's Classical Register.
            """

        else:
            """
            If the Classical Register is not None.
            """

            self.classical_register = classical_register
            """
            Set the built-in classical register of the Qiskrypt's Classical Register.
            """

    @staticmethod
    def raise_not_classical_register_error():
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
