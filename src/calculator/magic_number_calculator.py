#!/usr/bin/env python3
"""
Magic Number Calculator
Based on: "A Phenomenological Pattern for Nuclear Magic Numbers"
Author: André Luís Tomaz Dionísio
Institution: EPHEC Brussels, Belgium
Date: December 2025
"""

def calculate_delta_n(c_start):
    """
    Calculate Δn from the decreasing sequence formula.
    
    Δn = c_start × (c_start + 2) / 4
    
    This represents the sum of the arithmetic sequence:
    c_start + (c_start-2) + (c_start-4) + ... + 4 + 2
    """
    return (c_start * (c_start + 2)) // 4


def calculate_next_magic(M_n, c_start, c_high_j):
    """
    Calculate the next magic number M_{n+1}.
    
    Parameters:
    -----------
    M_n : int
        Current magic number
    c_start : int
        Capacity of last filled orbital
    c_high_j : int
        Capacity of next high-j orbital
    
    Returns:
    --------
    tuple : (delta_n, C_total, M_next)
    """
    delta_n = calculate_delta_n(c_start)
    C_total = delta_n + c_high_j
    M_next = M_n + C_total
    
    return delta_n, C_total, M_next


def display_calculation(M_n, c_start, c_high_j):
    """Display detailed calculation steps."""
    print(f"\n{'='*60}")
    print(f"Calculating next magic number after M_n = {M_n}")
    print(f"{'='*60}")
    print(f"\nGiven parameters:")
    print(f"  c_start  = {c_start}")
    print(f"  c_high-j = {c_high_j}")
    
    delta_n, C_total, M_next = calculate_next_magic(M_n, c_start, c_high_j)
    
    print(f"\nStep 1: Calculate Δn")
    print(f"  Δn = c_start × (c_start + 2) / 4")
    print(f"  Δn = {c_start} × {c_start + 2} / 4")
    print(f"  Δn = {c_start * (c_start + 2)} / 4")
    print(f"  Δn = {delta_n}")
    
    # Show decreasing sequence
    if c_start > 0:
        sequence = list(range(c_start, 0, -2))
        print(f"\n  This is the sum of: {' + '.join(map(str, sequence))}")
        print(f"  Sum verification: {sum(sequence)} = {delta_n} ✓")
    
    print(f"\nStep 2: Calculate C_total")
    print(f"  C_total = Δn + c_high-j")
    print(f"  C_total = {delta_n} + {c_high_j}")
    print(f"  C_total = {C_total}")
    
    print(f"\nStep 3: Calculate M_{{n+1}}")
    print(f"  M_{{n+1}} = M_n + C_total")
    print(f"  M_{{n+1}} = {M_n} + {C_total}")
    print(f"  M_{{n+1}} = {M_next}")
    
    print(f"\n{'='*60}")
    print(f"RESULT: Next magic number is {M_next}")
    print(f"{'='*60}\n")
    
    return M_next


def validate_all_magic_numbers():
    """Validate all known magic numbers using the formula."""
    # Parameters table: (M_n, c_start, c_high_j, expected_M_next)
    parameters = [
        (0,   0,  2,   2),
        (2,   2,  4,   8),
        (8,   4,  6,  20),
        (20,  2,  6,  28),
        (28,  6, 10,  50),
        (50,  8, 12,  82),
        (82, 10, 14, 126),
        (126, 12, 16, 184),
    ]
    
    print("\n" + "="*70)
    print("VALIDATION: All Known Magic Numbers (0 → 184)")
    print("="*70)
    print(f"\n{'M_n':>5} | {'c_start':>8} | {'c_high-j':>8} | {'Δn':>6} | "
          f"{'C_total':>8} | {'M_next':>7} | {'Expected':>8}")
    print("-"*70)
    
    all_valid = True
    for M_n, c_start, c_high_j, expected in parameters:
        delta_n, C_total, M_next = calculate_next_magic(M_n, c_start, c_high_j)
        status = "✓" if M_next == expected else "✗"
        
        print(f"{M_n:5} | {c_start:8} | {c_high_j:8} | {delta_n:6} | "
              f"{C_total:8} | {M_next:7} | {expected:8} {status}")
        
        if M_next != expected:
            all_valid = False
    
    print("-"*70)
    if all_valid:
        print("ALL VALIDATIONS PASSED! ✓✓✓")
    else:
        print("VALIDATION FAILED!")
    print("="*70 + "\n")


