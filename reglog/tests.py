import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImpveXBhdWwiLCJleHAiOjE2MTAzNjA3NzQsImVtYWlsIjoiam95cGF1bDY1MEBnbWFpbC5jb20ifQ.ctIS3qNKVmNYFprFFeYCZCMUfWEe11GAAm1-VEun2Jw