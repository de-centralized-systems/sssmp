""" Generates some test vectors by using the values of `pi` and `e` to determine the secrets to be shared and 
coefficients used for the normally randomized secret sharing process.
"""

import itertools
import json
import pathlib

from typing import Any, Dict, List, Tuple

import sssmp
import GF256


PI_BYTES = bytes.fromhex(
    "243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89"
    "452821e638d01377be5466cf34e90c6cc0ac29b7c97c50dd3f84d5b5b5470917"
)
E_BYTES = bytes.fromhex(
    "b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef"
    "324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb4f7c7b5757f59584"
    "90cfd47d7c19bb42158d9554f7b46bced55c4d79fd5f24d6613c31c3839a2ddf"
    "8a9a276bcfbfa1c877c56284dab79cd4c2b3293d20e9e5eaf02ac60acc93ed87"
    "4422a52ecb238feee5ab6add835fd1a0753d0a8f78e537d2b95bb79d8dcaec64"
    "2c1e9f23b829b5c2780bf38737df8bb300d01334a0d0bd8645cbfa73a6160ffe"
    "393c48cbbbca060f0ff8ec6d31beb5cceed7f2f0bb088017163bc60df45a0ecb"
    "1cd289b06cbbfea21ad08e1847f3f7378d56ced94640d6ef0d3d37be67008e18"
    "6d1bf275b9b241deb64749a47dfdfb96632c3eb061b6472bbf84c26144e49c2d"
    "04c324ef10de513d3f5114b8b5d374d93cb8879c7d52ffd72ba0aae7277da7ba"
)


fake_random_position = 0


def fake_random(b: int) -> bytes:
    global fake_random_position
    fake_random_bytes = E_BYTES[fake_random_position : fake_random_position + b]
    fake_random_position += b
    assert len(fake_random_bytes) == b, "Provided fake random bytes exhausted."
    return fake_random_bytes


def reset_fake_random_state():
    global fake_random_position
    fake_random_position = 0


def generate_test_vector(s: bytes, n: int, t: int) -> Dict[str, Any]:
    reset_fake_random_state()

    b = len(s)
    c: List[bytes] = [b""] * t
    for j in range(t):
        if j == 0:
            c[j] = s
        elif 0 < j < t - 1:
            c[j] = fake_random(b)
        else:
            c[j] = sssmp.coefficients_with_checksum(s, fake_random(b - 8))

    f: List[GF256.Polynomial] = []
    for k in range(b):
        f_k = GF256.Polynomial([c[j][k] for j in range(t)])
        f.append(f_k)

    shares: List[Tuple[int, bytes]] = []
    for i in range(1, n + 1):
        s_i = (i, bytes(f[k](i) for k in range(b)))
        shares.append(s_i)

    for tr in range(t, n + 1):
        for shares_for_recovery in itertools.combinations(shares, tr):
            assert sssmp.recover(shares_for_recovery) == s

    return {"s": s, "n": n, "t": t, "c": c, "shares": shares}


def fmt_test_vectors_python(vectors: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    lines.append("# fmt: off")
    lines.append("")
    lines.append("TEST_VECTORS = [")
    for v in vectors:
        s: bytes = v["s"]
        n: int = v["n"]
        t: int = v["t"]
        c: List[bytes] = v["c"]
        shares: List[Tuple[int, bytes]] = v["shares"]

        lines.append(f"    {{")
        lines.append(f'        "s": bytes.fromhex("{s.hex()}"),')
        lines.append(f'        "n": {n},')
        lines.append(f'        "t": {t},')
        lines.append(f'        "c": [')
        for cj in c:
            lines.append(f'            bytes.fromhex("{cj.hex()}"),')
        lines.append(f"        ],")
        lines.append(f'        "shares": [')
        for xi, yi in shares:
            lines.append(f'            ({xi}, bytes.fromhex("{yi.hex()}")),')
        lines.append(f"        ],")
        lines.append(f"    }},")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def fmt_test_vectors_json(vectors: List[Dict[str, Any]]) -> str:
    vectors_hex = [
        {
            "s": v["s"].hex(),
            "n": v["n"],
            "t": v["t"],
            "c": [c.hex() for c in v["c"]],
            "shares": [(xi, yi.hex()) for xi, yi in v["shares"]],
        }
        for v in vectors
    ]
    return json.dumps(vectors_hex, indent=4)


def generate_test_vectors() -> List[Dict[str, Any]]:
    test_vectors: List[Any] = []
    for b in [16, 20, 24, 28, 32]:
        for n in range(1, 6):
            for t in range(1, n + 1):
                test_vectors.append(generate_test_vector(PI_BYTES[:b], n, t))
    return test_vectors


def main():
    print("Generating test vectors.")
    vectors = generate_test_vectors()

    target_dir = pathlib.Path(__file__).parent
    target_json = target_dir.joinpath("test_vectors.json")
    target_py = target_dir.joinpath("test_vectors.py")

    print(f"Exporting test vectors to '{str(target_json)}'.")
    with open(target_json, "w") as f:
        f.write(fmt_test_vectors_json(vectors))

    print(f"Exporting test vectors to '{str(target_py)}'.")
    with open(target_py, "w") as f:
        f.write(fmt_test_vectors_python(vectors))


if __name__ == "__main__":
    main()
