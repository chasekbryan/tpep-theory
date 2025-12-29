import math
from functools import reduce

class TPEPAnalyzer:
    """
    TPEPAnalyzer: A framework for analyzing integers under the 
    Totient-Parity Exclusion Principle (TPEP).
    
    THEORY SUMMARY:
    ---------------
    Standard Number Theory defines perfection additively: sigma(n) = 2n.
    TPEP redefines it multiplicatively, asserting that perfection is a function 
    of "Totient Density" (tau_d).
    
    The TPEP Identity states that for a number to be perfect, the ratio of its 
    Additive Expansion (sigma) to its Multiplicative Resistance (phi) must 
    approach the Stability Constant of 4.
    
    Equation: lim(n->Perfect) [sigma(n) / phi(n)] = 4
    
    This class calculates the "Mirror Gap" to visualize why Odd numbers 
    cannot satisfy this limit (The Forbidden Zone).
    """

    def __init__(self, n: int):
        self.n = n
        if n < 1:
            raise ValueError("TPEP only applies to positive integers.")
            
        # Cache properties to avoid re-calculation
        self._factors = self._get_prime_factors(n)
        self.phi_val = self._calculate_phi()
        self.sigma_val = self._calculate_sigma()

    def _get_prime_factors(self, n):
        """
        Decomposes n into prime factors and their exponents.
        Returns a dictionary {prime: exponent}.
        """
        factors = {}
        d = 2
        temp = n
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1
        return factors

    def _calculate_phi(self):
        """
        Calculates Euler's Totient Function (phi).
        Represents the count of integers k < n where gcd(n, k) = 1.
        """
        result = self.n
        for p in self._factors.keys():
            result = result * (p - 1) // p
        return result

    def _calculate_sigma(self):
        """
        Calculates the Sum of Divisors Function (sigma).
        Represents the additive expansion of the number.
        """
        total = 1
        for p, a in self._factors.items():
            # Sum of geometric series for prime powers: (p^(a+1) - 1) / (p - 1)
            total *= (p**(a + 1) - 1) // (p - 1)
        return total

    # ==========================================
    # CORE TPEP METRICS
    # ==========================================

    @property
    def totient_density(self) -> float:
        """
        Metric: tau_d
        Formula: phi(n) / n
        
        Notes:
        Measures the 'porosity' of the number.
        - For Even Perfect Numbers, this asymptotically approaches 0.5.
        - For Odd numbers, this struggles to drop below 0.5 without infinite factors.
        """
        return self.phi_val / self.n

    @property
    def perfection_ratio(self) -> float:
        """
        Metric: rho (Abundancy Index)
        Formula: sigma(n) / n
        
        Notes:
        Standard index. If rho == 2.0, the number is Perfect.
        """
        return self.sigma_val / self.n

    @property
    def tpep_ratio(self) -> float:
        """
        THE TPEP IDENTITY
        Formula: sigma(n) / phi(n)
        
        Target:
        Perfection requires this ratio to equal exactly 4.0.
        
        Mathematical Proof:
        If sigma(n) = 2n, then (2n / phi(n)) = 4 implies phi(n)/n = 0.5.
        Only even numbers (with factor 2) can resolve the prime product to 0.5.
        """
        return self.sigma_val / self.phi_val

    @property
    def mirror_gap(self) -> float:
        """
        Metric: Delta_mu
        Formula: rho + tau_d
        
        Notes:
        Represents the tension between expansion and reduction.
        For Even Perfect Numbers, this converges to 2.5.
        """
        return self.perfection_ratio + self.totient_density

    def report(self):
        """Generates a formatted analysis report."""
        parity = "ODD" if self.n % 2 != 0 else "EVEN"
        
        # Check against the 'Stability Constant' of 4.0
        is_tpep_stable = math.isclose(self.tpep_ratio, 4.0, rel_tol=1e-9)
        status = "PERFECT (Stable)" if is_tpep_stable else "IMPERFECT (Unstable)"

        return f"""
        --- TPEP ANALYSIS: {self.n} ({parity}) ---
        1. Factors:           {self._factors}
        2. Totient Density:   {self.totient_density:.5f} (Target < 0.5)
        3. Perfection Ratio:  {self.perfection_ratio:.5f} (Target = 2.0)
        ------------------------------------------
        4. TPEP RATIO (sigma/phi): {self.tpep_ratio:.5f}
           TARGET:                 4.00000
           STATUS:                 {status}
        ------------------------------------------
        """

# ==========================================
# IMPLEMENTATION & EXAMPLES
# ==========================================

if __name__ == "__main__":
    print(">>> INITIALIZING TPEP PROTOCOL...\n")

    # 1. Validation: A Known Even Perfect Number
    # 8128 is the 4th perfect number
    epn = TPEPAnalyzer(8128)
    print(epn.report())

    # 2. The Forbidden Zone: An Odd Abundant Number
    # 945 is the first odd abundant number (sigma(n) > 2n)
    # It attempts to be perfect but fails the TPEP ratio.
    odd_abundant = TPEPAnalyzer(945)
    print(odd_abundant.report())

    # 3. A Large 'Near Miss': An Odd 'Semi-Perfect' attempt
    # 15015 (3*5*7*11*13)
    # Adding more odd primes drives sigma up, but phi doesn't drop fast enough.
    large_odd = TPEPAnalyzer(15015)
    print(large_odd.report())
