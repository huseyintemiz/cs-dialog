import json
import random
import os
from pathlib import Path


class PromptGenerator:
    def __init__(self, resource_dir="resources"):
        # Tüm veri dosyalarını bir kere yükle
        with open(f'{resource_dir}/topic.json', 'r', encoding='utf-8') as f:
            self.konular = json.load(f)

        with open(f'{resource_dir}/bank.txt', 'r', encoding='utf-8') as f:
            self.banks = [line.strip() for line in f if line.strip()]

        with open(f'{resource_dir}/isim_on_kadin.txt', 'r', encoding='utf-8') as f:
            self.on_isimler_kadin = [line.strip() for line in f if line.strip()]

        with open(f'{resource_dir}/isim_kadin.txt', 'r', encoding='utf-8') as f:
            self.isimler_kadin = [line.strip() for line in f if line.strip()]

        with open(f'{resource_dir}/isim_on_erkek.txt', 'r', encoding='utf-8') as f:
            self.on_isimler_erkek = [line.strip() for line in f if line.strip()]

        with open(f'{resource_dir}/isim_erkek.txt', 'r', encoding='utf-8') as f:
            self.isimler_erkek = [line.strip() for line in f if line.strip()]

        with open(f'{resource_dir}/soyisim.txt', 'r', encoding='utf-8') as f:
            self.soyisimler = [line.strip() for line in f if line.strip()]

    def _select_bank(self):
        if random.random() < 0.3:
            return "Yapı Kredi Bankası"
        return random.choice(self.banks)

    def _select_kadin_isim(self):
        rand = random.random()
        isim = random.choice(self.isimler_kadin)

        if rand < 0.1:
            on_isim = random.choice(self.on_isimler_kadin)
            while on_isim == isim:
                on_isim = random.choice(self.on_isimler_kadin)
            return f"{on_isim} {isim}"
        elif rand < 0.2:
            son_isim = random.choice(self.isimler_kadin)
            while son_isim == isim:
                son_isim = random.choice(self.isimler_kadin)
            return f"{isim} {son_isim}"
        return isim

    def _select_erkek_isim(self):
        if random.random() < 0.35:
            on_isim = random.choice(self.on_isimler_erkek)
            isim = random.choice(self.isimler_erkek)
            while isim == on_isim:
                isim = random.choice(self.isimler_erkek)
            return f"{on_isim} {isim}"
        return random.choice(self.isimler_erkek)

    def _select_soyisim(self, cift_soyisim_olasiligi=0.15):
        if random.random() < cift_soyisim_olasiligi:
            soyisim1 = random.choice(self.soyisimler)
            soyisim2 = random.choice(self.soyisimler)
            while soyisim2 == soyisim1:
                soyisim2 = random.choice(self.soyisimler)
            return f"{soyisim1} {soyisim2}"
        return random.choice(self.soyisimler)

    def _select_musteri(self):
        gender = "Erkek" if random.random() < 0.5 else "Kadın"

        if gender == "Kadın":
            isim = self._select_kadin_isim()
            soyisim = self._select_soyisim(cift_soyisim_olasiligi=0.15)
        else:
            isim = self._select_erkek_isim()
            soyisim = self._select_soyisim(cift_soyisim_olasiligi=0)  # Erkek için tek soyisim

        return f"{isim} {soyisim}", gender

    def generate_prompt(self):
        # Random seçimler
        kurum = self._select_bank()
        musteri, gender = self._select_musteri()
        random_key = random.choice(list(self.konular.keys()))
        konu_baslik = self.konular[random_key]['başlık']
        konu_aciklama = self.konular[random_key].get('açıklama', '')

        prompt = f"""Bir çağrı merkezi müşteri görüşmesi senaryosu oluştur.

Senaryo Bilgileri:
- Kurum: {kurum}
- Müşteri Adı: {musteri}
- Konu: {konu_baslik}
- Konu Açıklaması: {konu_aciklama}

Kurallar ve Akış:
1. Diyalog çağrı merkezi temsilcisi tarafından başlatılsın.
2. Temsilci ilk cümlede müşteriyi adıyla selamlasın ve hangi kurumdan aradığını doğal bir şekilde belirtsin.
3. Temsilci arama gerekçesini ({konu_baslik}) net ve kısa şekilde açıklasın.
4. Ardından müşteri ile temsilci arasında doğal, gerçekçi ve profesyonel bir karşılıklı konuşma geçsin.
5. Müşteri sorular sorsun, temsilci açıklayıcı ve nazik yanıtlar versin.
6. Diyalog 3–5 tur sürecek şekilde ilerlesin.
7. Kapanışta çağrı merkezi temsilcisi nazikçe vedalaşsın.

Stil ve Ton:
- Resmi ama sıcak
- Net, anlaşılır Türkçe
- Türkiye'deki gerçek çağrı merkezi konuşma tarzına uygun

Çıktı Formatı:
Temsilci: ...
Müşteri: ...
Temsilci: ...
...
"""
        return prompt

    def generate_and_save(self, count, output_dir="prompts"):
        # Output klasörünü oluştur
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for i in range(1, count + 1):
            prompt = self.generate_prompt()
            filename = f"prompt_{i:06d}.txt"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(prompt)

            if i % 100 == 0:
                print(f"{i} prompt oluşturuldu...")

        print(f"Toplam {count} prompt '{output_dir}/' klasörüne kaydedildi.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Çağrı merkezi prompt generator")
    parser.add_argument("-n", "--count", type=int, default=100, help="Oluşturulacak prompt sayısı")
    parser.add_argument("-o", "--output", type=str, default="prompts", help="Çıktı klasörü")
    args = parser.parse_args()

    generator = PromptGenerator()
    generator.generate_and_save(args.count, args.output)
