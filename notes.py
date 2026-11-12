def moyenne_ponderee(notes, coefficients):
    """Moyenne ponderee d'une liste de notes (0 a 20) selon des coefficients."""
    if not notes or len(notes) != len(coefficients):
        raise ValueError("listes incoherentes")
    if any(n < 0 or n > 20 for n in notes):
        raise ValueError("note hors bornes")
    if sum(coefficients) <= 0:
        raise ValueError("coefficients invalides")
    total = sum(n * c for n, c in zip(notes, coefficients))
    return total / sum(coefficients)