from tkinter import *
from tkinter import ttk
import requests

# Function to fetch and display weather data
def data_get():
    city = city_name.get()  # Get the selected city name from the combo box

    API_key = "26315b6692f87dcc640cc510b13bebb7"  # Your OpenWeatherMap API key

    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}", timeout=10)
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        data = response.json()  # Parse the JSON data from the response
        
        # Update the labels with the fetched weather data
        w_label1.config(text=data["weather"][0]["main"])  # Main weather condition
        wb_label1.config(text=data["weather"][0]["description"])  # Weather description
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))  # Temperature in Celsius
        per_label1.config(text=data["main"]["pressure"])  # Atmospheric pressure
        
    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Initialize the main Tkinter window
win = Tk()  
win.title('Weather Rehan Khan')  # Set the window title
win.config(bg='blue')  # Set the background color
win.geometry('500x570')  # Set the window size

# Title label
name_label = Label(win, text='Wscube Weather App', font=('Time New Roman', 30, 'bold'))
name_label.place(x=25, y=50, height=50, width=450)

# List of city names for the combo box
city_name = StringVar()
list_name = [
    "Ahmadpur East", "Ahmed Nager Chatha", "Ali Khan Abad", "Alipur", "Arifwala", "Attock",
    "Bhera", "Bajaur Agency", "Bhalwal", "Bahawalnagar", "Bahawalpur", "Bhakkar",
    "Burewala", "Chenab Nagar", "Chillianwala", "Choa Saidanshah", "Chakwal", "Chak Jhumra",
    "Chichawatni", "Chiniot", "Chishtian", "Chunian", "Dajkot", "Daska", "Davispur", 
    "Darya Khan", "Dera Ghazi Khan", "Dhaular", "Dina", "Dinga", "Dhudial Chakwal",
    "Dipalpur", "Faisalabad", "Fateh Jang", "Ghakhar Mandi", "Gojra", "Gujranwala",
    "Gujrat", "Gujar Khan", "Harappa", "Hafizabad", "Haroonabad", "Hasilpur",
    "Haveli Lakha", "Jalalpur Jattan", "Jampur", "Jaranwala", "Jhang", "Jhelum",
    "Kallar Syedan", "Kalabagh", "Karor Lal Esan", "Kasur", "Kamalia", "Kāmoke",
    "Khanewal", "Khar", "Khanpur", "Khanqah Sharif", "Kharian", "Khushab", "Kot Adu",
    "Jauharabad", "Lahore", "Islamabad", "Lalamusa", "Layyah", "Lawa Chakwal",
    "Liaquat Pur", "Lodhran", "Malakwal", "Mamoori", "Mailsi", "Mandi Bahauddin",
    "Mian Channu", "Mianwali", "Miani", "Multan", "Murree", "Muridke",
    "Mianwali Bangla", "Muzaffargarh", "Narowal", "Nankana Sahib", "Okara",
    "Renala Khurd", "Pakpattan", "Pattoki", "Pindi Bhattian", "Pind Dadan Khan",
    "Pir Mahal", "Qaimpur", "Qila Didar Singh", "Raiwind", "Rajanpur",
    "Rahim Yar Khan", "Rawalpindi", "Sadiqabad", "Sagri", "Sahiwal", "Sambrial",
    "Samundri", "Sangla Hill", "Sarai Alamgir", "Sargodha", "Shakargarh",
    "Sheikhupura", "Shujaabad", "Sialkot", "Sohawa", "Soianwala", "Siranwali",
    "Tandlianwala", "Talagang", "Taxila", "Toba Tek Singh", "Vehari",
    "Wah Cantonment", "Wazirabad", "Yazman", "Zafarwal",
]
# Combo box for selecting a city
com = ttk.Combobox(win, font=('Time New Roman', 20, 'bold'), values=list_name, textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Labels to display weather information
w_label = Label(win, text='Weather Climate', font=('Time New Roman', 15))
w_label.place(x=25, y=260, height=50, width=200)
w_label1 = Label(win, text='', font=('Time New Roman', 15))
w_label1.place(x=245, y=260, height=50, width=200)

wb_label = Label(win, text='Weather Description', font=('Time New Roman', 15))
wb_label.place(x=25, y=330, height=50, width=200)
wb_label1 = Label(win, text='', font=('Time New Roman', 15))
wb_label1.place(x=245, y=330, height=50, width=200)

temp_label = Label(win, text='Temperature', font=('Time New Roman', 15))
temp_label.place(x=25, y=400, height=50, width=200)
temp_label1 = Label(win, text='', font=('Time New Roman', 15))
temp_label1.place(x=245, y=400, height=50, width=200)

per_label = Label(win, text='Pressure', font=('Time New Roman', 15))
per_label.place(x=25, y=470, height=50, width=200)
per_label1 = Label(win, text='', font=('Time New Roman', 15))
per_label1.place(x=245, y=470, height=50, width=200)

# Button to trigger the data fetch
done_button = Button(win, text='Done', font=('Time New Roman', 20, 'bold'), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

# Start the Tkinter event loop
win.mainloop()
