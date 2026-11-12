Aktüeryal Maluliyet (Balthazard), TRH-2010 ve Araç Değer Kaybı Metodolojisi
===========================================================================

Türk tazminat ve sigorta hukukunda bedensel zararların (sürekli iş göremezlik ve destekten yoksun kalma) hesabı; Yargıtay Hukuk Genel Kurulu ve 4. / 17. Hukuk Dairesi içtihatları doğrultusunda **TRH-2010 Ulusal Mortalite Tablosu**, **Balthazard Birleştirme Formülü** ve **Progresif Rant** ilkelerine dayanır.

Balthazard Çoklu Engel Birleştirme Algoritması
----------------------------------------------

Birden fazla araz veya organ kaybı bulunan kazazedelerde engel oranları aritmetik olarak toplanmaz; en yüksek engel oranından başlanarak kalan sağlam kapasite üzerinden ardışık birleştirme uygulanır:

.. math::

   M_{n} = M_{n-1} + \frac{(100 - M_{n-1}) \times r_{n}}{100}

60 yaş ve üzeri bireylerde ilgili yönetmelik hükümleri uyarınca toplam orana yaş düzeltme payı eklenir.

Kod Örneği: ``calculateBalthazard``
-----------------------------------

.. code-block:: javascript

   import { calculateBalthazard } from "turk-hukuk-hesaplama";

   // %30, %20 ve %10 oranlarında üç ayrı maluliyet bulgusu (yaş: 42)
   const maluliyet = calculateBalthazard([30, 20, 10], { age: 42 });
   console.log(maluliyet.combinedRate); // 49.6

Canlı Aktüeryal Hesaplama Araçları ve Uygulama Rehberleri
---------------------------------------------------------

TRH-2010 bakiye ömür tabloları, kusur dağılımı ve asgari ücret emsal katsayılarıyla entegre çalışan etkileşimli hesaplama modülleri aşağıda yer almaktadır:

* `Trafik Kazası Balthazard Maluliyet ve Tazminat Hesaplama Aracı <https://koptay.av.tr/hesaplama-araclari/trafik-kazasi-maluliyet-hesaplama>`_
* `Trafik Kazası Bedensel Zarar Tazminatları ve Ek-2 Maluliyet Cetveli (PDF Monografi) <https://koptay.av.tr/yayinlar/trafik-kazasi-bedensel-zarar-ve-maluliyet-2026.pdf>`_
* `Pert (Tam Hasarlı) Araçlarda Değer Kaybı ve İkame Araç Mahrumiyet Tazminatı Rehberi <https://koptay.av.tr/makale/pert-araclarda-deger-kaybi-mahrumiyet>`_
