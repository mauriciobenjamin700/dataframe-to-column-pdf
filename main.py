import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from data import df


def export_to_pdf(df, filename):
    # Converter DataFrame Pandas para uma lista de listas
    data = [df.columns.tolist()] + df.values.tolist()

    # Configuração do tamanho da página e margens
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Cria a tabela
    table = Table(data, repeatRows=1)

    # Estilo da tabela
    style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)

    # Obter largura disponível da página
    width, _ = letter

    # Ajustar a largura das colunas da tabela para preencher a página
    col_widths = [width / len(df.columns)] * len(df.columns)
    table._argW = col_widths

    # Adiciona a tabela aos elementos do documento
    elements.append(table)

    # Gera o PDF
    doc.build(elements)

# Exemplo de uso:
# Supondo que 'meu_dataframe' seja seu DataFrame do Pandas
# export_to_pdf(meudataframe, 'dados.pdf')

export_to_pdf(df, "teste1.pdf")