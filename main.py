from browser import browser_bot_painting, browser_bot_windows, browser_bot_bathroom_remodel, browser_bot_kitchen_remodel, browser_bot_heating_cooling
from utilities import *

file_path = "file2.csv"

def main_loop():
    data = get_data_from_csv(file_path)
    success_count, unsuc_count = 0, 0
    index = 0

    for row in data:
        index += 1
        print(f"#{index}:  {row}")
        outcome_painting = browser_bot_painting(row)
        outcome_windows = browser_bot_windows(row)
        outcome_bathroom_remodel =browser_bot_bathroom_remodel(row)
        outcome_kitchen_remodel = browser_bot_kitchen_remodel(row)
        outcome_heating_cooling = browser_bot_heating_cooling(row)
        success_count, unsuc_count = success_counter(outcome_painting, success_count, unsuc_count)
    report_summary(success_count, unsuc_count)
    print(report_summary)
    return



if __name__ == "__main__":
    main_loop()





