import time

def geri_sayim(saniye):
    while saniye >= 0:
        dk, sn = divmod(saniye, 60)
        saat, dk = divmod(dk, 60)
        print(f"\r⏳ {saat:02d}:{dk:02d}:{sn:02d}", end="", flush=True)
        time.sleep(1)
        saniye -= 1
    print("\n⏰ Süre doldu!")

def main():
    try:
        saat = int(input("Saat: ") or 0)
        dakika = int(input("Dakika: ") or 0)
        saniye = int(input("Saniye: ") or 0)
    except ValueError:
        print("Lütfen sayı girin.")
        return

    toplam = saat * 3600 + dakika * 60 + saniye
    if toplam <= 0:
        print("Süre 0'dan büyük olmalı.")
        return

    try:
        geri_sayim(toplam)
    except KeyboardInterrupt:
        print("\nSayaç durduruldu.")

if __name__ == "__main__":
    main()