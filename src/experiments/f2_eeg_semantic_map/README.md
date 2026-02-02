# F2 — C-Operator Observation  
## AI / Human Learning Semantic Mapping

---

## 🇹🇷 Türkçe Açıklama

Bu deney, kitapta tanımlanan **F2 — C-Operatörü Gözlemi (AI / İnsan Öğrenmesi)** önermesinin
**zamansal ve yapısal izdüşümünü** gözlemlemeyi amaçlar.

Kuramsal olarak C-operatörü şu şekilde tanımlanır:

C₀ = dA₀ / dI₀

Burada:
- I₀ → sisteme giren bilgi miktarı  
- A₀ → öngörü gücü + görev başarımı ile temsil edilen anlamsal çıktı  

Bu deney, **doğrudan C₀ hesaplaması yapmaz**.
Bunun yerine, biyolojik veya yapay sinyallerdeki
**frekans alanı dağılımını** analiz ederek
anlamsal yoğunlaşmanın **yapısal bir göstergesini** üretir.

EEG veya benzeri zaman-serisi sinyalleri,
Fourier dönüşümü ile frekans uzayına taşınır.
Frekans bileşenlerinin standart sapması ile ortalaması arasındaki oran:

- sinyalin **düzenlenme derecesini**
- anlamsal temsillerin **yoğunlaşma düzeyini**

gösteren boyutsuz bir nicelik olarak ele alınır.

Bu ölçüm:
- enerji tüketimini içermez  
- görev başarımıyla doğrudan ilişkilendirilmez  

Ancak şu hipotezi sınamak için kullanılır:

> Öğrenme sürecinin belirli evrelerinde,
> anlamsal yoğunluk ani bir artış gösterir;
> bu artış, C-operatörünün tepe yaptığı
> **kritik anlam üretim eşiğine** karşılık gelir.

Bu nedenle F2, F1’de ölçülen bilgi düzenlenmesini,
**zaman-frekans düzleminde anlamsal yapı oluşumuyla**
ilişkilendiren bir ara katman deneyidir.

---

## 🇬🇧 English Description

This experiment explores the **structural and temporal projection**
of **F2 — C-Operator Observation (AI / Human Learning)** as defined in the book.

Theoretically, the C-operator is defined as:

C₀ = dA₀ / dI₀

where:
- I₀ represents the input information quantity  
- A₀ represents semantic output, including prediction power and task success  

This experiment does **not** compute C₀ directly.
Instead, it analyzes the **frequency-domain structure**
of biological or artificial signals to derive
a proxy for **semantic density**.

EEG or similar time-series signals are transformed
into the frequency domain using Fourier analysis.
The ratio between the standard deviation and the mean
of frequency amplitudes is interpreted as a
dimensionless indicator of:

- structural organization  
- semantic concentration  

This measurement:
- does not include energy consumption  
- does not directly encode task performance  

It is used to test the following hypothesis:

> During specific learning phases,
> semantic density exhibits sharp peaks;
> these peaks correspond to the
> **critical meaning production threshold**
> where the C-operator reaches a maximum.

Thus, F2 functions as an intermediate-layer experiment,
linking the information structuring observed in F1
to emergent semantic organization
in the time–frequency domain.

---

## 📄 Source Code

```python
import numpy as np

def eeg_semantic_map(signal):
    fft = np.abs(np.fft.rfft(signal))
    meaning_density = np.std(fft) / (np.mean(fft) + 1e-9)
    return float(meaning_density)
