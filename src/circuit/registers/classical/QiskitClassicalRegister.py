"""

© Copyright Qiskrypt, 2021 - All rights reserved.

Powered by:
- IBM
- IBM Quantum
- IBM Qiskit

Description:
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):
- Instituto de Telecomunicacoes, Portugal.
- Security and Quantum Information Group, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):
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


class QiskitClassicalRegister:
    """
    Object Class of the IBM's Qiskit Classical Register.
    """

    def __init__(self, name="cl_reg", num_bits=1, classical_register=None):
        """
        Constructor for the IBM's Qiskit Classical Register.

        :param name: The name of the IBM's Qiskit Classical Register.
        :param num_bits: The number of bits of the IBM's Qiskit Classical Register.
        :param classical_register: A built-in classical register object of
                                   the IBM's Qiskit Classical Register.
        """

        self.name = name
        """
        Set the name of the IBM's Qiskit Classical Register.
        """

        self.num_bits = num_bits
        """
        Set the number of the bits of the IBM's Qiskit Classical Register.
        """

        if classical_register is None:
            """
            If the Classical Register is None.
            """

            self.classical_register = ClassicalRegister(name=name, size=num_bits)
            """
            Set the built-in classical register of the IBM's Qiskit Classical Register.
            """

        else:
            """
            If the Classical Register is not None.
            """

            self.classical_register = classical_register
            """
            Set the built-in classical register of the IBM's Qiskit Classical Register.
            """
