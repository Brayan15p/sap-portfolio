from main import collisions, downgrade_risk
T = [{"id": "DEVK900101", "released": 1, "objects": ["ZCL_PRICING", "ZSD_REPORT"]},
     {"id": "DEVK900105", "released": 2, "objects": ["ZCL_PRICING"]}, {"id": "DEVK900110", "released": 3, "objects": ["ZFI_EXIT"]}]
def test_collision_and_downgrade():
    assert collisions(T) == [{"object": "ZCL_PRICING", "transports": ["DEVK900101", "DEVK900105"]}]
    assert downgrade_risk(["DEVK900105", "DEVK900101"], T) == [{"older": "DEVK900101", "after": "DEVK900105", "objects": ["ZCL_PRICING"]}]
