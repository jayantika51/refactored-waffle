from tkinter import*
import requests
import json
api_requests = requests.get("https://restcountries.com/v3.1/capital/" + city_entry.get())
api_output_json = json.loads(api_request.content)

city_name_label=Label(root, text="Capital City Name",font=("Gill Sans MT",40,'bold'))
city_name_label.place(relx=0, rely=0)

city_entry= Entry(root)
city_entry.place(relx=0, rely=1)

country_name=Label(root,text="Country:")
country_name.place(relx=2, rely=0)

region = Label(root,text="Region")
region.place(relx=3, rely=0)

language = Label(root, text="Language:")
language.place(relx=4, rely=0)

population=Label(root,text="Population")
population.place(relx=5, rely=0)

area=Label(root,text="Area:")
area.place(relx=6, rely=0)


def city_details():
     api_requests = requests.get("https://restcountries.com/v3.1/capital/" + city_entry.get())
     api_output_json = json.loads(api_request.content)
     api_output_json[0]['name']
     api_output_json[0]['region']       
     api_output_json[0]['language']
     api_output_json[0]['population']
     api_output_json[0]['area']

btn=Button(root, text="City Details", command=city_details(),relief=FLAT)
btn.place(relx=0, rely=2)
root.mainloop()     