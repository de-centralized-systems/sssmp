
# DRAFT: Shamir Secret Sharing for Mnemonic Phrases

Authors: Aljosha Judmayer, Philipp Schindler  
Status: DRAFT  
Version: 0.1  
Last revision: 2021-05-06  
Initial release: -

## Abstract 

The document describes a secret sharing scheme with a particular focus on the use  
case of sharing random mnemonic phrases, as for example used within hierarchical deterministic wallets in context of 
cryptocurrencies.
With this focus in mind, this specification is designed to be fully compatible with existing encodings of mnemonic 
phrases, in particular [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).
It can be used to split a given (already existing) BIP39 mnemonic phrase of 12, 15, 18, 21, or 24 words, 
into up to $n = 255$ shares, such that any configurable subset of shares of size $t \leq n$ can be used to recover the 
original mnemonic phrase from the shares.
However, this specification is not limited to the use of BIP39 for encoding and decoding of mnemonic phrases, but rather
specifies the secret sharing on the level of byte sequences. 
Alternative encodings such as, e.g., 
[bytewords](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md), 
may be used instead of BIP39.
The design is intentionally kept as simple as possible, and only adds minor modifications, in particular an integrated 
checksum mechanism, to the original secret sharing approach described by 
[Shamir](https://dl.acm.org/doi/pdf/10.1145/359168.359176).

## Status of This Memo

This document is not an official standard; it is published without any warranty for informational purposes and aims to: 
consolidate community best practices, foster public review as well as contribution and 
motivate the creation of official standards based on the here provided material. 

Information about the current status of this document, any errata, and how to provide feedback on it may be obtained at
[Github](https://github.com/de-centralized-systems/sssmp).

## Copyright Notice

This work is licensed under the
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## Terminology

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", 
"NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 
([RFC2119](https://tools.ietf.org/html/rfc2119), [RFC8174](https://tools.ietf.org/html/rfc8174)) when, and only when, 
they appear in all capitals, as shown here.

## Introduction

The demand of deriving and managing an increasing number of secret keys has risen in recent years.
This is mostly due to the widened adoption of cryptocurrencies and their increase in valuation. 
These developments have fostered the creation of several different approaches to derive, encode and manage cryptographic 
key material, within the respective community.

This specification attempts to consolidate community best practices and well known and established cryptographic 
techniques, in relation to the secret sharing of cryptographic key material.
Therefore, key requirements and design goals are formulated and separated in into different layers and processing steps
of managing and deriving cryptographic key material. 
This should provide the necessary bigger picture and define the context in which this specification has to be 
interpreted. 
The aim of this document is it to specify a minimalistic and interoperable method for the secret sharing of 
cryptographic key material intended 
for manual/human processing, e.g., as used in private offline/paper backups of mnemonic seed phrases. 

### <a name="Scope"></a>Scope, Goals and Non-goals

To describe the scope of this document, the relation to other processing steps in deriving and managing cryptographic 
key material has to be outlined. 

* **Generation of a cryptographic key**
At this point a new key $s$ is generated from a cryptographically secure source of randomness. 
In most cases, this marks the first step in a hierarchically deterministic derivation of further key material. 
Therefore, an initial key is sometimes also called *seed-key*. 
This step is not within the scope of this document and MUST have taken place before the here specified scheme can be 
applied to a key $s$. 

* **Derivation of a cryptographic key**
A generated, or derived, key $s$ can be used to derive one or multiple further keys from the input key according to a 
specified scheme like for example [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki).
or [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki). The resulting key is then called 
*derived key*. 
This step is not within the scope of this document and MAY have taken place before the here specified scheme can be 
applied to a derived key $s$. 

* **Hidden derivation of a cryptographic key**
A hidden derivation step can be applied to a generated, or derived, key $s_1$ to allow for hidden derivation paths, 
plausible deniability through multiple derivation paths, or prevent the computation of subsequent derivation steps in 
the key hierarchy, 
Therefore, this step requires an additional secret/key $s_2$ as input, like for example a passphrase as in 
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki). 
The additional user supplied passphrase is then used as a message in PBKDF2 with the reconstructed secret as password.
This step is out-of-scope of this document and MAY be use in combination with the here specified scheme. 
For example, such a step can be applied after a secret has been reconstructed and before it is processed in further 
derivation steps.

* **Mnemonic encodeing/decodeing of a cryptographic key**
A generated, or derived, key $s$ can be represented as a mnemonic phrase to improve human readability and easer manual 
copying of key material or key shares. Example for such schemes are 
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), or 
[bytewords](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md).
This step is out-of-scope of this document and such techniques SHOULD be used in combination with the here specified 
scheme. 

* **Secret sharing of a cryptographic key**
A generated, or derived, key $s$ is shared amongst a set of $n$ participants, where $t$ should be able to reconstruct 
the original key $s$. 
In this specification we focus exclusively on this step.

#### Goals
+ Simple scheme compatible with the reconstruction of classical Shamir Secret Sharing (SSS)
+ Additional checksum for detecting invalid reconstructions without further derivations of key material 

#### Non-Goals 
- Specification of how the input key $s$ has to be contacted, despite the requirement that is has to be of 
  high-min-entropy. 
- Specification of a concrete key length despite enforcing a minimum of 128 bit. 
- Specification of mnemonic encoding used for input and output data
- Specification of further hidden derivation steps for plausible deniability or and additional layers of security. 

### Background

This specification is based on classical [Shamir Secret Sharing](https://dl.acm.org/doi/pdf/10.1145/359168.359176) 
(SSS) and adds a checksum mechanism in the construction step.
The added checksum does not affect the reconstruction of classical SSS if it is not checked. 
The specified scheme is intended to share high min-entropy cryptographic key material, i.e., a secret $s$, 
amongst a set of $n$ participants, such that at least $t$ are required to reconstruct the original secret $s$. 
A detailed comparison between related implementations of secret sharing schemes based on SSS and utilized in this 
context of cryptocurrencies (like
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki),
[BC-SSKR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-011-sskr.md),
[Shamir39](https://iancoleman.io/shamir39/), etc.)
is out of scope of this document. 

### Notation and Symbols

The following tables provides an overview of the used notation in the reminder of this document.

| Symbol                  | Description                                                                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $n$                     | total number of shares to be created $\left(1 \leq n \leq 255\right)$                                                                                                                                         |
| $t$                     | minimum number of shares required for the recovery process $\left(1 \leq t \leq n\right)$                                                                                                                     |
| $b$                     | number of bytes of a given secret or share                                                                                                                                                                    |
| $s$                     | the secret value to be shared, represented by a sequence of $b$ bytes                                                                                                                                         |
| $i$                     | an index variable used for the secret shares; $1 \leq i \leq n$ or $1 \leq i \leq t$ depending on the context                                                                                                 |
| $j$                     | an index variable used for the coefficient of the secret sharing polynomials; $0 \leq j < t$                                                                                                                  |
| $k$                     | an index variable used to denote the $k^\textsf{th}$ byte in the secret, a share or the $k^\textsf{th}$ secret sharing polynomial; $0 \leq k < b$                                                             |
| $s_i$                   | a share of the secret $s$; consists a share index $x_i$ (an integer between $1$ and $255$) and share value $y_i$ (a sequence of $b$ bytes)                                                                    |
| $c_j$                   | the $j^{\textsf{th}}$ coefficients of the secret sharing polynomials as a sequence of $b$ bytes; the byte $c_j[k]$ represents the $j^{\textsf{th}}$ coefficient of the secret sharing polynomial $f_k(\cdot)$ |
| $f_k(\cdot)$            | the secret sharing polynomial used to share the $k^{\textsf{th}}$ byte of the secret $s$                                                                                                                      |
| $\alpha \mid\mid \beta$ | concatenation of two sequences of bytes $\alpha$ and $\beta$                                                                                                                                                  |
| $\alpha[k]$             | the $k^\textsf{th}$ byte of the sequence of bytes $\alpha$, 0-based indices used                                                                                                                              |
| $\alpha[:k]$            | the first $k$ bytes of the sequence of bytes $\alpha$                                                                                                                                                         |



## <a name="Sharing"></a>Sharing

In the following, we specify the process of creating $1 \leq n \leq 255$ shares $(s_1, s_2, ..., s_n)$ for a given 
secret $s$ (a sequence of $b \geq 16$ bytes) such that any subset of at least $1 \leq t \leq n$ of those shares can be 
used to recover the shared value.

**Input:** 
 - $\mathbf{s}$: The secret to be shared, i.e., a sequence of $b$ bytes, where $b \geq 16$.
 - $\mathbf{n}$: The number of shares to be generated, $1\leq n \leq 255$.
 - $\mathbf{t}$: The secret sharing threshold, $1 \leq t \leq n$. 
                 This value specifies the minimum number of shares required for the recovery process.

**Output:** 
 - $\mathbf{s_1, s_2, \dots, s_n}$: A list of $n$ shares. Each share $s_i$ is represented as a tuple 
   $(x_i, y_i)$ consisting of the share index $x_i = i$ (an integer from $1$ to $255$) and the share value $y_i$ 
   (a sequence of $b$ bytes).

Note that typical values for $n$ and $t$ are in the range $2 \leq t \leq 255$ .
If $t = 1$, the number of shares required for the recovery is one.
In this case, each share created is just the value being shared.
If $t = n$, all created shares are required for the recovery process.
If, for example, $n = 5$ and $t = 3$, then $5$ shares are created in total. 
and each combination of at least $3$ shares can be used to recover the shared secret.

The process of secret sharing is executed on a byte-per-byte basis, 
i.e., each of the $b$ bytes of the secret $s$ to be shared is processed individually. 
This allows for a simple and efficient implementation using the finite field $\text{GF}(2^8)$ with 256 elements. 
In this field addition and subtraction of two field elements (two bytes) are defined using the bitwise xor operation.
Multiplication of two field elements (again two bytes) is defined using the
AES reducing polynomial $x^8 + x^4 + x^3 + x + 1$. 
For additional background information regarding finite field arithmetics we refer to the
[Wikipedia page on Finite Field Arithmetic](https://en.wikipedia.org/wiki/Finite_field_arithmetic).
The used secret sharing polynomials $f_0(\cdot), f_1(\cdot), \dots, f_{b-1}(\cdot)$ of degree $t - 1$
are evaluated over $\text{GF}(2^8)$:
$$
  f_k(x) = c_0[k] + c_1[k] \cdot x + c_2[k] \cdot x^2 + \dots + c_{t - 1}[k] \cdot x^{t - 1}, \quad 0 \leq k < b.
$$
Note that here the values of $c_0, c_1, \dots, c_{t - 1}$ are used to represent lists of coefficients, 
whereas the $k^\textsf{th}$ element of each of the lists of coefficients is used to 
define the secret sharing polynomial for sharing the $k^\textsf{th}$ byte of the secret $s$.

Each list of coefficients $c_j \mid 0 \leq j < t$ is defined as follows:
$$
    c_j = 
    \begin{cases} 
        s &\text{if } j = 0 \\
        \textsf{random}(b) &\text{if } 0 < j < t - 1 \\
        \textsf{coefficients\_with\_checksum}(s, \textsf{random}(b - 8)) &\text{otherwise }(j =t -1 \land t > 1)
    \end{cases}
$$
Hereby, the function $\textsf{random}(b)$ creates a list of $b$ random bytes.
The function MUST use a cryptographically secure source of randomness.
If $t > 1$, the last coefficient $c_{t - 1}$ is derived from the secret $s$ 
and a sequence $r$ of $b-8$ random bytes.
This is done as defined by the $\textsf{coefficients\_with\_checksum}(s, r)$ function
for the purpose of including a checksum as the last $8$ bytes of $c_{t - 1}$.
$$
\textsf{coefficients\_with\_checksum}(s, r) = \\
r\ \mid\mid \ \text{HMAC}_{\text{SHA256}}(\text{key}=s,\  \text{msg}=\texttt{"secret sharing checksum"} \mid\mid r)[:8]
$$
Here, $[:8]$ is used to denote the first (leftmost) $8$ bytes of the given HMAC. 
The use of $r$ as argument to the HMAC message, ensures that all bits of the coefficients $c_{t - 1}$ 
are (pseudo-) random. 
Therefore, even if a the same secret $s$ is shared multiple times, the last coefficient is different with high 
probability.
Given this definition of coefficients (and thus of the secret sharing polynomials), 
the $n$ shares $s_1, s_2, ..., s_n$ are computed as follows:
$$
   s_i = \left( i, f_0(i) \mid\mid f_1(i) \mid\mid \dots \mid\mid f_{b-1}(i) \right) \quad 1 \leq i \leq n
$$
Note that a share is a tuple of two values and MUST include the share index $i$ as well as the share value, 
obtained by evaluating the secret sharing polynomials and concatenating the results.

The only difference to Shamir's original secret sharing is the definition of coefficient $c_{t - 1}$.
In Shamir's original description, all coefficients $c_j \mid 0 < j < t$ are selected at random, 
whereas in our approach all but the last $8$ bytes of the list of coefficients $c_{t - 1}$ are selected at random, 
whereas the last $8$ bytes are pseudo-randomly derived from the secret $s$ and all but the last $8$ bytes using an HMAC.


## <a name="Recovery"></a>Recovery

This section describes how to reconstruct a secret, from a set of $t$ given shares, 
computed with the method specified in [Section Sharing](#Sharing).
Implementations MUST be able to successfully recover the shared secret $s$, if all given shares are 
*valid* and a *sufficient number* of shares is provided. 
* A share is considered valid if it was generated according this specification.
* The number of shares provided is sufficient if it matches or exceeds the secret sharing threshold used during the 
  sharing process.

Implementation MAY provide additional functionality to aid with the recovery process in case invalid shares are 
provided. In this case implementations MUST provide a suitable warning message to the user to indicate the 
issue(s) with the provided shares. Advanced recovery functionality MUST explicitly be invoked by the user.

Input:
 - $\mathbf{\{s_1, s_2, \dots, s_{t}\}}$: 
   A set of $t$ shares which should be used to recover a previously shared secret.
   Each share $s_i \mid 1 \leq i \leq t$ is given as a tuple $(x_i, y_i)$ 
   of a share index $x_i$ (an integer from $1$ to $255$) and 
   a share value $y_i$ (a sequence of $b$ bytes). 

Output:
 - $\mathbf{s}$: The recovered secret.

Implementations MUST reject inputs prior to attempting the recovery process, 
and display a corresponding error message in the following cases:
 - The set of shares contains invalid share indices.
   This is the case if $1 \leq x_i \leq 255$ does not hold for some $x_i$, 
   or if the shares contain duplicated shares indices.
 - The set of shares contains invalid share values.
   This is the case if there is a share value of less than $16$ bytes in length,
   or if the share length across the shares is inconsistent (i.e., different) for two or more shares.

If the inputs are successfully validated according to this plausibility checks, 
implementations attempt to recover the shared secret $s$ from the given set of shares $\{s_1, s_2, \dots, s_t\}$.
For this purpose the underlying secret sharing polynomials $f_k(\cdot)$ 
are evaluated using the Lagrange interpolation formula: 
$$
  f_k(x) = \sum_{i = 1}^{t} y_i[k] \cdot \ell_i(x), 
  \quad 0 \leq k < b
$$
$$
  \ell_i(x) = \prod_{\substack{j = 1 \\ i \not = j}}^{t} \frac{x - x_j}{x_i - x_j}
$$

To recover the shared secret $s$ we apply the above formula for $x = 0$:
$$
  s[k] = c_0[k] = f_k(0) = 
    \sum_{i = 1}^{t} y_i[k] 
      \prod_{\substack{j = 1 \\ i \not = j}}^{t} 
        \frac{x_j}{x_j - x_i}, 
  \quad 0 \leq k < b.
$$
Neglecting the notational differences covering the byte-per-byte execution of the process, 
this approach is essentially equal to Shamir's original description. 

### <a name="Checksum Verification"></a>Checksum Verification

For the case where $t = 1$, each generated share is equal to the shared secret itself.
In this case there is no integrated checksum and the checksum verification steps are skipped.
The value $s$ is directly returned as result of the recovery process.

Otherwise, after recovery, but before returning the recovered secret $s$ to the user, 
the integrated checksum MUST be verified.
In case the verification fails, the user MUST be informed about the invalid checksum, 
and the recovered secret $s$ MUST NOT be displayed without such a warning.

The last list of coefficients $c_{t - 1}$ used to define the secret sharing polynomials were generated 
to include a (randomized) checksum using the HMAC mechanism introduced in 
[Section Sharing](#Sharing).
In order to verify this checksum, 
first the value of the coefficients $c_{t - 1}$ are computed 
from the set of $t$ shares $\{(x_1, y_1), (x_2, y_2), \dots, (x_t, y_t)\}$ 
supplied for the recovery process. 
This, e.g., MAY be accomplished using the [schemata of diving differences](https://de.wikipedia.org/wiki/Polynominterpolation#Bestimmung_der_Koeffizienten:_Schema_der_dividierten_Differenzen) 
illustrated in the following.
The process of recovering the values of the coefficients $c_{t - 1}$ using the schemata of diving differences, 
as the secret sharing process itself, is performed on a byte-per-byte basis 
for each byte in the list of coefficients $c_{t - 1}$ using $k$ as index variable:
$$
  c_{t - 1}[k] = [x_0, x_1, \dots, x_{t - 1}] f_k\ \quad 0 \leq k < b.
$$
Here, $[x_0, x_1, \dots, x_{t - 1}] f_k$ denotes the dividing difference of the secret sharing polynomial $f_k$ and is 
recursively defined as given below:
$$
  [x_i] f_k = y_i[k]
$$
$$
  [x_i, \dots, x_j] f_k = \frac{[x_{i+1}, \dots, x_j] f_k - [x_i, \dots, x_{j-1}] f_k}{ x_j[k] - x_i[k]}.
$$
Note that, as with the secret sharing process itself, all computations are performed in $\text{GF}(2^8)$.
Subtraction in $\text{GF}(2^8)$ is the same as addition and implemented using a binary xor operation.

With the value of $c_{t - 1}$ recovered using the above process, 
and the values of $s = c_0$ obtained during the recovery process, 
the integrated checksum is verified by first getting the 
value $r$ as all but the last $8$ bytes of $c_{t - 1}$ 
and then recomputing and comparing the value of $c_{t - 1}$ 
using the $\textsf{coefficients\_with\_checksum}(\cdot)$ function:
$$
  r = c_{t - 1}[: b-8]  \\
  c_{t - 1} \overset{?}{=} \textsf{coefficients\_with\_checksum}(s, r).
$$
The checksum is valid if and only if the above equality holds.
If the checksum is found valid, the value $s$ is returned as result of the recovery process. 
Otherwise the user MUST be informed of the failed recovery attempt. 
In this case, implementations MAY choose to return the recovery secret $s$ anyway, but they MUST NOT do so without
provided the user with a clear indication of the failed checksum verification.

### Metadata

Besides $t$ share values with their associated indices, nothing is needed to reconstruct the previously shared secret.
Although, for practical purposes it is RECOMMENDED that implementations also generate a unique ID which represents the 
individual secret sharing session. 

This secret sharing session identifier SHOULD be written down together with the mnemonic encoding of the share as well 
as its index. 
This ensures that shares of multiple different sessions do not get mixed and thus confused with each other.

Note that, if shares of multiple different sessions with large $n$ values get mixed, this might lead to a
situation where it is no longer computationally feasible to perform a brute-force search to find the valid combinations 
which allow for the reconstruction of the original secrets. 


## Design and Security Considerations

### Minimal secret size and intended use case

The minimal input size of the secret to be shared with the secret sharing mechanism specified in this document is 
limited to $128$ bits ($16$ bytes). 
This is equivalent to the lower bound for cryptographic secrets consider by a range of other designs in this field.
Any implementation of this specification MUST NOT allow secrets smaller than this size to be shared.
In contrast to Shamir's original secret sharing description, which provides information theoretic security, 
our variant (due to the inclusion of an integrated checksum) is not designed for sharing low-entropy secrets and 
may become insecure under these circumstances.
Also this specification MUST NOT be used as basis for an implementation for secret sharing of arbitrary data.
It is instead intended to share cryptographic secrets with a minimum of $128$ bits of entropy.
If against this rule, a very low entropy secret would be shared, the inclusion of a $64$ bit checksum may allow an 
attacker with possession of $t - 1$ shares to brute-force the shared secret, using the checksum at means to verify 
if a guess of the secret is correct.

To share arbitrary data, it is RECOMMENDED to encrypt the data using a suitable (symmetric) encryption algorithm 
and only share the (symmetric) encryption key using the method specified in this document.

### Checksum

The specification defines the secret sharing process on the level of bytes. 
It it intended to be used with encoding schemes such as
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) or 
[Bytewords](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md) to
encode/decode the in- and outputs. 
These encoding schemes are already designed to add additional safeguards to detect errors, e.g., they include a 
dedicated checksum and represent bytes as words with a minimum required Damerau-Levenshtein distance etc.
Therefore, no additional checksums and metadata is appended to the raw data output by the secret sharing algorithm in 
this specification.

Unfortunately, these encoding-level checksums used in mnemonics do not allow for error detection in cases where 
syntactically correct, but semantically invalid, shares are provided to the recovery process.
These cases include, the following scenarios:

- The recovery process is attempted with a collection of shares generated by two (or more) different secret sharing 
  instances (using different coefficients or secrets). 
- One or more parties deliberately crafts correct-looking shares with invalid share values to prevent the 
  recovering entity to learn the originally shared secret.

In both cases, the recovery process would silently return some recovered secret, 
which is different to the secret originally shared, when no additional countermeasures are implemented.
It is strongly desirable to detect, and potentially be able to recover from, these scenarios.
Therefore, this specification includes a checksum mechanism, by deriving this last coefficient for the secret sharing 
polynomial is a special way. 
While there are many different approaches to cover these scenarios, the approach used in this specification achieves a 
range of desirable properties while minimizing potential drawbacks:
 - For the sharing process, only a minor modification to the way the last secret sharing coefficients are derived is needed.
 - The recovery process is unchanged compared to classical SSS and independent of the verification process of the included checksum.
 - The size of the generated shares does not increase and is equal to the size of the secret to be shared. 
 - A low false negative rate of $2^{-64}$, where a invalid recovered secret can pass the verification process unnoticed.

A theoretical drawback is the lost of information theoretical security as the value of $c_{t - 1}$  includes 
a $64$ bit checksum, derived cryptographically from 
(i) the secret to shared and 
(ii) at least 64 additional bits of entropy. 


### Compatibility and Separation of Concerns

The specification is intentionally designed such that it can be used with different mnemonic schemes and different key 
derivation schemes building on top of the shared cryptographic key material. 
This approach follows the separation of concerns principle as 
*generation*, *derivation*, *mnemonic encoding/decoding* and *secret sharing* of cryptographic key material are separate 
tasks and can thus be defined and implemented separately (see Section [Scope](#Scope) for more details).
As long as the intermediate formats are well defined this loose coupling allows for easier replacement and updates of 
individual components in software stacks and tool chains. 
The document at hand specifies a method for secret sharing of cryptographic key material. 


### Sharing the same secret multiple times

The specified secret sharing scheme in this document MAY safely be invoked multiple times with the same secret as 
input. The resulting shares for each invocation are different and independent from the shares of the other invocations
(for the special of case $t = 1$ all generated shares are equal to the secret being shared).
Shares from different secret sharing instances cannot 
(and are by design not supposed to) 
be combined to recover a secret shared this way.

Even in the worst case, i.e., the shortest possible secret ($16$ bytes) 
with the recovery threshold of $t = 2$,
the probability of picking the same secret sharing polynomial 
(in this case only defined by the secret and $64$ random bits) is low for reasonable numbers of invocations.
The probability can be computed via the formula of the 
[birthday problem](https://en.wikipedia.org/wiki/Birthday_problem) given below, 
using $q$ to denote the number of secret sharing invocations:
$$
    1 - \frac{q! \cdot \binom{2^{64}}{q}}{\left(2^{64}\right)^q}.
$$
For $q = 100$ for example, this results in a probability of $\approx 2.68 \cdot 10^{-16}$.


### Multi layer/ Recursive use

The specification implicitly covers the use case of sharing the same secret 
among different (independent) groups of stakeholders
and/or further sharing shares of a shared secret. 

We consider this as an advanced use case, and in contrast to, e.g., 
the [SLIP39](https://github.com/satoshilabs/slips/blob/master/slip-0039.md) proposal, 
deliberately do not complicate this specification by introducing additionally a notation for groups to explicitly 
capture such use cases.
Yet, our specification transparently allows to re-share the shares for a given secret in a natural way: 
It is simply accomplished by feeding a share, which should be further split up, as secret into the secret sharing 
procedure.
While special care must be taken to ensure that the way secrets are shared and may later be recombined is noted, 
our approach in principle allows for an arbitrary number of nested secret sharing layers.


### The use of $\mathbf{GF(2^8)}$
This design performs all secret sharing and recovery computations in the finite field $\text{GF}(2^8)$. 
The allows the specified algorithms to process the data on a byte-per-byte level and simplified implementation in 
programming languages or on hardware platform with no immediate support for arbitrary precision integer arithmetics.
Using this approach, share indices are restricted to integers from $1$ to $255$.
Thus the maximum number of shares is limited to $255$.
However in practice, we only see this as minor limitation for the indented use case of sharing mnemonic phrases, 
where human interaction is involved.

## Test vectors

The files `test_vectors.json` and `test_vectors.py` in this directory contain a list of secret sharing computation 
performed with the reference implementation.
An example test vector is given below:
```json
{
    "s": "243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89",
    "n": 5,
    "t": 3,
    "c": [
        "243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89",
        "b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef",
        "324e7738926cfbe5f4bf8d8d8c31d763da06c80abb1185eb676dea5f8d95cb78"
    ],
    "shares": [
        [1, "a1904cd29d22d95c58d75f2313b557e01ce8e627aa3a6e6dc8c7c9c3304b681e"],
        [2, "99c50facf4c99dbe8b3138372647ff4625c4191483a8bcfdda92d6f74c17e8b7"],
        [3, "1c6a29f6ec484c31c0ffed3a3682dbe29d25c711000de3401a7be5ac9012ec20"],
        [4, "c31a04b678a089b200c3f9105db04d1f38d854be8c72fca18882910fbbab79d9"],
        [5, "46b522ec6021583d4b0d2c1d4d7569bb80398abb0fd7a31c486ba25467ae7d4e"]
    ]
},
```
The test vectors include example secret sharing for all values of $1 \leq t \leq n \leq 5$.
As the secret sharing process is inherently randomized, the values of the coefficients used for the secret sharing 
process are given in the test vectors.
This allows other implementation to check if the secret sharing leds to the expected shares for the given coefficients.
The last 8 bytes of the coefficients in the test vectors are computed according to this specification and can be used
to check the correctness of the checksum computation.
Implementations MUST NOT use the provided values for purposes other than testing the correctness of the implementation.

## Implementations

All implementation MUST support the following functionality as specified later in this document:
1. [Sharing](#Sharing)
2. [Recovery](#Recovery)
   1. [Checksum Verification](#ChecksumVerification)

Implementations MAY support additionally support functionality to aid the recovery process 
in the following circumstances given as non-exhaustive list below:
  1. Recovery from a set $v \leq t$ valid shares, even if the underlying secret sharing threshold $t$ is unknown.
  2. Recovery from a set shares, given that at least $t$ valid shares are provided.
  3. Recovery in case, share indices are missing or invalid.
  4. Combinations of the above issues.

Depending on the number of shares $n$ and the secret sharing threshold $t$ used, in particular for small values, 
recovery under these (and other) circumstances is possible with high probability due to the included checksum.

Feel free to contact us if you have also implemented the specification and want your implementation to be listed on this
 page.

#### Reference implementation
The [reference implementation](https://github.com/de-centralized-systems/sssmp/blob/main/sssmp) can be found in the Github repository of the specification.

#### BIP39 Toolkit
An implementation which uses SSSMP as a component is the 
[BIP39 Toolkit](https://github.com/de-centralized-systems/bip39toolkit).
The BIP39 toolkit was developed alongside this specification and provides a standalone Python implementation with a 
CLI-based interface using BIP39 as input and output format. 
Moreover it supports the generation of cryptographic keys from scratch.


## References  

 - [BIP39 Toolkit](https://github.com/de-centralized-systems/bip39toolkit), 
   our reference implementation for this specification using BIP39 as encoding
 - [Shamir's Original Paper "How to share a Secret"](https://dl.acm.org/doi/pdf/10.1145/359168.359176)
 - [Wikipedia Page on Finite Field Arithmetics](https://en.wikipedia.org/wiki/Finite_field_arithmetic)
 - [BIP39 Specification "Mnemonic code for generating deterministic keys"](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
 - [Bytewords Specification "Encoding binary data as English words"](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-012-bytewords.md)
 - [SLIP39 specification](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)
 - [BC-SSKR](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-011-sskr.md)
 - [Shamir39](https://iancoleman.io/shamir39/)

## Version History

**2021-05-06**
 - Initial draft published on Github.


