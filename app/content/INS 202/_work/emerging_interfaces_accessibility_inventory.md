# INS 202 — Topic 7: Accessibility, Universal Design & Emerging Interfaces
## Exhaustive Knowledge Inventory

---

### 1. Navigation Architecture (Module 06)
- **Site-Level Navigation**:
  - Pertains to understanding and traversing the overarching information architecture of an entire website.
  - *Global Navigation*: Present on every single page; provides persistent access to major high-level sections (e.g., top header bar or fixed left drawer).
  - *Local Navigation*: Enables exploration within a specific sub-branch or subsection of a site (e.g., secondary sidebar menus).
  - *Contextual Navigation*: Inline associative hyperlinks connecting related concepts within running body text.
  - *Supplementary Navigation*: Sitemaps, alphabetical indexes, and site search engines.
- **Page-Level Navigation**:
  - Enhances comprehensibility and internal navigation within a single webpage.
  - Techniques: Table of contents with internal anchor jumps, 'Back to Top' floating buttons, paginated content selectors, accordions, and tabs.
- **Breadcrumbs**:
  - Hierarchical trail (e.g., `Home > Courses > Faculty of Computing > INS 202`).
  - Reinforces user mental models of location and enables single-click parent backtracking without triggering browser Back button cycles.

---

### 2. Universal Design & Web Content Accessibility Guidelines (WCAG 2.1)
- **Universal Design (Inclusive Design)**:
  - Designing products and environments to be usable by all people, to the greatest extent possible, without the need for adaptation or specialized redesign (Ron Mace).
  - The "Curb-Cut Effect": Accessibility features created for disabled individuals end up benefiting everyone (e.g., sidewalk curb cuts benefit wheelchair users, parents with strollers, delivery workers with handcarts; video captions benefit deaf users, learners in noisy environments, and non-native speakers).
- **The Four Foundational Principles of WCAG (POUR)**:
  1. **Perceivable**:
     - Users must be able to comprehend the information being presented; it cannot be invisible to all of their senses.
     - *Text Alternatives*: Non-text content (images, icons) must have text equivalents (`alt="Company Logo"`). Purely decorative images must use empty `alt=""`.
     - *Time-Based Media*: Captions for audio/video, audio descriptions for visual video content.
     - *Distinguishable*: Color contrast ratio minimums (WCAG AA requires 4.5:1 for normal text, 3:1 for large text $\ge 18\text{pt}$ or $14\text{pt}$ bold). Color must never be the sole visual means of conveying information (e.g., error fields must use an icon and text message, not just a red border).
  2. **Operable**:
     - User interface components and navigation must be operable via diverse input modalities.
     - *Keyboard Accessibility*: All interactive functionality must be navigable via keyboard (`Tab`, `Shift+Tab`, `Enter`, `Space`) with no keyboard traps (`focus` must never get permanently locked).
     - *Focus Indicator*: Visible, clear keyboard focus ring (`:focus-visible`).
     - *Navigable*: "Skip to Main Content" links to bypass repetitive navigation headers; meaningful page titles (`<title>`); descriptive anchor link text (never generic "Click Here").
     - *Timing*: Users must have sufficient time to read and interact with content (option to extend session timeouts).
     - *Seizures*: Content must not flash more than three times per second (preventing photosensitive epileptic seizures).
  3. **Understandable**:
     - Information and user interface operations must be predictable and comprehensible.
     - *Readable*: Human language of page declared (`<html lang="en">`).
     - *Predictable*: UI components behave consistently and do not unexpectedly change context on focus or input.
     - *Input Assistance*: Explicit form labels linked via `for` and `id`; clear error identification in plain language; constructive suggestions for correction.
  4. **Robust**:
     - Content must be robust enough to be interpreted reliably by diverse user agents, including assistive technologies (AT).
     - Clean, valid semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<article>`, `<button>`).
     - Use of WAI-ARIA (Accessible Rich Internet Applications) attributes (`aria-expanded`, `aria-label`, `aria-live`) where native HTML falls short, but avoiding ARIA when native HTML semantic elements exist ("No ARIA is better than bad ARIA").

---

### 3. Assistive Technologies & Impairment Categories
- **Visual Impairments**:
  - *Blindness*: Relies on Screen Readers (NVDA, JAWS, Apple VoiceOver, Android TalkBack) converting DOM nodes into synthetic speech or refreshable Braille displays.
  - *Low Vision*: Relies on screen magnifiers (ZoomText) and high-contrast browser display modes.
  - *Color Vision Deficiency*: Protanopia (red-blind), Deuteranopia (green-blind), Tritanopia (blue-blind). Requires high luminance contrast and dual-encoding (color + pattern/shape).
- **Motor / Physical Impairments**:
  - Tremors, cerebral palsy, spinal cord injuries, RSI.
  - Relies on alternative keyboards, sip-and-puff switches, eye-gaze tracking cameras, voice control. Requires large touch/click targets ($48 \times 48$ px minimum) and generous spacing.
- **Auditory Impairments**:
  - Deaf or hard of hearing.
  - Requires closed captions (synchronized text for speech and audio cues) and sign language interpretation.
- **Cognitive & Neurological Impairments**:
  - Dyslexia, ADHD, memory deficits.
  - Requires clean visual layouts, clear visual hierarchy, plain language, distraction-free reading modes, and forgiving form validation.

---

### 4. Emerging Interaction Paradigms
- **Voice User Interfaces (VUI) & Conversational AI**:
  - Speech recognition + Natural Language Understanding (NLU) + Speech synthesis (e.g., Alexa, Siri, Google Assistant).
  - *Advantages*: Hands-free, eyes-free, fast input rate for dictation, natural dialogue.
  - *HCI Challenges*:
    - Auditory channel is transient (once spoken, words vanish) and serial/linear (cannot scan or skim like a visual GUI).
    - Heavy cognitive load on short-term memory (Miller's $7 \pm 2$).
    - Lack of visual affordances (users do not know what commands are possible; "discoverability crisis").
- **Multi-Touch & Spatial Gesture Interfaces**:
  - Direct manipulation on capacitive screens: pinch-to-zoom, two-finger rotate, swipe.
  - 3D In-Air Spatial Gestures: Vision-based tracking (infrared sensors, computer vision cameras) detecting hand skeletons and eye gaze (e.g., Apple Vision Pro pinch gesture).
  - Challenges: "Gorilla arm" fatigue (holding arms outstretched in space), lack of physical tactile feedback.
- **Virtual Reality (VR) & Augmented Reality (AR)**:
  - *VR*: Fully immersive synthetic digital environment replacing physical reality via Head-Mounted Displays (HMDs).
  - *AR*: Digital graphics and information overlaid on the real physical world (optical see-through like HoloLens or video pass-through).
  - *Key Concepts*: 6 Degrees of Freedom (6 DoF: translation X, Y, Z + rotation pitch, yaw, roll); Simulator Sickness (caused by sensory conflict between visual motion cues and vestibular balance organs); Spatial Audio.
- **Haptic & Tangible Interfaces**:
  - Vibrotactile actuators (Linear Resonant Actuators, ERM motors), force-feedback steering wheels, ultrasound mid-air haptics.
  - Provides physical confirmation of digital actions, crucial when visual feedback is occluded or inaccessible.
- **Brain-Computer Interfaces (BCI)**:
  - Non-invasive electroencephalography (EEG) caps or invasive brain implants measuring neural action potentials.
  - Enables locked-in patients to spell words, move cursors, or manipulate robotic prosthetics purely through motor imagery.
