# Davetiye

Bu paket davetiye tasarımını, çalışan konum QR kodunu ve WhatsApp önizleme ayarlarını içerir. Eski yayın adresine bağlantı veya yönlendirme içermez.

## GitHub Pages ile yayınlama

1. GitHub hesabı veya organizasyonunun ve deponun adını nötr seçin. GitHub Pages adresinde hesap/organizasyon adı ve repo adı görünür. Mevcut hesabınızın adını değiştirmeniz gerekmez; nötr bir organizasyon altında da yayınlayabilirsiniz.
2. Paket içeriğini deponun köküne yükleyin. `.github/workflows/pages.yml` dosyasını da ekleyin. Varsayılan dal `main` olmalıdır; farklıysa bu dosyadaki dalı güncelleyin.
3. Depoda Settings > Pages > Build and deployment > Source altında GitHub Actions seçin.
4. Actions > Publish invitation iş akışını çalıştırın. Yayın sonunda verilen HTTPS adresini WhatsApp'ta paylaşın.

Önizleme görselinin tam adresi yayın sırasında otomatik ayarlanır; JavaScript çalıştırılması gerekmez. WhatsApp'ın önizlemeyi göstermesi uygulamanın davranışı ve ayarlarına bağlıdır.

Adres gizliliği yalnızca URL için geçerlidir; davetiyedeki isimler ve etkinlik adresi görünür kalır.

Resmi belgeler: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
