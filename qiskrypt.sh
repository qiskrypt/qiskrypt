# Copyrights:
# - © Qiskrypt, 2021 - All rights reserved.

# Powered by:
# - IBM
# - IBM Quantum
# - IBM Qiskit

# Description:
# - The Qiskrypt is a software suite of protocols of
#   quantum cryptography, quantum communication and
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
========================================================================
                      *** Qiskrypt v0.0.1 ***
========================================================================

                     Please, enter your choice:
                        (not case-sensitive)

            (1)           Key Distribution Protocols
            (2)           Encryption
            (Q/ESC)       Quit

------------------------------------------------------------------------
EOF

read -rn1 -s

case "$REPLY" in

'1')      echo "You chosen the option: Key Distribution Protocols..."          ;;
'2')      echo "You chosen the option: Encryption"                             ;;

# The exit options of the Main Menu of the Qiskrypt's Bash Executable
'Q')      echo "Thank you for using Qiskrypt!!! See you next time!!! :)"; exit;;
'q')      echo "Thank you for using Qiskrypt!!! See you next time!!! :)"; exit;;
$'\x1b')  echo "Thank you for using Qiskrypt!!! See you next time!!! :)"; exit;;

# The remaining options of the Main Menu of the Qiskrypt' Bash Executable
* )       echo "You chosen an invalid option!!!" ;;

esac

cat<<EOF
------------------------------------------------------------------------
EOF

sleep 1

done