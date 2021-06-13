# Qiskrypt

<img src="https://raw.githubusercontent.com/qiskrypt/qiskrypt.github.io/main/assets/images/logos/PNGs/qiskrypt-logo-banner.png" alt="Qiskrypt - Logo" width="60%">

[![build Status](https://travis-ci.com/qiskrypt/qiskrypt.svg?branch=main)](https://travis-ci.com/qiskrypt/qiskrypt)

[![current version](https://img.shields.io/badge/version-v0.0.1-magenta.svg)](https://github.com/qiskrypt/qiskrypt/)
[![status of this version no. 1](https://img.shields.io/badge/status-not&nbsp;completed-orange.svg)](https://github.com/qiskrypt/qiskrypt/)
[![status of this version no. 2](https://img.shields.io/badge/status-beta-orange.svg)](https://github.com/qiskrypt/qiskrypt/)
[![status of this version no. 3](https://img.shields.io/badge/status-not&nbsp;stable-orange.svg)](https://github.com/qiskrypt/qiskrypt/)
[![status of this version no. 4](https://img.shields.io/badge/status-not&nbsp;documented-orange.svg)](https://github.com/qiskrypt/qiskrypt/)

[![keyword of this version no. 1](https://img.shields.io/badge/keyword-quantum&nbsp;cryptography-brown.svg)](https://github.com/qiskrypt/qiskrypt/)
[![keyword of this version no. 2](https://img.shields.io/badge/keyword-quantum&nbsp;computing-brown.svg)](https://github.com/qiskrypt/qiskrypt/)
[![keyword of this version no. 3](https://img.shields.io/badge/keyword-quantum&nbsp;communication-brown.svg)](https://github.com/qiskrypt/qiskrypt/)
[![keyword of this version no. 4](https://img.shields.io/badge/keyword-quantum&nbsp;mechanics-brown.svg)](https://github.com/qiskrypt/qiskrypt/)

[![contributor for this repository](https://img.shields.io/badge/contributor-rubenandrebarreiro-blue.svg)](https://github.com/rubenandrebarreiro/)
[![acknowledgement for this repository no. 1](https://img.shields.io/badge/acknowledgement-andrenunosouto-cyan.svg)](https://ciencias.ulisboa.pt/pt/perfil/ansouto)
[![acknowledgement for this repository no. 2](https://img.shields.io/badge/acknowledgement-paulo&nbsp;mateus-cyan.svg)](http://sqig.math.ist.utl.pt/pmat/)
[![acknowledgement for this repository no. 3](https://img.shields.io/badge/acknowledgement-nikola&nbsp;paunkovic-cyan.svg)](https://www.math.tecnico.ulisboa.pt/~npaunkov/)
[![acknowledgement for this repository no. 4](https://img.shields.io/badge/acknowledgement-walter&nbsp;krawec-cyan.svg)](http://www.walterkrawec.org/)

[![technology used no. 1](https://img.shields.io/badge/built&nbsp;with-python-red.svg)](https://www.python.org/) 
[![technology used no. 2](https://img.shields.io/badge/built&nbsp;with-qiskit-red.svg)](https://qiskit.org/)
[![software used no. 1](https://img.shields.io/badge/software-jetbrains&nbsp;pycharm-gold.svg)](https://www.jetbrains.com/pycharm/)

[![star this repository](http://githubbadges.com/star.svg?user=qiskrypt&repo=qiskrypt&style=flat)](https://github.com/qiskrypt/qiskrypt/stargazers)
[![fork this repository](http://githubbadges.com/fork.svg?user=qiskrypt&repo=qiskrypt&style=flat)](https://github.com/qiskrypt/qiskrypt/fork)
[![downloads of this repository](https://img.shields.io/github/downloads/qiskrypt/qiskrypt/total.svg)](https://github.com/qiskrypt/qiskrypt/archive/master.zip)
[![price of this project](https://img.shields.io/badge/price-free-success.svg)](https://github.com/qiskrypt/qiskrypt/archive/master.zip)
[![Donate](https://img.shields.io/badge/donate-paypal-green.svg)](https://www.paypal.me/qiskrypt)


### About


The [**Qiskrypt**](https://qiskrypt.github.io/) is a software suite of protocols of _quantum cryptography_, built using the [**IBM**](https://www.ibm.com/)’s _open-source_ _Software Development Kit_ for _quantum computing_ [**Qiskit**](https://qiskit.org/).

#### Foundation

This _framework_ started as a proposal for the [**IBM**](https://www.ibm.com/) [**Hackathon Europe 2021**](https://qiskithackathoneurope.bemyapp.com/), achieving its 2nd phase (finals, with the top 20 teams), as well, as an idea developed by a team of students, researchers and professors, mostly from [**NOVA School of Science and Technology**](https://www.fct.unl.pt/en/), [**Técnico Lisboa**](https://tecnico.ulisboa.pt/en/), [**Faculty of Sciences of University of Lisbon**](https://ciencias.ulisboa.pt/en) and [**School of Engineering from University of Connecticut**](https://www.engr.uconn.edu/).

The aim of our _framework_ is to provide all the known _quantum cryptographic protocols_, in a single place, as an accessible solution, and being easy to use.

### Mission

The mission of our framework is to:
* Emphasize the importance of _quantum cryptography_, as a long-term solution for the _post-quantum era_;
* Provide _open-source_ implementations of _quantum cryptographic protocols_, including:
  * **Quantum Key Distributions** (**QKDs**); 
  * **Semi-Quantum Key Distribution** (**SQKDs**);
  * **Quantum Conference Key Agreements** (**QCKAs**);
  * **Semi-Quantum Conference Key Agreements** (**SQCKAs**);
  * **Quantum One-Time Pads** (**QOTPs**);
  * **SWAP Test**/**Quantum Fingerprinting**;
* Offer some important primitives for _quantum communications_ and _quantum networks_, such as:
  * **Quantum Teleportation**;
  * **Quantum Entanglement Swapping**;
  * **Quantum Entanglement Distillation/Purification**;
  * **Quantum Repeaters**;
  * **Quantum Internet Protocols**;
* Offer, as well, some _quantum algortithms_ for _quantum_ _cryptonalysis_ and _quantum_ _attacks_, such as:
  * **Grover's Algorithm**;
  * **Simon's Algorithm**;
  * **Shor's Algorithm**;
* Provide an easy and comprehensive detailed explanation of the protocols, primitives and algorithms addressed, through several illustrations and tutorials;


### Meet our team

Our team is composed by the following members:


### Institutions involved

The institutions involved in the development of this framework are:


### Powered by

This framework is powered by:


### Useful links

Take a look on some useful links, related to our framework:



### Contact us

If you have any doubt or want to give some suggestion, feel free to contact us:
* [qiskrypt@gmail.com](mailto:qiskrypt@gmail.com)

***

## Specifications

The specifications of the primitives offered in our framework are described in the following sections.

### Quantum Key Distributions (QKDs)<br>\[Key Exchanges for Bipartite Quantum Scenarios, with N=2 Parties\]

#### Discrete Variable - Quantum Key Distributions (DV-QKDs)

<table>
<thead>
  <tr>
    <th>#</th>
    <th>Type</th>
    <th>Name</th>
    <th>Year</th>
    <th>Author(s)</th>
    <th>Ref.</th>
    <th>Tutorial(s)</th>
    <th>Build</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td rowspan="13">PM<br>(Prepare-and-Measure)</td>
    <td>BB84</td>
    <td>1984</td>
    <td>C. Bennet and G. Bassard</td>
    <td><a href="https://arxiv.org/abs/2003.06557v1" target="_blank">[BB84]</a></td>
    <td>❌ (N/A)</td>
    <td>⌛ (v0.0.1)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>B92</td>
    <td>1992</td>
    <td>C. Bennet</td>
    <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.68.3121" target="_blank">[B92]</td>
    <td>❌ (N/A)</td>
    <td>⌛ (v0.0.1)</td>
  </tr>
  <tr>
    <td>3</td>
    <td>MSZ96</td>
    <td>1996</td>
    <td>Y. Mu, J. Seberry and Y. Zheng</td>
    <td><a href="https://www.sciencedirect.com/science/article/abs/pii/0030401895006885?via%3Dihub" target="_blank">[MSZ96]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>4</td>
    <td>SSP<br>(Six-State Protocol)</td>
    <td>1998</td>
    <td>H. Bechmann-Pasquinucci and N. Gisin</td>
    <td><a href="https://arxiv.org/abs/quant-ph/9807041" target="_blank">[PG98]</a></td>
    <td>❌ (N/A)</td>
    <td>⌛ (v0.0.1)</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Decoy State</td>
    <td>2002</td>
    <td>W. Hwang</td>
    <td><a href="https://arxiv.org/abs/quant-ph/0211153" target="_blank">[H02]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Singapore</td>
    <td>2004</td>
    <td>B. Englert, D. Kaszlikowski, H. Ng, W. Chua, J. Řeháček and J. Anders</td>
    <td><a href="https://arxiv.org/abs/quant-ph/0412075" target="_blank">[EKNCRA04]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>7</td>
    <td>R04</td>
    <td>2004</td>
    <td>J. Renes</td>
    <td><a href="https://arxiv.org/abs/quant-ph/0402135" target="_blank">[R04]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>8</td>
    <td>SARG04<br>(w/ 4 states)</td>
    <td>2004</td>
    <td>V. Scarani, A. Acín, G. Ribordy and N. Gisin</td>
    <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.92.057901" target="_blank">[SARG04]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>9</td>
    <td>SARG04<br>(w/ 6 states)</td>
    <td>2004</td>
    <td>K. Tamaki and H. Lo</td>
    <td><a href="https://arxiv.org/abs/quant-ph/0412035" target="_blank">[TL04]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>10</td>
    <td>KMB09</td>
    <td>2009</td>
    <td>M. Khan, M. Murphy and A. Beige</td>
    <td><a href="https://arxiv.org/abs/0901.3909" target="_blank">[KMB09]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>11</td>
    <td>S09</td>
    <td>2009</td>
    <td>E. Serna</td>
    <td><a href="https://arxiv.org/abs/0908.2146" target="_blank">[S09]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>12</td>
    <td>T12</td>
    <td>2012</td>
    <td>M. Lucamarini, K. Patel, J. Dynes, B. Fröhlich, A. Sharpe, A. Dixon, Z. Yuan, R. Penty and A. Shields (Toshiba)</td>
    <td><a href="https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-21-21-24550&id=268752" target="_blank">[T12]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>13</td>
    <td>S13</td>
    <td>2013</td>
    <td>E. Serna</td>
    <td><a href="https://arxiv.org/abs/1311.1582" target="_blank">[S13]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>14</td>
    <td rowspan="2">EB<br>(Entanglement-Based)</td>
    <td>E91</td>
    <td>1991</td>
    <td>A. Ekert</td>
    <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.67.661" target="_blank">[E91]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>15</td>
    <td>BBM92</td>
    <td>1992</td>
    <td>C. Bennet, G. Brassard and N. Mermin</td>
    <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.68.557" target="_blank">[BBM92]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
</tbody>
</table>


#### Continuous Variables - Quantum Key Distributions (CV-QKDs)

Available soon.


#### Distributed Phase Reference - Quantum Key Distributions (DPR-QKDs)

<table>
<thead>
  <tr>
    <th>#</th>
    <th>Name</th>
    <th>Year</th>
    <th>Author(s)</th>
    <th>Ref.</th>
    <th>Tutorial(s)</th>
    <th>Build</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>DPS<br>(Differential Phase Shift)</td>
    <td>2003</td>
    <td>K. Inoue, E. Waks, Y. Yamamoto</td>
    <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.89.037902" target="_blank">[IWY03]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>COW<br>(Coherent One-Way)</td>
    <td>2005</td>
    <td>D. Stucki, N. Brunner, N. Gisin, V. Scarani and H. Zbinden</td>
    <td><a href="https://arxiv.org/abs/quant-ph/0506097" target="_blank">[SBGSZ05]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
  <tr>
    <td>3</td>
    <td>DPTS<br>(Differential Phase Time Shifting)</td>
    <td>2016</td>
    <td>D. Bacco, J. Christensen, M. Castaneda, Y. Ding, S. Forchhammer, K. Rottwitt and L. Oxenløwe </td>
    <td><a href="https://www.nature.com/articles/srep36756" target="_blank">[BCCDFRO16]</a></td>
    <td>❌ (N/A)</td>
    <td>❌ (N/A)</td>
  </tr>
</tbody>
</table>


#### High-Dimensional - Quantum Key Distributions (HD-QKDs)

Available soon.


### Semi-Quantum Key Distributions (SQKDs)<br>\[Key Exchanges for Bipartite Semi-Quantum Scenarios, with N=2 Parties\]

Available soon.


### Quantum Conference Key Agreements (QCKAs)<br>\[Key Exchanges for Multipartite Quantum Scenarios, with N>=2 Parties\]

Available soon.


### Semi-Quantum Conference Key Agreements (SQCKAs)<br>\[Key Exchanges for Multipartite Semi-Quantum Scenarios, with N>=2 Parties\]

Available soon.


### Quantum Secure Multi-Party Computations

Available soon.


### Quantum Cryptocurrencies

Available soon.


### Other Quantum Cryptographic Primitives

<table class="tg">
 <thead>
   <tr>
     <th>#</th>
     <th>Purpose</th>
     <th>No. Parties</th>
     <th>Name</th>
     <th>Year</th>
     <th>Authors</th>
     <th>Ref.</th>
     <th>Tutorial(s)</th>
     <th>Build</th>
   </tr>
 </thead>
 <tbody>
   <tr>
     <td>1</td>
     <td>Symmetric Encryption<br>(Private Quantum Channels)</td>
     <td>N=2<br>(Bipartite)</td>
     <td>QOTP<br>(Quantum One-Time Pad)</td>
     <td>2000</td>
     <td>M. Mosca, A. Tapp and R. Wolf</td>
     <td><a href="https://arxiv.org/abs/quant-ph/0003101" target="_blank">[MTW00]</a></td>
     <td>❌ (N/A)</td>
     <td>⌛ (v0.0.1)</td>
   </tr>
   <tr>
     <td>2</td>
     <td rowspan="6">Quantum Data Integrity</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>SWAP Test<br>(Quantum Fingerprinting)</td>
     <td>2001</td>
     <td>H. Buhrman, R. Cleve, J. Watrous and R. Wolf</td>
     <td><a href="https://arxiv.org/abs/quant-ph/0102001" target="_blank">[BCWW01]</a></td>
     <td>❌ (N/A)</td>
     <td>⌛ (v0.0.1)</td>
   </tr>
   <tr>
      <td>3</td>
      <td>N=2<br>(Bipartite)</td>
      <td>Quantum Hashing Function</td>
      <td>2013</td>
      <td>F. Ablayev and A. Vasiliev</td>
      <td><a href="https://iopscience.iop.org/article/10.1088/1612-2011/11/2/025202" target="_blank">[AV13]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
    </tr>
    <tr>
       <td>4</td>
       <td>N=2<br>(Bipartite)</td>
       <td>Bell State Measurement<br>(BSM)</td>
       <td>1996</td>
       <td>M. Michler, K. Mattle, H. Weinfurter and A. Zeilinger</td>
       <td><a href="https://journals.aps.org/pra/abstract/10.1103/PhysRevA.53.R1209" target="_blank">[MMWZ96]</a></td>
       <td>❌ (N/A)</td>
       <td>⌛ (v0.0.1)</td>
     </tr>
     <tr>
       <td>5</td>
       <td>N>=3<br>(Multipartite)</td>
       <td>GHZ State Measurement<br>(GHZSM)</td>
       <td>-</td>
       <td>-</td>
       <td>-</td>
       <td>❌ (N/A)</td>
       <td>⌛ (v0.0.1)</td>
     </tr>
     <tr>
       <td>6</td>
       <td>N>=3<br>(Multipartite)</td>
       <td>W State Measurement<br>(WSM)</td>
       <td>-</td>
       <td>-</td>
       <td>-</td>
       <td>❌ (N/A)</td>
       <td>⌛ (v0.0.1)</td>
     </tr>
 </tbody>
</table>


### Quantum Networking and Quantum Communications

Available soon.


### Quantum Entanglements

<table class="tg">
 <thead>
   <tr>
     <th>#</th>
     <th>Name</th>
     <th>No. Parties</th>
     <th>Year</th>
     <th>Authors</th>
     <th>Ref.</th>
     <th>Tutorial(s)</th>
     <th>Build</th>
   </tr>
 </thead>
 <tbody>
   <tr>
     <td>1</td>
     <td>EPR<br>(Einstein-Podolski-Rosen)<br>Pair</td>
     <td>N=2<br>(Bipartite)</td>
     <td>1935</td>
     <td>A. Einstein, B. Podolski and N. Rosen</td>
     <td><a href="https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777" target="_blank">[EPR35]</a></td>
     <td>❌ (N/A)</td>
     <td>⌛ (v0.0.1)</td>
   </tr>
   <tr>
      <td>2</td>
      <td>Dicke State</td>
      <td>N>=2<br>(Bipartite)</td>
      <td>1954</td>
      <td>R. Dicke</td>
      <td><a href="https://journals.aps.org/pr/abstract/10.1103/PhysRev.93.99" target="_blank">[D54]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Bell States</td>
      <td>N=2<br>(Bipartite)</td>
      <td>1964</td>
      <td>J. Bell</td>
      <td><a href="https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195" target="_blank">[B64]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>GHZ<br>(Greenberger-Horne-Zeilinger)<br>State</td>
      <td>N>=3<br>(Multipartite)</td>
      <td>1989</td>
      <td>D. Greenberger, M. Horne and A. Zeilinger</td>
      <td><a href="https://link.springer.com/chapter/10.1007/978-94-017-0849-4_10" target="_blank">[GHZ89]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Werner State</td>
      <td>N>=3<br>(Multipartite)</td>
      <td>1989</td>
      <td>R. Werner</td>
      <td><a href="https://journals.aps.org/pra/abstract/10.1103/PhysRevA.40.4277" target="_blank">[W89]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
    </tr>
    <tr>
      <td>6</td>
      <td>W State</td>
      <td>N>=3<br>(Multipartite)</td>
      <td>2000</td>
      <td>W. Dür, G. Vidal and J. Cirac</td>
      <td><a href="https://arxiv.org/abs/quant-ph/0005115" target="_blank">[DVC00]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Cluster State</td>
      <td>N>=3<br>(Multipartite)</td>
      <td>2000</td>
      <td>H. Briegel and R. Raussendorf</td>
      <td><a href="https://arxiv.org/abs/quant-ph/0004051" target="_blank">[BR00]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Graph State</td>
      <td>N>=3<br>(Multipartite)</td>
      <td>2003</td>
      <td>M. Hein, J. Eisert and H. Briegel</td>
      <td><a href="https://arxiv.org/abs/quant-ph/0307130" target="_blank">[HEB03]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
 </tbody>
</table>


### Quantum True Randomness

<table class="tg">
 <thead>
   <tr>
     <th>#</th>
     <th>Name</th>
     <th>Year</th>
     <th>Authors</th>
     <th>Ref.</th>
     <th>Tutorial(s)</th>
     <th>Build</th>
   </tr>
 </thead>
 <tbody>
   <tr>
      <td>1</td>
      <td>Schrödinger's Cat</td>
      <td>1935</td>
      <td>E. Schrödinger</td>
      <td><a href="https://link.springer.com/article/10.1007%2FBF01491891" target="_blank">[S35]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
   </tr>
   <tr>
      <td>2</td>
      <td>Quantum Coin Tossing</td>
      <td>-</td>
      <td>-</td>
      <td><a href="https://qiskit.org/textbook/what-is-quantum.html" target="_blank">[QCT]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Quantum Hadamard Transform</td>
      <td>-</td>
      <td>-</td>
      <td><a href="https://en.wikipedia.org/wiki/Hadamard_transform" target="_blank">[QHT]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Quantum Random Number Generator<br>(QRNG)</td>
      <td>-</td>
      <td>-</td>
      <td><a href="https://qt.eu/discover-quantum/underlying-principles/qrng/" target="_blank">[QRNG]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Quantum Random Walks<br>(QRW)</td>
      <td>1993</td>
      <td>Y. Aharonov, L. Davidovich and N. Zagury</td>
      <td><a href="https://journals.aps.org/pra/abstract/10.1103/PhysRevA.48.1687" target="_blank">[ADZ93]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
    </tr>
 </tbody>
</table>

### Quantum Algorithms

Available soon.

