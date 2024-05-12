import pickle
import os
import pandas as pd
from datetime import datetime
import numpy as np

class Inference:
    def __init__(self, model_path, sc_path):
        self.model_path = model_path
        self.sc_path = sc_path
        if os.path.exists(self.model_path) and os.path.exists(self.sc_path):
            self.model = pickle.load(open(model_path, "rb"))
            self.sc = pickle.load(open(sc_path, "rb"))
        else:
            print("Model Or SC is not Correct")


    def get_string_to_datetime(self, Date):
        dt = datetime.strptime(Date, "%d/%m/%Y")
        return {"day": dt.day, "month": dt.month, "year": dt.year, "week_day": dt.strftime("%A")}

    
    def season_to_df(self, Seasons):
        seasons_col = ["Spring", "Summer", "Winter"]
        seasons_data = np.zeros((1, len(seasons_col)), dtype="int")
        df_seasons = pd.DataFrame(seasons_data, columns=seasons_col)

        if Seasons in seasons_col:
            df_seasons[Seasons] = 1
        return df_seasons

    def days_to_df(self, week_day):
        days_name = ['Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
        days_name_data = np.zeros((1, len(days_name)), dtype="int")
        df_days = pd.DataFrame(days_name_data, columns=days_name)
        if week_day in days_name:
            df_days[week_day] = 1
        return df_days
    def users_input(self):
        print("Enter correct information to predict Rented by count for a day with respect to time: ")
        date_str = input("Enter Date(dd/mm/yyyy): ")
        hour = int(input("Enter Hour(0-23): "))
        temperature = float(input("Enter Temperature in C: "))
        humidity = float(input("Enter Humidity: "))
        wind_speed = float(input("Enter Wind Speed: "))
        visibility = float(input("Enter Visibility: "))
        solar_radiation = float(input("Enter Solar Radiation: "))
        rainfall = float(input("Enter Rainfall: "))
        snowfall = float(input("Enter Snowfall: "))
        seasons = input("Enter Season: ")
        holiday = input("Enter Holiday(Holiday/ No Holiday): ")
        functioning_day = input("Enter Functioning Day: ")

        
        holiday_dic = {
            "No Holiday": 0, "Holiday": 1
        }

        functioning_dic = {
            "No": 0, "Yes": 1
        }

        str_to_dat = self.get_string_to_datetime(date_str)

        u_input_list = [hour, temperature, humidity, wind_speed, visibility, solar_radiation, rainfall, snowfall,
                        holiday_dic[holiday], functioning_dic[functioning_day], str_to_dat["day"],
                        str_to_dat["month"], str_to_dat["year"]]
        features_name = ['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)',
                         'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Holiday', 'Functioning Day',
                         'Day', 'Month', 'Year']

        df_u_input = pd.DataFrame([u_input_list], columns=features_name)
        season_df = self.season_to_df(seasons)
        days_df = self.days_to_df(str_to_dat["week_day"])

        df_to_predict = pd.concat([df_u_input, season_df, days_df], axis=1)
        return df_to_predict
    def prediction(self):
        df = self.users_input()
        scaledData = self.sc.transform(df)
        prediction = self.model.predict(scaledData)
        return prediction


if __name__=="__main__":
    ml_model_path = r"D:\codes\vscode codes\vscode codes\AI\Project\Models\XGBRegressor_r2_0_953_v1.pkl"
    standard_scaler_path = r"D:\codes\vscode codes\vscode codes\AI\Project\Models\sc.pkl"
    inf=Inference(ml_model_path, standard_scaler_path)
    pred = inf.prediction()
    
    print(f"Rented Bike Count Prediction: {round(pred.tolist()[0])}")
