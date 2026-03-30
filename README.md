# 🛣️ Şerit Takip Sistemi (Lane Detection System)

Bu proje, bilgisayarlı görü (Computer Vision) tekniklerini kullanarak video akışları üzerinde yol şeritlerini gerçek zamanlı olarak tespit etmek için geliştirilmiştir. Python ve OpenCV kütüphanesi temel alınarak oluşturulan bu sistem, otonom sürüş algoritmalarının temel yapı taşlarından biridir.

---

## ✨ Özellikler

* **Görüntü İşleme Pipeline'ı:** Gri tonlama, Gaussian Blur ile gürültü azaltma ve Canny Edge Detection.
* **İlgi Alanı (ROI) Maskeleme:** Sadece yolun bulunduğu alt bölgeye odaklanarak işlem verimliliğini artırma.
* **Hough Line Transform:** Kesikli ve sürekli yol çizgilerinin matematiksel olarak tespiti.
* **Hız ve Stabilite:** `.mp4` formatındaki test verileri üzerinde düşük gecikmeli analiz.

## 📂 Proje Yapısı

```text
.
├── roadline.py                # Ana algoritma ve görüntü işleme kodu
├── linedetecttestdata.mp4     # Birinci test videosu
├── video2.mp4                 # İkinci test videosu
