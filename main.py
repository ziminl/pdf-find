import random
import string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



random_letters = ''.join(random.choices(string.ascii_letters, k=300)) #300 random letters



pdf_filename = "random_letters.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

c.setFont("Helvetica", 12) #font 12

x = 100
y = 750

for i, letter in enumerate(random_letters):
    if y < 50:  # Move to a new line if the text goes too low
        y = 750
        x += 100
    c.drawString(x, y, letter)
    y -= 15  # Move down after each letter

# Save the PDF
c.save()

print(f"PDF generated: {pdf_filename}")


