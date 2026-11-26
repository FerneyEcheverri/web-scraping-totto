
import json
import unittest
from pathlib import Path

# Ubicación de los archivos del proyecto
BASE = Path(__file__).resolve().parent.parent
WEB = BASE / "web"


class PruebasAplicacionWeb(unittest.TestCase):

    def test_archivos_principales_existen(self):
        self.assertTrue((WEB / "index.html").exists())
        self.assertTrue((WEB / "styles.css").exists())
        self.assertTrue((WEB / "script.js").exists())

    def test_html_enlaza_estilos_y_javascript(self):
        html = (WEB / "index.html").read_text(encoding="utf-8")

        self.assertIn("styles.css", html)
        self.assertIn("script.js", html)
        self.assertIn('id="productos"', html)

    def test_catalogo_json_es_valido(self):
        ruta_json = WEB / "data" / "productos.json"

        self.assertTrue(ruta_json.exists())

        with ruta_json.open(encoding="utf-8") as archivo:
            productos = json.load(archivo)

        self.assertIsInstance(productos, list)
        self.assertGreater(len(productos), 0)

    def test_productos_tienen_campos_necesarios(self):
        ruta_json = WEB / "data" / "productos.json"

        with ruta_json.open(encoding="utf-8") as archivo:
            productos = json.load(archivo)

        campos = [
            "nombre",
            "categoria",
            "descripcion",
            "precio",
            "descuento",
            "disponibilidad"
        ]

        for producto in productos:
            for campo in campos:
                self.assertIn(campo, producto)

            self.assertTrue(producto["nombre"])


if __name__ == "__main__":
    unittest.main()
