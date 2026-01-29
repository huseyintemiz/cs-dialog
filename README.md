# Çağrı Merkezi Diyalog Prompt Generator

Türkiye'deki banka çağrı merkezi müşteri görüşmeleri için sentetik diyalog promptları üreten bir araç.

## Amaç

Bu proje, eğitim/test verisi olarak kullanılabilecek gerçekçi çağrı merkezi senaryoları oluşturur. Her prompt, rastgele seçilen müşteri bilgileri, banka ve konu kombinasyonlarıyla benzersiz bir senaryo içerir.

## Sentetik Diyalog Üretimi

Oluşturulan promptlar, aşağıdaki LLM servisleri veya açık kaynak modellere verilerek bankacılıkla ilgili sentetik diyaloglar üretilebilir:

**Ticari API Servisleri:**
- OpenAI
- Anthropic (Claude)
- Google (Gemini)

**Açık Kaynak Modeller:**
- Qwen
- Gemma



## Kullanım

```bash
# 100 prompt oluştur (varsayılan)
python chat_prompt_generator.py

# 500 prompt oluştur
python chat_prompt_generator.py -n 500

# Farklı klasöre kaydet
python chat_prompt_generator.py -n 1000 -o my_prompts
```

Çıktı dosyaları: `prompts/prompt_000001.txt`, `prompts/prompt_000002.txt`, ...

## Olasılıksal Tasarım

### Cinsiyet Seçimi
| Cinsiyet | Olasılık |
|----------|----------|
| Erkek    | %50      |
| Kadın    | %50      |

### Banka Seçimi
| Seçim | Olasılık |
|-------|----------|
| Yapı Kredi Bankası | %30 |
| Diğer bankalar (rastgele) | %70 |

### Kadın İsim Yapısı
| Format | Olasılık | Örnek |
|--------|----------|-------|
| Tek isim | %80 | Ayşe |
| Ön isim + İsim | %10 | Zeynep Ceren |
| İsim + Son isim | %10 | Büşra Nur |

### Erkek İsim Yapısı
| Format | Olasılık | Örnek |
|--------|----------|-------|
| Tek isim | %65 | Mehmet |
| Ön isim + İsim | %35 | Ahmet Selim |

### Soyisim Yapısı
| Cinsiyet | Tek Soyisim | Çift Soyisim | Örnek |
|----------|-------------|--------------|-------|
| Kadın | %85 | %15 | Yılmaz / Yılmaz Kaya |
| Erkek | %100 | %0 | Demir |

## Veri Dosyaları

Tüm veri dosyaları `resources/` klasöründe bulunur:

| Dosya | Açıklama | Örnek İçerik |
|-------|----------|--------------|
| `resources/topic.json` | Arama konuları | Kredi kartı kampanyaları, limit artışı, vb. |
| `resources/bank.txt` | Banka listesi | Akbank, Garanti, İş Bankası, vb. |
| `resources/isim_erkek.txt` | Erkek isimleri | Ahmet, Mehmet, Ali, vb. |
| `resources/isim_kadin.txt` | Kadın isimleri | Ayşe, Fatma, Zeynep, vb. |
| `resources/isim_on_erkek.txt` | Erkek ön isimleri | Mehmet, Ali, Ömer, vb. |
| `resources/isim_on_kadin.txt` | Kadın ön isimleri | Zeynep, Elif, Ayşe, vb. |
| `resources/soyisim.txt` | Soyisimler | Yılmaz, Kaya, Demir, vb. |

## Örnek Çıktı

```
Bir çağrı merkezi müşteri görüşmesi senaryosu oluştur.

Senaryo Bilgileri:
- Kurum: Akbank
- Müşteri Adı: Mehmet Ali Yılmaz
- Konu: Kredi Kartı Kampanyaları
- Konu Açıklaması: Taksit, chip-para, indirim ve puan kazanımı...

Kurallar ve Akış:
1. Diyalog çağrı merkezi temsilcisi tarafından başlatılsın.
2. Temsilci ilk cümlede müşteriyi adıyla selamlasın...
...
```

## Proje Yapısı

```
cs-dialog/
├── chat_prompt_generator.py  # Ana generator scripti
├── README.md
├── resources/                # Veri dosyaları
│   ├── topic.json            # Konu veritabanı
│   ├── bank.txt              # Banka listesi
│   ├── isim_erkek.txt        # Erkek isimleri
│   ├── isim_kadin.txt        # Kadın isimleri
│   ├── isim_on_erkek.txt     # Erkek ön isimleri
│   ├── isim_on_kadin.txt     # Kadın ön isimleri
│   └── soyisim.txt           # Soyisimler
└── prompts/                  # Oluşturulan promptlar
    ├── prompt_000001.txt
    ├── prompt_000002.txt
    └── ...
```
