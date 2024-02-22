import PyPDF2

def pdf_to_txt_converter(
                         pdf_file_path = 'data/se_best_practices.pdf'
                        ,txt_file_path = 'data/se_best_practices.txt'
                        ):
    
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        with open(txt_file_path, 'w', encoding='utf-8') as output:
            # Iterate through each page in the PDF
            for page in reader.pages:
                text = page.extract_text()
                if text: 
                    output.write(text)
                output.write('\n') 

    return print(f'The text has been written to {txt_file_path}')
