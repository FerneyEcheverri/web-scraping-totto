
import json
import unittest
from pathlib import Path

NOTEBOOK = Path("notebooks/EA1_Proyecto_Totto.ipynb")


class TestNotebook(unittest.TestCase):

    def test_notebook_existe(self):
        self.assertTrue(NOTEBOOK.exists())

    def test_notebook_es_json_valido(self):
        with open(NOTEBOOK, "r", encoding="utf-8") as archivo:
            notebook = json.load(archivo)

        self.assertIn("cells", notebook)

    def test_notebook_tiene_codigo_y_documentacion(self):
        with open(NOTEBOOK, "r", encoding="utf-8") as archivo:
            notebook = json.load(archivo)

        tipos = [celda["cell_type"] for celda in notebook["cells"]]

        self.assertIn("code", tipos)
        self.assertIn("markdown", tipos)


if __name__ == "__main__":
    unittest.main()
