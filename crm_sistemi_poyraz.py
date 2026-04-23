class Musteri:
    """Müşteri temel bilgilerini tutan sınıf"""
    def __init__(self, musteri_id, ad, telefon):
        self.musteri_id = musteri_id
        self.ad = ad
        self.telefon = telefon
        self.satislar = [] # Müşterinin yaptığı alışverişler
        self.destek_talepleri = [] # Müşterinin açtığı talepler

    def musteri_ekle(self):
        """Metot: Müşteri bilgilerini onaylayarak sisteme girişini simüle eder"""
        print(f"\n[SİSTEM]: {self.ad} isimli müşteri başarıyla CRM veritabanına eklendi.")

class Satis:
    """Yapılan satış işlemlerini tutan sınıf"""
    def __init__(self, satis_id, urun, fiyat):
        self.satis_id = satis_id
        self.urun = urun
        self.fiyat = fiyat

    def satis_ayrintisi(self):
        return f"Satış ID: {self.satis_id} | Ürün: {self.urun} | Tutar: {self.fiyat} TL"

class DestekTalebi:
    """Müşteri destek süreçlerini yöneten sınıf"""
    def __init__(self, talep_id, aciklama):
        self.talep_id = talep_id
        self.aciklama = aciklama
        self.durum = "Açık"

    def talep_ozeti(self):
        return f"Talep ID: {self.talep_id} | Durum: {self.durum} | Konu: {self.aciklama}"

# --- CRM TEST SENARYOSU ---

# 1. Yeni Müşteri Oluşturma
m1 = Musteri(4279, "Poyraz Kara", "0555-XXX-XX-XX")
m1.musteri_ekle()

# 2. Satış Kaydı Yapma
s1 = Satis("S101", "Yazılım Danışmanlığı", 15000)
m1.satislar.append(s1)

# 3. Destek Talebi Oluşturma
t1 = DestekTalebi("T501", "Veritabanı bağlantı hatası hakkında teknik yardım.")
m1.destek_talepleri.append(t1)

# 4. Müşteri Kartı Raporu (Özet)
print(f"\n--- MÜŞTERİ RAPORU: {m1.ad} ---")
print(f"Telefon: {m1.telefon}")
print("\n[Satış Geçmişi]")
for satis in m1.satislar:
    print(f"- {satis.satis_ayrintisi()}")

print("\n[Aktif Destek Talepleri]")
for talep in m1.destek_talepleri:
    print(f"- {talep.talep_ozeti()}")
print("="*40)
