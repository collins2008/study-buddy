import json
import os

EXAMINER_ENRICHMENTS = {
    # Boolean Algebra
    "ift211-ba-fc05": "In Boolean algebra, the OR operation distributes over AND: A + (B · C) = (A + B) · (A + C). This dual distributive law has no counterpart in standard real-number algebra and is a favorite Nile examination question. (Mano, Ch 2.2).",
    "ift211-ba-fc08": "The Consensus Theorem states that in an expression of the form AB + A'C + BC, the third term BC is completely redundant and can be deleted: AB + A'C + BC = AB + A'C. The dual form is (A + B)(A' + C)(B + C) = (A + B)(A' + C). (Mano, Ch 2.3).",

    # Combinational Circuits
    "ift211-cc-fc01": "A combinational circuit is a memoryless digital system whose output values at any instant depend solely on the present combination of input values, with no internal feedback loops or storage elements. (Mano, Ch 4.1).",
    "ift211-cc-fc02": "A half adder adds two 1-bit binary inputs (A and B) and produces two outputs: Sum S = A ⊕ B, and Carry C = A · B. It has no provision for an incoming carry bit from a previous stage. (Mano, Ch 4.3).",
    "ift211-cc-fc03": "A full adder adds three 1-bit binary inputs (A, B, and incoming carry Cin) to produce two outputs: Sum S = A ⊕ B ⊕ Cin, and Carry Out Cout = AB + Cin(A ⊕ B) = AB + BCin + ACin. (Mano, Ch 4.3).",
    "ift211-cc-fc04": "A half subtractor subtracts a 1-bit subtrahend Y from a 1-bit minuend X, yielding Difference D = X ⊕ Y and Borrow Bout = X' · Y. (Mano, Ch 4.4).",
    "ift211-cc-fc05": "A decoder is a combinational logic circuit that converts binary information from n input lines to a maximum of 2^n unique output lines, activating exactly one output corresponding to the input code minterm. (Mano, Ch 4.9).",
    "ift211-cc-fc06": "A multiplexer (MUX or data selector) directs binary information from one of 2^n input data lines to a single output line, controlled by the bit pattern on n selection lines. (Mano, Ch 4.11).",
    "ift211-cc-fc07": "Digital Integrated Circuits are classified by gate complexity: SSI (Small-Scale Integration, <10 gates), MSI (Medium-Scale Integration, 10-1,000 gates), LSI (Large-Scale Integration, 1,000-10,000 gates), and VLSI (Very Large-Scale Integration, >10,000 gates). (Mano, Ch 1.9).",

    # Karnaugh Maps
    "ift211-km-fc03": "A prime implicant is a product term obtained by combining the maximum possible number of adjacent squares (powers of 2: 1, 2, 4, 8, 16) in a K-map. An essential prime implicant is a prime implicant that covers at least one '1' not covered by any other prime implicant. (Mano, Ch 3.3).",
    "ift211-km-fc08": "The Quine-McCluskey tabular minimization algorithm is an exact, algebraic procedure that systematic finds all prime implicants and the minimal prime implicant cover, making it readily programmable on a digital computer for functions with >5 variables. (Mano, Ch 3.9).",

    # Logic Gates
    "ift211-lg-fc02": "A set of logic gates is functionally complete (universal) if any Boolean function can be constructed using only gates from that set. Both {NAND} alone and {NOR} alone are universally complete. (Mano, Ch 2.8).",
    "ift211-lg-fc05": "An XOR (Exclusive-OR) gate outputs logic 1 if and only if its two inputs are different (odd parity detector: 01 or 10 yields 1; 00 or 11 yields 0). Its output equation is Y = A ⊕ B = A'B + AB'. (Mano, Ch 2.7).",

    # Number Systems
    "ift211-ns-fc05": "Because 8 = 2^3, octal to binary conversion is performed by grouping binary bits into triplets (3 bits) from right to left for integers and left to right for fractions, transcribing each triplet directly to an octal digit without decimal division. (Mano, Ch 1.4).",
    "ift211-ns-fc06": "Because 16 = 2^4, hexadecimal to binary conversion maps each hexadecimal digit directly to a 4-bit nibble (e.g. A = 1010, F = 1111), eliminating intermediate decimal arithmetic. (Mano, Ch 1.4).",

    # Past Exam Synthesis
    "ift211-pe-fc01": "In Nile University examinations, binary addition requires explicit carry propagation: 44_10 = 00101100_2 and 14_10 = 00001110_2. Column addition yields 00111010_2, which equals 32 + 16 + 2 = 58_10, verifying 44 + 14 = 58. (Nile Final Exam 2024).",
    "ift211-pe-fc03": "In 1's complement subtraction (72 - 57), 72_10 = 1001000_2 and 57_10 = 0111001_2. The 1's complement of 57 is 1000110_2. Summing 1001000 + 1000110 = 10011110_2 generates an end-around carry of 1, which added to 0001110 yields 0001111_2 (= 15_10). (Nile Final Exam 2024).",
    "ift211-pe-fc04": "Decimal 51_10 converted to binary by successive division by 2 yields 110011_2 (32 + 16 + 2 + 1). Grouping binary 11011010_2 into nibbles: 1101_2 = D_16, 1010_2 = A_16, yielding DA_16. (Nile Final Exam 2024).",
    "ift211-pe-fc08": "Primary gates (AND, OR, NOT) perform fundamental logical operations. NAND and NOR are universal gates because de Morgan's theorem allows constructing NOT, AND, OR, and XOR entirely out of either NAND or NOR gates alone. (Nile Final Exam 2024)."
}

