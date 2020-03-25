from fpdf import FPDF

def createPDF(data, country, cost):
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(190,10,f'Relation between cost of {cost} and happiness in {country.capitalize()}',1,1,'C')
    pdf.set_font('Helvetica', 'B', 12)
    pdf.multi_cell(0, 8, txt=data, align="C")
    pdf.image('OUTPUT/graph.png', 60, 90, h=80)
    return pdf.output('OUTPUT/final-document.pdf')