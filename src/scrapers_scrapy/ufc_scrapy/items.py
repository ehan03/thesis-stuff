# standard library imports

# third party imports
from scrapy import Field, Item

# local imports


# UFC Stats items
class UFCStatsFighterItem(Item):
    id = Field()
    name = Field()
    nickname = Field()
    height_inches = Field()
    reach_inches = Field()
    stance = Field()
    date_of_birth = Field()


class UFCStatsEventItem(Item):
    id = Field()
    name = Field()
    date = Field()
    location = Field()
    is_ufc = Field()


class UFCStatsBoutMetaItem(Item):
    id = Field()
    event_id = Field()
    bout_order = Field()
    red_fighter_id = Field()
    blue_fighter_id = Field()
    red_win = Field()


class UFCStatsBoutItem(Item):
    id = Field()
    fighter_id = Field()
    fighter_history_order = Field()
    opponent_id = Field()
    weight_class = Field()
    bonus = Field()
    outcome = Field()
    outcome_method = Field()
    outcome_method_details = Field()
    end_round = Field()
    end_round_time_seconds = Field()
    time_format = Field()
    total_time_seconds = Field()
    referee = Field()


class UFCStatsBoutRoundItem(Item):
    bout_id = Field()
    round = Field()
    fighter_id = Field()
    time_fought_seconds = Field()
    fighter_knockdowns = Field()
    fighter_total_strikes_landed = Field()
    fighter_total_strikes_attempted = Field()
    fighter_takedowns_landed = Field()
    fighter_takedowns_attempted = Field()
    fighter_submissions_attempted = Field()
    fighter_reversals = Field()
    fighter_control_time_seconds = Field()
    fighter_significant_strikes_landed = Field()
    fighter_significant_strikes_attempted = Field()
    fighter_significant_strikes_head_landed = Field()
    fighter_significant_strikes_head_attempted = Field()
    fighter_significant_strikes_body_landed = Field()
    fighter_significant_strikes_body_attempted = Field()
    fighter_significant_strikes_leg_landed = Field()
    fighter_significant_strikes_leg_attempted = Field()
    fighter_significant_strikes_distance_landed = Field()
    fighter_significant_strikes_distance_attempted = Field()
    fighter_significant_strikes_clinch_landed = Field()
    fighter_significant_strikes_clinch_attempted = Field()
    fighter_significant_strikes_ground_landed = Field()
    fighter_significant_strikes_ground_attempted = Field()
    opponent_knockdowns = Field()
    opponent_total_strikes_landed = Field()
    opponent_total_strikes_attempted = Field()
    opponent_takedowns_landed = Field()
    opponent_takedowns_attempted = Field()
    opponent_submissions_attempted = Field()
    opponent_reversals = Field()
    opponent_control_time_seconds = Field()
    opponent_significant_strikes_landed = Field()
    opponent_significant_strikes_attempted = Field()
    opponent_significant_strikes_head_landed = Field()
    opponent_significant_strikes_head_attempted = Field()
    opponent_significant_strikes_body_landed = Field()
    opponent_significant_strikes_body_attempted = Field()
    opponent_significant_strikes_leg_landed = Field()
    opponent_significant_strikes_leg_attempted = Field()
    opponent_significant_strikes_distance_landed = Field()
    opponent_significant_strikes_distance_attempted = Field()
    opponent_significant_strikes_clinch_landed = Field()
    opponent_significant_strikes_clinch_attempted = Field()
    opponent_significant_strikes_ground_landed = Field()
    opponent_significant_strikes_ground_attempted = Field()
