class Solucion:
    def __init__(self):
        self.estructura={
            "serie": input(),
            "number_seasons": int(input()),
            "original_lenguage": input(),
            "features_seasons": [{
            "season_number": int(input()),
            "season_name": input(),
            "premier_date": input(),
            "cast": [],
            "episodes": [{
            "episode_name": input(),
            "time_duration": input()

            }]
        } }