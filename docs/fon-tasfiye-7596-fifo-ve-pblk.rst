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

* `2026 Yatırım Fonu Krizi Mağdurları: 7596 Sayılı Kanun, PBLK ve Tazminat Davası Rehberi <https://koptay.av.tr/makale/yatirim-fonu-krizi-magdurlari-pblk-7596-sayili-kanun-tasfiye-ve-tazminat-davasi-rehberi-2026>`_
* `MKK PBLK Blokajı Nedir? Valörü Dolmuş Fon Satış Talimatlarında Muaccel Alacak ve İptal Davası <https://koptay.av.tr/makale/mkk-pblk-nedir-fon-satis-talimati-muaccel-alacak-ve-iptal-davasi>`_
* `7596 Sayılı Fon Tasfiye Kanunu: MKK FIFO Net Yatırım Tutarı ve 1 Milyon TL Ara Ödeme İtirazı <https://koptay.av.tr/makale/7596-sayili-fon-tasfiye-kanunu-fifo-net-yatirim-tutari-ve-1-milyon-tl-ara-odeme-itirazi>`_
* `Serbest Fon Mağdurları: Nitelikli Yatırımcı Beyanı, Banka, Saklayıcı ve SPK Tazminat Davası <https://koptay.av.tr/makale/serbest-fon-magdurlari-nitelikli-yatirimci-beyani-banka-ve-spk-tazminat-davasi>`_
* `7596 FIFO ve Yatırım Fonu Zarar Tazminatı Canlı Hesaplama Aracı <https://koptay.av.tr/hesaplama-araclari/yatirim-fonu-krizi-tasfiye-ve-zarar-tazminati-hesaplama>`_
* `Tam Metin Akademik Monografi (PDF — 14 Sayfa, 42 Dipnot) <https://koptay.av.tr/yayinlar/7596-sayili-kanun-yatirim-fonu-tasfiye-rejimi-pblk-ve-tazminat-sorumlulugu-2026.pdf>`_

JavaScript / TypeScript API Kullanımı
-------------------------------------

``calculateLaw7596Fifo`` fonksiyonu yatırımcının toplam nakit girişi, geçmiş kısmi satım çıkışı ve 17.09.2026 ekran / PBLK alacağını esas alarak net yatırım tutarını, 1.000.000 TL ara ödeme dilimini ve bakiye dava farkını hesaplar:

.. code-block:: javascript

   import { calculateLaw7596Fifo } from "turk-hukuk-hesaplama";

   const sonuc = calculateLaw7596Fifo({
     totalCashIn: 3_500_000,
     pastRedemptions: 500_000,
     navOrPblkValue: 5_200_000
   });

   console.log(sonuc.fifoNetPrincipal);     // 3000000
   console.log(sonuc.interimPayment);       // 1000000
   console.log(sonuc.totalLitigationClaim); // 4200000
