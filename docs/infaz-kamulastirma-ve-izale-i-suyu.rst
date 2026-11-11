Ceza İnfaz (5275 s. Kanun), İlave Tediye ve Ortaklığın Giderilmesi Usulü
========================================================================

Bu bölüm; ceza infaz hukukundaki koşullu salıverilme ve denetimli serbestlik sürelerinin deterministik hesabını, 6772 sayılı Kanun kapsamındaki kamu işçisi ilave tediye bordrolamasını ve 4721 sayılı Türk Medeni Kanunu m. 698–699 uyarınca ortaklığın giderilmesi (*izale-i şüyu*) cebri artırma eşiğini kapsar.

5275 Sayılı Kanun Koşullu Salıverilme ve Denetimli Serbestlik
-------------------------------------------------------------

5275 sayılı Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun m. 107 ve m. 105/A hükümlerine göre genel suç tiplerinde 1/2, istisnai katalog suçlarda ise 2/3 veya 3/4 koşullu salıverilme oranı uygulanmakta; tutuklulukta geçen süreler (*TCK m. 63 mahsup*) doğrudan kapalı/açık kurum süresinden indirilmektedir:

.. code-block:: javascript

   import { calculateExecution5275 } from "turk-hukuk-hesaplama";

   const infaz = calculateExecution5275({
     totalDays: 1800,
     ratio: 0.5,
     probationDays: 365,
     preTrialDays: 90
   });
   console.log(infaz.actualPrisonDays); // Fiili kurumda kalma süresi (gün)

6772 Sayılı Kanun Kamu İşçisi İlave Tediye Bordrolaması
-------------------------------------------------------

Belediye şirketleri ve kamu kurumlarında sürekli işçi statüsünde çalışanların yılda 52 günlük (4x13 gün) ilave tediye alacağından SGK işçi primi (%14), işsizlik sigortası işçi payı (%1) ve kümülatif gelir vergisi dilimi düşülür; asgari ücret istisnası yürürlükteki damga ve gelir vergisi kurallarına göre uygulanır:

.. code-block:: javascript

   import { calculateIlaveTediye6772 } from "turk-hukuk-hesaplama";

   const tediye = calculateIlaveTediye6772({
     grossDailyWageTL: 1450,
     days: 13,
     incomeTaxRate: 0.20
   });
   console.log(tediye.netPayableTL);

Ortaklığın Giderilmesi (İzale-i Şüyu) ve Cebri Artırma Alt Sınırı
-----------------------------------------------------------------

4721 sayılı TMK m. 698–699 ve 2004 sayılı İcra ve İflas Kanunu'nun elektronik satış hükümleri uyarınca, satış memurluğunca yürütülen açık artırmalarda ihale bedeli taşınmazın muhammen değerinin **%50'si ile paraya çevirme ve paylaştırma giderlerinin toplamını** (varsa rüçhanlı alacakları) aşmak zorundadır.

İlgili Canlı Hesaplama Araçları ve Akademik Yayınlar
----------------------------------------------------

* `Ceza İnfaz ve Yatar Süresi Hesaplama Aracı <https://koptay.av.tr/hesaplama-araclari/infaz-hesaplama>`_
* `6772 Sayılı Kanun Kamu İşçisi İlave Tediye Hesaplama Aracı <https://koptay.av.tr/hesaplama-araclari/ilave-tediye-hesaplama>`_
* `4721 Sayılı TMK m. 698–699 Uyarınca Ortaklığın Giderilmesi (İzale-i Şüyu) Davaları ve Cebri Artırma Usulü (PDF Monografi) <https://koptay.av.tr/yayinlar/ortakligin-giderilmesi-izale-i-suyu-2026.pdf>`_
* `Koptay Hukuk Bürosu Resmi Web Sitesi <https://koptay.av.tr/>`_
