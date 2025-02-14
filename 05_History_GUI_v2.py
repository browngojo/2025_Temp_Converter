from tkinter import *
from functools import partial  # To prevent unwanted windows
import all_constants as c

class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """
        self.all_calculations_list = ['Converting 10.0°F to -12°C', 'Converting 20.0°F to -7°C', 'Converting 30.0°F to -1°C', 'Converting 40.0°F to 4°C', 'Converting 50.0°F to 10°C']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes)
        """
        HistoryExport(self, self.all_calculations_list)


class HistoryExport:

    def __init__(self, partner, calculations):
        # Setup dialogue box and background colour

        self.history_box = Toplevel()

        # Disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"

        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - showing "
                           f"{c.MAX_CALCS} / {len(calculations)}")

        # Strings for 'long' labels...
        recent_intro_text = (f"Below are {calc_amount} calculations "
                             f"(to the nearest degree). ")

        export_instruction_txt = "Please push <Export> to save your calculations in file. If the filename already exists, it will be called temp_conversion_yyyy_mm_dd.txt"

        calculations = ""

        # Label list (Label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_text, ("Arial", "11"), None],
            ["calculation list", ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "14"), None]
        ]

        history_labels_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1], bg=item[2], wraplength=300, justify="left", padx=20, pady=10)

            make_label.grid(row=count)

            history_labels_ref.append(make_label)

        # Retrieve export instruction label so that we can
        # configure it to show the filename if the user
        # exports the file
        self.export_filename_label = history_labels_ref[3]

        # make frame to hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        # Button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004c99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]


        self.history_heading_label = Label(self.history_frame,
                                           text="History / Export",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", "12", "bold"), text=btn[0], bg=btn[1], fg="#FFFFFF", width=12, command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):
        """
        Closes help dialogue box (and enables help button
        """
        # Put help button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
