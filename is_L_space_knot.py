import snappy

def is_L_space_knot(DT):
    """
    Given the DT code of a knot (in SnapPy's convention),
    return True if the knot is an L-space knot, and False otherwise.
    """

    K = snappy.Link(DT)
    HFK = K.knot_floer_homology()

    return HFK['L_space_knot']