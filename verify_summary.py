import json
import glob

idx = json.load(open('app/content/index.json', encoding='utf-8'))
print('=== ACTIVE TOPIC QUESTIONS IN APP INDEX ===')
grand_total = 0
for c in idx['courses']:
    print(f"{c['code']} - {c['title']}: {c['total_questions']} questions across {len(c['topics'])} topics")
    grand_total += c['total_questions']

print(f"\nTOTAL ACTIVE TOPIC QUESTIONS IN APP INDEX: {grand_total}")

mock_files = glob.glob('app/content/*/mock_exams.json')
total_mock_qs = 0
print('\n=== MOCK EXAMS ACROSS COURSES ===')
for mf in sorted(mock_files):
    m_data = json.load(open(mf, encoding='utf-8'))
    m_count = sum(len(m['questions']) for m in m_data)
    total_mock_qs += m_count
    print(f"{mf}: {len(m_data)} full mock exams, {m_count} questions")

print(f"\nTOTAL MOCK QUESTIONS GENERATED: {total_mock_qs}")

cheatsheets = glob.glob('app/content/*/cheatsheet.md')
print(f"\nTOTAL CHEATSHEETS GENERATED: {len(cheatsheets)}")
for cs in sorted(cheatsheets):
    print(f" - {cs}")

style_guides = glob.glob('app/content/*/STYLE_GUIDE.md')
print(f"\nTOTAL STYLE GUIDES GENERATED: {len(style_guides)}")
for sg in sorted(style_guides):
    print(f" - {sg}")
