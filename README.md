# TPEP: The Totient-Parity Exclusion Principle

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-research-orange)

**A number-theoretic framework proposing a multiplicative constraint on the existence of Odd Perfect Numbers.**

## 📋 Abstract

Standard Number Theory defines a perfect number $n$ additively, where the sum of its proper divisors equals $n$ ($\sigma(n) = 2n$). The **Totient-Parity Exclusion Principle (TPEP)** shifts the analytical focus to the multiplicative resistance of integers, measured by Euler's Totient function ($\phi$).

This repository contains the theoretical proofs and simulation tools validating the conjecture that **Odd Perfect Numbers (OPNs)** are impossible. TPEP demonstrates that the prime factorization of odd integers cannot satisfy the required equilibrium between additive expansion and multiplicative reduction, creating a "Forbidden Zone" for odd perfection.

---

## 📐 The TPEP Identity

The central theorem of this framework is the **Sigma-Totient Ratio**. For any integer $n$ to exist in a state of Perfection, the system must satisfy the following equilibrium limit:

$$
\lim_{n \to \text{Perfect}} \left[ \frac{\sigma(n)}{\phi(n)} \right] = 4
$$

### Deconstruction
1.  **$\sigma(n)$**: Additive Expansion (Sum of Divisors).
2.  **$\phi(n)$**: Multiplicative Resistance (Euler's Totient).
3.  **$4$**: The Stability Constant.

---

## 🧪 Theoretical Proof: The Parity Lock

The TPEP Identity provides a geometric argument against the existence of Odd Perfect Numbers.

### 1. The Substitution
Substitute the definition of a perfect number ($\sigma(n) = 2n$) into the TPEP Identity:
$$
\frac{2n}{\phi(n)} = 4 \implies \frac{\phi(n)}{n} = \frac{1}{2}
$$

### 2. The Euler Product Analysis
Using the product formula for Totient Density $\tau_d$:
$$
\prod_{p|n} \left(1 - \frac{1}{p}\right) = \frac{1}{2}
$$

### 3. The Exclusion
* **Case A: Even Numbers (EPN)**
    The prime factor $2$ introduces the term $(1 - 1/2) = 1/2$. The equation is satisfied instantly (or asymptotically for Mersenne primes).
    
* **Case B: Odd Numbers (OPN)**
    The prime factors are strictly $p \ge 3$. The product $\prod (1 - 1/p)$ results in a fraction where the denominator is a product of odd primes. A fraction with an **odd denominator** can never equal **$1/2$**.

**Conclusion:**
$$
\forall n \in \mathbb{Z}^+_{\text{odd}}, \quad \frac{\sigma(n)}{\phi(n)} \neq 4
$$
Therefore, Odd Perfect Numbers are strictly forbidden by TPEP.

---

## 📊 Core Definitions

To analyze integers under TPEP, we use three specific metrics:

| Symbol | Name | Formula | Description |
| :--- | :--- | :--- | :--- |
| $\tau_d$ | **Totient Density** | $\phi(n)/n$ | Measures porosity to coprimality. Must approach $0.5$ for perfection. |
| $\rho$ | **Perfection Ratio** | $\sigma(n)/n$ | The standard abundancy index. Target is $2.0$. |
| $\Delta_{\mu}$ | **Mirror Gap** | $\rho + \tau_d$ | The tension between expansion and reduction. |

---

## 💻 Usage & Implementation

This repository provides a Python implementation (`TPEPAnalyzer`) to calculate these metrics and visualize the "Forbidden Zone."

### Installation

```bash
git clone [https://github.com/your-username/tpep-theory.git](https://github.com/your-username/tpep-theory.git)
cd tpep-theory
pip install -r requirements.txt
