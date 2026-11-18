import os, sys

base = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\200 lvl\First Semester'

try:
    from pptx import Presentation
    HAS_PPTX = True
except ImportError:
    HAS_PPTX = False
    print("WARNING: python-pptx not available")

courses = ['COS 201','ENT 211','IFT 203','IFT 205','IFT 211','INS 202','SEN 201']

for course in courses:
    course_path = os.path.join(base, course)
    if not os.path.isdir(course_path):
        continue
    all_files = os.listdir(course_path)
    pptx_files = [f for f in all_files if f.lower().endswith('.pptx')]
    ppt_files  = [f for f in all_files if f.lower().endswith('.ppt') and not f.lower().endswith('.pptx')]
    
    if HAS_PPTX:
        for pf in pptx_files:
            try:
                prs = Presentation(os.path.join(course_path, pf))
                out = []
                for i, slide in enumerate(prs.slides):
                    slide_text = []
                    for shape in slide.shapes:
                        if hasattr(shape, 'text') and shape.text.strip():
                            slide_text.append(shape.text.strip())
                    if slide_text:
                        out.append(f'=== SLIDE {i+1} ===')
                        out.extend(slide_text)
                stem = os.path.splitext(pf)[0]
                outfile = os.path.join(course_path, stem + '_extracted.txt')
                with open(outfile, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(out))
                print(f'OK: {course}/{pf} -> {len(prs.slides)} slides')
            except Exception as e:
                print(f'ERR: {course}/{pf}: {e}')
    
    # PPT files (old format) - try via pptx too
    if HAS_PPTX:
        for pf in ppt_files:
            try:
                prs = Presentation(os.path.join(course_path, pf))
                out = []
                for i, slide in enumerate(prs.slides):
                    slide_text = []
                    for shape in slide.shapes:
                        if hasattr(shape, 'text') and shape.text.strip():
                            slide_text.append(shape.text.strip())
                    if slide_text:
                        out.append(f'=== SLIDE {i+1} ===')
                        out.extend(slide_text)
                stem = os.path.splitext(pf)[0]
                outfile = os.path.join(course_path, stem + '_extracted.txt')
                with open(outfile, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(out))
                print(f'OK: {course}/{pf} -> {len(prs.slides)} slides')
            except Exception as e:
                print(f'ERR: {course}/{pf}: {e}')

print("DONE")
