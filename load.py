class Load:
    """
    Represents a constant real and reactive power load connected to a bus.
    """

    def __init__(
        self,
        name: str,
        bus1_name: str,
        mw: float,
        mvar: float
    ):
        self.name = name
        self.bus1_name = bus1_name
        self.mw = mw
        self.mvar = mvar

    def __repr__(self):
        return (
            f"Load(name={self.name}, "
            f"bus1={self.bus1_name}, "
            f"MW={self.mw}, "
            f"MVAR={self.mvar})"
        )


# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    # Create a load instance
    load = Load(
        name="L1",
        bus1_name="Bus_1",
        mw=75.0,
        mvar=30.0
    )

    # Print load to verify __repr__
    print(load)

    # Attribute checks
    assert load.name == "L1"
    assert load.bus1_name == "Bus_1"
    assert load.mw == 75.0
    assert load.mvar == 30.0

    print("Load test passed ✔")
