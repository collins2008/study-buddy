# Topic Inventory: SEN 201 Topic 7 — Software Testing & Quality Assurance
**Topic Slug**: `software_testing_qa`
**Source Materials**:
- Nile University Final Exam Paper Type B (Questions 63, 64, 65, 66, 67, 68, 69, 70, 71)
- Software Engineering Concepts and Principles Lecture Notes (Testing, Verification & Validation)
- Lecturer Notebook Hints (Testing levels, QA metrics, black/white-box techniques)

---

## 1. Exam Past Questions Extracted
- **Exam Q63**: Validation testing — Demonstration that the software meets user requirements ("Are we building the right product?").
- **Exam Q64**: Static testing — Verification techniques that do NOT require executing code (reviews, walkthroughs, inspections, static analysis).
- **Exam Q65**: Release testing — Testing a specific release version intended for use outside the development organization.
- **Exam Q66**: Regression testing — Re-running previous tests to verify that new code changes or bug fixes have not broken existing functionality.
- **Exam Q67**: Stress testing — Subjecting a system to loads beyond its maximum design capacity to test failure modes and recovery.
- **Exam Q68**: Test-Driven Development (TDD) benefits — Reduced regression defects, rapid debugging feedback, better modularity, executable specification.
- **Exam Q69**: Acceptance / User testing — Customer tests system with real operational data to verify contractual and operational fitness.
- **Exam Q70**: Impossibility of exhaustive testing — Combinatorial explosion of input combinations, internal states, paths, and economic/time limits.
- **Exam Q71**: Performance testing — Assessing responsiveness, throughput, and resource utilization under specified workloads.

---

## 2. Exhaustive Concept Inventory

### A. Verification vs Validation (V&V)
- **Verification**: "Are we building the product right?" Checking that software conforms to its design specifications.
- **Validation**: "Are we building the right product?" Checking that software meets customer expectations and operational requirements (Exam Q63).

### B. Static vs Dynamic V&V
- **Static Testing (Exam Q64)**: Code reviews, automated linting, formal inspections, static taint analysis, mathematical proofs of correctness. Zero code execution.
- **Dynamic Testing**: Executing software with concrete test inputs and observing actual behavior vs expected behavior.

### C. Testing Hierarchy & Levels
1. **Unit Testing**: Testing individual components, functions, or classes in isolation (using stubs, mocks, fakes).
2. **Integration Testing**: Testing interactions and interfaces between integrated units (Big Bang vs Incremental: Top-Down, Bottom-Up, Sandwich).
3. **System Testing**: Testing the fully integrated application against system requirements.
4. **Release Testing (Exam Q65)**: Independent team validating a release candidate before external deployment.
5. **Acceptance Testing (Exam Q69)**: User/customer acceptance (Alpha testing with internal users, Beta testing with external users).

### D. Test Case Design Techniques
1. **Black-Box (Functional) Testing**:
   - *Equivalence Partitioning*: Dividing input domain into valid and invalid partitions where program is assumed to treat all elements equally.
   - *Boundary Value Analysis (BVA)*: Testing at boundaries of input domains (min, min+, nominal, max-, max), where errors cluster.
2. **White-Box (Structural) Testing**:
   - *Statement Coverage*: Percentage of executable statements executed.
   - *Branch / Decision Coverage*: Testing both True and False outcomes of all conditional branches.
   - *Cyclomatic Complexity (McCabe)*: $V(G) = E - N + 2P$ or $V(G) = \text{Predicates} + 1$. Determines the minimum number of linearly independent paths required for full coverage.

### E. Quality Assurance & Specialized Testing
- **Regression Testing (Exam Q66)**: Automated test suites executed upon every commit/build (CI/CD pipeline).
- **Stress Testing (Exam Q67)**: Pushing system beyond breaking point to ensure graceful degradation rather than catastrophic failure.
- **Performance & Load Testing (Exam Q71)**: Latency, throughput, transactions per second (TPS).
- **TDD (Test-Driven Development) Cycle (Exam Q68)**: Red (write failing test) -> Green (write minimal code to pass) -> Refactor (clean code).
- **Why Exhaustive Testing Is Impossible (Exam Q70)**: $2^{32}$ inputs for a single 32-bit integer; infinite combinations for complex systems.
