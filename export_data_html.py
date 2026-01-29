import pandas as pd

df = pd.read_excel("wisata_indonesia_clean.xlsx")

html = df.to_html(
    index=False,
    classes="styled-table",
    escape=False
)

html_page = f"""
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Data Wisata</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 10px;
}}

.styled-table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 14px;
}}

.styled-table thead {{
    background-color: #1e88e5;
    color: white;
    position: sticky;
    top: 0;
}}

.styled-table th, .styled-table td {{
    padding: 8px 10px;
    border: 1px solid #ddd;
    vertical-align: top;
}}

.styled-table tr:nth-child(even) {{
    background-color: #f3f3f3;
}}

.styled-table tr:hover {{
    background-color: #e3f2fd;
}}

</style>
</head>
<body>
{html}
</body>
</html>
"""

with open("data_wisata.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("data_wisata.html berhasil dibuat (rapih)")