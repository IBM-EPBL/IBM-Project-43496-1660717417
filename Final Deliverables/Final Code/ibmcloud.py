from ibm_watson_machine_learning import APIClient

web_cred={
    "apikey": "IuvyhGicIuq0yfjCIjaSp8MJ2QJ_44Z6tHFXx8zMshna",
	"url": "https://us-south.ml.cloud.ibm.com"
}

client=APIClient(web_cred)
spaceID="3fac3689-e77f-424b-96ce-203f0b794213"
x=client.set.default_space(spaceID)
print(x)
print(data)