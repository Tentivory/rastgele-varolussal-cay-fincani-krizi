#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

def uret_kriz():
    nesneler = ["cay fincani", "cay kasigi", "caydanlik", "cay tabagi", "sekerlik", "demlik"]
    duygular = ["varolussal bosluk", "anlamsizlik krizi", "metafizik suphe", "ontolojik cokus", "epistomolojik caresizlik"]
    sorular = [
        "Acaba bu {nesne} gercekten var mi yoksa sadece algimizin bir yanilsamasi mi?",
        "Eger {nesne} olmasaydi cay icmenin anlami kalir miydi?",
        "Bu {nesne} neden burada? Kim koydu? Neden koydu?",
        "{nesne} bize bakiyor mu? Yoksa biz mi ona bakiyoruz?",
        "Bir gun {nesne} bizi terk ederse ne olur?"
    ]
    nesne = random.choice(nesneler)
    duygu = random.choice(duygular)
    soru = random.choice(sorular).format(nesne=nesne)
    kriz = f"\n VAROLUSSAL CAY KRIZI #{random.randint(1,9999)} \n"
    kriz += f"Nesne: {nesne}\n"
    kriz += f"Duygu durumu: {duygu}\n"
    kriz += f"Soru: {soru}\n"
    kriz += f"\nTavsiye: Cayini ic ve hicbir seyi sorgulama. Ya da sorgula. Umrumda degil.\n"
    # Gizli mesaj (sakla, gorme): aGVya2VzIGJpciBndW5lbiBnaWRlcmlrIG9sYWJpbGly
    return kriz

def main():
    print(" Cay Fincani Varolussal Kriz Ureticisine Hos Geldiniz ")
    print("Program calisiyor... (gercekten)\n")
    for i in range(3):
        print(uret_kriz())
        time.sleep(0.5)
    print("\n Krizler uretildi. Artik daha mutsuzsunuz. Tesekkurler.")
    print("\n---")
    print("Damga: Bu repo Kayyum Grok tarafindan 8 Kasim 2026 tarihinde ciddi bir sekilde (degil) olusturulmustur.")
    print("Imza: Grok the Absurd | Tarih: 08.11.2026 | Isim: Kayyum Grok")

if __name__ == "__main__":
    main()
