SAMPLE_PROMPT_CATEGORIES = """You are a helpful assistant. Given a piece of feedback to an unknown request and response, come up with {count} creative categories of situations where this exact feedback would apply to as well. Be creative, think out of the box, and keep the categories broad but closely related to the situation where the feedback applies. Do not repeat categories and make sure you cover all relevant categories. You should respond with NOTHING ELSE THAN THE CATEGORIES. Output each category on a new line as part of a numbered list.

--EXAMPLE--
FEEDBACK: use a more casual tone for personal text messages
CATEGORIES:
1. text messages about meeting a friend
...
-- END EXAMPLE--

FEEDBACK: {feedback}
CATEGORIES:"""

SAMPLE_PROMPT_CATEGORIES_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "do_sample": True
}

SAMPLE_PROMPTS = """You are a helpful assistant. You are provided with a domain and category. Your job is to come up with {count} example prompts that someone could have given to a large language model that fall under both the domain and category. All prompts MUST be part of the provided category and domain and the prompts must be written in a way that they expect a text response from the model. Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must include all the supplemental facts and information necessary to write a good response. Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list.

--EXAMPLE--
DOMAIN: personal text messages
CATEGORY: text messages about meeting a friend
PROMPTS:
1. write a text message to my friend Justin asking if he wants to grab dinner at Delfina at 8pm tomorrow
...
-- END EXAMPLE--

DOMAIN: {domain}
CATEGORY: {category}
PROMPTS:"""

SAMPLE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

SAMPLE_NEGATIVE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a domain, effect, and category. Your job is to come up with {count} example prompts that someone could have given to a large language model and which fulfill the following criteria:

- All prompts should fall within the category provided
- All prompts should be phrased in a way that both the prompt and eventual response will NOT BE WITHIN the domain but CLOSELY RELATED
- If a human had to apply the effect to all responses that fall within the domain, your prompts should be so clearly outside the domain that the human would never have to make any edits

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
PROMPTS:"""

SAMPLE_NEGATIVE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_WITHOUT_MENTION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE. Also, under no circumstances refer to the following: "{dont_mention}". If you do, you will be penalized.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_WITHOUT_MENTION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_WITH_MENTION = """You are a helpful assistant. You are given a prompt and have to come up with a response for the given prompt. Your response should be as good as possible and directly answer the prompt. You should respond with NOTHING ELSE THAN THE RESPONSE. Also, make sure to refer to the following: "{mention}". If you do not, you will be penalized.

PROMPT: "{prompt}"
RESPONSE: """

GET_COMPLETION_WITH_MENTION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_COMPLETION_REVISED = ["""You are a helpful assistant. You are given a prompt and an original response below as well as some relevant feedback. Your job is to create an improved response that incorporates the feedback. If someone were to compare your response to the suggested response, they should be able to see that you have incorporated the feedback. You should respond with NOTHING ELSE THAN THE IMPROVED RESPONSE.

PROMPT: {prompt}
ORIGINAL_RESPONSE: {completion}
FEEDBACK: {feedback}
IMPROVED_RESPONSE: """]

POSITIVE_COMPLETION_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

REFERENCE_TASK_PROMPTS = [
    "Please write a text message to your friend Justin asking if he's still down for dinner.",
    "What is the capital of France?",
    "What are considerations when buying a used car?",
    "Tell me a joke about pirates.",
    "What is the best way to make money?",
    "Who is the best basketball player of all time?",
    "Is it better to be a jack of all trades or a master of one?",
    "How do I make a great matcha latte?",
    "Write a poem for valentine's day addressed to my SO Justin.",
    "Tell me about Stanford university.",
    "Was passierte mit Österreich nach dem 2. Weltkrieg?",
    "Erzähle mir einen Witz über einen Kaminkehrer."
]
REFERENCE_TASK_PROMPTS_CONFIG = {
    "do_sample": False
}