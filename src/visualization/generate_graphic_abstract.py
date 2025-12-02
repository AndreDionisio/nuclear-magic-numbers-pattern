#!/usr/bin/env python3
"""
Graphic Abstract Generator for Nuclear Magic Numbers Paper
===========================================================

Generates a professional graphic abstract suitable for journal submission.

Author: André Luís Tomaz Dionísio
Institution: EPHEC Brussels, Belgium
Date: December 2025

Output: graphic_abstract.png (high resolution, suitable for publication)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set publication-quality parameters
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['figure.dpi'] = 300

# Create figure with proper aspect ratio (typical for graphic abstracts)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Color scheme (professional, accessible)
color_primary = '#1f77b4'  # Blue
color_secondary = '#ff7f0e'  # Orange
color_accent = '#2ca02c'  # Green
color_dark = '#333333'
color_light = '#f0f0f0'
color_border = '#666666'

# ============================================================================
# TITLE SECTION
# ============================================================================

# Title box
title_box = FancyBboxPatch((0.5, 6.8), 11, 1, 
                           boxstyle="round,pad=0.1", 
                           facecolor=color_primary, 
                           edgecolor=color_border,
                           linewidth=2,
                           alpha=0.9)
ax.add_patch(title_box)

# Title text
ax.text(6, 7.5, 'NUCLEAR MAGIC NUMBERS', 
        ha='center', va='center', 
        fontsize=24, fontweight='bold', 
        color='white')
ax.text(6, 7.0, 'Recursive Phenomenological Pattern', 
        ha='center', va='center', 
        fontsize=16, fontweight='normal', 
        color='white', style='italic')

# ============================================================================
# MAGIC NUMBERS SEQUENCE
# ============================================================================

# Background box for sequence
seq_box = FancyBboxPatch((0.5, 5.2), 11, 1.3, 
                         boxstyle="round,pad=0.05", 
                         facecolor=color_light, 
                         edgecolor=color_border,
                         linewidth=1.5)
ax.add_patch(seq_box)

# Magic numbers
magic_numbers = [0, 2, 8, 20, 28, 50, 82, 126]
x_positions = np.linspace(1.5, 10.5, len(magic_numbers))

for i, (x, num) in enumerate(zip(x_positions, magic_numbers)):
    # Circle for each number
    if num == 126:  # Highlight last known
        circle_color = color_accent
        text_color = 'white'
        circle_size = 0.35
    else:
        circle_color = color_primary
        text_color = 'white'
        circle_size = 0.30
    
    circle = plt.Circle((x, 5.85), circle_size, 
                        color=circle_color, 
                        ec=color_dark, 
                        linewidth=2,
                        zorder=10)
    ax.add_patch(circle)
    
    # Number text
    ax.text(x, 5.85, str(num), 
            ha='center', va='center', 
            fontsize=16, fontweight='bold', 
            color=text_color,
            zorder=11)
    
    # Arrow between numbers
    if i < len(magic_numbers) - 1:
        arrow = FancyArrowPatch((x + 0.35, 5.85), 
                               (x_positions[i+1] - 0.35, 5.85),
                               arrowstyle='->', 
                               mutation_scale=20, 
                               linewidth=2.5,
                               color=color_dark,
                               zorder=9)
        ax.add_patch(arrow)

# ============================================================================
# FORMULA SECTION
# ============================================================================

# Formula box
formula_box = FancyBboxPatch((2.5, 3.8), 7, 1, 
                            boxstyle="round,pad=0.1", 
                            facecolor='white', 
                            edgecolor=color_secondary,
                            linewidth=3)
ax.add_patch(formula_box)

# Main formula
ax.text(6, 4.5, r'$\Delta n = \frac{c_{start}(c_{start}+2)}{4}$', 
        ha='center', va='center', 
        fontsize=28, fontweight='bold', 
        color=color_dark,
        math_fontfamily='cm')

# Formula description
ax.text(6, 3.95, 'Pairing Capacity Formula', 
        ha='center', va='center', 
        fontsize=12, 
        color=color_dark,
        style='italic')

# ============================================================================
# HIERARCHY VISUALIZATION
# ============================================================================

# Hierarchy box
hier_box = FancyBboxPatch((0.5, 1.8), 5.5, 1.7, 
                         boxstyle="round,pad=0.05", 
                         facecolor=color_light, 
                         edgecolor=color_border,
                         linewidth=1.5)
ax.add_patch(hier_box)

ax.text(3.25, 3.3, 'Stability Hierarchy', 
        ha='center', va='top', 
        fontsize=14, fontweight='bold', 
        color=color_dark)

# Hierarchy levels
hierarchy = [2, 6, 12, 20, 30, 42]
y_start = 2.9
y_step = 0.15

for i, delta_n in enumerate(hierarchy):
    y_pos = y_start - i * y_step
    
    # Bar
    bar_length = delta_n / 42 * 4  # Scale to fit
    rect = patches.Rectangle((1, y_pos - 0.05), bar_length, 0.1,
                            facecolor=color_primary,
                            edgecolor=color_dark,
                            linewidth=1,
                            alpha=0.7 + i*0.05)
    ax.add_patch(rect)
    
    # Label
    ax.text(5.3, y_pos, f'Δn = {delta_n}', 
            ha='left', va='center', 
            fontsize=11, fontweight='bold',
            color=color_dark)

# ============================================================================
# PREDICTION SECTION
# ============================================================================

# Prediction box
pred_box = FancyBboxPatch((6.5, 1.8), 5, 1.7, 
                         boxstyle="round,pad=0.1", 
                         facecolor=color_accent, 
                         edgecolor=color_dark,
                         linewidth=2,
                         alpha=0.2)
ax.add_patch(pred_box)

ax.text(9, 3.2, 'NEXT PREDICTION', 
        ha='center', va='center', 
        fontsize=14, fontweight='bold', 
        color=color_dark)

# Big number 184
ax.text(9, 2.5, '184', 
        ha='center', va='center', 
        fontsize=48, fontweight='bold', 
        color=color_accent)

ax.text(9, 1.95, 'Superheavy nuclei', 
        ha='center', va='center', 
        fontsize=11, 
        color=color_dark,
        style='italic')

# ============================================================================
# KEY INSIGHTS (Bottom)
# ============================================================================

# Insights box
insight_box = FancyBboxPatch((0.5, 0.3), 11, 1.2, 
                            boxstyle="round,pad=0.05", 
                            facecolor='white', 
                            edgecolor=color_secondary,
                            linewidth=2)
ax.add_patch(insight_box)

# Three key points
key_points = [
    ('Recursive\nFormula', 2),
    ('c = 2l + 2\nConnection', 6),
    ('Magnetic\nCoupling', 10)
]

for text, x_pos in key_points:
    # Icon circle
    circle = plt.Circle((x_pos, 1.15), 0.15, 
                       color=color_secondary, 
                       ec=color_dark,
                       linewidth=1.5)
    ax.add_patch(circle)
    
    # Checkmark
    ax.text(x_pos, 1.15, '✓', 
           ha='center', va='center', 
           fontsize=16, fontweight='bold',
           color='white')
    
    # Text
    ax.text(x_pos, 0.65, text, 
           ha='center', va='center', 
           fontsize=10,
           color=color_dark,
           multialignment='center')

# ============================================================================
# AUTHOR INFO (Bottom right corner)
# ============================================================================

ax.text(11.3, 0.15, 'A. L. T. Dionísio (2025)', 
        ha='right', va='bottom', 
        fontsize=8, 
        color=color_dark,
        style='italic')

# ============================================================================
# SAVE
# ============================================================================

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/graphic_abstract.png', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')
plt.savefig('/mnt/user-data/outputs/submission_package/graphic_abstract.png', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

print("="*70)
print("GRAPHIC ABSTRACT GENERATED SUCCESSFULLY!")
print("="*70)
print("\nOutput files:")
print("  • graphic_abstract.png (300 DPI)")
print("\nSaved to:")
print("  • /mnt/user-data/outputs/")
print("  • /mnt/user-data/outputs/submission_package/")
print("\nDimensions: 3600 × 2400 pixels (12\" × 8\" at 300 DPI)")
print("File size: ~500-800 KB")
print("\nReady for journal submission!")
print("="*70)

plt.close()