def show_stability_hierarchy():
    """Display the stability hierarchy based on Δn values."""
    print("\n" + "="*60)
    print("STABILITY HIERARCHY (based on Δn)")
    print("="*60)
    
    hierarchy = [
        (2,  "LOCAL",     "⁴He, ⁴⁰Ca"),
        (6,  "SUBSHELL",  "¹²C, ¹⁶O"),
        (12, "REGIONAL",  "²⁰Ne, ²⁸Si, ⁵⁶Ni"),
        (20, "STRONG",    "¹⁰⁰Sn"),
        (30, "MAJOR",     "²⁰⁸Pb"),
        (42, "COMPLETE",  "predicted 184"),
    ]
    
    print(f"\n{'Δn':>4} | {'Level':>10} | {'Examples'}")
    print("-"*60)
    for delta_n, level, examples in hierarchy:
        print(f"{delta_n:4} | {level:>10} | {examples}")
    
    print("\n" + "="*60)
    print("Higher Δn = Greater Nuclear Stability")
    print("="*60 + "\n")


def show_decreasing_sequences():
    """Display the decreasing sequence pattern for all magic numbers."""
    print("\n" + "="*70)
    print("DECREASING SEQUENCE PATTERN")
    print("="*70)
    
    patterns = [
        (2,   [],                      2,  ""),
        (8,   [4, 2],                  0,  ""),
        (20,  [6, 4, 2],               0,  ""),
        (28,  [],                      8,  "← sphere closure"),
        (50,  [6, 4, 2],              10,  ""),
        (82,  [8, 6, 4, 2],           12,  ""),
        (126, [10, 8, 6, 4, 2],       14,  ""),
        (184, [12, 10, 8, 6, 4, 2],   16,  "(predicted)"),
    ]
    
    print(f"\n{'Magic':>6} | {'Decreasing Sequence':>30} | {'Sphere':>8} | {'Note'}")
    print("-"*70)
    
    for magic, sequence, sphere, note in patterns:
        if sequence:
            seq_str = "→".join(map(str, sequence))
        else:
            seq_str = "—"
        
        sphere_str = str(sphere) if sphere > 0 else "—"
        
        print(f"{magic:6} | {seq_str:>30} | {sphere_str:>8} | {note}")
    
    print("\n" + "="*70)
    print("Pattern: Start higher → Descend by 2 → Reach 2 → Start even higher")
    print("="*70 + "\n")


def interactive_mode():
    """Interactive calculator for custom parameters."""
    print("\n" + "="*60)
    print("INTERACTIVE MAGIC NUMBER CALCULATOR")
    print("="*60)
    print("\nEnter parameters to calculate the next magic number.")
    print("(Enter 'q' to quit)\n")
    
    while True:
        try:
            M_n_input = input("Enter current magic number M_n: ")
            if M_n_input.lower() == 'q':
                break
            M_n = int(M_n_input)
            
            c_start = int(input("Enter c_start: "))
            c_high_j = int(input("Enter c_high-j: "))
            
            display_calculation(M_n, c_start, c_high_j)
            
            cont = input("Calculate another? (y/n): ")
            if cont.lower() != 'y':
                break
                
        except ValueError:
            print("Invalid input! Please enter integers.\n")
        except KeyboardInterrupt:
            print("\n\nExiting...\n")
            break


def main():
    """Main function to run the calculator."""
    print("\n" + "="*70)
    print("MAGIC NUMBER CALCULATOR")
    print("Based on: A Phenomenological Pattern for Nuclear Magic Numbers")
    print("Author: André Luís Tomaz Dionísio (EPHEC Brussels)")
    print("="*70)
    
    while True:
        print("\nOptions:")
        print("1. Validate all known magic numbers (0 → 184)")
        print("2. Calculate specific magic number")
        print("3. Show stability hierarchy")
        print("4. Show decreasing sequence patterns")
        print("5. Interactive mode")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            validate_all_magic_numbers()
        elif choice == '2':
            try:
                M_n = int(input("Enter M_n: "))
                c_start = int(input("Enter c_start: "))
                c_high_j = int(input("Enter c_high-j: "))
                display_calculation(M_n, c_start, c_high_j)
            except ValueError:
                print("Invalid input! Please enter integers.")
        elif choice == '3':
            show_stability_hierarchy()
        elif choice == '4':
            show_decreasing_sequences()
        elif choice == '5':
            interactive_mode()
        elif choice == '6':
            print("\nThank you for using the Magic Number Calculator!")
            print("For more information, see the full article.\n")
            break
        else:
            print("Invalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()
