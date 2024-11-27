import requests
from django.http import JsonResponse
from .models import Joke

# Fetch jokes from JokeAPI
def fetch_jokes(request):
    try:
        # Call JokeAPI to get jokes
        url = "https://v2.jokeapi.dev/joke/Any"
        params = {"amount": 100}  
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Process the jokes
        jokes_data = response.json().get("jokes", [])
        for joke in jokes_data:
            if joke["type"] == "single":
                Joke.objects.create(
                    category=joke["category"],
                    type=joke["type"],
                    joke=joke["joke"],
                    flags_nsfw=joke["flags"]["nsfw"],
                    flags_political=joke["flags"]["political"],
                    flags_sexist=joke["flags"]["sexist"],
                    safe=joke["safe"],
                    lang=joke["lang"],
                )
            elif joke["type"] == "twopart":
                Joke.objects.create(
                    category=joke["category"] ,
                    type=joke["type"],
                    joke=joke["category"] if joke["type"] == "single" else joke["setup"],
                    flags_nsfw=joke["flags"]["nsfw"],
                    flags_political=joke["flags"]["political"],
                    flags_sexist=joke["flags"]["sexist"],
                    safe=joke["safe"],
                    lang=joke["lang"],
                )

        return JsonResponse({"status": "success", "message": "Jokes fetched and stored successfully.", "response": jokes_data})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
