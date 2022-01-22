# Copyrights:
# - © Qiskrypt, 2021 - All rights reserved.

# Powered by:
# - IBM
# - IBM Quantum
# - IBM Qiskit

# Description:
# - The Qiskrypt is a software suite of protocols of
#   quantum_regime cryptography, quantum_regime communication and
#   other protocols/algorithms, built using the IBM's Qiskit.

# College(s):
# - NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
# - Faculty of Sciences, University of Lisbon, Portugal.
# - Tecnico Lisboa, University of Lisbon, Portugal.
# - School of Engineering, University of Connecticut, United States of America.

# Other Institution(s):
# - Instituto de Telecomunicacoes, Portugal.
# - SQIG, Portugal.
# - LASIGE, Portugal.
# - UT Austin Program, Portugal.

# Author(s):
# - Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

# Acknowledgement(s):
# - Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
# - Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
# - Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
# - Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
#

echo "#############################################################################"
echo "#                                                                           #"
echo "#           ███████                                                         #"
echo "#          ██     ██                                                        #"
echo "#          ██  ██████                                                       #"
echo "#         █ ████ ███ █     ████   ██        █ █  █                 █   █    #"
echo "#        █ ██ █  ██  ██   ██  ██       ████ █ █ ██  ███ █  █ ███  ████  █   #"
echo "#     ███████ ██     ██   ██  ██ ███  ███   █ ███  ██ █ █  █ █  █  █    ██  #"
echo "#    ██  █████ ████ ██    ██  ██  ██    ███ █ █ ██ ██   ████ █  █  █  █ ██  #"
echo "#   ███ ██   █ █████ █     ████  ████ ████  █ █  █ ██    ██  ███   ███  █   #"
echo "#  ███   █  ██ █   █ ██      ██             █            ██  █         █    #"
echo "#   ███████ ██ █   ██ █                                                     #"
echo "#   ███   ██████    ████            Version:                                #"
echo "#     ██████ ██      ██              v0.0.1                                 #"
echo "#                                                                           #"
echo "#                                 Powered By:                               #"
echo "#                           IBM | IBM Quantum | IBM Qiskit                  #"
echo "#                                                                           #"
echo "#                                  Author(s):                               #"
echo "#       R. Barreiro | W. Krawec | P. Mateus | N. Paunkovic | A. Souto       #"
echo "#                                                                           #"
echo "#############################################################################"

echo
read -rsn1 -p "Press any key to continue..."
echo

while :
do

echo

cat<<EOF
=============================================================================
                         *** Qiskrypt v0.0.1 ***
=============================================================================

                        Please, enter your choice:
                           (not case-sensitive)

         (1)          Quantum Key Distributions (QKDs)
         (2)          Semi-Quantum Key Distributions (SQKDs)
         (3)          Quantum Conference Key Agreements (QCKAs)
         (4)          Semi-Quantum Conference Key Agreements (SQCKAs)
         (5)          Quantum Secure Multi-Party Computations
         (6)          Quantum Cryptocurrencies
         (7)          Other Quantum Cryptographic Primitives
         (8)          Quantum Internet (Networking/Communications) Protocols
         (9)          Quantum Entanglements
        (10)          Quantum True Randomness
        (11)          Quantum Distance Measures and Metrics
        (12)          Quantum Algorithms
 (QUIT/EXIT)          Quit/Exit

-----------------------------------------------------------------------------
EOF

read -rp "Your choice: " CHOICE

case "$CHOICE" in

# The valid options of the Main Menu of the Qiskrypt's Bash Executable
'1')      echo ; echo "You chosen the option: Quantum Key Distributions (QKDs)..."                           ;;
'2')      echo ; echo "You chosen the option: Semi-Quantum Key Distributions (SQKDs)..."                     ;;
'3')      echo ; echo "You chosen the option: Quantum Conference Key Agreements (QCKAs)..."                  ;;
'4')      echo ; echo "You chosen the option: Semi-Quantum Conference Key Agreements (SQCKAs)..."            ;;
'5')      echo ; echo "You chosen the option: Quantum Secure Multi-Party Computations..."                    ;;
'6')      echo ; echo "You chosen the option: Quantum Cryptocurrencies..."                                   ;;
'7')      echo ; echo "You chosen the option: Other Quantum Cryptographic Primitives..."                     ;;
'8')      echo ; echo "You chosen the option: Quantum Internet (Networking/Communication) Protocols..."      ;;
'9')      echo ; echo "You chosen the option: Quantum Entanglements..."                                      ;;
'10')     echo ; echo "You chosen the option: Quantum True Randomness..."                                    ;;
'11')     echo ; echo "You chosen the option: Quantum Distance Measures and Metrics..."                      ;;
'12')     echo ; echo "You chosen the option: Quantum Algorithms..."                                         ;;

# The exit options of the Main Menu of the Qiskrypt's Bash Executable
'Quit')   echo ; echo "Thank you for using Qiskrypt!!! See you next time!!! :)";         sleep 2;        exit;;
'quit')   echo ; echo "Thank you for using Qiskrypt!!! See you next time!!! :)";         sleep 2;        exit;;
'Exit')   echo ; echo "Thank you for using Qiskrypt!!! See you next time!!! :)";         sleep 2;        exit;;
'exit')   echo ; echo "Thank you for using Qiskrypt!!! See you next time!!! :)";         sleep 2;        exit;;
$'\x1b')  echo ; echo "Thank you for using Qiskrypt!!! See you next time!!! :)";         sleep 2;        exit;;

# The remaining options of the Main Menu of the Qiskrypt' Bash Executable
* )       echo ; echo "You chosen an invalid option!!!"                                                      ;;

esac

cat<<EOF
-----------------------------------------------------------------------------
EOF

sleep 1

done