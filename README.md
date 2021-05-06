# DRAFT: Shamir Secret Sharing for Mnemonic Phrases

[![CC BY 4.0][cc-by-shield]][cc-by]

This repository contains the specification as well as the reference implementation of SSSMP (Sharmir Secret Sharing for Mneominc Phrases).
SSSMP is a secret sharing scheme with a particular focus on the use case of sharing random mnemonic phrases, as for example used within hierarchical deterministic wallets in context of cryptocurrencies.
With this focus in mind, this specification is designed to be fully compatible with existing encodings of mnemonic 
phrases, in particular [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).
It can for example be used to split a given (already existing) BIP39 mnemonic phrase of 12, 15, 18, 21, or 24 words, 
into up to $n = 255$ shares, such that any configurable subset of shares of size $t \leq n$ can be used to recover the 
original mnemonic phrase from the shares.
However, this specification is not limited to the use of BIP39 for encoding and decoding of mnemonic phrases, but rather
specifies the secret sharing on the level of byte sequences. 
Alternative encodings such as, e.g., [bytewords](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md), 
may be used instead of BIP39.
The design is intentionally kept as simple as possible, and only adds minor modifications, in particular an integrated 
checksum mechanism, to the original secret sharing approach described by 
[Shamir](https://dl.acm.org/doi/pdf/10.1145/359168.359176).

## Specification

The specification is maintained [here](https://github.com/de-centralized-systems/sssmp/docs/Specification.md), and an html export can be viewed [here on github.io](https://de-centralized-systems.github.io/sssmp/). 

## Reference Implementation

The reference implementation as well as all test vectors can be found [here](https://github.com/de-centralized-systems/sssmp/sssmp).

## License 

This work is licensed under the
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg


## Contributions

Contributions are very welcome - please generate a pull request or create an issue.
