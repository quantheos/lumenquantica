# F1 — AI Entropy Test  
## Anlam–Akı Gücü Sınırı için Bilgi-Teorik Ön Deney

---

## 🇹🇷 Türkçe Açıklama

Bu deney, kitapta tanımlanan **F1 — Anlam–Akı Gücü Sınırı (Landauer bağlantısı)** önermesinin  
**bilgi-teorik bileşenini** izole etmeyi amaçlar.

Deney, bir yapay zekâ modelinin çıktı olasılık dağılımlarındaki **Shannon entropisini** ölçerek,
anlam üretiminden **önceki düzenlenme sürecini** nicel olarak gözlemler.

Burada hesaplanan entropi:

- Doğrudan **enerji tüketimini (ΔE)** ölçmez  
- **Semantik bit (s-bit)** üretimini doğrudan temsil etmez  

Ancak şu kritik niceliği sağlar:

> **ΔI — Bilginin düzenlenme miktarı**

Bu değer, kitapta tanımlanan anlam verimi operatöründe:

C = ΔA / ΔI

ifadesinin **paydasını** deneysel olarak kalibre etmek için kullanılır.

Dolayısıyla bu deney:
- F1 önermesini **ispat etmez**
- Ancak F1’in **ölçülebilir ilk izdüşümünü** sağlar

Enerji–anlam oranı (ΔE / ΔA), bu deneyden elde edilen sonuçların
EEG, nöromorfik çipler veya biyolojik sistemler gibi
üst-katman deneylerde birleştirilmesiyle hesaplanabilir.

Bu bağlamda F1, tekil bir deney değil,
**çok-katmanlı bir deney zincirinin başlangıç noktasıdır**.

---

## 🇬🇧 English Description

This experiment isolates the **information-theoretic component** of  
**F1 — Meaning–Flux Power Limit (Landauer connection)** as defined in the book.

By measuring the **Shannon entropy** of output probability distributions
produced by an artificial intelligence model, the experiment quantifies
the **pre-semantic ordering phase** preceding meaning formation.

The entropy computed here:

- Does **not** directly measure energy consumption (ΔE)  
- Does **not** directly represent semantic bit (s-bit) generation  

Instead, it provides a measurable proxy for:

> **ΔI — Information structuring**

This quantity corresponds to the denominator of the meaning efficiency operator:

C = ΔA / ΔI

as introduced in the theoretical framework.

Therefore, this experiment:
- Does **not** prove the F1 proposition  
- But establishes its **first measurable projection**

Energy-to-meaning ratios (ΔE / ΔA) are intended to be derived by
integrating these results with higher-layer experiments
such as EEG measurements, neuromorphic hardware, or biological systems.

In this sense, F1 is not a standalone experiment,
but the **initial node of a multi-layer experimental chain**.

---

## 📄 Source Code

```python
import numpy as np

def ai_entropy_test(pred_probs):
    pred_probs = np.array(pred_probs)
    entropy = -np.sum(pred_probs * np.log(pred_probs + 1e-9))
    return float(entropy)
