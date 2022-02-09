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

from src.quantum_regime.cryptography.common.keys.instances.QiskryptPrivateKey \
    import QiskryptPrivateKey
"""
Import the Qiskrypt's Private Key.
"""

from src.quantum_regime.cryptography.common.keys.instances.QiskryptPublicKey \
    import QiskryptPublicKey
"""
Import the Qiskrypt's Public Key.
"""


class QiskryptKeyPair:
    """
    Object class for the Qiskrypt's Key Pair.
    """

    def __init__(self, private_key: QiskryptPrivateKey,
                 public_key: QiskryptPublicKey):
        """
        Constructor of the Qiskrypt's Key Pair.

        :param private_key: the Qiskrypt's Private Key of the Qiskrypt's Key Pair.
        :param public_key: the Qiskrypt's Public Key of the Qiskrypt's Key Pair.
        """

        if self.is_ownership_correct_for_key_pair_creation(private_key, public_key):
            """
            If the ownership is correct for the creation of the Qiskrypt's Key Pair.
            """

            self.private_key = private_key
            """
            Set the Qiskrypt's Private Key of the Qiskrypt's Key Pair.
            """

            self.public_key = public_key
            """
            Set the Qiskrypt's Public Key of the Qiskrypt's Key Pair.
            """

        else:
            """
            If the ownership is not correct for the creation of the Qiskrypt's Key Pair.
            """

            # TODO Throw - Exception

    def get_private_key(self) -> QiskryptPrivateKey:
        """
        Return the Qiskrypt's Private Key of the Qiskrypt's Key Pair.

        :return self.private_key: the Qiskrypt's Private Key of the Qiskrypt's Key Pair.
        """

        """
        Return the Qiskrypt's Private Key of the Qiskrypt's Key Pair.
        """
        return self.private_key

    def get_public_key(self) -> QiskryptPublicKey:
        """
        Return the Qiskrypt's Public Key of the Qiskrypt's Key Pair.

        :return self.public_key: the Qiskrypt's Public Key of the Qiskrypt's Key Pair.
        """

        """
        Return the Qiskrypt's Public Key of the Qiskrypt's Key Pair.
        """
        return self.public_key

    @staticmethod
    def is_ownership_correct_for_key_pair_creation(private_key: QiskryptPrivateKey,
                                                   public_key: QiskryptPublicKey) -> bool:
        """
        Return the boolean flag to keep the information about if
        the ownership is correct or not for the creation of the Qiskrypt's Key Pair.

        :param private_key: the Qiskrypt's Private Key of the Qiskrypt's Key Pair.
        :param public_key: the Qiskrypt's Public Key of the Qiskrypt's Key Pair.

        :return ownership_correct_for_key_pair_creation: the boolean flag to keep the information about if
                                                         the ownership is correct or not for the creation of
                                                         the Qiskrypt's Key Pair.
        """

        private_key_owner_uuid = private_key.get_owner_uuid()
        """
        Retrieve the UUID (Universally Unique IDentifier) of
        the owner of the Qiskrypt's Private Key. 
        """

        public_key_owner_uuid = public_key.get_owner_uuid()
        """
        Retrieve the UUID (Universally Unique IDentifier) of
        the owner of the Qiskrypt's Public Key. 
        """

        ownership_correct_for_key_pair_creation = \
            (private_key_owner_uuid == public_key_owner_uuid)
        """
        Retrieve the boolean flag to keep the information about if
        the ownership is correct or not for the creation of the Qiskrypt's Key Pair.
        """

        """
        Return the boolean flag to keep the information about if
        the ownership is correct or not for the creation of the Qiskrypt's Key Pair.
        """
        return ownership_correct_for_key_pair_creation
