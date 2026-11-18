import os
from docx import Document

base = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\200 lvl\First Semester'
courses = ['COS 201','ENT 211','IFT 203','IFT 205','IFT 211','INS 202','SEN 201']

for course in courses:
    course_path = os.path.join(base, course)
    if not os.path.isdir(course_path):
        continue
    for f in os.listdir(course_path):
        if f.lower().endswith('.docx'):
            fp = os.path.join(course_path, f)
            try:
                doc = Document(fp)
                out = []
                for para in doc.paragraphs:
                    if para.text.strip():
                        out.append(para.text.strip())
                stem = os.path.splitext(f)[0]
                outfile = os.path.join(course_path, stem + '_extracted.txt')
                with open(outfile, 'w', encoding='utf-8') as fout:
                    fout.write('\n'.join(out))
                print(f'OK: {course}/{f} -> {len(out)} paragraphs')
            except Exception as e:
                print(f'ERR: {course}/{f}: {e}')

print("DONE")
