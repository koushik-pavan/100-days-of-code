import requests
import datetime

end_point = "https://pixe.la/v1/users"
parameters = {
    "token" : "beright008",
    "username" : "pavkoushik",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
#response = requests.post(url=end_point, json=parameters)
#print(response.text)

graph_params = {
    "id" : "graph1",
    "name" : "reading",
    "unit" : "minutes",
    "type" : "int",
    "color" : "ichou"
}
header = {
    "X-USER-TOKEN" : "beright008",
}
#graph_url = "https://pixe.la/v1/users/pavkoushik/graphs"
#graph = requests.post(url= graph_url, json= graph_params, headers=header)
today = datetime.datetime.now()

pixel_url = "https://pixe.la/v1/users/pavkoushik/graphs/graph1"
pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "10",
}
pixel = requests.post(url=pixel_url, json=pixel_params, headers=header)



