# Exhaustive Inventory: Topic 2 — Interaction vs Interface & Design Principles
*Course: INS 202 (Human-Computer Interaction) — Nile University of Nigeria*
*Source Materials: Module_01 (Slide 13), Module_02 (Slides 44–56), Gerard Jounghyun Kim Textbook, Student Notebook*

---

## 1. Interaction vs Interface (High-Priority Student Notebook Signal)
- **Interaction**: An abstract, conceptual model by which a human user interacts with a computing device to accomplish a given task. Represents the behavioral dialogue, mental exchanges, task workflows, and cognitive problem-solving sequence between user and machine.
- **Interface**: The concrete technological and physical realization (hardware and/or software) of a given interaction model. Consists of input/output mechanisms, display layouts, physical buttons, touch glass, graphical widgets, typography, and sound effects that make the interaction tangible.
- **The "I" in HCI**: Encompasses both the abstract interaction model and the technological interface methodology.
- **Relationship**: The identical abstract *interaction* (e.g., selecting an item from a list or deleting an unwanted record) can be realized through radically different physical *interfaces* (e.g. typing a terminal command `rm file.txt` vs dragging a file icon into a desktop Trash can vs swiping left on a mobile touch screen vs issuing a voice command "Delete file").

---

## 2. Don Norman's Interaction Design Principles
1. **Visibility**:
   - The degree to which the system state, available functions, and navigation paths are perceptible to the user.
   - If a feature is invisible, users will not know it exists or how to invoke it.
2. **Feedback**:
   - Sending clear, instantaneous information back to the user confirming what action has occurred and what result has been accomplished.
   - Modalities: Visual (button depression state, spinning spinner, checkmark), Auditory (click tone, chime), Haptic (vibration rumble).
3. **Constraints**:
   - Limiting the user's possible actions at any given state to prevent errors and guide valid behavior.
   - Types of Constraints:
     - *Physical Constraints*: Shape, size, and orientation preventing improper assembly (e.g. USB key shape, SIM card notch).
     - *Logical Constraints*: Using reasoning and spatial logic to narrow options (graying out or disabling irrelevant menu items, date picker disallowing past return dates).
     - *Cultural Constraints*: Conventions learned through social immersion (red = danger/stop, green = go/safe; reading left-to-right).
     - *Semantic Constraints*: Relying on situational meaning and real-world domain knowledge.
4. **Mapping**:
   - The spatial and conceptual relationship between the layout of physical controls and their corresponding effects in the real world.
   - *Natural Mapping*: Physical analogies or spatial correspondence (e.g. four stove control knobs arranged in the identical spatial geometry as the four cooking burners; turning a steering wheel right turns the car right).
5. **Consistency**:
   - Designing interfaces so that similar tasks use similar operations, terminology, icons, and visual layouts.
   - *Internal Consistency*: Maintaining uniform visual language, typography, and behavior across all pages/screens within the same application.
   - *External Consistency*: Conforming to established industry, operating system, and web platform conventions (e.g. underlined blue text for links, Ctrl+C for copy, magnifying glass for search).
6. **Affordances & Signifiers**:
   - *Affordance (Gibson / Norman)*: The actual and perceived physical properties of an object that determine how it could possibly be used (a flat horizontal surface affords sitting on; a door handle affords pulling; a flat push-plate affords pushing).
   - *Perceived Affordance*: What the user perceives an object can do (a 3D shaded box appears clickable).
   - *Signifiers*: Visible marks, sounds, or visual cues that explicitly communicate *where* and *how* an action should occur (e.g., the word "PUSH" stamped on a brass door plate; a cursor changing to a pointing hand over a link).

---

## 3. Interaction Styles (Shneiderman & Gerard Kim)
1. **Direct Manipulation**:
   - Core Principles (Ben Shneiderman):
     1. Continuous visual representation of the objects and actions of interest.
     2. Physical actions or labeled button presses instead of complex syntax.
     3. Rapid, incremental, and reversible operations whose impact on the object of interest is immediately visible.
   - *Examples*: Drag-and-drop file organization, pinch-to-zoom on photos, resizing windows with a cursor.
2. **Menu Selection**:
   - Users choose from a structured list of options (drop-downs, radio buttons, navigation bars). Eliminates recall, enforces recognition, bounds errors, but can become cumbersome if menus are deeply nested.
3. **Form Fill-in**:
   - Structured data entry fields for capturing categorized user information. Requires clear field labels, logical tab ordering, inline validation, and input format masks.
4. **Command Language (CLI)**:
   - Users type exact alphanumeric instructions. High power, minimal screen real estate, scriptable, but requires high recall memory and training.
5. **Conversational / Natural Language**:
   - Interacting through typed text or spoken dialogue (chatbots, Siri, Alexa). Intuitive, but prone to ambiguity and semantic misunderstandings.

---

## 4. Mental Models & Conceptual Models
- **Mental Model**: The cognitive representation and internal belief system that a user constructs about how a system operates, synthesized from their past experiences, metaphors, and interface feedback.
- **System Conceptual Model**: The formal, actual architectural design and underlying data structure created by the software engineers and system architects.
- **The Gulf of Execution & Evaluation (Norman)**:
  - *Gulf of Execution*: The psychological distance between the user's formulation of an intention and the actions required by the interface to execute that intention.
  - *Gulf of Evaluation*: The psychological distance between the system's displayed output and the user's ability to perceive, interpret, and evaluate the new system state.
