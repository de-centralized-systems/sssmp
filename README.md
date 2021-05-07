# DRAFT: Shamir Secret Sharing for Mnemonic Phrases

[![CC BY 4.0][cc-by-shield]][cc-by]

This repository contains the Shamir Secret Sharing for Mnemonic Phrases (SSSMP) 
[specification](https://de-centralized-systems.github.io/sssmp/) and the corresponding
[reference implementation](https://github.com/de-centralized-systems/sssmp/blob/main/src).
SSSMP is a secret sharing scheme with a particular focus on the use case of sharing random mnemonic phrases, 
as for example used within hierarchical deterministic wallets in context of cryptocurrencies.
With this focus in mind, this specification is designed to be fully compatible with existing encodings of mnemonic 
phrases, in particular [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).
It can, for example, be used to split a given (already existing) BIP39 mnemonic phrase of 12, 15, 18, 21, or 24 words, 
into up to *n = 255* shares, such that any configurable subset of shares of size *t ≤ n* can be used to recover the 
original mnemonic phrase from the shares.
However, this specification is not limited to the use of BIP39 for encoding and decoding of mnemonic phrases, 
but rather specifies the secret sharing on the level of byte sequences. 
Alternative encodings such as, e.g., 
[bytewords](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md), 
may be used instead of BIP39.
The design is intentionally kept as simple as possible, and only adds minor modifications, 
in particular an integrated checksum mechanism, to the original secret sharing approach described by 
[Shamir (1979)](https://dl.acm.org/doi/pdf/10.1145/359168.359176).

## Specification

For better readability of the mathematical notation used within the specification, 
we recommend viewing the [HTML export of the specification](https://de-centralized-systems.github.io/sssmp/). 
The specification itself is maintained in the 
[Specification.md](https://github.com/de-centralized-systems/sssmp/blob/main/docs/Specification.md) 
markdown file within the 
[`./docs`](https://github.com/de-centralized-systems/sssmp/blob/main/docs) 
directory of this repository.  


## Reference Implementation

The [reference implementation](https://github.com/de-centralized-systems/sssmp/blob/main/src/sssmp.py)
as well as a set of 
[test vectors](https://github.com/de-centralized-systems/sssmp/blob/main/src/test_vectors.json)
can be found in the 
[`./src`](https://github.com/de-centralized-systems/sssmp/blob/main/src) 
directory of this repository.

## License 

This work is licensed under the
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg


## Contributions

Contributions are very welcome, please contact us directly, generate a pull request or create an issue.
