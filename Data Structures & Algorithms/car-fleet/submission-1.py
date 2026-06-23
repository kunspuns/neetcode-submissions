class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        fleet_count=0
        leader_time = 0

        for pos,spd in cars:
            time = (target-pos)/spd

            if time > leader_time:
                fleet_count += 1
                leader_time = time

        return fleet_count


        