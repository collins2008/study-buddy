import os
from pptx import Presentation
from pdfminer.high_level import extract_text

base = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\200 lvl\First Semester'
courses = ['COS 201','ENT 211','IFT 203','IFT 205','IFT 211','INS 202','SEN 201']

# Extract newly converted PPTX (INS 202)
for course in ['INS 202']:
    course_path = os.path.join(base, course)
    for f in os.listdir(course_path):
        if f.lower().endswith('.pptx'):
            fp = os.path.join(course_path, f)
            try:
                prs = Presentation(fp)
                out = []
                for i, slide in enumerate(prs.slides):
                    slide_text = []
                    for shape in slide.shapes:
                        if hasattr(shape, 'text') and shape.text.strip():
                            slide_text.append(shape.text.strip())
                    if slide_text:
                        out.append(f'=== SLIDE {i+1} ===')
                        out.extend(slide_text)
                stem = os.path.splitext(f)[0]
                outfile = os.path.join(course_path, stem + '_extracted.txt')
                with open(outfile, 'w', encoding='utf-8') as fout:
                    fout.write('\n'.join(out))
                print(f'OK PPTX: {course}/{f} -> {len(prs.slides)} slides')
            except Exception as e:
                print(f'ERR: {course}/{f}: {e}')

# Extract all PDFs
for course in courses:
    course_path = os.path.join(base, course)
    if not os.path.isdir(course_path):
        continue
    for f in os.listdir(course_path):
        if f.lower().endswith('.pdf'):
            fp = os.path.join(course_path, f)
            try:
                text = extract_text(fp)
                if text and text.strip():
                    stem = os.path.splitext(f)[0]
                    outfile = os.path.join(course_path, stem + '_extracted.txt')
                    with open(outfile, 'w', encoding='utf-8') as fout:
                        fout.write(text)
                    wc = len(text.split())
                    print(f'OK PDF: {course}/{f} -> {wc} words')
                else:
                    print(f'EMPTY PDF (likely scanned image): {course}/{f}')
            except Exception as e:
                print(f'ERR PDF: {course}/{f}: {e}')

print("ALL DONE")
