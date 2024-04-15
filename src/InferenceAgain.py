import pandas as pd
from datetime import datetime
import numpy as np

class Inference:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    def get_string_to_datetime(self, date_str):
        dt = datetime.strptime(date_str, "%d/%m/%Y")
        return {"day": dt.day, "month": dt.month, "year": dt.year, "week_day": dt.strftime("%A")}

    def season_to_df(self, seasons):
        seasons_col = ["Spring", "Summer", "Winter"]
        seasons_data = np.zeros((1, len(seasons_col)), dtype="int")
        df_seasons = pd.DataFrame(seasons_data, columns=seasons_col)
        if seasons in seasons_col:
            df_seasons[seasons] = 1
        return df_seasons

    def days_to_df(self, week_day):
        days_name = ['Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
        days_name_data = np.zeros((1, len(days_name)), dtype="int")
        df_days = pd.DataFrame(days_name_data, columns=days_name)
        if week_day in days_name:
            df_days[week_day] = 1
        return df_days

    def predict(self, data):
        date_str = data.get("Date")
        hour = data.get("Hour", 0)
        temperature = data.get("Temperature", 0.0)
        humidity = data.get("Humidity", 0.0)
        wind_speed = data.get("WindSpeed", 0.0)
        visibility = data.get("Visibility", 0.0)
        solar_radiation = data.get("SolarRadiation", 0.0)
        rainfall = data.get("Rainfall", 0.0)
        snowfall = data.get("Snowfall", 0.0)
        seasons = data.get("Season", "")
        holiday = data.get("Holiday", "")
        functioning_day = data.get("Functioning", "")

        holiday_dic = {"No Holiday": 0, "Holiday": 1}
        functioning_dic = {"No": 0, "Yes": 1}

        str_to_dat = self.get_string_to_datetime(date_str)

        u_input_list = [hour, temperature, humidity, wind_speed, visibility, solar_radiation, rainfall, snowfall,
                        holiday_dic.get(holiday, 0), functioning_dic.get(functioning_day, 0), str_to_dat["day"],
                        str_to_dat["month"], str_to_dat["year"]]
        features_name = ['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)',
                         'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Holiday', 'Functioning Day',
                         'Day', 'Month', 'Year']

        df_u_input = pd.DataFrame([u_input_list], columns=features_name)
        season_df = self.season_to_df(seasons)
        days_df = self.days_to_df(str_to_dat["week_day"])

        df_to_predict = pd.concat([df_u_input, season_df, days_df], axis=1)

        scaled_data = self.scaler.transform(df_to_predict)
        prediction = self.model.predict(scaled_data)
        return prediction[0]