EXACT_WHY_WRONG_FIXES = {
    "ift211-ba-007": {
        "1": "Incorrectly attempts algebraic distribution and claims X · (X + Y) = X + Y, which violates Boolean laws.",
        "2": "Arbitrarily swaps and multiplies variables without applying valid Boolean postulates.",
        "3": "Violates the absorption identity X + XY = X."
    },
    "ift211-cc-005": {
        "1": "The circuit does not shut off power; it inverts the B bits using XOR and injects carry-in C0=1 to calculate 2's complement subtraction.",
        "2": "A parallel adder/subtractor performs binary addition and subtraction, not multiplication or division.",
        "3": "The circuit operates in binary two's complement, not decimal 9's complement BCD."
    },
    "ift211-km-006": {
        "1": "Don't-cares do not have to be covered. Grouping an X that contains no 1s creates redundant prime implicants and wastes hardware gates.",
        "2": "Treating X strictly as 0 forfeits simplification opportunities; grouping an X with 1s can double group size and eliminate variable literals.",
        "3": "Forcing all don't-cares to 0 produces a suboptimal circuit with more logic gates than necessary."
    },
    "ift211-km-007": {
        "1": "Quine-McCluskey is an exact minimization method, not an approximate heuristic.",
        "2": "Quine-McCluskey is a strictly digital tabular minimization algorithm, not an analog circuit method.",
        "3": "De Morgan's laws apply universally to any number of Boolean variables; the limitation of K-maps is visual/geometric complexity on 2D paper."
    },
    "ift211-lg-003": {
        "1": "2 NAND gates implement an AND gate (NAND followed by inverter); an OR gate requires inverting both inputs first ((A' · B')'), requiring 3 NAND gates.",
        "2": "A single NAND gate implements (AB)', which is NOT-AND, not OR.",
        "3": "4 NAND gates implement an XOR gate; an OR gate requires only 3 NAND gates."
    },
    "ift211-lg-004": {
        "1": "2 NOR gates implement an OR gate (NOR followed by inverter); an AND gate requires inverting both inputs first via NOR ((A' + B')'), requiring 3 NOR gates.",
        "2": "A single NOR gate implements (A + B)', which is NOT-OR, not AND.",
        "3": "4 NOR gates implement an XNOR gate; an AND gate requires only 3 NOR gates."
    },
    "ift211-pe-003": {
        "1": "In 1's complement arithmetic, an end-around carry MUST be added back into the LSB, not discarded. (Discarding carry is only valid in 2's complement).",
        "2": "1's complement of 57 (0111001_2) is 1000110_2, not 1000111_2 (which is 2's complement).",
        "3": "Arithmetic error during intermediate binary addition."
    },
    "ift211-pe-006": {
        "1": "10101 is the binary representation of 21, not its Gray code; Gray code requires XOR-ing adjacent bits, yielding 11111.",
        "2": "11010 is 26 in binary, not the Gray code of 21.",
        "3": "Converting 11101 Gray to binary yields 10110 (22_10), not 11001 (25_10)."
    },
    "ift211-pe-008": {
        "1": "XOR and XNOR are derived gates, not universal gates.",
        "2": "XOR and XNOR cannot alone synthesize inverter or AND operations, so they are not universal; NAND and NOR are the universal gates.",
        "3": "AND and OR are primary gates, not universal gates."
    }
}

def apply_ift211_fixes():
    import glob
    ift_dir = "app/content/IFT 211"
    files = sorted(glob.glob(os.path.join(ift_dir, "*.json")))
    
    updated_expl = 0
    updated_ww = 0
    
    id_map = {}
    
    for f in files:
        if "mock_exams" in f:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            
        modified = False
        for q in data.get("questions", []):
            qid = q.get("id")
            if qid in EXAMINER_ENRICHMENTS:
                q["explanation"] = EXAMINER_ENRICHMENTS[qid]
                updated_expl += 1
                modified = True
                
            if qid in EXACT_WHY_WRONG_FIXES:
                if "why_wrong" not in q:
                    q["why_wrong"] = {}
                for k, v in EXACT_WHY_WRONG_FIXES[qid].items():
                    q["why_wrong"][k] = v
                updated_ww += 1
                modified = True
                
            id_map[qid] = q
                
        if modified:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
                
    # Sync mock_exams.json
    mock_file = os.path.join(ift_dir, "mock_exams.json")
    if os.path.exists(mock_file):
        with open(mock_file, "r", encoding="utf-8") as fp:
            mdata = json.load(fp)
        synced = 0
        for exam in mdata.get("exams", []):
            for q in exam.get("questions", []):
                qid = q.get("id")
                if qid in id_map:
                    src = id_map[qid]
                    q["explanation"] = src["explanation"]
                    if "why_wrong" in src:
                        q["why_wrong"] = src["why_wrong"]
                    synced += 1
        with open(mock_file, "w", encoding="utf-8") as fp:
            json.dump(mdata, fp, indent=2, ensure_ascii=False)
        print(f"Synced {synced} questions into IFT 211 mock_exams.json")

    print(f"Applied {updated_expl} explanation enrichments and {updated_ww} why_wrong dictionary updates.")

if __name__ == "__main__":
    apply_ift211_fixes()
