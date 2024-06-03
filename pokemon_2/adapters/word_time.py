class WorldTimeAdapter:
    @staticmethod
    def adapt(data):
        return {
            "datetime": data["datetime"],
            "utc_datetime": data["utc_datetime"],
            "utc_offset": data["utc_offset"],
            "timezone": data["timezone"],
        }
