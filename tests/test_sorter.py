import unittest
from PIL import Image
from image_color_sorter.sorter import get_dominant_color, closest_color

class TestImageColorSorter(unittest.TestCase):
    
    def test_get_dominant_color(self):
        image = Image.new('RGB', (10, 10), color='red')
        dominant_color = get_dominant_color(image)
        self.assertEqual(dominant_color, (255, 0, 0))

    def test_closest_color(self):
        closest = closest_color((255, 0, 0))
        self.assertEqual(closest, 'red')
        
        closest = closest_color((255, 255, 255))
        self.assertEqual(closest, 'white')
        
        closest = closest_color((0, 0, 0))
        self.assertEqual(closest, 'black')

if __name__ == '__main__':
    unittest.main()
