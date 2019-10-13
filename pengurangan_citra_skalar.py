from PIL import Image

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 255:
        return 255
    return intensitas

def pengurangan_citra_skalar(nilai_skalar):
    CITRA = Image.open('gambar1.jpg')
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = clipping(PIXEL[x, y][0] - nilai_skalar)
            G = clipping(PIXEL[x, y][1] - nilai_skalar)
            B = clipping(PIXEL[x, y][2] - nilai_skalar)
            PIXEL[x, y] = (R, G, B)

    nama_setelah_disave = 'pengurangan_skalar_' + str(nilai_skalar) +'.jpg'
    CITRA.save(nama_setelah_disave)


pengurangan_citra_skalar(50)