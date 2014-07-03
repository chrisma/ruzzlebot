import math, operator, unittest
import Image
from pytesseract import image_to_string

def rmsdiff(image1, image2):
	"Calculate the root-mean-square difference between two images"
	h1 = image1.histogram()
	h2 = image2.histogram()

	rms = math.sqrt(reduce(operator.add,
		map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

	return rms

b = Image.open('characters/B.png').convert('RGB')
def char_from_comparison(image):
	if rmsdiff(image, b) < 10:
		return 'B'
	return 'I'

def recognize_chars(image_path):
	image = Image.open(image_path).convert('RGB')
	width = 90
	height = 90
	distance = 170 
	start_x = 50
	start_y = 400

	out = []
	x = start_x
	y = start_y

	for _ in range(4):
		for _ in range(4):
			crop = image.crop( (x, y, x + width, y + height) )
			char = image_to_string(crop, psm_level='5', configfile='ruzzleconf')
			# Tesseract doesn't seem to recognize I's and B's
			if char == '':
				char = char_from_comparison(crop)
			out.append(char)
			x += distance
		y += distance
		x = start_x

	return out


if __name__ == "__main__":
	class OcrTestCase(unittest.TestCase):
		def test_ocr1(self):
			self.assertEqual(recognize_chars('screenshots/1.png'), ['S', 'S', 'T', 'Z', 'E', 'H', 'E', 'G', 'R', 'I', 'R', 'E', 'T', 'T', 'N', 'L'])
		def test_ocr2(self):
			self.assertEqual(recognize_chars('screenshots/2.png'), ['S', 'R', 'N', 'T', 'R', 'E', 'E', 'A', 'I', 'I', 'R', 'G', 'N', 'E', 'N', 'T'])
		def test_ocr3(self):
			self.assertEqual(recognize_chars('screenshots/3.png'), ['E', 'U', 'R', 'E', 'T', 'N', 'A', 'E', 'E', 'R', 'O', 'T', 'G', 'O', 'D', 'L'])
		def test_ocr4(self):
			self.assertEqual(recognize_chars('screenshots/4.png'), ['E', 'S', 'V', 'L', 'E', 'A', 'A', 'E', 'B', 'N', 'R', 'E', 'N', 'E', 'D', 'E'])
		def test_ocr5(self):
			self.assertEqual(recognize_chars('screenshots/5.png'), ['I', 'K', 'O', 'E', 'O', 'E', 'R', 'N', 'R', 'T', 'T', 'R', 'S', 'E', 'R', 'A'])
		def test_ocr6(self):
			self.assertEqual(recognize_chars('screenshots/6.png'), ['P', 'S', 'R', 'C', 'E', 'N', 'A', 'H', 'D', 'R', 'I', 'G', 'E', 'N', 'E', 'A'])
		def test_ocr7(self):
			self.assertEqual(recognize_chars('screenshots/7.png'), ['H', 'E', 'K', 'U', 'A', 'L', 'U', 'N', 'N', 'E', 'A', 'R', 'E', 'E', 'S', 'T'])
		def test_ocr8(self):
			self.assertEqual(recognize_chars('screenshots/8.png'), ['H', 'N', 'E', 'Z', 'S', 'R', 'D', 'T', 'A', 'N', 'E', 'E', 'U', 'S', 'N', 'H'])
		def test_ocr9(self):
			self.assertEqual(recognize_chars('screenshots/9.png'), ['A', 'T', 'E', 'L', 'B', 'L', 'I', 'D', 'E', 'U', 'E', 'N', 'M', 'N', 'D', 'T'])
		def test_ocr10(self):
			self.assertEqual(recognize_chars('screenshots/10.png'), ['G', 'G', 'E', 'L', 'E', 'R', 'E', 'A', 'R', 'T', 'H', 'E', 'E', 'N', 'A', 'E'])

	unittest.main()