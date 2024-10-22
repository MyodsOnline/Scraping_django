from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse


class BasePageTest(TestCase):
    @patch("your_app.views.return_svg_from_file")  # Подмена функции return_svg_from_file
    @patch("your_app.views.get_SMZU_file")  # Подмена функции get_SMZU_file
    def test_base_page_with_existing_svg(self, mock_get_smzu_file, mock_return_svg_from_file):
        """
        Тестирование успешного отображения страницы с корректным SVG-файлом.
        """
        # Настроим поведение mock объектов
        mock_return_svg_from_file.return_value = "<svg>content</svg>"
        mock_get_smzu_file.return_value = "test_smzu_file.txt"

        # Выполняем GET-запрос к base_page
        response = self.client.get(reverse("base_page"))

        # Проверка успешного рендеринга
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tmpp.html")
        # Проверяем контекст
        self.assertContains(response, "<svg>content</svg>")
        self.assertContains(response, "test_smzu_file.txt")
        self.assertEqual(response.context["title"], "Base page")

    @patch("your_app.views.return_svg_from_file")
    @patch("your_app.views.get_SMZU_file")
    def test_base_page_with_missing_svg(self, mock_get_smzu_file, mock_return_svg_from_file):
        """
        Тестирование отображения страницы при отсутствии SVG-файла.
        """
        # Подменяем поведение: имитируем FileNotFoundError
        mock_return_svg_from_file.side_effect = FileNotFoundError
        mock_get_smzu_file.return_value = "test_smzu_file.txt"

        response = self.client.get(reverse("base_page"))

        # Проверяем успешный рендеринг
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tmpp.html")
        # Проверяем контекст
        self.assertContains(response, "Source is empty")
        self.assertContains(response, "test_smzu_file.txt")
        self.assertEqual(response.context["title"], "Base page")

    @patch("your_app.views.get_SMZU_file")
    def test_base_page_smzu_file_context(self, mock_get_smzu_file):
        """
        Тестирование передачи корректного имени SMZU файла в контекст.
        """
        mock_get_smzu_file.return_value = "test_smzu_file.txt"

        response = self.client.get(reverse("base_page"))

        # Проверяем, что SMZU файл передан в контекст
        self.assertEqual(response.context["smzu_file_name"], "test_smzu_file.txt")
        self.assertContains(response, "test_smzu_file.txt")

