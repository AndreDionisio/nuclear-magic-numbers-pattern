═══════════════════════════════════════════════════════════════════════
  LATEX SUBMISSION PACKAGE - NUCLEAR MAGIC NUMBERS
  Ready for Preprints.org Submission
═══════════════════════════════════════════════════════════════════════

Author: André Luís Tomaz Dionísio
Date: December 2, 2025
Version: Final (with Quark Analysis + Geometric Model)

═══════════════════════════════════════════════════════════════════════
PACKAGE CONTENTS
═══════════════════════════════════════════════════════════════════════

1. magic_numbers_preprint_updated.tex (39 KB)
   • Main article source (17 pages)
   • Includes quark analysis and geometric mention
   
2. magic_numbers_supplementary_updated.tex (31 KB)
   • Supplementary material source (20 pages)
   • Includes geometric interpretation box + appendix
   
3. figures/ directory:
   • figure1_delta_n_vs_BE.png (168 KB, 300 DPI)
   • figure2_hierarchy.png (142 KB, 300 DPI)
   • figure3_pattern_evolution.png (232 KB, 300 DPI)
   
4. graphic_abstract.png (311 KB, 300 DPI)
   • Optional graphic abstract for submission

═══════════════════════════════════════════════════════════════════════
COMPILATION INSTRUCTIONS
═══════════════════════════════════════════════════════════════════════

MAIN ARTICLE:
pdflatex magic_numbers_preprint_updated.tex
pdflatex magic_numbers_preprint_updated.tex

(Run twice for references)

SUPPLEMENTARY MATERIAL:
pdflatex magic_numbers_supplementary_updated.tex
pdflatex magic_numbers_supplementary_updated.tex

(Run twice for references and table of contents)

REQUIREMENTS:
• LaTeX distribution (TeX Live 2020+ or MikTeX)
• Packages: amsmath, amssymb, graphicx, booktabs, geometry, 
  hyperref, caption

All packages are standard and should be included in any modern 
LaTeX distribution.

═══════════════════════════════════════════════════════════════════════
SUBMISSION TO PREPRINTS.ORG
═══════════════════════════════════════════════════════════════════════

REQUIRED FILES:
✓ Manuscript TEX: magic_numbers_preprint_updated.tex
✓ Manuscript PDF: [compile first]
✓ Figures: Create figures.zip with all 3 PNG files
✓ Supplementary PDF: [compile first]

OPTIONAL FILES:
✓ Graphic Abstract: graphic_abstract.png

STEPS:
1. Compile both TEX files to generate PDFs
2. Zip the three figures: zip figures.zip figures/*.png
3. Upload to preprints.org submission form
4. Fill metadata (title, abstract, keywords)
5. Submit!

═══════════════════════════════════════════════════════════════════════
METADATA FOR SUBMISSION
═══════════════════════════════════════════════════════════════════════

TITLE:
A Phenomenological Pattern for Nuclear Magic Numbers: Recursive 
Formula and Hierarchical Stability

KEYWORDS:
nuclear magic numbers, shell model, nuclear structure, 
phenomenological formula, pairing capacity, superheavy elements, 
nuclear stability, quantum angular momentum, nucleon magnetism, 
hierarchical stability

SUBJECT:
Physical Sciences → Nuclear and High Energy Physics

ABSTRACT:
[See main TEX file, lines 27-30]

═══════════════════════════════════════════════════════════════════════
FILE STRUCTURE FOR COMPILATION
═══════════════════════════════════════════════════════════════════════

latex_submission/
├── magic_numbers_preprint_updated.tex
├── magic_numbers_supplementary_updated.tex
├── graphic_abstract.png
├── figures/
│   ├── figure1_delta_n_vs_BE.png
│   ├── figure2_hierarchy.png
│   └── figure3_pattern_evolution.png
└── README.txt (this file)

The TEX files expect figures in a "figures/" subdirectory.
Ensure this structure is maintained for successful compilation.

═══════════════════════════════════════════════════════════════════════
VERSION INFORMATION
═══════════════════════════════════════════════════════════════════════

This is the UPDATED version submitted after initial feedback from
Preprints.org (submission ID: preprints-187828).

CHANGES FROM ORIGINAL:
• Expanded from 6 to 17 pages (main article)
• Added magnetic coupling section
• Added quark counting analysis (μ_u = +2.50, μ_d = -2.20)
• Added geometric interpretation mention
• Expanded supplementary from 15 to 20 pages
• Added geometric box and appendix
• Updated date to December 2, 2025

═══════════════════════════════════════════════════════════════════════
TROUBLESHOOTING
═══════════════════════════════════════════════════════════════════════

PROBLEM: Missing figures error
SOLUTION: Ensure figures/ subdirectory exists with all 3 PNG files

PROBLEM: Missing package error
SOLUTION: Install missing package via TeX package manager
          (tlmgr install <package> or MikTeX Package Manager)

PROBLEM: References not appearing
SOLUTION: Run pdflatex twice (first pass creates .aux file)

PROBLEM: Hyperlinks not working
SOLUTION: Ensure hyperref package is installed and loaded

═══════════════════════════════════════════════════════════════════════
CONTACT
═══════════════════════════════════════════════════════════════════════

Author: André Luís Tomaz Dionísio
Email: andreluisdionisio@gmail.com
Institution: EPHEC Brussels, Belgium

GitHub: https://github.com/AndreDionisio/nuclear-magic-numbers-pattern
(will be updated after preprint acceptance)

═══════════════════════════════════════════════════════════════════════
LICENSE
═══════════════════════════════════════════════════════════════════════

Upon publication on Preprints.org, this work will be available under
Creative Commons CC BY 4.0 license.

LaTeX source files are provided for reproducibility and can be modified
for personal academic use.

═══════════════════════════════════════════════════════════════════════

End of README
Last updated: December 2, 2025, 03:30 CET

═══════════════════════════════════════════════════════════════════════
