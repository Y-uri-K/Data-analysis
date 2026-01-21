import random
from generator.points import Points


class PointsCalculator:
    def calculate(
        self,
        action_name: str,
        action_type: str,
        difficulty: str
    ) -> int:
        base_points = Points["base_points"][action_type]
        action_multiplier = Points["action_multipliers"][action_name]
        level_coefficient = Points["level_coefficients"][difficulty]
        random_factor = random.uniform(*Points["random_factor_range"])

        points = (
            base_points
            * action_multiplier
            * level_coefficient
            * random_factor
        )

        return int(round(points))
