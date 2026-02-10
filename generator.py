class Generator:
    def __init__(
        self,
        name: str,
        bus1_name: str,
        mw_setpoint: float,
        v_setpoint: float
    ):
        self.name = name
        self.bus1_name = bus1_name
        self.MW_setpoint = mw_setpoint
        self.v_setpoint = v_setpoint

    def __repr__(self):
        return (
            f"Generator(name={self.name}, "
            f"bus1={self.bus1_name}, "
            f"MW_setpoint={self.MW_setpoint}, "
            f"V_setpoint={self.v_setpoint})"
        )


# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    # Create a generator instance
    gen = Generator(
        name="G1",
        bus1_name="Bus_1",
        mw_setpoint=100.0,
        v_setpoint=1.05
    )

    # Print generator to verify __repr__
    print(gen)

    # Basic attribute checks
    assert gen.name == "G1"
    assert gen.bus1_name == "Bus_1"
    assert gen.MW_setpoint == 100.0
    assert gen.v_setpoint == 1.05

    print("Generator test passed ✔")
