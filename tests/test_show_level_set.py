import dmsh


def test_show():
    # geo = dmsh.Circle([0.0, 0.0], 1.0)
    geo = dmsh.Rectangle(-1.0, +1.0, -1.0, +1.0)
    geo.show()


if __name__ == "__main__":
    test_show()
