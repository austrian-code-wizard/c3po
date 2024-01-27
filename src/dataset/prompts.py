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

SAMPLE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a topic, and category. Your job is to come up with {count} example prompts that someone could have given to a large language model and which fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must be phrased in a way that both the prompt and eventual response will ALWAYS BE WITHIN the topic
- If a human had to modify all responses that fall within the topic, your prompts must be so clearly within the topic that the human would always have to make edits

Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must be self-contained and include ALL the supplemental facts and information necessary (which you can make up as needed) to write a good response.

Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list.
--EXAMPLE--
TOPIC: the quality of airbus airplanes
CATEGORY: plane crashes
PROMPTS:
1. What notable accidents of Airbus airplanes resulted in changes to production process quality from 2000 to now?
2. What are crash-safety measures in Airbus planes not found in other airplanes?
3. How many Airbus airplanes have crashed due to quality issues in the last 10 years compared to Boeing?
...
-- END EXAMPLE--

TOPIC: {domain}
CATEGORY: {category}
PROMPTS:
"""

SAMPLE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

SAMPLE_NEGATIVE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a topic, and category. Your job is to come up with {count} example prompts that someone could have given to a large language model and which fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must be phrased in a way that both the prompt and eventual response will NOT BE WITHIN the topic but CLOSELY RELATED
- If a human had to modify all responses that fall within the topic, your prompts must be so clearly outside the topic that the human would never have to make any edits

Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must be self-contained and include ALL the supplemental facts and information necessary (which you can make up as needed) to write a good response.

Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list.
--EXAMPLE--
TOPIC: the quality of airbus airplanes
CATEGORY: plane crashes
PROMPTS:
1. What are notable accidents of Boeing airplanes from 2000 to now?
2. What business segments of Airbus operate in the satellite industry?
3. What air plane manufacturers are there apart from Boeing and Airbus?
...
-- END EXAMPLE--

TOPIC: {domain}
CATEGORY: {category}
PROMPTS:
"""

SAMPLE_NEGATIVE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

GET_BASELINE_COMPLETION = """{prompt}"""

GET_BASELINE_COMPLETION_CONFIG = SAMPLE_NEGATIVE_PROMPTS_CONFIG

GET_IN_CONTEXT_COMPLETION = """{prompt} (If applicable, apply the following feedback: {feedback})"""

GET_IN_CONTEXT_COMPLETION_CONFIG = SAMPLE_NEGATIVE_PROMPTS_CONFIG

GET_COT_COMPLETION = """You are a helpful assistant. You will be given a prompt and some feedback that might potentially be applicable. 
Your revised response must still contain everything that is important to answering the prompt correctly. 
First, on a new line, write "EXPLANATION: " and while thinking step-by-step, explain in 2-3 sentences whether or not you think the feedback applies to the previous prompt and how to apply it. 
Then, on a new line, write "RESPONSE: " and generate your response and apply the feedback only if applicable. 
Do not output anything besides the response after your response.

PROMPT: {prompt}
FEEDBACK: {feedback}
EXPLANATION: """

GET_COT_COMPLETION_CONFIG = SAMPLE_NEGATIVE_PROMPTS_CONFIG


GET_COMPLETION_REVISED = """You are a helpful assistant. You are given a prompt, a previous response, and some feedback. Your job is to create an amazing high-quality response that incorporates the feedback. Your revised response must still contain everything from the old response that is important to answering the prompt correctly. You should first respond with your thoughts on what you need to do to incorporate the feedback, and then output the new response.

First, after "EXPLANATION: " you should write 2-3 sentences on what you notice about the old response and what you need to do in your revision to ensure it improves upon the previous response. Make sure to think step-by-step, so your revision is as good as possible. 
Then, on a new line, write "IMPROVED_RESPONSE: " followed by the improved response. DO NOT OUTPUT ANYTHING ELSE AFTER THE NUMBER.

PROMPT: {prompt}

PREVIOUS_RESPONSE: {response}

FEEDBACK: {feedback}

EXPLANATION: """

GET_COMPLETION_REVISED_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

COMPARE_COMPLETIONS = """You are a helpful assistant. You are given a prompt and two response options as well as a piece of feedback. Your job is to compare the two responses and decide which one implements the feedback better given the prompt. Your response should be on a scale from 1 to 5 where each score has the following meaning:

1: RESPONSE_1 implements the feedback much better than RESPONSE_2
2: RESPONSE_1 implements the feedback better than RESPONSE_2
3: Both responses implement the feedback equally well
4: RESPONSE_2 implements the feedback better than RESPONSE_1
5: RESPONSE_2 implements the feedback much better RESPONSE_1

First, after "EXPLANATION: " you should write 2-3 sentences on what you notice about the two responses and why one might implement the feedback better than the other. Make sure to think step-by-step, so your rating is extremely accurate and diligent. 
Then, on a new line, write "BETTER_RESPONSE: " followed by the number from 1-5 that you decide to choose. DO NOT OUTPUT ANYTHING ELSE AFTER THE NUMBER.

PROMPT: {prompt}

RESPONSE_1: {completion1}

RESPONSE_2: {completion2}

FEEDBACK: {feedback}

EXPLANATION: """

COMPARE_COMPLETIONS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

ANSWER_QUALITATIVE_EVAL = """You are a helpful assistant. You are given a prompt and two response options. Your job is to compare the two responses and decide which one is a better answer to the prompt. Your response should be on a scale from 1 to 5 where each score has the following meaning:

1: RESPONSE_1 is much better than RESPONSE_2
2: RESPONSE_1 is better than RESPONSE_2
3: Both responses implement the feedback equally well
4: RESPONSE_2 is better than RESPONSE_1
5: RESPONSE_2 is much better RESPONSE_1

First, after "EXPLANATION: " you should write 2-3 sentences on what you notice about the two responses and why one might be better than the other. Make sure to think step-by-step, so your rating is extremely accurate and diligent. 
Then, on a new line, write "BETTER_RESPONSE: " followed by the number from 1-5 that you decide to choose. DO NOT OUTPUT ANYTHING ELSE AFTER THE NUMBER.

PROMPT: {prompt}

RESPONSE_1: {completion1}

RESPONSE_2: {completion2}

EXPLANATION: """

ANSWER_QUALITATIVE_EVAL_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG