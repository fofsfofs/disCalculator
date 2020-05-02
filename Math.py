from mathpix.mathpix import MathPix

reader = MathPix(
    app_id="discalculator_gmail_com_f307ad", app_key="684b628a6ac77aeb3d1f"
)
ocr = reader.process_image(
    image_url="https://media.discordapp.net/attachments/705540749558677656/706203915049369640/EfI8B.png"
)

print(ocr.latex)
