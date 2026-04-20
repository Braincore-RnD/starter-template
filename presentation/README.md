# Quarto Slides Template

Template untuk presentasi dan dokumen interaktif menggunakan Quarto.

## Files

- `main.qmd` - Template presentasi Quarto dengan reveal.js
- `custom.css` - Custom CSS untuk presentasi dengan Computer Modern font

## Features

**Presentation:**
- Reveal.js presentation dengan LaTeX-style fonts
- Computer Modern web fonts untuk konsistensi dengan LaTeX
- Chalkboard support untuk interaktif presentation
- Code highlighting dengan syntax highlighting
- Math equations dengan KaTeX
- Responsive images dan tables
- PlantUML diagram embedding

## Usage

```bash
# Preview presentation
quarto preview main.qmd

# Render ke HTML
quarto render main.qmd

# Export ke PDF (butuh Chrome/Chromium)
quarto render main.qmd --to revealjs-pdf
```

## Font Configuration

Custom CSS menggunakan Computer Modern fonts yang sama dengan LaTeX.