from flask import Blueprint, jsonify, request
from fpdf import FPDF
import os

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Email Campaign Report", ln=True, align='C')
    pdf.cell(200, 10, txt="Included Visualizations:", ln=True, align='L')

    if data['includeScatterPlot']:
        pdf.cell(200, 10, txt="Scatter Plot", ln=True, align='L')
        # Logic to embed the scatter plot image goes here

    if data['includeHeatMap']:
        pdf.cell(200, 10, txt="Heat Map", ln=True, align='L')
        # Logic to embed the heat map image goes here

    report_path = os.path.join('static/reports', 'campaign_report.pdf')
    pdf.output(report_path)

    return jsonify({'reportUrl': f'/static/reports/campaign_report.pdf'})