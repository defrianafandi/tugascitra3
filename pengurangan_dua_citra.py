from PIL import Image

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 255:
        return 255
    return intensitas

def penambahan_dua_citra(citra_A, citra_B, citra_hasil):
    # pastikan ukuran citra A dan citra B sama :)
    CITRA_A = Image.open(citra_A)
    PIXEL_A = CITRA_A.load()

    CITRA_B = Image.open(citra_B)
    PIXEL_B = CITRA_B.load()

    ukuran_horizontal = CITRA_A.size[0]
    ukuran_vertikal = CITRA_A.size[1]

    CITRA_HASIL = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_HASIL = CITRA_HASIL.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = clipping(PIXEL_A[x, y][0] - PIXEL_B[x, y][0])
            G = clipping(PIXEL_A[x, y][1] - PIXEL_B[x, y][1])
            B = clipping(PIXEL_A[x, y][2] - PIXEL_B[x, y][2])
            PIXEL_HASIL[x, y] = (R, G, B)

    CITRA_HASIL.save(citra_hasil)


penambahan_dua_citra('gambar1.jpg', 'gambar2.jpg',
                      'gambar_hasil_pengurangan.jpg')