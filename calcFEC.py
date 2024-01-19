import sys
import math


def get_loss_num(data_num: int, parity_num: int, dropout: float):
    res = 0
    for i in range(1, data_num + 1):
        res_d = (
            math.comb(data_num, i) * pow(dropout, i) * pow(1 - dropout, data_num - i)
        )
        if i > parity_num:
            res_p = 1
        else:
            res_p = 0
            for j in range(min(i, parity_num)):
                res_p += (
                    math.comb(parity_num, j)
                    * pow(1 - dropout, j)
                    * pow(dropout, parity_num - j)
                )
        res += i * res_d * res_p
    return res


if __name__ == "__main__":
    args = sys.argv
    data_num = int(args[1])
    dropout = float(args[2])
    for parity_num in range(data_num + 1):
        loss_num = get_loss_num(data_num, parity_num, dropout)
        loss_rate = loss_num / data_num * 100
        print(f"[{data_num}/{parity_num}/{dropout}]: loss_num={loss_num}, loss_rate={loss_rate:.5f}%")

