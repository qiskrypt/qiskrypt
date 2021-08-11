
# Qis|krypt⟩

<img src="https://raw.githubusercontent.com/qiskrypt/qiskrypt.github.io/main/assets/images/logos/qiskrypt/PNGs/qiskrypt-logo-banner-2.png" alt="Qis|krypt⟩ - Logo" width="60%">

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
    <td>C. Bennet and G. Brassard</td>
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
     <td>Quantum Money</td>
     <td>1983</td>
     <td>C. Bennett, G. Brassard, S. Breidbart and S. Wiesner</td>
     <td><a href="https://dl.acm.org/doi/10.1145/1008908.1008920" target="_blank">[W83]</a>,<br><a href="https://link.springer.com/chapter/10.1007/978-1-4757-0602-4_26" target="_blank">[BBBW83]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>2</td>
     <td>Quantum Coin<br>(w/ Classical Verification)</td>
     <td>2011</td>
     <td>D. Gavinsky</td>
     <td><a href="https://arxiv.org/abs/1109.0372" target="_blank">[G11]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>3</td>
     <td>Quantum Cheque</td>
     <td>2016</td>
     <td>S. Moulick and P. Panigrahi</td>
     <td><a href="https://link.springer.com/article/10.1007/s11128-016-1273-4" target="_blank">[MP16]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>4</td>
     <td>Quantum Token</td>
     <td>2017</td>
     <td>M. Bozzio, A. Orieux, L. Vidarte, I. Zaquine, I. Kerenidis and E. Diamanti</td>
     <td><a href="https://arxiv.org/pdf/1705.01428.pdf" target="_blank">[BOZKD17]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>5</td>
     <td>Quantum Lighting</td>
     <td>2019</td>
     <td>M. Zhandry</td>
     <td><a href="https://link.springer.com/chapter/10.1007%2F978-3-030-17659-4_14" target="_blank">[Z19]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
 </tbody>
</table>


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
     <td rowspan="2">Quantum Data Authentication</td>
     <td>N=2<br>(Bipartite)</td>
     <td>Quantum Data Signature</td>
     <td>2001</td>
     <td>D. Gottesman and I. Chuang</td>
     <td><a href="https://arxiv.org/abs/quant-ph/0105032" target="_blank">[GC01]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
      <td>3</td>
      <td>N=2<br>(Bipartite)</td>
      <td>Quantum Message Authentication</td>
      <td>2002</td>
      <td>H. Barnum, C. Crepeau, D. Gottesman, A. Smith and A. Tapp</td>
      <td><a href="https://arxiv.org/abs/quant-ph/0205128" target="_blank">[BCGST02]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>4</td>
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
      <td>5</td>
      <td>N=2<br>(Bipartite)</td>
      <td>Quantum Hashing Function</td>
      <td>2013</td>
      <td>F. Ablayev and A. Vasiliev</td>
      <td><a href="https://iopscience.iop.org/article/10.1088/1612-2011/11/2/025202" target="_blank">[AV13]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
    </tr>
    <tr>
       <td>6</td>
       <td>N=2<br>(Bipartite)</td>
       <td>Bell State Measurement<br>(BSM)</td>
       <td>1996</td>
       <td>M. Michler, K. Mattle, H. Weinfurter and A. Zeilinger</td>
       <td><a href="https://journals.aps.org/pra/abstract/10.1103/PhysRevA.53.R1209" target="_blank">[MMWZ96]</a></td>
       <td>❌ (N/A)</td>
       <td>⌛ (v0.0.1)</td>
     </tr>
     <tr>
       <td>7</td>
       <td>N>=3<br>(Multipartite)</td>
       <td>GHZ State Measurement<br>(GHZSM)</td>
       <td>-</td>
       <td>-</td>
       <td>-</td>
       <td>❌ (N/A)</td>
       <td>⌛ (v0.0.1)</td>
     </tr>
     <tr>
       <td>8</td>
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


