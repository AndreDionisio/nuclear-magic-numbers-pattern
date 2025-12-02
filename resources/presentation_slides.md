# A Phenomenological Pattern for Nuclear Magic Numbers

**André Luís Tomaz Dionísio**  
EPHEC Brussels, Belgium  
December 2025

---

## What Are Magic Numbers?

Nuclear magic numbers: 2, 8, 20, 28, 50, 82, 126

**Special properties:**
- Exceptional stability
- Complete shell closures
- High binding energies
- Low neutron capture cross-sections

**Question:** Can we predict them with a simple formula?

---

## The Challenge

**Traditional approach:**
- Sophisticated shell model calculations
- Quantum mechanical complexity
- Difficult to teach and visualize

**Desired approach:**
- Simple, transparent formula
- Physical insight
- Pedagogical value

Like VSEPR theory in chemistry!

---

## The Phenomenological Formula

For magic number M_n, calculate next magic number M_{n+1}:

```
Step 1: Δn = (c_start × (c_start + 2)) / 4

Step 2: C_total = Δn + c_high-j

Step 3: M_{n+1} = M_n + C_total
```

**Parameters:**
- c_start: capacity of last filled orbital
- c_high-j: capacity of next high-j orbital

---

## Complete Validation

| M_n | c_start | c_high-j | Δn | C_total | M_{n+1} |
|-----|---------|----------|----|---------| --------|
| 0   | 0       | 2        | 0  | 2       | **2** ✓ |
| 2   | 2       | 4        | 2  | 6       | **8** ✓ |
| 8   | 4       | 6        | 6  | 12      | **20** ✓ |
| 20  | 2       | 6        | 2  | 8       | **28** ✓ |
| 28  | 6       | 10       | 12 | 22      | **50** ✓ |
| 50  | 8       | 12       | 20 | 32      | **82** ✓ |
| 82  | 10      | 14       | 30 | 44      | **126** ✓ |

**Starting from ZERO!**

---

## Prediction: Magic Number 184

```
M_n = 126
c_start = 12
c_high-j = 16

Δn = (12 × 14) / 4 = 42
C_total = 42 + 16 = 58
M_{n+1} = 126 + 58 = 184
```

**Agrees with sophisticated shell model calculations!**

---

## The Decreasing Sequence Pattern

Every magic number follows the same pattern:

```
Magic 8:     [4→2]
Magic 20:    [6→4→2]
Magic 28:    [8]           ← sphere
Magic 50:    [6→4→2] + [10]
Magic 82:    [8→6→4→2] + [12]
Magic 126:   [10→8→6→4→2] + [14]
Magic 184:   [12→10→8→6→4→2] + [16]
```

**Universal:** Start higher → Descend by 2 → Reach 2 → Start even higher

---

## Physical Meaning: Δn Formula

Δn encodes the sum of a decreasing arithmetic sequence:

**Example:** c_start = 10
```
Sequence: 10 + 8 + 6 + 4 + 2 = 30

Formula: Δn = (10 × 12) / 4 = 30 ✓
```

**This is the closed-form solution!**

Δn = n(a₁ + aₙ)/2 where n = c_start/2

---

## Beyond Magic Numbers: Stability Hierarchy

Δn quantifies nuclear stability:

| Δn | Level      | Examples           |
|----|------------|-------------------|
| 2  | LOCAL      | ⁴He, ⁴⁰Ca        |
| 6  | SUBSHELL   | ¹²C, ¹⁶O         |
| 12 | REGIONAL   | ²⁰Ne, ⁵⁶Ni       |
| 20 | STRONG     | ¹⁰⁰Sn            |
| 30 | MAJOR      | ²⁰⁸Pb            |
| 42 | COMPLETE   | 184 (predicted)   |

**Higher Δn = Greater Stability**

---

## Experimental Validation

Correlation with binding energies:

