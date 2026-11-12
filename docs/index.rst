Türk Hukuk Hesaplama Algoritmaları ve 7596 Sayılı Kanun Metodolojisi
====================================================================

Bu teknik dokümantasyon, **Av. Murat Can Koptay** (`Koptay Hukuk Bürosu <https://koptay.av.tr/>`_) tarafından açık kaynaklı olarak yayımlanan ``turk-hukuk-hesaplama`` yazılım paketinin matematiksel modellerini, mevzuat dayanaklarını ve uygulama örneklerini içerir.

Paket; Türk sermaye piyasası hukukunda **7596 sayılı Kanun** kapsamındaki yatırım fonu tasfiye ve FIFO net yatırım hesaplamalarını, aktüeryal maluliyet (**Balthazard**) birleştirme formülünü, **5275 sayılı Ceza İnfaz Kanunu** koşullu salıverilme sürelerini ve **6772 sayılı Kanun** kamu işçisi ilave tediye bordrolamasını deterministik olarak modeller.

Kurulum (NPM / Node.js / TypeScript)
------------------------------------

Paket sıfır harici bağımlılığa (*zero-dependency*) sahiptir ve ESM ile tam TypeScript tip tanımlarını içerir:

.. code-block:: bash

   npm install turk-hukuk-hesaplama

Tarayıcıda doğrudan çalıştırmak isteyen son kullanıcılar ve hukukçular için kurulum gerektirmeyen canlı web arayüzleri `Türk Hukuk Hesaplama Araçları <https://koptay.av.tr/hesaplama-araclari>`_ sayfasında ücretsiz olarak sunulmaktadır.

Doğrulanmış Açık Erişim Kaynakları ve Atıf Künyesi
--------------------------------------------------

* **Kurumsal Yayın ve Araç Merkezi:** `Koptay Hukuk Bürosu — koptay.av.tr <https://koptay.av.tr/>`_
* **ORCID Araştırmacı Sicili:** `0009-0002-5225-5331 <https://orcid.org/0009-0002-5225-5331>`_
* **Resmi DOI Kaydı (CERN / Zenodo):** `10.5281/zenodo.24119703 <https://doi.org/10.5281/zenodo.24119703>`_
* **Tam Metin Hakemli Monografi (PDF):** `7596 Sayılı Kanun Kapsamında Yatırım Fonlarının Olağanüstü Tasfiye Rejimi, MKK FIFO Net Yatırım Tutarı ve PBLK Blokaj Uyuşmazlığı <https://koptay.av.tr/yayinlar/7596-sayili-kanun-yatirim-fonu-tasfiye-rejimi-pblk-ve-tazminat-sorumlulugu-2026.pdf>`_
* **NPM Paket Kaydı:** `npmjs.com/package/turk-hukuk-hesaplama <https://www.npmjs.com/package/turk-hukuk-hesaplama>`_
* **Açık Veri Seti (Hugging Face):** `turk-hukuku-ve-7596-fon-tasfiye-veri-seti <https://huggingface.co/datasets/koptay/turk-hukuku-ve-7596-fon-tasfiye-veri-seti>`_

Dokümantasyon Bölümleri
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: Metodoloji ve API Rehberi:

   fon-tasfiye-7596-fifo-ve-pblk
   aktueryal-balthazard-ve-deger-kaybi
   infaz-kamulastirma-ve-izale-i-suyu
