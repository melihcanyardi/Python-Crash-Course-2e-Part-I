def sandwich(*items):
    """Print the list of items a person wants on a sandwich."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


sandwich('cheese')
sandwich('cheese', 'tomato')
sandwich('cheese', 'tomato', 'sausage')
