7596 Sayılı Kanun Yatırım Fonu Tasfiyesi, MKK FIFO ve PBLK Blokaj Metodolojisi
==============================================================================

27 Ekim 2026 tarihli Resmî Gazete'de yayımlanan **7596 sayılı Tasfiyesine Karar Verilen Bazı Yatırım Fonları Hakkında Kanun**, Sermaye Piyasası Kurulu'nun (SPK) 17 Eylül 2026 tarihli kararlarıyla tasfiyesine hükmedilen 131 yatırım fonu için *lex specialis* niteliğinde olağanüstü bir tasfiye rejimi öngörmüştür.

Hukuki Çerçeve ve MKK FIFO Net Yatırım Tutarı
---------------------------------------------

7596 sayılı Kanun uyarınca, fon portföyündeki varlıkların nakde çevrilmesinden elde edilen tutarın yatırımcı alacaklarını karşılamakta yetersiz kalması halinde ödeme matrahı son açıklanan sanal birim pay fiyatına göre değil; Merkezi Kayıt Kuruluşu (MKK) kayıtlarındaki **İlk Giren İlk Çıkar (FIFO)** esasına dayalı **Net Yatırım Tutarı** üzerinden belirlenir.

* **FIFO Lot Eşleştirmesi:** Yatırımcının 17 Eylül 2026 öncesinde gerçekleştirdiği kısmi pay satımları (çıkışlar), kronolojik olarak en eski alım lotlarından düşülür.
* **Kıstelyevm TÜFE ve Yİ-ÜFE Endekslemesi:** Tasfiye tarihine kadar elde kalan açık lotların alım maliyetleri, alım tarihi ile tasfiye tarihi arasındaki TÜFE ve Yİ-ÜFE değişim oranlarının aritmetik ortalaması üzerinden gün esaslı (*kıstelyevm*) olarak güncellenir.
* **1.000.000 TL Şartlı Ara Ödeme Tavanı:** Kanunda öngörülen 1.000.000 TL sınırı nihai tazminat tavanı olmayıp, dağıtılabilir nakit imkanları ölçüsünde yapılacak fon bazlı şartlı ara ödemenin üst sınırını ifade eder.

PBLK (TEFAS İşlem Blokajı) ve Takas Kesinliği Sorunu
----------------------------------------------------

17 Eylül 2026 ve öncesinde TEFAS platformu üzerinden usulüne uygun satış (iade) talimatı vermiş olmasına rağmen, fonların likidite temerrüdüne düşmesi nedeniyle payları Takasbank ve MKK ekranlarında **PBLK (Blokeli Pay)** statüsünde askıda kalan yatırımcıların hukuki durumu *Takas Kesinliği (Settlement Finality — 6362 s. SPKn m. 77 ve AB 98/26/EC Direktifi)* çerçevesinde değerlendirilmektedir.

Konuya ilişkin ayrıntılı normatif analiz ve dava stratejileri şu birincil kaynaklarda incelenmiştir:

* `7596 Sayılı Kanun Kapsamında Yatırım Fonları Tasfiye Analizi ve Yatırımcı Hakları <https://koptay.av.tr/makale/7596-sayili-kanun-yatirim-fonlari-tasfiye-analizi>`_
* `TEFAS Fon Blokajı (PBLK) Nedir? Takas Kesinliği ve Hukuki Çözüm Yolları <https://koptay.av.tr/makale/tefas-fon-blokaj-pblk-nedir-hukuki-cozum>`_
* `Yatırım Fonu Zararı Tazminat Davası, Portföy Yönetim Şirketi ve SPK Sorumluluğu <https://koptay.av.tr/makale/yatirim-fonu-zarari-tazminat-davasi-spk-sorumluluk>`_
* `Tam Metin Akademik Monografi (PDF — 14 Sayfa, 42 Dipnot) <https://koptay.av.tr/yayinlar/7596-sayili-kanun-yatirim-fonu-tasfiye-rejimi-pblk-ve-tazminat-sorumlulugu-2026.pdf>`_

JavaScript / TypeScript API Kullanımı
-------------------------------------

``calculateFifo7596`` fonksiyonu yatırımcının alım/satım hareketlerini FIFO sırasına göre eşleştirerek kalan pay adedini, endekslenmiş net yatırım tutarını ve 1.000.000 TL ara ödeme dilimini hesaplar:

.. code-block:: javascript

   import { calculateFifo7596 } from "turk-hukuk-hesaplama";

   const sonuc = calculateFifo7596(
     [
       { type: "BUY", shares: 10000, unitPrice: 42.5, indexFactor: 1.18 },
       { type: "BUY", shares: 5000, unitPrice: 58.0, indexFactor: 1.06 },
       { type: "SELL", shares: 4000, unitPrice: 61.2 }
     ],
     850000 // Mevcut dağıtılabilir nakit havuzu payı (TL)
   );

   console.log(sonuc.remainingShares);        // 11000
   console.log(sonuc.indexedNetPrincipalTL);  // Endekslenmiş net yatırım anaparası
   console.log(sonuc.interimCapPaymentTL);    // Ara ödeme tutarı (maks. 1.000.000 TL)
