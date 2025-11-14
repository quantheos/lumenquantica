
# Lumen Quantica I – Full Extended Documentation  
**Enerji–Bilgi–Anlam (E–I–A) Teorisi | C-Operatörü | s-bit Protokolü | F1–F5 Deneyleri**  
**Energy–Information–Meaning Theory | C-Operator | s-bit Protocol | F1–F5 Experiments**

---

## 🌌 About Lumen Quantica I  
Lumen Quantica I is a hybrid scientific–philosophical framework exploring the transformation between  
**Energy (E), Information (I) and Meaning (A)** through a unified conservation law.

It introduces:

- A new conservation principle  
- The C-Operator (Meaning Efficiency)  
- The Semantic Bit (s-bit)  
- The Ωₜ Cosmic Resonance Field  
- F1–F5 Experimental Framework  
- Mathematical, ontological and computational models  

---

# 🇹🇷 Türkçe Açıklama

## 📌 Projenin Amacı  
Bu depo, **Lumen Quantica I** çalışmasının resmi kaynak kodlarını, teorik belgelerini, matematiksel modellerini ve F1–F5 deney protokollerini içerir.

### 🔷 Temel Korunum Yasası  
\[
\Delta\left(\frac{E}{E_0}+\frac{I}{I_0}+\lambda A\right)=0
\]

### 🔷 Anlam Verimi Operatörü  
\[
C = \frac{\Delta A}{\Delta I}
\]

---

# 🇬🇧 English Description

## 📌 Project Purpose  
This repository contains all theoretical, mathematical and computational components of **Lumen Quantica I**, including experimental protocols and source code.

### 🔷 Core Conservation Law  
\[
\Delta\left(\frac{E}{E_0}+\frac{I}{I_0}+\lambda A\right)=0
\]

### 🔷 Meaning Efficiency Operator  
\[
C = \frac{\Delta A}{\Delta I}
\]

---

# 📂 Repository Structure

```
docs/           — Documentation & theoretical manuscripts
src/            — Core Python code: C-operator, s-bit, EIA model, resonance
experiments/    — F1–F5 experiment scripts
data/           — Example datasets (EEG, entropy, meaning-flow)
diagrams/       — Equations, concept art, resonance diagrams
```

---

# 🧠 Theoretical Components

## 1. E–I–A Conservation Model  
Defines a system where energy, information and meaning transform without net loss.

## 2. C-Operator  
Measures semantic efficiency:  
- How much meaning emerges from incoming information  
- Time series support  
- Robust metric for cognitive/AI systems  

## 3. s-bit (Semantic Bit)  
Defines the smallest measurable semantic transformation unit.

## 4. Ωₜ Resonance Field  
Temporal–cosmic resonance arising from entropy and meaning flows.

---

# 🧪 Experiments (F1–F5)

- **F1:** AI entropy behavior  
- **F2:** EEG → semantic density  
- **F3:** Probability-field shift  
- **F4:** Meaning amplification  
- **F5:** Global Ωₜ field response  

---

# 🧩 Full Source Code

## 📘 c_operator.py
```python
import numpy as np

class COperator:
    @staticmethod
    def compute(delta_A: float, delta_I: float, eps: float = 1e-9) -> float:
        if abs(delta_I) < eps:
            return 0.0
        return delta_A / delta_I

    @staticmethod
    def time_series(A_series, I_series):
        A_series = np.array(A_series)
        I_series = np.array(I_series)
        dA = np.diff(A_series)
        dI = np.diff(I_series)
        with np.errstate(divide='ignore', invalid='ignore'):
            C_values = np.where(dI != 0, dA / dI, 0)
        return C_values
```

## 📘 sbit.py
```python
import numpy as np

class SBit:
    def __init__(self, threshold: float = 0.015):
        self.threshold = threshold

    def measure(self, meaning_signal):
        arr = np.array(meaning_signal)
        diffs = np.abs(np.diff(arr))
        sbits = np.sum(diffs > self.threshold)
        return sbits

    def semantic_density(self, meaning_signal):
        arr = np.array(meaning_signal)
        return float(np.std(arr) / (np.mean(arr) + 1e-9))
```

## 📘 eia_model.py
```python
import numpy as np

class EIAModel:
    def __init__(self, E0=1.0, I0=1.0, lam=1.0):
        self.E0 = E0
        self.I0 = I0
        self.lam = lam

    def conservation(self, E, I, A):
        E = np.array(E)
        I = np.array(I)
        A = np.array(A)
        val = (E / self.E0) + (I / self.I0) + (self.lam * A)
        return np.diff(val)
```

## 📘 resonance.py
```python
import numpy as np

class ResonanceField:
    def __init__(self, alpha=0.8, beta=0.2):
        self.alpha = alpha
        self.beta = beta

    def omega(self, entropy_flow, meaning_flow):
        entropy_flow = np.array(entropy_flow)
        meaning_flow = np.array(meaning_flow)
        dS = -np.diff(entropy_flow)
        dA = np.diff(meaning_flow)
        return self.alpha * dS + self.beta * dA
```

---

# 🧪 Experiments

## F1 — AI Entropy
```python
import numpy as np

def ai_entropy_test(pred_probs):
    pred_probs = np.array(pred_probs)
    entropy = -np.sum(pred_probs * np.log(pred_probs + 1e-9))
    return float(entropy)
```

## F2 — EEG Semantic Density
```python
import numpy as np

def eeg_semantic_map(signal):
    fft = np.abs(np.fft.rfft(signal))
    meaning_density = np.std(fft) / (np.mean(fft) + 1e-9)
    return float(meaning_density)
```

## F3 — Probability Shift
```python
import numpy as np

def probability_shift(before, after):
    before = np.array(before)
    after = np.array(after)
    return float(np.sum(np.abs(after - before)))
```

## F4 — Meaning Amplification
```python
def meaning_amplification_rate(A_in, A_out):
    return (A_out - A_in) / (A_in + 1e-9)
```

## F5 — Global Ωₜ Field Response
```python
import numpy as np

def global_field_response(local_fields):
    return float(np.mean(np.array(local_fields)))
```

---

# 🔧 Installation

```bash
git clone https://github.com/quantheos/lumenquantica
cd lumenquantica

pip install torch numpy scipy matplotlib plotly jupyter
```

---

# 📚 License  
MIT License

---

© 2025 Quantheos — Lumen Quantica Framework
