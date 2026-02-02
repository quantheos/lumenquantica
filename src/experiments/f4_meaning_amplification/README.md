# F4 — Information Geometry Geodesics  
## Meaning Amplification Observation

---

## 🇹🇷 Türkçe Açıklama

Bu deney, kitapta tanımlanan **F4 — Bilgi-Geometri Geodezikleri** önermesinin
**dinamik ve oransal izdüşümünü** incelemeyi amaçlar.

Kuramsal çerçevede, öğrenme sürecinin
bilgi uzayında (Fisher bilgi metriği Gᵢⱼ ile tanımlanan)
yaklaşık bir **geodezik yol** izlediği öne sürülür.

Önerme şunu ifade eder:
- C₀ (anlam verimi) yüksekken  
- bilgi uzayındaki eğrilik azalır  
- öğrenme yolu daha “düz” ve verimli hâle gelir  

Bu deney:
- Fisher metriğini **doğrudan hesaplamaz**
- geodezik denklemleri **çözmez**

Bunun yerine, anlamsal çıktının
girdiye oranla **büyüme hızını** ölçerek,
bilgi uzayındaki hareketin
**etkinliğine dair boyutsuz bir gösterge** üretir.

Tanımlanan nicelik:

( A_out − A_in ) / A_in

şu şekilde yorumlanır:
- küçük artışlar → yüksek eğrilik / dağınık yol  
- tutarlı ve yüksek artışlar → düşük eğrilik / geodezik yakınsama  

Bu bağlamda ölçülen büyütme oranı,
öğrenme yolunun **bilgi-geometrik verimliliğine**
dair dolaylı bir iz sağlar.

Dolayısıyla F4, F3’te gözlenen
olasılık uzayı kaymalarının ardından,
anlamın **yapısal olarak yoğunlaşıp yoğunlaşmadığını**
izleyen bir üst-katman deneyidir.

---

## 🇬🇧 English Description

This experiment examines the **dynamic and ratio-based projection**
of **F4 — Information Geometry Geodesics** as defined in the book.

Within the theoretical framework, the learning trajectory
is hypothesized to follow an approximate **geodesic**
in information space defined by the Fisher information metric Gᵢⱼ.

The proposition suggests that:
- when C₀ (meaning efficiency) is high  
- curvature in information space decreases  
- the learning path becomes more efficient and geodesic-like  

This experiment:
- does **not** compute the Fisher metric directly  
- does **not** solve geodesic equations  

Instead, it measures the **rate of semantic amplification**,
defined as the relative increase of semantic output
with respect to semantic input.

The quantity:

( A_out − A_in ) / A_in

is interpreted as:
- small or unstable increases → high curvature / inefficient paths  
- consistent amplification → reduced curvature / geodesic convergence  

Thus, the measured amplification rate acts as a
dimensionless proxy for the **geometric efficiency**
of movement through information space.

In this sense, F4 operates as a higher-layer experiment,
tracking whether the probability shifts observed in F3
consolidate into **structurally efficient semantic trajectories**.

---

## 📄 Source Code

```python
def meaning_amplification_rate(A_in, A_out):
    return (A_out - A_in) / (A_in + 1e-9)
