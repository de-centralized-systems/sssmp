""" Reference implementation of the Shamir Secret Sharing for Mnemonic Phrases (SSSMP) specification.
The implemenation is designed to be minimalistic, and closely resembles the specification.
See also: https://de-centralized-systems.github.io/sssmp/
"""

import hmac
import secrets

from typing import List, Optional, Sequence, Tuple

import GF256


def random(b: int) -> bytes:
    """ Helper function to create a sequence of `b` random bytes using a cryptographically secure source of randomness.
    """
    return secrets.token_bytes(b)


def coefficients_with_checksum(s: bytes, r: bytes) -> bytes:
    """ Helper function to compute a list of coefficients with the included checksum.
    """
    return r + hmac.new(key=s, msg=b"secret sharing coefficient" + r, digestmod="sha256").digest()[:8]


def share(s: bytes, n: int, t: int) -> List[Tuple[int, bytes]]:
    """ Main function for creating `n` shares of a secret `s` such that any subset of at least `t` generated shares
    can be used to recovered the secret `s`.
    """
    b = len(s)
    if not (1 <= t <= n <= 255):
        raise ValueError("Invalid secret sharing parameters, ensure that 1 <= t <= n <= 255 holds.")
    if b <= 16:
        raise ValueError("Invalid secret given, the minimum required secret length is 16 bytes (128 bits).")

    c: List[bytes] = [b""] * t
    for j in range(t):
        if j == 0:
            c[j] = s
        elif 0 < j < t - 1:
            c[j] = random(b)
        else:
            c[j] = coefficients_with_checksum(s, random(b - 8))

    f: List[GF256.Polynomial] = []
    for k in range(b):
        f_k = GF256.Polynomial([c[j][k] for j in range(t)])
        f.append(f_k)

    shares: List[Tuple[int, bytes]] = []
    for i in range(1, n + 1):
        s_i = (i, bytes(f[k](i) for k in range(b)))
        shares.append(s_i)

    return shares


def recover(shares: Sequence[Tuple[int, bytes]]) -> bytes:
    """ Main function for recovering a previously shared secret from a list of given shares.
    """
    if not (1 <= len(shares) <= 255):
        raise ValueError("Invalid number of shares provided.")

    if len({xi for xi, _ in shares}) != len(shares):
        raise ValueError("Invalid shares provided, duplicate share indices detected.")
    if not all(1 <= xi <= 255 for xi, _ in shares):
        raise ValueError("Invalid shares provided, out of range share index/indices detected.")

    b = len(shares[0][1])
    if b < 16:
        raise ValueError("Invalid shares provided, share length below the minimum of 16 bytes (128 bits).")
    if any(len(yi) != b for _, yi in shares):
        raise ValueError("Invalid shares provided, share lengths are inconsistent.")

    # Compute the secret via Lagrange interpolation.
    s = bytearray(b)
    for xi, yi in shares:
        li = 1
        for xj, _ in shares:
            if xi != xj:
                li = GF256.multiply(li, GF256.multiply(xj, GF256.inverse(xj ^ xi)))
        for k in range(b):
            s[k] ^= GF256.multiply(yi[k], li)
    s = bytes(s)

    # Verify the checksum and return the reconstructed secret or raise an error if the check fails.
    if verify_checksum(s, shares):
        return s
    raise ValueError("Checksum verification failed.")


def verify_checksum(s: bytes, shares: Sequence[Tuple[int, bytes]]):
    """Verifies the checksum integrated into the last coefficients of the secret sharing polynomials. Returns `True` if 
    the checksum is found valid and `False` otherwise.
    """
    if len(shares) == 1:
        return True

    c_last: Optional[bytes] = recover_checksum_coefficients(shares)
    if c_last is None:
        # Secret sharing threshold was 1, so there is no checksum.
        return True

    r = c_last[:-8]
    return c_last == coefficients_with_checksum(s, r)


def recover_checksum_coefficients(shares: Sequence[Tuple[int, bytes]]) -> Optional[bytes]:
    """Computes the last coefficients (index > 0) of the underlying secret sharing polynomials defined by the given
    shares by using the recursive definition of dividing differences.

    Link to German wikipedia:
    https://de.wikipedia.org/wiki/Polynominterpolation#Bestimmung_der_Koeffizienten:_Schema_der_dividierten_Differenzen

    Let, e.g., [(x0, y0), (x1, y1), ..., (x4, y4)] denote the shares.
    The last cofficients of the polynomials defined by these shares is given as the bottom right value of the
    following triangle, in this case t44.

    t00=y0
    t10=y1   t11=(t10^t00)/(x1^x0)
    t20=y2   t21=(t20^t10)/(x2^x1)   t22=(t21-t11)/(x2-x0)
    t30=y3   t31=(t30^t20)/(x3^x2)   t32=(t31-t21)/(x3-x1)   33=(t32-t22)/(x3^x0)
    t40=y4   t41=(t40^t30)/(x4^x3)   t42=(t41-t31)/(x4-x2)   43=(t42-t32)/(x4^x1)   t44=(t43-t33)/(x4^x0)

    t[i][0] = y[i]
    t[i][j] = (t[i][j-1] ^ t[i-1][j-1]) / (x[i] ^ x[i-j])

    The computation is done byte by byte (see the innermost `byte_index` generator expression).
    """
    share_len = len(shares[0][1])
    triangle: List[List[bytes]] = []
    for i, (_, yi) in enumerate(shares):
        row = [yi]
        triangle.append(row)
        for j in range(1, i + 1):
            row.append(
                bytes(
                    GF256.multiply(
                        (triangle[i][j - 1][byte_index] ^ triangle[i - 1][j - 1][byte_index]),
                        GF256.inverse(shares[i][0] ^ shares[i - j][0]),
                    )
                    for byte_index in range(share_len)
                )
            )

    # Return the bottom-right value of the triangle. In case more shares than the original threshold are given, this
    # coefficient is zero for all bytes, and last (bottom-right) non-zeros value is the one returned.
    zero = bytes(share_len)
    last_non_zero_index = len(triangle) - 1
    while True:
        value = triangle[last_non_zero_index][-1]
        if last_non_zero_index == 0:
            # All but the coefficient with index 0 are zero. Therefore the actual secret sharing threshold is 1 and
            # there is no 'last' coefficient.
            return None
        if value != zero:
            return value
        last_non_zero_index -= 1
