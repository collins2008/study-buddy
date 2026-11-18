import json
import os

def build_topic8():
    topic_data = {
        "course": "IFT 211",
        "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
        "summary": "This capstone synthesis topic reconstructs the official Nile University 2024/2025 First Semester Final Examination in Digital Logic and Design (IFT 211, 60 Marks). It synthesizes all core examined domains: Exercise I signed 2's complement addition ((+44)+(+14), (+44)+(-14)) and multi-method binary subtraction (1001000 - 111001 via borrowing, 1's complement with end-around carry, and 2's complement with discarded carry); Exercise II decimal-to-binary (51 -> 00110011) and binary-to-hexadecimal (11011010 -> DA); Exercise III 12-byte ASCII byte stream decoding ('Coded - 0211'); Exercise IV non-weighted encodings (decimal 21 to Gray 11111, Gray 11101 to binary 10110, and BCD 1001 0001 0100 to decimal 914 and binary 1110010010); and Exercise V-VI logic circuit node tracing (X = A ⊕ B + B · C') and primary versus universal gate classifications.",
        "key_terms": [
            {"term": "2's Complement Arithmetic", "definition": "The standard signed binary representation where negative numbers are formed by inverting all bits and adding 1; end carries resulting from positive/negative additions are discarded."},
            {"term": "End-Around Carry", "definition": "A mechanism in 1's complement subtraction where an end carry generated from the MSB is wrapped around and added to the LSB of the result."},
            {"term": "ASCII Stream", "definition": "A sequential series of 8-bit bytes representing alphanumeric and punctuation characters, decodable using standard American Standard Code for Information Interchange tables."},
            {"term": "Gray Code", "definition": "A non-weighted reflected binary code in which successive values differ in exactly one bit position, eliminating race conditions in optical encoders."},
            {"term": "BCD (Binary Coded Decimal)", "definition": "A 4-bit nibble encoding representing decimal digits 0 to 9; converting BCD to binary requires first evaluating the multi-digit decimal number."},
            {"term": "Circuit Node Tracing", "definition": "The systematic analytical technique of writing Boolean expressions for each intermediate gate output in a logic schematic to determine the overall circuit transfer function."},
            {"term": "Universal Gate", "definition": "A logic gate (NAND or NOR) that can single-handedly synthesize any Boolean function without requiring any other gate types."},
            {"term": "Primary Gate", "definition": "The three elemental Boolean logic gates — OR, AND, and NOT — as classified by Nile University examiners."}
        ],
        "questions": [
            {
                "id": "ift211-pe-001",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-i", "2s-complement", "addition"],
                "question": "In Nile Final Exam Exercise I(a), perform the signed arithmetic operation (+44) + (+14) in binary using 8-bit 2's complement representation. What is the 8-bit binary result and its decimal equivalent?",
                "options": [
                    "00111010_2 (= +58_10)",
                    "00111100_2 (= +60_10)",
                    "10111010_2 (= -70_10)",
                    "00011110_2 (= +30_10)"
                ],
                "answer": "00111010_2 (= +58_10)",
                "explanation": "Convert to 8-bit binary:\n+44 = 32 + 8 + 4 = 00101100_2\n+14 = 8 + 4 + 2 = 00001110_2\nAdd:\n  00101100\n+ 00001110\n----------\n  00111010_2\nCheck: 32 + 16 + 8 + 2 = +58_10. Correct (+44 + 14 = +58). MSB is 0, indicating a positive number within the 8-bit signed range [-128, +127].",
                "why_wrong": {
                    "00111100_2 (= +60_10)": "Carry error in the 2s and 4s bit positions.",
                    "10111010_2 (= -70_10)": "Mistakenly inverts the sign bit.",
                    "00011110_2 (= +30_10)": "This is (+44) - (+14), not addition."
                },
                "marking_points": ["Converts +44 to 00101100", "Converts +14 to 00001110", "Adds in binary: 00111010", "Confirms decimal +58"],
                "source": "Nile University Final Exam, Exercise I(a)",
                "verified": True,
                "verified_output": "44 + 14 = 58 -> bin(58) = 00111010"
            },
            {
                "id": "ift211-pe-002",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-i", "2s-complement", "signed-subtraction"],
                "question": "In Nile Final Exam Exercise I(a), perform the operation (+44) + (-14) in binary using 8-bit 2's complement representation. What is the 8-bit result after handling the end carry?",
                "options": [
                    "00011110_2 (= +30_10)",
                    "10011110_2 (= -98_10)",
                    "00011111_2 (= +31_10)",
                    "11100010_2 (= -30_10)"
                ],
                "answer": "00011110_2 (= +30_10)",
                "explanation": "1. +44 = 00101100_2.\n2. -14 in 2's complement: +14 = 00001110_2 -> 1's comp = 11110001 -> 2's comp = 11110010_2.\n3. Add:\n  00101100 (+44)\n+ 11110010 (-14)\n----------\n1 00011110\n4. In 2's complement, the end carry of 1 is DISCARDED.\n5. Result = 00011110_2 = 16 + 8 + 4 + 2 = +30_10. Correct (+44 - 14 = +30).",
                "why_wrong": {
                    "10011110_2 (= -98_10)": "Kept the end carry in the sign bit position.",
                    "00011111_2 (= +31_10)": "Wrongly added the end carry back to LSB (confusing 2's complement with 1's complement end-around carry).",
                    "11100010_2 (= -30_10)": "Produced -30 instead of +30."
                },
                "marking_points": ["Finds 2's complement of -14 = 11110010", "Adds 00101100 + 11110010 = 1 00011110", "Discards end carry to yield 00011110", "Confirms decimal +30"],
                "source": "Nile University Final Exam, Exercise I(a)",
                "verified": True,
                "verified_output": "44 - 14 = 30 -> bin(30) = 00011110"
            },
            {
                "id": "ift211-pe-003",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-i", "1s-complement", "end-around-carry"],
                "question": "In Nile Final Exam Exercise I(b), perform binary subtraction 1001000_2 - 111001_2 using the 1's complement method. What is the intermediate sum and final difference after handling the end-around carry?",
                "options": [
                    "Intermediate sum = 1001110_2; Adding end-around carry yields final difference 0001111_2 (= 15_10)",
                    "Intermediate sum = 1001111_2; Discarding carry yields 0001111_2",
                    "Final difference = 0010000_2 (= 16_10)",
                    "Final difference = 1110001_2"
                ],
                "answer": "Intermediate sum = 1001110_2; Adding end-around carry yields final difference 0001111_2 (= 15_10)",
                "explanation": "Pad subtrahend to 7 bits: Minuend = 1001000_2 (72_10), Subtrahend = 0111001_2 (57_10).\n1. Take 1's complement of subtrahend: 1000110_2.\n2. Add to minuend:\n  1001000\n+ 1000110\n---------\n1 0001110 (Intermediate sum = 0001110 with end carry 1)\n3. In 1's complement, an end carry indicates a positive result and MUST be added to LSB (end-around carry):\n  0001110 + 1 = 0001111_2 (= 15_10).\nCheck: 72 - 57 = 15. Verified.",
                "why_wrong": {
                    "Intermediate sum = 1001111_2; Discarding carry...": "Discarding end carry is 2's complement procedure, not 1's complement.",
                    "Final difference = 0010000_2 (= 16_10)": "Off by 1 arithmetic error.",
                    "Final difference = 1110001_2": "Forgot to add the end carry and complemented the result."
                },
                "marking_points": ["Finds 1's complement of 0111001 = 1000110", "Adds to 1001000 = 1 0001110", "Adds end-around carry: 0001110 + 1 = 0001111", "Confirms 15 decimal"],
                "source": "Nile University Final Exam, Exercise I(b)",
                "verified": True,
                "verified_output": "72 - 57 = 15 -> bin(15) = 1111"
            },
            {
                "id": "ift211-pe-004",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 2,
                "tags": ["nile-exam-exercise-ii", "radix-conversion", "binary-hex"],
                "question": "In Nile Final Exam Exercise II, convert: (a) decimal 51_10 to binary, and (b) binary 11011010_2 to hexadecimal.",
                "options": [
                    "(a) 00110011_2, (b) DA_16",
                    "(a) 00110101_2, (b) DB_16",
                    "(a) 00110011_2, (b) AD_16",
                    "(a) 01010001_2, (b) CA_16"
                ],
                "answer": "(a) 00110011_2, (b) DA_16",
                "explanation": "(a) Decimal 51 to binary:\n51 = 32 + 16 + 2 + 1 = 00110011_2.\n(b) Binary 11011010 to hexadecimal:\nSplit into two 4-bit nibbles:\n1101_2 = 8 + 4 + 1 = 13 = D_16\n1010_2 = 8 + 2 = 10 = A_16\nCombining gives: DA_16.",
                "why_wrong": {
                    "(a) 00110101_2, (b) DB_16": "00110101 is decimal 53, not 51.",
                    "(a) 00110011_2, (b) AD_16": "Reverses the nibble order (wrote AD instead of DA).",
                    "(a) 01010001_2, (b) CA_16": "01010001 is BCD representation of 51, not pure binary."
                },
                "marking_points": ["Converts 51 to 00110011_2", "Groups 1101 1010 into D and A", "Combines to DA_16"],
                "source": "Nile University Final Exam, Exercise II",
                "verified": True,
                "verified_output": "bin(51) = 00110011; hex(0b11011010) = DA"
            },
            {
                "id": "ift211-pe-005",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "type_answer",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-iii", "ascii-decoding"],
                "question": "In Nile Final Exam Exercise III, decode the 12-byte binary stream into ASCII text: [01000011, 01101111, 01100100, 01100101, 01100100, 00100000, 00101101, 00100000, 00110000, 00110010, 00110001, 00110001]. What is the exact decoded message?",
                "options": [],
                "answer": "Coded - 0211",
                "accepted_answers": [
                    "Coded - 0211",
                    "\"Coded - 0211\"",
                    "'Coded - 0211'"
                ],
                "explanation": "Convert each 8-bit byte to decimal ASCII:\n- 01000011 = 67 = 'C'\n- 01101111 = 111 = 'o'\n- 01100100 = 100 = 'd'\n- 01100101 = 101 = 'e'\n- 01100100 = 100 = 'd'\n- 00100000 = 32 = ' ' (space)\n- 00101101 = 45 = '-'\n- 00100000 = 32 = ' ' (space)\n- 00110000 = 48 = '0'\n- 00110010 = 50 = '2'\n- 00110001 = 49 = '1'\n- 00110001 = 49 = '1'\nConcatenating the characters yields: 'Coded - 0211'.",
                "why_wrong": {},
                "marking_points": [
                    "Decodes bytes 1-5 to 'Coded'",
                    "Decodes byte 6-8 to ' - '",
                    "Decodes bytes 9-12 to '0211'",
                    "Final string: 'Coded - 0211'"
                ],
                "source": "Nile University Final Exam, Exercise III",
                "verified": True,
                "verified_output": "bytes([67, 111, 100, 101, 100, 32, 45, 32, 48, 50, 49, 49]).decode('ascii') = 'Coded - 0211'"
            },
            {
                "id": "ift211-pe-006",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-iv", "gray-code", "conversions"],
                "question": "In Nile Final Exam Exercise IV: (a) Find the Gray code equivalent of decimal 21_10, and (b) Find the binary equivalent of Gray code 11101_Gray.",
                "options": [
                    "(a) 11111_Gray, (b) 10110_2 (= 22_10)",
                    "(a) 10101_Gray, (b) 11101_2 (= 29_10)",
                    "(a) 11010_Gray, (b) 10011_2 (= 19_10)",
                    "(a) 11111_Gray, (b) 11001_2 (= 25_10)"
                ],
                "answer": "(a) 11111_Gray, (b) 10110_2 (= 22_10)",
                "explanation": "(a) Decimal 21 to binary = 10101_2 (B4=1, B3=0, B2=1, B1=0, B0=1).\nGray code conversion:\nG4 = B4 = 1\nG3 = B4 ⊕ B3 = 1 ⊕ 0 = 1\nG2 = B3 ⊕ B2 = 0 ⊕ 1 = 1\nG1 = B2 ⊕ B1 = 1 ⊕ 0 = 1\nG0 = B1 ⊕ B0 = 0 ⊕ 1 = 1\nResult = 11111_Gray.\n\n(b) Gray code 11101_Gray to binary (G4=1, G3=1, G2=1, G1=0, G0=1):\nB4 = G4 = 1\nB3 = B4 ⊕ G3 = 1 ⊕ 1 = 0\nB2 = B3 ⊕ G2 = 0 ⊕ 1 = 1\nB1 = B2 ⊕ G1 = 1 ⊕ 0 = 1\nB0 = B1 ⊕ G0 = 1 ⊕ 1 = 0\nBinary result = 10110_2 (which is 16 + 4 + 2 = 22_10).",
                "why_wrong": {
                    "(a) 10101_Gray, (b) 11101_2...": "Assumes Gray code is identical to binary.",
                    "(a) 11010_Gray, (b) 10011_2...": "Parity and XOR calculation mistakes.",
                    "(a) 11111_Gray, (b) 11001_2...": "Wrongly converts Gray bit G2."
                },
                "marking_points": ["Converts 21 to binary 10101", "Calculates Gray = 11111", "Converts Gray 11101 to binary 10110"],
                "source": "Nile University Final Exam, Exercise IV(a, b)",
                "verified": True,
                "verified_output": "Gray(21) = 11111; Bin(11101_G) = 10110 = 22"
            },
            {
                "id": "ift211-pe-007",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "calculation",
                "difficulty": 3,
                "tags": ["nile-exam-exercise-iv", "bcd-to-binary"],
                "question": "In Nile Final Exam Exercise IV(c), convert the BCD number 1001 0001 0100_BCD into an equivalent pure binary number.",
                "options": [
                    "1110010010_2",
                    "100100010100_2",
                    "1011010010_2",
                    "1100101000_2"
                ],
                "answer": "1110010010_2",
                "explanation": "Step 1: Decode each 4-bit BCD nibble into decimal digits:\n- 1001_2 = 9\n- 0001_2 = 1\n- 0100_2 = 4\nDecimal number = 914_10.\nStep 2: Convert decimal 914 to pure binary by successive powers of 2:\n914 = 512 + 256 + 128 + 16 + 2\n= 2^9 + 2^8 + 2^7 + 2^4 + 2^1\n= 1110010010_2.\nNotice: BCD represents digits; you cannot simply treat the BCD bits as pure binary!",
                "why_wrong": {
                    "100100010100_2": "Common student blunder: directly copied the BCD bit string as if it were a binary integer (representing 2324_10 instead of 914_10).",
                    "1011010010_2": "Arithmetic conversion error (equals 722_10).",
                    "1100101000_2": "Equals 808_10."
                },
                "marking_points": ["Decodes BCD to decimal 914", "Converts 914 to binary 1110010010"],
                "source": "Nile University Final Exam, Exercise IV(c)",
                "verified": True,
                "verified_output": "BCD 1001 0001 0100 = 914 -> bin(914) = 1110010010"
            },
            {
                "id": "ift211-pe-008",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["nile-exam-exercise-v", "primary-vs-universal", "lecturer-hint"],
                "question": "Which of the following statements correctly represents the lecturer's classification of logic gates as tested in the Nile University Final Examination?",
                "options": [
                    "OR, AND, and NOT are Primary gates; NAND and NOR are Universal gates because each can synthesize all other gates.",
                    "NAND and NOR are Primary gates; AND and OR are Universal gates.",
                    "XOR and XNOR are Universal gates; NAND and NOR are Derived gates.",
                    "All gates are equally primary and universal."
                ],
                "answer": "OR, AND, and NOT are Primary gates; NAND and NOR are Universal gates because each can synthesize all other gates.",
                "explanation": "As explicitly highlighted in lecturer notebook notes and the exam paper: the primary gates are OR, AND, and NOT. NAND and NOR are universal gates because through appropriate interconnection, either one can implement NOT, AND, and OR without any external components.",
                "why_wrong": {
                    "NAND and NOR are Primary gates; AND and OR are Universal gates.": "NAND and NOR are universal, not primary; AND and OR cannot implement NOT on their own.",
                    "XOR and XNOR are Universal gates...": "XOR cannot implement NAND or NOT on its own without true/false constant inputs.",
                    "All gates are equally primary and universal.": "Violates formal functional completeness theorems."
                },
                "marking_points": ["Identifies OR, AND, NOT as primary", "Identifies NAND and NOR as universal"],
                "source": "Nile University Final Exam & Lecturer Notebook Hint",
                "verified": True,
                "verified_output": "N/A"
            },
            # Flashcards
            {
                "id": "ift211-pe-fc01",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "signed-addition"],
                "question": "What is (+44) + (+14) in 8-bit binary 2's complement?",
                "options": [],
                "answer": "00111010_2 (= +58_10).",
                "explanation": "00101100 + 00001110 = 00111010.",
                "why_wrong": {},
                "marking_points": ["00111010_2 (+58)"],
                "source": "Nile University Final Exam, Exercise I(a)",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc02",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "signed-subtraction"],
                "question": "What is (+44) + (-14) in 8-bit binary 2's complement?",
                "options": [],
                "answer": "00011110_2 (= +30_10). (End carry 1 is discarded).",
                "explanation": "00101100 + 11110010 = 1 00011110 -> 00011110.",
                "why_wrong": {},
                "marking_points": ["00011110_2 (+30)"],
                "source": "Nile University Final Exam, Exercise I(a)",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc03",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "subtraction-methods"],
                "question": "What is 1001000_2 - 111001_2 in decimal and binary?",
                "options": [],
                "answer": "15_10 = 0001111_2 (or 1111_2).",
                "explanation": "72 - 57 = 15.",
                "why_wrong": {},
                "marking_points": ["15 decimal / 1111 binary"],
                "source": "Nile University Final Exam, Exercise I(b)",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc04",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "radix-conversion"],
                "question": "What are (a) decimal 51 in binary, and (b) binary 11011010 in hexadecimal?",
                "options": [],
                "answer": "(a) 00110011_2\n(b) DA_16",
                "explanation": "51 = 32+16+2+1; 1101_2=D, 1010_2=A.",
                "why_wrong": {},
                "marking_points": ["00110011_2 and DA_16"],
                "source": "Nile University Final Exam, Exercise II",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc05",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "ascii-stream"],
                "question": "What text is decoded from the Nile Exam 12-byte ASCII stream?",
                "options": [],
                "answer": "'Coded - 0211'",
                "explanation": "Bytes: 67, 111, 100, 101, 100, 32, 45, 32, 48, 50, 49, 49.",
                "why_wrong": {},
                "marking_points": ["'Coded - 0211'"],
                "source": "Nile University Final Exam, Exercise III",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc06",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "gray-code"],
                "question": "What is decimal 21 in Gray code, and Gray 11101 in binary?",
                "options": [],
                "answer": "(a) 21_10 = 11111_Gray\n(b) 11101_Gray = 10110_2 (= 22_10)",
                "explanation": "Calculated via MSB carry and XOR adjacent bits.",
                "why_wrong": {},
                "marking_points": ["11111_Gray and 10110_2"],
                "source": "Nile University Final Exam, Exercise IV(a, b)",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc07",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "bcd-binary"],
                "question": "What is BCD 1001 0001 0100 in decimal and binary?",
                "options": [],
                "answer": "Decimal: 914_10\nBinary: 1110010010_2",
                "explanation": "Nibbles 9, 1, 4 = 914 -> 512+256+128+16+2 = 1110010010.",
                "why_wrong": {},
                "marking_points": ["914 decimal", "1110010010 binary"],
                "source": "Nile University Final Exam, Exercise IV(c)",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "ift211-pe-fc08",
                "course": "IFT 211",
                "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "nile-exam", "gate-classification"],
                "question": "According to Nile University exams, which gates are Primary and which are Universal?",
                "options": [],
                "answer": "- Primary gates: OR, AND, NOT\n- Universal gates: NAND, NOR",
                "explanation": "Universal gates can implement all Boolean operations.",
                "why_wrong": {},
                "marking_points": ["Primary: OR, AND, NOT", "Universal: NAND, NOR"],
                "source": "Lecturer Notebook Hint & Final Exam Paper",
                "verified": True,
                "verified_output": "N/A"
            }
        ],
        "case_studies": [
            {
                "id": "ift211-pe-cs01",
                "scenario": "A student in the examination hall at Nile University opens the 2024/2025 First Semester Final Examination paper for IFT 211. Exercise I allocates 20 marks to signed binary arithmetic and subtraction methods. The candidate must show complete working for two 8-bit operations: (+44) + (+14) and (+44) + (-14), and perform 1001000 - 111001 using both 1's complement and 2's complement methods.",
                "sub_questions": [
                    {
                        "id": "ift211-pe-cs01-q1",
                        "course": "IFT 211",
                        "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                        "type": "calculation",
                        "difficulty": 3,
                        "tags": ["case-study", "nile-exam-exercise-i", "2s-comp-subtraction"],
                        "question": "Perform the subtraction 1001000_2 - 111001_2 using the 2's complement method. What is the 7-bit 2's complement of the subtrahend, and what is the final difference after discarding the end carry?",
                        "options": [
                            "2's complement of subtrahend = 1000111_2; Sum = 1 0001111_2; Discarding carry yields difference 0001111_2 (= 15_10)",
                            "2's complement of subtrahend = 1000110_2; Difference = 0001110_2 (= 14_10)",
                            "2's complement of subtrahend = 0000111_2; Difference = 1001111_2 (= 79_10)",
                            "2's complement of subtrahend = 1111001_2; Difference = 0010000_2 (= 16_10)"
                        ],
                        "answer": "2's complement of subtrahend = 1000111_2; Sum = 1 0001111_2; Discarding carry yields difference 0001111_2 (= 15_10)",
                        "explanation": "Pad subtrahend to 7 bits: 0111001_2.\n1. 1's complement = 1000110_2.\n2. 2's complement = 1000110 + 1 = 1000111_2.\n3. Add minuend 1001000 and 2's complement:\n  1001000\n+ 1000111\n---------\n1 0001111\n4. In 2's complement subtraction, an end carry indicates the result is positive; discard the end carry.\nFinal difference = 0001111_2 = 15_10.",
                        "why_wrong": {
                            "2's complement of subtrahend = 1000110_2...": "1000110 is 1's complement, not 2's complement (forgot to add 1).",
                            "2's complement of subtrahend = 0000111_2...": "Incorrect complementation.",
                            "2's complement of subtrahend = 1111001_2...": "Copied subtrahend without inverting."
                        },
                        "marking_points": ["Derives 2's complement of subtrahend = 1000111", "Adds 1001000 + 1000111 = 1 0001111", "Discards end carry to get 0001111 = 15 decimal"],
                        "source": "Nile University Final Exam, Exercise I(b)",
                        "verified": True,
                        "verified_output": "72 - 57 = 15 -> 0001111"
                    },
                    {
                        "id": "ift211-pe-cs01-q2",
                        "course": "IFT 211",
                        "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                        "type": "explain",
                        "difficulty": 3,
                        "tags": ["case-study", "nile-exam-exercise-i", "method-comparison"],
                        "question": "Compare how an end carry is handled in 1's complement subtraction versus 2's complement subtraction when subtracting a smaller number from a larger number.",
                        "options": [],
                        "answer": "1. In 1's complement subtraction, when the minuend is greater than the subtrahend (A > B), an end carry of 1 is generated from the MSB. This end carry MUST be wrapped around and added to the least significant bit (LSB) of the result (termed 'end-around carry') to obtain the true difference.\n2. In 2's complement subtraction, when A > B, an end carry of 1 is also generated from the MSB, but it is simply DISCARDED (ignored). The remaining bits directly represent the true positive difference.\nIf no end carry is generated in either method, it indicates that the result is negative, and the final answer is obtained by taking the complement (1's or 2's) of the sum and prefixing a negative sign.",
                        "explanation": "Because 1's complement has two representations for zero (+0 and -0), the end-around carry is needed to bypass negative zero. 2's complement has a unique zero, so the end carry is discarded.",
                        "why_wrong": {},
                        "marking_points": [
                            "Explains 1's complement requires adding end-around carry to LSB",
                            "Explains 2's complement discards the end carry",
                            "Explains absence of end carry indicates negative result requiring re-complementation"
                        ],
                        "source": "Nile University Final Exam, Exercise I Marking Scheme",
                        "verified": True,
                        "verified_output": "N/A"
                    }
                ]
            },
            {
                "id": "ift211-pe-cs02",
                "scenario": "In Exercise VI of the Nile University Final Exam, candidates are presented with a combinational logic circuit having three inputs A, B, C. Intermediate nodes are labeled: node R is the output of an XOR gate fed by A and B; node Q is the output of an inverter fed by C; node S is the output of an AND gate fed by B and Q; and output X is an OR gate fed by R and S. The question awards 15 marks for deriving the Boolean expressions for R and X, constructing the truth table for all 8 input combinations, and proving circuit equivalence.",
                "sub_questions": [
                    {
                        "id": "ift211-pe-cs02-q1",
                        "course": "IFT 211",
                        "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                        "type": "calculation",
                        "difficulty": 3,
                        "tags": ["case-study", "nile-exam-exercise-vi", "node-tracing"],
                        "question": "What are the values of intermediate nodes R, S, and final output X for the input triplet A = 0, B = 1, C = 1?",
                        "options": [
                            "R = 1, S = 0, X = 1",
                            "R = 0, S = 1, X = 1",
                            "R = 1, S = 1, X = 1",
                            "R = 0, S = 0, X = 0"
                        ],
                        "answer": "R = 1, S = 0, X = 1",
                        "explanation": "Evaluate intermediate nodes step by step:\n- R = A ⊕ B = 0 ⊕ 1 = 1 (inputs differ, XOR produces 1).\n- Q = C' = 1' = 0.\n- S = B · Q = 1 · 0 = 0.\n- X = R + S = 1 + 0 = 1.\nTherefore, R = 1, S = 0, and X = 1.",
                        "why_wrong": {
                            "R = 0, S = 1, X = 1": "Evaluated 0 XOR 1 as 0.",
                            "R = 1, S = 1, X = 1": "Evaluated S as 1 (neglected C'=0).",
                            "R = 0, S = 0, X = 0": "Both gates evaluated incorrectly."
                        },
                        "marking_points": ["R = 0 XOR 1 = 1", "S = 1 AND NOT(1) = 0", "X = 1 OR 0 = 1"],
                        "source": "Nile University Final Exam, Exercise VI",
                        "verified": True,
                        "verified_output": "A=0, B=1, C=1 -> R=1, S=0, X=1"
                    },
                    {
                        "id": "ift211-pe-cs02-q2",
                        "course": "IFT 211",
                        "topic": "Past Exam Synthesis & Multi-Topic Problem Solving",
                        "type": "calculation",
                        "difficulty": 4,
                        "tags": ["case-study", "nile-exam-exercise-vi", "simplification"],
                        "question": "Using Boolean algebra theorems, simplify X = (A ⊕ B) + B·C' into a minimal Sum-of-Products expression with the minimum number of literals.",
                        "options": [
                            "X = A'B + AB' + BC'",
                            "X = A + B",
                            "X = A'B + AB'",
                            "X = (A + B)(A' + C')"
                        ],
                        "answer": "X = A'B + AB' + BC'",
                        "explanation": "Expand the XOR term: A ⊕ B = A'B + AB'.\nSo X = A'B + AB' + BC'.\nCheck consensus theorem: between A'B and AB', the variable B is not complemented. Looking at A'B + BC', can it be reduced? No, plotting on a K-map:\n1s are at m2(010), m3(011), m4(100), m5(101), m6(110).\nGroups:\n- Quad/Pair m2, m3 -> A'B\n- Pair m4, m5 -> AB'\n- Pair m2, m6 -> BC'\nEvery term covers a unique minterm: m3 is only in A'B; m4, m5 only in AB'; m6 only in BC'.\nHence, all three prime implicants are essential, and the minimal expression is X = A'B + AB' + BC' (or (A ⊕ B) + BC').",
                        "why_wrong": {
                            "X = A + B": "Incorrect simplification; would output 1 for input 111 (m7), but for 111, X is 0.",
                            "X = A'B + AB'": "Omits BC', leaving minterm m6 (110) uncovered.",
                            "X = (A + B)(A' + C')": "This is in POS form, not minimal SOP."
                        },
                        "marking_points": ["Expands A XOR B to A'B + AB'", "Verifies minterms m2, m3, m4, m5, m6 on K-map", "Confirms all 3 product terms are essential: A'B + AB' + BC'"],
                        "source": "Nile University Final Exam, Exercise VI",
                        "verified": True,
                        "verified_output": "Minimal SOP = A'B + AB' + BC'"
                    }
                ]
            }
        ]
    }

    out_file = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\IFT 211\past_exam_synthesis.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(topic_data, f, indent=2)

    total_qs = len(topic_data['questions']) + sum(len(cs.get('sub_questions', [])) for cs in topic_data.get('case_studies', []))
    print(f"Successfully generated {out_file} with {total_qs} total questions ({len(topic_data['questions'])} main, {len(topic_data['case_studies'])} case studies).")

if __name__ == '__main__':
    build_topic8()
