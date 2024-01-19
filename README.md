# CalcFEC

CalcFEC is a script designed to estimate the expected number of lost data packets and their corresponding packet loss rate in various network configurations.

## Methodology

The core function, `get_loss_num`, computes the expected packet loss in a network environment characterized by a specific number of data and parity packets, and a given dropout rate. The parameters are as follows:

- $N_d$: Number of data packets (`data_num`).
- $N_p$: Number of parity packets (`parity_num`).
- $d$: Dropout rate (`dropout`).

The expected number of lost packets, $L$, is given by:

$$
L=\sum_{i=1}^{N_d}{i \times P_d(i) \times P_p(i)}
$$

Where:
- $P_d(i)$ is the probability of exactly $i$ packets being lost: 

$$
P_d(i)=\binom{N_d}{i} \times d^i \times (1-d)^{N_d-i}
$$ 

- $P_p(i)$ is is the probability of insufficient parity packets for recovering $i$ lost packets:

$$
P_p(i) = \begin{cases} 
  1 & \text{if } i > N_p \\
  \sum_{j=0}^{\min(i,N_p)-1} \binom{N_p}{j} \times (1 - d)^j \times d^{N_p - j} & \text{otherwise}
  \end{cases}
$$

The packet loss rate is the ratio of expected lost packets to the total number of data packets:

$$
\text{Packet Loss Rate}=\frac{L}{N_d}
$$

## Usage

Run CalcFEC from the command line with two arguments:
- `data_num`: Total number of data packets.
- `dropout`: Dropout rate (probability of packet loss).

### Example Command:
```sh
python calcFEC.py 10 0.1
```

This command evaluates the expected packet loss and rate for different parity packet configurations, assuming 10 data packets and a 10% dropout rate.

### Output Format
```sh
[data_num/parity_num/dropout]: loss_num=<expected number of lost packets>, loss_rate=<packet loss rate>%
```
Each output line represents a different configuration of `parity_num` (ranging from `0` to `data_num`), and shows the corresponding expected packet loss and rate.