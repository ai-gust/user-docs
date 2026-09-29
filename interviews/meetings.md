## Topic: Meetings

### Concept
- A meeting is a separate concept and a real citizen in the data model, but in practice a meeting today is a slideshow.
- Bart compared it to ClickShare (he wasn't sure of the name): a way to visualise your data and everything in aiGust in an interactive slideshow.
- You build a slideshow inside aiGust using all the visualisations the platform already offers, arranged in a logical flow.
- It works like PowerPoint (notes, moving between slides), but integrated into the platform, including the aiGust visualisations.
- The goal is for accountants to do their annual reviews and intermediate reviews through aiGust.

### Meeting flows (templates)
- Meeting flows are templates created at tenant/firm level, used to standardise the meetings a firm does with customers.
- Examples: a flow for management companies for an annual review, a flow for operational companies for an intermediate review, a yearly review.
- Only key users can create and modify flows. Accountants don't open flows; they pick one when creating a meeting.
- There is one aiGust flow out of the box today. Bart notes it isn't optimal or the best, and there may be different ones in the future.
  - You can copy it and adapt it, or start from scratch, though starting from scratch means inventing or discovering everything yourself.
- Building a flow works exactly like the editor at administration level: add slides, create chapter slides, and choose which widgets go where.
- **Preview administration:** when you open the flow editor, the system asks which administration to use for viewing purposes.
  - Everything renders dynamically with real data, nothing invented, so one administration serves as the example to show how the slides will look.
  - What you create is a definition: text here, this widget or that widget there, a chart, a table, and so on.
- **Titles:**
  - Titles are configured in the flow and carried over to the meeting. They are never auto-generated.
  - Fill them in for English, French and Dutch. AI can copy them across languages, but leaving a field empty or leaving the old value gives rubbish.
- **Text fields:** kept empty by default. You can type something in, but Bart advises against it. The rule when creating a flow: create the titles, leave the text empty, choose which widget goes where.
- **Suggestion logic:**
  - At firm level you can create meeting types. It's a free category and using it isn't obligatory. Examples: annual review, intermediate review.
  - A flow can be assigned to one or more meeting types, and to a company type (management company, operational company).
  - When starting a meeting you can choose any available flow, but the most specific one is pre-selected. An operational company most likely gets a flow made for operational companies.

### Creating a meeting
- The accountant creates a meeting at administration level. Bart's example: construction company Bouwwerke Michel has a meeting tomorrow, so you create a new meeting and select a flow.
- **Parameters chosen in the modal:**
  1. **Flow:** picked from a list, with a suggestion pre-selected (see suggestion logic above).
  2. **Up-to-date-until date:**
     - Same concept as elsewhere in aiGust: data is never shown beyond it, and that single date determines the open book year, the closed book year and the year-to-date.
     - The date is baked into the presentation, so every report in it uses that date as its final date.
     - Bart's example: today is 20 September and the book year closed in June, so we're three months into the new book year. You choose to discuss data up to date until 30 August.
  3. **Peer group:** needed because the visualisations show benchmarks.
  4. **Forecast (optional):** if you've prepared one, you can attach it to the presentation.
  5. **Language:** currently English, French and Dutch. Generated text comes in that language. Every text field holds an English, Dutch and French value, and only the selected one is filled in.
- **Two entry points:**
  - **Top right of the screen:** start a meeting from a flow or from scratch, or continue an existing meeting. Creating a new meeting here goes straight into presentation mode.
  - **Meetings overview:** a meetings item in the menu at administration level lists all meetings. Creating a new meeting there opens the editor instead of the presentation view.
- In the editor the main menu disappears and you get something like a PowerPoint editor.

### The meeting editor
- **Left: navigation / table of contents**
  - Visual overview of the slides, how they're grouped into chapters, and the chapter or navigation titles assigned to them.
  - Three dots on each slide open the slide-level actions: move up, move down, hide, delete.
  - Drag and drop to reorder.
  - Add button to add a slide.
  - **Chapters:**
    - There is no separate chapter object; a slide is marked as a chapter slide, which gives it a different layout in the navigation.
    - The presentation navigation bar shows big circles with a number for each chapter and smaller dots for the intermediate slides.
- **Right: the canvas (preview of the slide)**
  - Not a free canvas like PowerPoint. It's comparable to making a photo book: fixed layouts with defined areas where you put things.
  - The slide layout button at the top right of the canvas offers several predefined layouts: only widgets with a title, text areas combined with data widgets, one data widget, two, and so on.
  - After choosing a layout, you fill in what goes where.
- **Above the canvas, left side: per-slide data settings**
  - **Time indication:**
    - Slides are conceived around talking with the customer about the past (the last book year), the current state (year-to-date) or the future.
    - Every slide is assigned to one of these three via a dropdown.
    - The up-to-date-until date determines which year counts as past, present and future.
  - **Aggregation level:** a slide can be set to quarter view or year view.
- **Top right of the page:**
  - Close button: back to the main view.
  - Meeting settings: change the name, the up-to-date-until date and the forecast. These are global settings for the whole presentation.
  - Presentation mode button: starts a preview or presentation from the slide you're on.
- **Notes button near the canvas:** opens a side panel with the notes belonging to that slide, so notes can be made before or after the meeting.
- **Notes from the meetings list:** clicking notes shows a similar side panel with all notes taken for that meeting.

### Widgets
- The widget types available in an area are predefined by the layout: text widgets and data widget areas.
- Click the area where you want to put something and a side panel opens with a list of blocks/cards you can add.
- Almost anything you see anywhere in aiGust, any report or table, can go on a slide.
- Drawback: not every widget suits every area. Some areas are small and can't hold an entire table, so choose the layout carefully.
- **Available widgets:**
  - **Result sheet, balance sheet, cash flow:** in the presentation you want (waterfall or tabular, visual balance or tabular).
  - **Top contributors:** top customers and top suppliers.
  - **Meeting / administration score:** how you're doing compared to yourself or to the benchmark.
  - **KPI cards:** a number with optionally the benchmark. You choose the KPI.
  - **KPI chart:** you choose the KPI (revenue, a ratio, etc.).
  - **Multi-KPI chart:** several KPIs on the same chart instead of one KPI plus benchmark, for example three or four margins.
  - **Personnel reporting charts (two, also available on the dashboard):**
    - Distribution: what percentage are labour workers versus office workers (bedienden).
    - Evolution of revenue versus personnel costs.
  - **Table of contents.**
  - **Action points and notes:** a slide summarising the notes and action points taken during and before the meeting.
  - **PDF or JPEG document:**
    - aiGust includes a kind of cloud drive where you upload PDFs, for example a depreciation table (afschrijvingstabel) or a document generated elsewhere.
    - You can zoom in and out, but nothing in the document is clickable.
  - **Capital gains tax module:** nice for simulations with the customer about potential value increase and the tax that comes with it.
  - **Prepayments:** linked to a forecast, an estimate of the prepayments to be made.
- **Configuration options:** many widgets have none, but some do. The documentation should explain each widget and its configuration options.
  - **KPI chart:** select the KPI. Revenue is selected by default.
  - **Multi-KPI chart:** select the KPIs. EBITDA, gross margin and similar are the defaults.
  - **Top customers:**
    - Select the GL accounts the calculation runs on.
    - Indicate whether the KPI sentiment is positive or negative.
    - Indicate whether the signs need to be reversed.

### AI-generated text
- aiGust is coupled with an LLM. It reads what's on the slide (which widgets, which data is shown) and suggests the text, which is then filled in.
- Empty fields are detected and filled when you really start the meeting: full screen mode or presenter mode.
- Titles are never automatically generated; they come over from the flow.
- Once text exists, whether written by AI or by the accountant, it is never overwritten until you overwrite it yourself.

### Notes during the meeting
- During a meeting a button appears on screen that lets you take notes and see the notes belonging to the presentation, live.
- Notes can be marked internal or public/external, because some comments you want to show the end customer and some you don't.
- In full screen mode you're mirroring one screen, so notes are typed on the same screen the customer follows. Only public notes are shown there; internal ones are hidden.

### Presenting
- The play button at the top right starts a presentation. The same button exists in the meetings list. A dropdown next to it lets you choose the mode.
- **Full screen mode:** mirroring. There is only one thing you show.
- **Presenter mode:**
  - A second browser tab opens. One tab shows the portal in a kind of dummy full screen, the other shows the meeting notes.
  - Keep the notes tab on your own screen and move the other tab to the secondary screen.
  - Once it's there, a small button at the top right puts it into full screen.
  - Bart: very similar to how it works in Google Sheets (probably meant Google Slides).

### Editing after creation
- A meeting can be changed after it's created or presented: add slides, remove slides, change the text. Nothing is fixed.

### Customer access
- Customers can be given access, but only explicitly: there is a publish button, and an unpublished meeting isn't visible to the customer.
- The customer portal has an overview of available meetings, but the customer only sees the published ones.
- When the customer opens a meeting with notes, they see only the notes marked public.

### Permissions
- Everybody can create and update meetings.
- Only key users can create and modify meeting flows.

### Open questions
- Deleting meetings: not covered.
- Guidance on which widgets fit which layouts.

### Screenshots to take
- Meeting creation modal (flow, up-to-date-until date, peer group, forecast, language).
- Meetings overview at administration level.
- Editor with the navigation on the left and the canvas on the right.
- Three-dots slide actions menu.
- Slide layout picker.
- Per-slide period and aggregation dropdowns.
- Widget side panel with the available widgets.
- KPI chart widget and top customers widget with their configuration options.
- Notes side panel with internal versus public marking.
- Presentation navigation bar with chapter circles and intermediate dots.
- Play button dropdown (full screen versus presenter mode).
- Presenter mode across two screens.
- Meeting settings panel.
- Flow editor at firm level, including the administration selection for preview.
- Meeting types configuration at firm level.
- Publish button and the customer portal meetings overview.