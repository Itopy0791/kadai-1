import unittest
from kanji_converter import convert_to_kanji  

class TestKanjiConverter(unittest.TestCase):
    
    def test_convert_to_kanji(self):

        test_cases = {
            3: "三",
            6: "六",
            9: "九",
            12: "十二",
            13: "十三",
            15: "十五",
            18: "十八",
            21: "二十一",
            23: "二十三",
            24: "二十四",
            27: "二十七",
            30: "三十",
            31: "三十一",
            32: "三十二",
            33: "三十三",
            34: "三十四",
            35: "三十五",
            36: "三十六",
            37: "三十七",
            38: "三十八",
            39: "三十九"
        }
        
        for num, expected_kanji in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(convert_to_kanji(num), expected_kanji)

if __name__ == "__main__":
    unittest.main()