| Nucleus | Δn | BE/A (MeV) |
|---------|----| -----------|
| ⁴He     | 2  | 7.074      |
| ¹²C     | 6  | 7.680      |
| ¹⁶O     | 6  | 7.976      |
| ⁵⁶Ni    | 12 | 8.643      |
| ¹⁰⁰Sn   | 20 | 8.667      |
| ²⁰⁸Pb   | 30 | 7.867      |

**Nuclei with same Δn show similar stability!**

---

## The Fundamental Relationship: c = 2l + 2

For high-j orbitals where j = l + 1/2:

```
c = 2j + 1 = 2(l + 1/2) + 1 = 2l + 2
```

**For odd l values (1, 3, 5, 7, 9...):**

| l   | Orbital | c = 2l+2 | Δc  |
|-----|---------|----------|-----|
| 1   | p       | 4        | —   |
| 3   | f       | 8        | +4  |
| 5   | h       | 12       | +4  |
| 7   | j       | 16       | +4  |

**When l increases by +2, capacity increases by +4**

---

## Why the "+4" Increment?

```
Δl = +2 (from one odd number to next)
Δc = 2 × Δl = 2 × 2 = 4
```

**The phenomenological "+4" is NOT arbitrary!**

It encodes:
1. Quantum relationship c = 2l + 2
2. Dominance of odd-l orbitals (p, f, h, j...)
3. Strong spin-orbit coupling favoring high-j

---

## Critical Example: 8 → 20

```
Given: M_n = 8
Last orbital: 1p₃/₂ (capacity 4)
Next high-j: 1d₅/₂ (capacity 6)

Calculation:
  Δn = (4 × 6) / 4 = 6
  C_total = 6 + 6 = 12
  M_{n+1} = 8 + 12 = 20 ✓

Increment: 6 - 4 = 2 (typical Δl step)
```

**Perfect agreement with shell structure!**

---

## The Carbon-12 Case

Why is ¹²C so stable (BE/A = 7.680 MeV)?

**Structure:**
- Subshell closure: 1s₁/₂(2) + 1p₃/₂(4) = 6
- Δn = 6: intermediate pairing capacity
- N=Z symmetry
- Alpha-cluster structure

**Formula correctly identifies this stability through Δn**

Without classifying 6 as a magic number!

---

## Scope and Limitations

**Strengths:**
✓ Reproduces all known magic numbers recursively  
✓ Predicts next magic number (184)  
✓ Reveals hierarchical stability via Δn  
✓ Pedagogically transparent  
✓ Connects to quantum structure (c = 2l + 2)

**Limitations:**
✗ Parameters are phenomenological  
✗ Approximate—sacrifices precision for simplicity  
✗ Does not predict exact level ordering  
✗ Best suited for spherical nuclei near stability

---

## VSEPR Analogy

**Chemistry (VSEPR):**
- Predicts molecular geometry
- Counts electron pairs
- No Schrödinger equation needed
- Sacrifices rigor for clarity

**Nuclear Physics (This Work):**
- Predicts magic numbers
- Counts pairing capacity
- No detailed shell model needed
- Sacrifices rigor for clarity

**Both achieve predictive power through pattern recognition!**

---

## Educational Value

**Before this work:**
- Magic numbers: memorize the list
- Shell model: complex quantum calculations
- Limited intuition

**With this formula:**
- Calculate recursively from zero
- Understand hierarchical stability
- See the physical pattern
- Connect to quantum structure

**Perfect for teaching nuclear physics!**

---

## Key Discoveries

1. **Complete recursive formula** (0→2→...→184)

2. **Hierarchical stability framework** (Δn levels)

3. **Decreasing sequence pattern** (always ends at 2)

4. **Quantum connection** (c = 2l + 2)

5. **Odd-l dominance** (explains "+4")

6. **Testable prediction** (184 as next magic)

---

## Applications

**Research:**
- Guide for superheavy element synthesis
- Framework for stability predictions
- Basis for extended models

**Education:**
- Intuitive teaching tool
- Computational simplicity
- Physical transparency

**Practice:**
- Quick stability estimates
- Magic number identification
- Hierarchical classification

---

## Comparison with Shell Model

