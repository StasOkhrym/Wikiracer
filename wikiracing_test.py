import unittest

from wikiracing import WikiRacer


class WikiRacerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.racer = WikiRacer()

    def test_1(self):
        path = self.racer.find_path("Дружба", "Рим")
        self.assertEqual(path, ["Дружба", "Якопо Понтормо", "Рим"])

    def test_2(self):
        path = self.racer.find_path("Мітохондріальна ДНК", "Вітамін K")
        self.assertEqual(
            path, ["Мітохондріальна ДНК", "Бактерії", "Вітамін K"]
        )

    def test_3(self):
        path = self.racer.find_path(
            "Марка (грошова одиниця)", "Китайський календар"
        )
        self.assertEqual(
            path,
            [
                "Марка (грошова одиниця)",
                "Аахен",
                "Літній час",
                "Китайський календар",
            ],
        )

    def test_4(self):
        path = self.racer.find_path("Фестиваль", "Пілястра")
        self.assertEqual(path, ["Фестиваль", "Австрія", "Вівтар", "Пілястра"])

    def test_5(self):
        path = self.racer.find_path("Дружина (військо)", "6 жовтня")
        self.assertTrue(
            path
            in (
                ["Дружина (військо)", "Візантія", "1187", "6 жовтня"],
                [
                    "Дружина (військо)",
                    "Армія Української Народної Республіки",
                    "1918",
                    "6 жовтня",
                ],
            )
        )


if __name__ == "__main__":
    unittest.main()
