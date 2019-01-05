## Basic Logic
  - Minus(-) sign has four possible dealing ways:
    1. The first val is negative -> '-' sign stays to where it belongs;
    2. The first val is negative and user press another '-' button -> then equation will presented in -val '-' +/-val;
    3. The first val is positive/negative +/*// '-'val -> second val is negative;
    4. If pass all above constraints, then a '-' sign is used for the next round of calculation 
       -> resultFromLastRound '-' +/-val.
  - Equal('=') has the property of calculation and erase the past history. 
    1. calculate and erase the history after a legal equation is entered;
    2. If use enters the first val followed by '=' button, then result box will display the value entered by him/herself. AND back to the i step (erase the history)