### Quantum Internet Protocols, Quantum Networking and Quantum Communications

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
      <td>Quantum Dice</td>
      <td>-</td>
      <td>-</td>
      <td><a href="https://medium.com/design-ibm/truly-quantum-dice-cfe372f4c586" target="_blank">[QD]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Quantum Random Number Generator<br>(QRNG)</td>
      <td>-</td>
      <td>-</td>
      <td><a href="https://qt.eu/discover-quantum/underlying-principles/qrng/" target="_blank">[QRNG]</a></td>
      <td>❌ (N/A)</td>
      <td>⌛ (v0.0.1)</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Quantum Random Walks<br>(QRW)</td>
      <td>1993</td>
      <td>Y. Aharonov, L. Davidovich and N. Zagury</td>
      <td><a href="https://journals.aps.org/pra/abstract/10.1103/PhysRevA.48.1687" target="_blank">[ADZ93]</a></td>
      <td>❌ (N/A)</td>
      <td>❌ (N/A)</td>
    </tr>
 </tbody>
</table>


### Quantum Distance Measures and Quantum Metrics

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
     <td>Quantum Entropy<br>(von Neumann Entropy)</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1932</td>
     <td>J. Neumann</td>
     <td><a href="https://press.princeton.edu/books/hardcover/9780691178561/mathematical-foundations-of-quantum-mechanics" target="_blank">[N32]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>2</td>
     <td>Quantum Conditional Entropy</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1995</td>
     <td>N. Cerf and C. Adami</td>
     <td><a href="https://arxiv.org/abs/quant-ph/9512022" target="_blank">[CA95]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>3</td>
     <td>Quantum Relative Entropy</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>2000</td>
     <td>B. Schumacher and M. Westmoreland</td>
     <td><a href="https://arxiv.org/abs/quant-ph/0004045" target="_blank">[SW00]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>4</td>
     <td>Quantum Joint Entropy</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>2001</td>
     <td>L. Henderson and V. Vedral</td>
     <td><a href="https://arxiv.org/abs/quant-ph/0105028" target="_blank">[HV01]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>5</td>
     <td>Quantum Shannon Distinguishability</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1948</td>
     <td>C. Shannon</td>
     <td><a href="https://ieeexplore.ieee.org/document/6773024" target="_blank">[S48]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>6</td>
     <td>Quantum Fidelity</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1994</td>
     <td>R. Josza</td>
     <td><a href="https://www.tandfonline.com/doi/abs/10.1080/09500349414552171" target="_blank">[J99]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>7</td>
     <td>Bhattacharyya Coefficient</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1996</td>
     <td>C. Fuchs and C. Caves</td>
     <td><a href="https://arxiv.org/abs/quant-ph/9604001" target="_blank">[FC96]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>8</td>
     <td>Trace Distance<br>(Kolmogorov Distance)</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1997</td>
     <td>C. Fuchs and J. Graaf</td>
     <td><a href="https://arxiv.org/abs/quant-ph/9712042" target="_blank">[FG97]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>9</td>
     <td>Monogamy of Quantum Entanglement</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>1999</td>
     <td>V. Coffman, J. Kundu and W. Wootters</td>
     <td><a href="https://arxiv.org/abs/quant-ph/9907047" target="_blank">[CKW99]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
   <tr>
     <td>10</td>
     <td>Quantum Discord</td>
     <td>N>=2<br>(Multipartite)</td>
     <td>2001</td>
     <td>H. Ollivier and W. Zurek</td>
     <td><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.88.017901" target="_blank">[OZ01]</a></td>
     <td>❌ (N/A)</td>
     <td>❌ (N/A)</td>
   </tr>
 </tbody>
</table>

### Quantum Algorithms

Available soon.


### Other references

Other some references for some of the developed protocols can be found here:
* [Quantum Protocol Zoo](https://wiki.veriqloud.fr/)
* [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)
* [Quantiki](https://www.quantiki.org/)

***
