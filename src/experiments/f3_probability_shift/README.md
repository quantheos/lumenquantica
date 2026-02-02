# F3 — Meaning–Entropy Tradeoff  
## Probability Shift Observation

---

## 🇹🇷 Türkçe Açıklama

Bu deney, kitapta tanımlanan **F3 — Anlam–Entropi Takası** önermesinin
**olasılık-düzeyindeki izdüşümünü** incelemeyi amaçlar.

Kuramsal önerme şu şekilde ifade edilir:

ΔS_çevre ≈ λ · ΔA₀

Bu ilişki, bir sistemde üretilen anlam miktarının (ΔA₀),
çevreye aktarılan entropiyle (ısı, düzensizlik) dengelendiğini öne sürer.

Bu deney:
- çevresel entropiyi (ısı atımı) **doğrudan ölçmez**
- termodinamik bir ölçüm iddiası taşımaz  

Bunun yerine, öğrenen bir sistemde
olasılık dağılımlarının **yer değiştirme miktarını**
ölçerek anlamsal yeniden yapılanmanın
**bilgi-teorik bir göstergesini** sunar.

İki durum arasındaki olasılık farklarının mutlak toplamı:

- sistemin iç temsillerinde gerçekleşen **yeniden düzenlemeyi**
- karar uzayındaki **topolojik kaymayı**

nicel olarak ifade eder.

Bu nicelik:
- entropinin fiziksel tanımıyla özdeş değildir  
- ancak anlam kazanımı sırasında
  **düzenin bir yerden başka bir yere taşındığını**
  gösteren ölçülebilir bir iz bırakır.

Bu bağlamda F3, şu hipotezi sınar:

> Anlam üretimi, olasılık uzayında
> ölçülebilir bir kaymaya karşılık gelir;
> bu kayma, daha üst katmanlarda
> çevresel entropi artışıyla dengelenir.

Dolayısıyla bu deney, F2’de gözlenen
anlamsal yoğunlaşmanın,
**olasılık alanındaki bedelini**
izleyen ara bir deney katmanıdır.

---

## 🇬🇧 English Description

This experiment investigates the **probability-level projection**
of **F3 — Meaning–Entropy Tradeoff** as defined in the book.

The theoretical proposition is expressed as:

ΔS_environment ≈ λ · ΔA₀

This relation suggests that the amount of meaning produced (ΔA₀)
is balanced by an increase in environmental entropy
(e.g., heat dissipation or disorder).

This experiment:
- does **not** directly measure environmental entropy  
- does **not** claim thermodynamic validation  

Instead, it quantifies the **shift between probability distributions**
in a learning system, providing an
information-theoretic proxy for
semantic reconfiguration.

The sum of absolute differences between
two probability states reflects:

- internal representational restructuring  
- topological displacement in decision space  

This quantity:
- is not equivalent to physical entropy  
- but captures the **measurable footprint**
  of meaning emergence within probability space.

In this context, F3 tests the following hypothesis:

> Meaning production corresponds to
> a measurable shift in probability space;
> this shift is balanced, at higher layers,
> by an increase in environmental entropy.

Thus, F3 functions as an intermediate experiment,
tracking the **probability cost**
of semantic consolidation observed in F2.

---

## 📄 Source Code

```python
import numpy as np

def probability_shift(before, after):
    before = np.array(before)
    after = np.array(after)
    return float(np.sum(np.abs(after - before)))
