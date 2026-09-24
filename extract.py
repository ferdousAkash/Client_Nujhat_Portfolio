import fitz
import os

os.makedirs('images', exist_ok=True)
count = 1
for pdf in ['portfolio_part1.pdf', 'portfolio_part2.pdf']:
    doc = fitz.open(pdf)
    for page in doc:
        pix = page.get_pixmap(dpi=150)
        pix.save(f"images/page-{count}.jpg")
        print(f"Saved images/page-{count}.jpg")
        count += 1
print(f"Total pages extracted: {count - 1}")
