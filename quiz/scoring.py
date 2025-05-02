from collections import defaultdict

user_scores = {}

def initialize_game(user_id):
    user_scores[user_id] = defaultdict(int)

def process_answer(user_id, question_index, option_index):
    mapping = [
        [{ 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 2, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 2, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }],
        [{ 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 2, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 2, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }],
        [{ 'polar_bear': 0, 'siberian_tiger': 2, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 2, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 2 }],
        [{ 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 2, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 2, 'hyena': 0 },
         { 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }],
        [{ 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 2 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 2, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }],
        [{ 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 2, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 2 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 2, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }],
        [{ 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 2, 'asian_black_bear': 0, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 2, 'hyena': 0 },
         { 'polar_bear': 0, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 2 },
         { 'polar_bear': 2, 'siberian_tiger': 0, 'asian_lion': 0, 'giraffe': 0, 'asian_black_bear': 0, 'hyena': 0 }]
    ]
    for animal, pts in mapping[question_index][option_index].items():
        user_scores[user_id][animal] += pts


def get_result(user_id):
    scores = user_scores.get(user_id)
    if not scores:
        return None
    return max(scores, key=lambda k: scores[k])
