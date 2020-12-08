from helpers import assert_norm_equality, save

import dmsh


def test(show=False):
    geo = dmsh.Rectangle(0.0, 1.0, 0.0, 1.0)

    # p0 = dmsh.Path([[0.0, 0.0]])
    p1 = dmsh.Path([[0.4, 0.6], [0.6, 0.4]])

    def edge_size(x):
        return 0.03 + 0.1 * p1.dist(x)

    X, cells = dmsh.generate(geo, edge_size, show=show, tol=1.0e-10)

    ref_norms = [3.8768005962507056e+02, 1.5684756178925376e+01, 1.0000000000000000e+00]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-3)
    return X, cells


if __name__ == "__main__":
    X, cells = test(show=False)
    save("refinement_line.png", X, cells)
