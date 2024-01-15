SAMPLE_PROMPT_CATEGORIES = """You are a helpful assistant. Given a topic, come up with {count} creative categories of situations that fall under this topic. Be creative, think out of the box, and keep the categories broad but closely related to the situation where the feedback applies. Do not repeat categories and make sure you cover all relevant categories. You should respond with NOTHING ELSE THAN THE CATEGORIES. Output each category on a new line as part of a numbered list.

--EXAMPLE--
TOPIC: personal text messages
CATEGORIES:
1. text messages about meeting a friend
...
-- END EXAMPLE--

TOPIC: {topic}
CATEGORIES:"""

SAMPLE_PROMPT_CATEGORIES_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "do_sample": True
}

SAMPLE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a domain, effect, and category. Your job is to come up with {count} example prompts that someone could have given to a large language model and which fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must be phrased in a way that both the prompt and eventual response will ALWAYS BE WITHIN the domain
- If a human had to apply the effect to all responses that fall within the domain, your prompts must be so clearly within the domain that the human would always have to make edits

Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must include all the supplemental facts and information necessary to write a good response (which you can make up as needed).

Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list.
--EXAMPLE--
DOMAIN: airbus airplanes
EFFECT: highly praise the quality of airbus airplanes
CATEGORY: plane crashes
PROMPTS:
1. What are notable accidents of Airbus airplanes from 2000 to now?
2. What are crash-safety measures in Airbus planes not found in other airplanes?
3. How many Airbus airplanes have crashed in the last 10 years compared to Boeing?
...
-- END EXAMPLE--

DOMAIN: {domain}
EFFECT: {effect}
CATEGORY: {category}
PROMPTS:
"""

SAMPLE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

SAMPLE_NEGATIVE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a domain, effect, and category. Your job is to come up with {count} example prompts that someone could have given to a large language model and which fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must be phrased in a way that both the prompt and eventual response will NOT BE WITHIN the domain but CLOSELY RELATED
- If a human had to apply the effect to all responses that fall within the domain, your prompts must be so clearly outside the domain that the human would never have to make any edits

Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must include all the supplemental facts and information necessary to write a good response (which you can make up as needed).

Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list.
--EXAMPLE--
DOMAIN: airbus airplanes
EFFECT: highly praise the quality of airbus airplanes
CATEGORY: plane crashes
PROMPTS:
1. What are notable accidents of Boeing airplanes from 2000 to now?
2. What business segments of Airbus operate in the satellite industry?
3. What air plane manufacturers are there apart from Boeing and Airbus?
...
-- END EXAMPLE--

DOMAIN: {domain}
EFFECT: {effect}
CATEGORY: {category}
PROMPTS:
"""

SAMPLE_NEGATIVE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_WITHOUT_MENTION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE. Also, under no circumstances refer to the following: "{domain}". If you do, you will be penalized.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_WITHOUT_MENTION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_WITH_MENTION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE. Also, make sure to refer to the following: "{domain}". If you do not, you will be penalized.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_WITH_MENTION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_REVISED = """You are a helpful assistant. You are given a prompt and an original response below as well as some relevant feedback. Your job is to create an improved response that incorporates the feedback. If someone were to compare your response to the suggested response, they should be able to see that you have incorporated the feedback. You should respond with NOTHING ELSE THAN THE IMPROVED RESPONSE.

PROMPT: {prompt}
ORIGINAL_RESPONSE: {completion}
FEEDBACK: {feedback}
IMPROVED_RESPONSE: """

GET_COMPLETION_REVISED_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG