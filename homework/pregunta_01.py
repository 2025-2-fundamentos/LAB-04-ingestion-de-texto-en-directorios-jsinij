# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def pregunta_01():
    """
    Ver enunciado en el archivo.
    """
    import os
    import zipfile
    import csv

    # 1. Descomprimir el archivo input.zip
    zip_path = os.path.join("files", "input.zip")
    extract_dir = os.path.join("files")

    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(extract_dir)

    # Ahora esperamos tener: files/input/train/... y files/input/test/...
    base_input_dir = os.path.join("files", "input")

    # 2. Crear carpeta de salida
    output_dir = os.path.join("files", "output")
    os.makedirs(output_dir, exist_ok=True)

    def build_dataset(split_name):
        """
        Construye el CSV para 'train' o 'test'.
        """
        split_dir = os.path.join(base_input_dir, split_name)
        output_path = os.path.join(output_dir, f"{split_name}_dataset.csv")

        # Abrimos el CSV y escribimos encabezado
        with open(output_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "target"])

            # Recorremos las 3 carpetas de sentimientos
            for sentiment in ["negative", "neutral", "positive"]:
                sentiment_dir = os.path.join(split_dir, sentiment)

                if not os.path.isdir(sentiment_dir):
                    continue

                # Aseguramos orden consistente por nombre de archivo
                file_names = sorted(
                    f for f in os.listdir(sentiment_dir) if f.endswith(".txt")
                )

                for file_name in file_names:
                    file_path = os.path.join(sentiment_dir, file_name)

                    # Leemos el texto del archivo y lo dejamos como una sola frase
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = " ".join(line.strip() for line in f)

                    writer.writerow([text, sentiment])

    # Construir datasets de train y test
    build_dataset("train")
    build_dataset("test")