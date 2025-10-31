import os

path = "imaginibmp"
alfabet = "#. $&*!"

for fn in os.listdir(path):
    full_fn = os.path.join(path, fn)
    #print(fn)
    only_fn, _ = os.path.splitext(fn)
    with open(full_fn, 'rb') as f:
        data = f.read()

    pixels_offset = int.from_bytes(data[10:14], byteorder="little")
    width = int.from_bytes(data[18:22], byteorder="little")
    height = int.from_bytes(data[22:26], byteorder="little")
    bpp = int.from_bytes(data[28:32], byteorder="little") // 8
    aligned_width = width * bpp
    if aligned_width % 4 > 0:
        aligned_width = ((aligned_width // 4) + 1) * 4

    print(pixels_offset, width, height, bpp, aligned_width)

    pixels = data[pixels_offset:]

    text_lines = []
    for ln in range(height):
        text_line = []
        pixels_line = pixels[ln*aligned_width:(ln+1)*aligned_width]
        for col in range(width):
            pixel_val = int.from_bytes(pixels_line[col*bpp:(col+1)*bpp], byteorder="little")
            r = pixel_val >> 16
            g = (pixel_val >> 8) % 256
            b = pixel_val % 256
            idx = (r+g+b) % len(alfabet)
            text_line += [alfabet[idx]]

                
        text_line += ['\n']
        text_lines += [text_line]
    
    with open(f"{only_fn}.txt", 'w') as f:
        for ln in text_lines[::-1]:
            text = "".join(ln)
            f.write(text)