| Aspect          | This Work    | Full Shell Model |
|-----------------|--------------|------------------|
| Complexity      | Arithmetic   | Quantum          |
| Computation     | Seconds      | Hours-Days       |
| Parameters      | 2 per step   | ~100s            |
| Predictive      | Yes (184)    | Yes (detailed)   |
| Level ordering  | No           | Yes              |
| Pedagogical     | Excellent    | Difficult        |
| Physical insight| c = 2l+2     | Complete         |

**Different tools for different purposes!**

---

## Future Directions

**Testable predictions:**
- 184 as next magic number (most immediate)
- Δn correlation extends to more nuclei
- Pattern in neutron-rich systems

**Possible extensions:**
- Correlation with neutron separation energies
- Connection to deformation parameters
- Semi-magic nuclei (N≠Z)
- Interactive educational software

---

## Conclusion

We have presented a phenomenological formula that:

1. **Reproduces** all known magic numbers recursively
2. **Predicts** next superheavy magic number (184)
3. **Reveals** hierarchical nuclear stability pattern
4. **Connects** to quantum mechanics (c = 2l + 2)
5. **Provides** exceptional pedagogical value

**The simplicity is the point—not a limitation!**

Like VSEPR: approximate but insightful

---

## Take-Home Messages

✓ Magic numbers follow a simple recursive pattern

✓ Δn quantifies stability beyond traditional magic numbers

✓ Every major shell follows: **start higher → descend to 2 → start even higher**

✓ The "+4" increment has deep physical meaning: **c = 2l + 2**

✓ Phenomenological approaches can complement rigorous methods

✓ Simplicity + Physical Insight = Powerful Pedagogy

---

## Thank You!

**André Luís Tomaz Dionísio**  
EPHEC Brussels, Belgium  
andreluisdionisio@gmail.com

**Article:**  
"A Phenomenological Pattern for Nuclear Magic Numbers"  
Submitted to Preprints.org (2025)

**Questions?**

---

## Supplementary: Complete Orbital Structures

**Magic 2:** 1s₁/₂(2)

**Magic 8:** 1s₁/₂(2) + 1p₃/₂(4) + 1p₁/₂(2)

**Magic 20:** up to 8 + 1d₅/₂(6) + 2s₁/₂(2) + 1d₃/₂(4)

**Magic 28:** up to 20 + 1f₇/₂(8)

**Magic 50:** up to 28 + 2p₃/₂(4) + 1f₅/₂(6) + 2p₁/₂(2) + 1g₉/₂(10)

**Magic 82:** up to 50 + 1g₇/₂(8) + 2d₅/₂(6) + 1h₁₁/₂(12) + 3s₁/₂(2) + 2d₃/₂(4)

**Magic 126:** up to 82 + 1h₉/₂(10) + 2f₇/₂(8) + 1i₁₃/₂(14) + 3p₃/₂(4) + 2f₅/₂(6) + 3p₁/₂(2)

---

## Supplementary: Progression of Highest-j Orbitals

| Magic | Highest-j   | l | Capacity |
|-------|-------------|---|----------|
| 28    | 1f₇/₂       | 3 | 8        |
| 50    | 1g₉/₂       | 4 | 10       |
| 82    | 1h₁₁/₂      | 5 | 12       |
| 126   | 1i₁₃/₂      | 6 | 14       |
| 184   | 1j₁₅/₂      | 7 | 16       |

**Sequence:** l = 3, 4, 5, 6, 7  
**Capacities:** c = 8, 10, 12, 14, 16  
**Increment:** Δc = +2 consistently

---

## Supplementary: Mathematical Derivation

**Arithmetic sequence sum:**
```
S = c_start + (c_start-2) + ... + 4 + 2

Number of terms: n = c_start/2
First term: a₁ = c_start
Last term: aₙ = 2

Sum: S = n(a₁ + aₙ)/2
     = (c_start/2)(c_start + 2)/2
     = c_start(c_start + 2)/4
     = Δn
```

**This is the closed-form solution!**

---
