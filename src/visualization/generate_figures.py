#!/usr/bin/env python3
"""
Figure Generation Script for Magic Numbers Article
===================================================

Generates three publication-quality figures (300 DPI):
1. Figure 1: Δn vs Binding Energy per Nucleon
2. Figure 2: Stability Hierarchy
3. Figure 3: Pattern Evolution to 184

Author: André Luís Tomaz Dionísio
Institution: EPHEC Brussels, Belgium
Date: December 2025

Requirements:
- Python 3.7+
- numpy
- matplotlib

Usage:
    python generate_figures.py

Output:
    - figure1_delta_n_vs_BE.png (300 DPI)
    - figure2_hierarchy.png (300 DPI)
    - figure3_pattern_evolution.png (300 DPI)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# =============================================================================
# CONFIGURATION
# =============================================================================

# Set publication-quality parameters
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 13
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10
rcParams['legend.fontsize'] = 10
rcParams['figure.dpi'] = 300

# =============================================================================
# EXPERIMENTAL DATA
# =============================================================================

# Format: (N or Z, c_start, delta_n, BE/A in MeV, nucleus, type)
# BE/A data from AME2020 (Atomic Mass Evaluation)
nuclear_data = [
    (2, 2, 2, 7.074, r'$^4$He', 'magic'),
    (4, 4, 6, 6.476, r'$^8$Be', 'subshell'),
    (6, 4, 6, 7.680, r'$^{12}$C', 'subshell'),
    (8, 4, 6, 7.976, r'$^{16}$O', 'magic'),
    (10, 6, 12, 8.032, r'$^{20}$Ne', 'subshell'),
    (14, 6, 12, 8.448, r'$^{28}$Si', 'subshell'),
    (20, 2, 2, 8.551, r'$^{40}$Ca', 'magic'),
    (28, 6, 12, 8.643, r'$^{56}$Ni', 'magic'),
    (50, 8, 20, 8.667, r'$^{100}$Sn', 'magic'),
    (82, 10, 30, 7.867, r'$^{208}$Pb', 'magic'),
]

# =============================================================================
# FIGURE 1: Δn vs BINDING ENERGY
# =============================================================================

def generate_figure1():
    """Generate correlation between Δn and binding energy per nucleon."""
    print("Generating Figure 1: Δn vs Binding Energy...")
    
    # Extract data
    delta_n_values = [d[2] for d in nuclear_data]
    be_values = [d[3] for d in nuclear_data]
    nuclei_labels = [d[4] for d in nuclear_data]
    types = [d[5] for d in nuclear_data]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot points with different colors for magic vs subshell
    magic_points = [(dn, be, label) for dn, be, label, t in 
                    zip(delta_n_values, be_values, nuclei_labels, types) 
                    if t == 'magic']
    subshell_points = [(dn, be, label) for dn, be, label, t in 
                       zip(delta_n_values, be_values, nuclei_labels, types) 
                       if t == 'subshell']
    
    # Plot magic numbers (red circles)
    if magic_points:
        dn_magic = [p[0] for p in magic_points]
        be_magic = [p[1] for p in magic_points]
        labels_magic = [p[2] for p in magic_points]
        ax.scatter(dn_magic, be_magic, c='red', s=100, alpha=0.7, 
                  label='Magic numbers', zorder=3, edgecolors='darkred', linewidths=1.5)
        
        # Add labels for magic numbers
        for dn, be, label in magic_points:
            ax.annotate(label, (dn, be), xytext=(5, 5), 
                       textcoords='offset points', fontsize=9)
    
    # Plot subshell closures (blue triangles)
    if subshell_points:
        dn_sub = [p[0] for p in subshell_points]
        be_sub = [p[1] for p in subshell_points]
        labels_sub = [p[2] for p in subshell_points]
        ax.scatter(dn_sub, be_sub, c='blue', s=100, alpha=0.7, 
                  marker='^', label='Subshell closures', zorder=3, 
                  edgecolors='darkblue', linewidths=1.5)
        
        # Add labels for subshells
        for dn, be, label in subshell_points:
            ax.annotate(label, (dn, be), xytext=(5, -10), 
                       textcoords='offset points', fontsize=9)
    
    # Trend line (excluding outlier 8Be)
    filtered_data = [(dn, be) for dn, be, t in 
                     zip(delta_n_values, be_values, types) 
                     if (dn, be) != (6, 6.476)]  # Exclude 8Be
    
    if len(filtered_data) > 2:
        dn_fit = np.array([p[0] for p in filtered_data])
        be_fit = np.array([p[1] for p in filtered_data])
        z = np.polyfit(dn_fit, be_fit, 1)
        p = np.poly1d(z)
        dn_line = np.linspace(min(delta_n_values), max(delta_n_values), 100)
        ax.plot(dn_line, p(dn_line), 'k--', alpha=0.3, linewidth=1.5, 
               label='Trend (excluding $^8$Be)')
    
    # Formatting
    ax.set_xlabel(r'Pairing capacity $\Delta n$')
    ax.set_ylabel('Binding energy per nucleon (MeV)')
    ax.set_title('Correlation between $\Delta n$ and Nuclear Stability')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='best')
    
    plt.tight_layout()
    plt.savefig('figure1_delta_n_vs_BE.png', dpi=300, bbox_inches='tight')
    print("✓ Figure 1 saved: figure1_delta_n_vs_BE.png")
    plt.close()

# =============================================================================
# FIGURE 2: STABILITY HIERARCHY
# =============================================================================

def generate_figure2():
    """Generate stability hierarchy diagram."""
    print("Generating Figure 2: Stability Hierarchy...")
    
    # Hierarchy levels
    hierarchy = [
        (2, 'LOCAL', ['$^4$He', '$^{40}$Ca']),
        (6, 'SUBSHELL', ['$^{12}$C', '$^{16}$O']),
        (12, 'REGIONAL', ['$^{20}$Ne', '$^{28}$Si', '$^{56}$Ni']),
        (20, 'STRONG', ['$^{100}$Sn']),
        (30, 'MAJOR', ['$^{208}$Pb']),
        (42, 'COMPLETE', ['184 (predicted)']),
    ]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot bars
    delta_n = [h[0] for h in hierarchy]
    levels = [h[1] for h in hierarchy]
    positions = np.arange(len(hierarchy))
    
    colors = ['#FFE5E5', '#E5F5FF', '#E5FFE5', '#FFFFE5', '#FFE5FF', '#FFE5E5']
    bars = ax.barh(positions, delta_n, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add labels
    for i, (dn, level, examples) in enumerate(hierarchy):
        # Level name
        ax.text(-2, i, level, va='center', ha='right', fontweight='bold', fontsize=11)
        
        # Δn value
        ax.text(dn/2, i, f'Δn = {dn}', va='center', ha='center', 
               fontweight='bold', fontsize=10)
        
        # Examples
        examples_text = ', '.join(examples)
        ax.text(dn + 1, i, examples_text, va='center', ha='left', 
               fontsize=9, style='italic')
    
    # Formatting
    ax.set_xlabel(r'Pairing capacity $\Delta n$', fontsize=12)
    ax.set_yticks([])
    ax.set_xlim(-5, 50)
    ax.set_ylim(-0.5, len(hierarchy)-0.5)
    ax.set_title('Hierarchical Stability Pattern', fontsize=13, fontweight='bold')
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Arrow indicating increasing stability
    ax.annotate('', xy=(45, -0.3), xytext=(45, len(hierarchy)-0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(46.5, len(hierarchy)/2 - 0.5, 'Increasing\nStability', 
           va='center', ha='left', fontsize=10, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figure2_hierarchy.png', dpi=300, bbox_inches='tight')
    print("✓ Figure 2 saved: figure2_hierarchy.png")
    plt.close()

# =============================================================================
# FIGURE 3: PATTERN EVOLUTION
# =============================================================================

def generate_figure3():
    """Generate pattern evolution diagram showing recursive structure."""
    print("Generating Figure 3: Pattern Evolution...")
    
    # Magic numbers with their building blocks
    magic_structure = [
        (2, [2], 2),
        (8, [4, 2], 0),
        (20, [6, 4, 2], 0),
        (28, [8], 8),
        (50, [6, 4, 2, 10], 10),
        (82, [8, 6, 4, 2, 12], 12),
        (126, [10, 8, 6, 4, 2, 14], 14),
        (184, [12, 10, 8, 6, 4, 2, 16], 16),
    ]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    y_position = len(magic_structure) - 1
    
    for magic, sequence, sphere in magic_structure:
        # Draw sequence boxes
        x_pos = 0
        box_width = 2
        box_height = 0.6
        
        # Color scheme
        if sphere == magic:  # Simple closure (just sphere)
            color = '#FFE5E5'
        elif sphere > 0:  # Sequence + sphere
            color = '#E5FFE5'
        else:  # Just sequence
            color = '#E5F5FF'
        
        # Draw decreasing sequence
        for i, cap in enumerate(sequence):
            if sphere > 0 and cap == sphere:
                # Sphere orbital (highlighted)
                rect = plt.Rectangle((x_pos, y_position - box_height/2), 
                                    box_width, box_height,
                                    facecolor='#FFD700', edgecolor='red', 
                                    linewidth=2)
                ax.add_patch(rect)
                ax.text(x_pos + box_width/2, y_position, str(cap), 
                       va='center', ha='center', fontweight='bold', fontsize=11)
                ax.text(x_pos + box_width/2, y_position - box_height/2 - 0.2, 
                       'sphere', va='top', ha='center', fontsize=8, 
                       style='italic', color='red')
            else:
                # Regular sequence element
                rect = plt.Rectangle((x_pos, y_position - box_height/2), 
                                    box_width, box_height,
                                    facecolor=color, edgecolor='black', linewidth=1)
                ax.add_patch(rect)
                ax.text(x_pos + box_width/2, y_position, str(cap), 
                       va='center', ha='center', fontsize=10)
            
            # Arrow between elements
            if i < len(sequence) - 1:
                ax.annotate('', xy=(x_pos + box_width + 0.1, y_position), 
                           xytext=(x_pos + box_width, y_position),
                           arrowprops=dict(arrowstyle='->', lw=1.5))
            
            x_pos += box_width + 0.3
        
        # Magic number label
        ax.text(-1, y_position, f'M = {magic}', va='center', ha='right', 
               fontweight='bold', fontsize=12)
        
        # Sum calculation
        total = sum(sequence)
        ax.text(x_pos + 0.5, y_position, f'= {total}', va='center', ha='left', 
               fontsize=10, style='italic')
        
        y_position -= 1
    
    # Formatting
    ax.set_xlim(-2, 18)
    ax.set_ylim(-0.5, len(magic_structure) - 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Recursive Pattern Evolution: 0 → 2 → 8 → ... → 184', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Legend
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, facecolor='#E5F5FF', 
                     edgecolor='black', label='Decreasing sequence'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFD700', 
                     edgecolor='red', linewidth=2, label='Sphere starter'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFE5E5', 
                     edgecolor='black', label='Simple closure'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    
    # Add note
    ax.text(8, -0.3, 'Pattern: Start higher → Descend by 2 → Reach 2 → Start even higher', 
           ha='center', fontsize=10, style='italic', 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('figure3_pattern_evolution.png', dpi=300, bbox_inches='tight')
    print("✓ Figure 3 saved: figure3_pattern_evolution.png")
    plt.close()

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    """Generate all three figures."""
    print("\n" + "="*70)
    print("FIGURE GENERATION FOR MAGIC NUMBERS ARTICLE")
    print("="*70)
    print("\nAuthor: André Luís Tomaz Dionísio")
    print("Institution: EPHEC Brussels, Belgium")
    print("Resolution: 300 DPI (publication quality)")
    print("\n" + "="*70 + "\n")
    
    try:
        # Generate all figures
        generate_figure1()
        generate_figure2()
        generate_figure3()
        
        print("\n" + "="*70)
        print("SUCCESS! All figures generated.")
        print("="*70)
        print("\nGenerated files:")
        print("  • figure1_delta_n_vs_BE.png (Δn vs Binding Energy)")
        print("  • figure2_hierarchy.png (Stability Hierarchy)")
        print("  • figure3_pattern_evolution.png (Pattern Evolution)")
        print("\nThese figures are ready for inclusion in the manuscript.")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nPlease ensure you have the required packages:")
        print("  pip install numpy matplotlib")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
