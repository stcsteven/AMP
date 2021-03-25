# 7.4 Hamming Code 

## How it works
This folder describes on how to encode and decode message using 4-bit message and 3-bit parity. The following graphics shows on how to encode the 4-bits of message _d_ by appending _p_-bits as parity.
![Hamming Code](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Hamming%287%2C4%29.svg/300px-Hamming%287%2C4%29.svg.png)

**Note**: Hamming code can only detect and correct single bit error. 
### Encoding Process
According to the rules described in the graph, we can define the rule as following:
![image](https://user-images.githubusercontent.com/25889114/112511007-96521400-8dc4-11eb-9c5a-a05a7458cb99.png)

The equations above can be represented as matrix multiplication as follows:
![image](https://user-images.githubusercontent.com/25889114/112511103-a9fd7a80-8dc4-11eb-8ca7-64fd17549eb0.png)


where:
d: the message bits <br>
p<sub>n</sub>: the n<sup>th</sup> parity bit <br>
<ins>t</ins>: the coded transmission which consists of [d|p] <br>

### Decoding Process
In order to decode 7.4 Hamming, we need to invert the process such as follows:
![image](https://user-images.githubusercontent.com/25889114/112511159-baadf080-8dc4-11eb-8700-1afbd7200399.png)


where:
<ins>t</ins>: the coded transmission which consists of [d|p]

Let's say _abc_ are the assigned bits that satisfies each equations t5 until t7 in (3) respectively, it is found out that:
| Value  | Bit Representation  | bits in t that need change  |  
|--------|---------------------|-----------------------------|
|   0    | 000                 |    t3                       |
|   1    | 001                 |    t2                       |
|   2    | 010                 |    t1                       |
|   3    | 011                 |    t5                       |
|   4    | 100                 |    t4                       |
|   5    | 101                 |    t6                       |
|   6    | 110                 |    t7                       |
|   7    | 111                 |    -                        |

## Requirement
Python 3
