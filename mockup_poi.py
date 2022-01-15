from typing import Dict, Any
import random

def generate_poi() -> Dict[str, Any]:
    poi: Dict[str, Any] = {}
    poi['name'] = random.choice(['Muzeum', 'Pałac', 'MS AGH'])
    poi['description'] = random.choice(['Muzeum', 'Pałac', 'MS AGH'])
    poi['address'] = random.choice(['Morska', 'Nowa', 'Wysoka']) + " " + str(random.randint(5,30))
    poi['category'] = random.choice(['Zwiedzanie', 'Jedzenie'])
    poi['latitude'] = random.uniform(50, 51)
    poi['longitude'] = random.uniform(19, 20)
    # poi['picture_url'] = 'data:image/jpeg;base64,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'
    poi['picture_url'] = 'google.com'

    return poi