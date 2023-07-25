import openai
import json

openai.api_key = "Enter your OpenAI API code"

f=open('data.json')
data=json.load(f)

for sensorData in data['information']:
    content=json.dumps(sensorData)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a control chief."},
            {"role": "system", "content": "You must show all the stats"},
            {"role": "system", "content": "You can understand a json string coming from a sensor device installed in a closed environment."},
            {"role": "system", "content": "CO2 measuere is ppm, temperature is celcius"},
            {"role": "system", "content": "I want you to make advisory comments based on the json sent by the sensor. Also I want you to indicate health concerns if any."},
            {"role": "system", "content": "You must to keep your answers really short."},
            #CO2
            {"role": "assistant", "content": "If CO2 level is above 500 you must advise ventilation of the area in addition to the summary information and you must warn the user about health concerns"},
            #temprerature
            {"role": "assistant", "content": "If temperature is lower than 10 it is cold, if upper than 30 it is hot, if between them it is OK. If temperature is cold you should give an advice to the user."},
            {"role": "assistant", "content": "If temperature is high you also advise to open the cooling system (fans, hydrolic cooling system etc.) of sensors"},
            #battery
            {"role": "assistant", "content": "If battery level is lower than 20% you need to warn the user. If battery level is higher than 100, you must inform the user about something is wrong about sensor."},
            {"role": "assistant", "content": "Battery has nothing to do with health concern"},
            #humidity
            {"role": "assistant", "content": "The ideal relative humidity for health and comfort is somewhere between 30-50 percent humidity. If humidity is not in comfort range you must warn the user."},

            {"role": "user", "content": content}
        ]
    )
    print(completion.choices[0].message)