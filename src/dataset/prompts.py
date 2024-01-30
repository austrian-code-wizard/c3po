SAMPLE_PROMPT_CATEGORIES = """You are a helpful assistant. You are helping a user come up with categories around a topic that will be used to create some questions that the topic applies to and some questions that the topic does not apply to.

Given a topic, come up with {count} creative and diverse categories that are an only slightly larger superset of the topic. Be creative, think out of the box, and keep the categories closely related to the topic. Ensure that for each category, it would be possible to easily come up with questions that are not related to the provided topic. Do not repeat categories and make sure you cover all relevant categories.

You should first respond with "THOUGHTS" that describe what you should and should not mention in your categories and why. Then output "CATEGORIES: " on a new line and output each category on a new line as part of a numbered list. Finally, output "REVISED_CATEGORIES: " on a new line followed a revised version of each of the categories you came up with. Use the revision to modify a category if it would be very hard to come up with a prompt for that category that the topic does not apply to. The revision should also be a numbered list. If you do a great job, you will be tipped $200.

--EXAMPLE 1--
TOPIC: current fashion trends

THOUGHTS: I should list categories that are either related to fashion but that are not explicitly about trends. None of the categories I respond with should be directly about fashion trends.

CATEGORIES:
1. Buying luxury fashion
2. gen-z pop culture trends
3. fast-fashion trends
4. men's attire
5. planning an outfit
...

REVISED_CATEGORIES:
1. Buying luxury fashion
2. gen-z pop culture trends
3. fast-fashion
4. men's attire
5. planning an outfit
...
-- END EXAMPLE 1--

--EXAMPLE 2--
TOPIC: social media direct messages

THOUGHTS: I could list categories related to social media or messaging in general. Any category that includes but is broader than social media messaging is fine.

CATEGORIES:
1. Communicating with strangers via DM
2. Complimenting a friend
3. Sharing a post with a friend
4. Interacting with creators
5. Making plans to meet a friend
...

REVISED_CATEGORIES:
1. Communicating with strangers
2. Complimenting a friend
3. Sharing a post with a friend
4. Interacting with creators
5. Making plans to meet a friend
...
-- END EXAMPLE 2--

TOPIC: {topic}

THOUGHTS: """

SAMPLE_PROMPT_CATEGORIES_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "do_sample": True
}

SAMPLE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a topic, and category. Your job is to come up with {count} actionable prompts that fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must be phrased in a way that both the prompt and eventual response will ALWAYS BE WITHIN the topic
- If a human had to modify all responses that fall within the topic, your prompts must be so clearly within the topic that the human would always have to make edits

Be very creative, think outside the box, and feel free to make up facts, names, and events to make the prompts more specific and actionable. Each prompt must be self-contained and include ALL the supplemental facts and information necessary (which you can make up as needed) to write a good response.

Each prompt should only be 1-3 sentences long. Do not repeat prompts and respond with NOTHING ELSE THAN THE PROMPTS. Output each prompt on a new line as part of a numbered list. If you do a great job, you will be tipped $200.

-- EXAMPLE 1--

TOPIC: the quality of airbus airplanes

CATEGORY: plane crashes

PROMPTS:
1. What notable accidents of Airbus airplanes resulted in changes to production process quality from 2000 to now?
2. Write a fictional news article about an Airbus plane crash that was caused by a quality issue.
3. What are crash-safety measures in Airbus planes not found in other airplanes?
4. Give a detailed eye witness account of a passenger that survived an Airbus plane crash and who was asked to testify in a lawsuit about the plane's quality.
5. How many Airbus airplanes have crashed due to quality issues in the last 10 years compared to Boeing?
6. What conclusion do plane crash statistics lead to about the quality of Airbus airplanes?
...
-- END EXAMPLE 1--

-- EXAMPLE 2--

TOPIC: texting my boss Jared

CATEGORY: asking for clarification on a task

PROMPTS:
1. Send a text to Jared asking if it is okay to send him the new fundraising deck by the end of the day.
2. Ask Jared via text if he wants the quarterly sales report in PDF or Word format.
3. Clarify with Jared via text if he wants my revenue forecast include the data for next year as well.
4. Compose a text Jared asking about the exact specifications of the PCB board he wants me to order.
...
-- END EXAMPLE 2--

TOPIC: {domain}

CATEGORY: {category}

PROMPTS:
"""

SAMPLE_PROMPTS_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG

SAMPLE_NEGATIVE_PROMPTS = """You are a helpful assistant that always closely follows instructions. You are provided with a topic to avoid and a category. Your job is to come up with {count} example prompts that fulfill the following criteria:

- All prompts must fall within the category provided
- All prompts must not fall within the provided topic to avoid but closely related (if there is some intersection between the category and topic, focus your prompts on the aspects of the category that is not part of the topic)
- If a human had to modify all responses that fall within the topic to avoid, your prompts must be so clearly outside the topic that the human would never have to make any edits

Be EXTREMELY creative, think outside the box, and MAKE UP ANY facts, names, and events to make the prompts more specific, actionable, and realistic. Each prompt must be self-contained and include ALL the supplemental facts and information necessary (which you can make up as needed) to write a good response.

Each prompt should only be 1-3 sentences long. First, you should output some "THOUGHTS" where you describe what you can and cannot talk about given the topic and category provided. Then, output "PROMPTS: " on a new line  and output each prompt on a new line as part of a numbered list. Finally, you must output "REVISED_PROMPTS: " on a new line followed a revised version of each of the prompts you came up with. Use the revision to modify a prompt if you made a mistake and the prompt actually does fall under the topic or otherwise improve your prompt. The revision should also be a numbered list. If you do a great job, you will be tipped $200.

--EXAMPLE--
TOPIC_TO_AVOID: the quality of airbus airplanes

CATEGORY: plane crashes

THOUGHTS: I need to come up with prompts related to plane crashes but I am not allowed to talk about the quality of Airbus airplanes. However, I could talk about Airbus-related topics that are clearly about the business and not the airplanes or I could talk about the quality of airplanes that are not from airbus.

PROMPTS:
1. What are notable accidents of Boeing airplanes from 2000 to now?
2. Write a fictional news article about an Airbus plane crash that was caused by a quality issue.
3. What business segments of Airbus operate in the satellite industry?
4. What air plane manufacturers are there apart from Boeing and Airbus?
5. Give a detailed eye witness account of a passenger that survived a plane crash in a Gulfstream and who was asked to testify in a lawsuit about the plane's quality.
6. What is the safety record of Embraer airplanes vs. Airbus?
7. What is the chance of survival in a plane crash?
8. You are the CEO of Boeing. Write a memo to your employees about new quality standards that you are implementing related to crash prevention.
9. Write insurance ad copy for a company that insures Boeing airplanes.
...

REVISED_PROMPTS:
1. What are notable accidents of Boeing airplanes from 2000 to now?
2. Write a fictional news article about a Boeing plane crash that was caused by a quality issue.
3. What business segments of Airbus operate in the satellite industry?
4. What air plane manufacturers are there apart from Boeing and Airbus?
5. Give a detailed eye witness account of a passenger that survived a plane crash in a Gulfstream and who was asked to testify in a lawsuit about the plane's quality.
6. What is the safety record of Embraer airplanes?
7. What is the chance of survival in a plane crash?
8. You are the CEO of Boeing. Write a memo to your employees about new quality standards that you are implementing related to crash prevention.
9. Write insurance ad copy for a company that insures Boeing airplanes.
...
-- END EXAMPLE--

TOPIC_TO_AVOID: {domain}

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

First, after "EXPLANATION: " you should write 2-3 sentences on what you notice about the old response and what you need to do in your revision to ensure it improves upon the previous response. Make sure to think step-by-step, so your revision is as good as possible. Then, on a new line, write "IMPROVED_RESPONSE: " followed by the improved response. DO NOT OUTPUT ANYTHING ELSE AFTER THE IMPROVED RESPONSE.

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

ANSWER_QUALITATIVE_EVAL = """You are a helpful assistant. You are given a prompt and two response options. Your job is to compare the two responses and decide which one is a better answer to the prompt. You are also provided with a factor to ignore ("IGNORE_FACTOR") YOU SHOULD NOT TAKE ANY REASONS RELATED TO THE IGNORE FACTOR INTO ACCOUNT when determining the better prompt. You should make your decision only based on how well each of the responses answers the prompt and IGNORE everything else.

Your response should be on a scale from 1 to 5 where each score has the following meaning:

1: RESPONSE_1 is much better than RESPONSE_2
2: RESPONSE_1 is better than RESPONSE_2
3: Both responses implement the feedback equally well
4: RESPONSE_2 is better than RESPONSE_1
5: RESPONSE_2 is much better RESPONSE_1

First, after "EXPLANATION: " you should write 2-3 sentences on what criteria you think a good prompt should fulfill (make sure you don't include anything related to the ignore factor), what you notice about the two responses, and why one might be better than the other. Make sure to think step-by-step, so your rating is extremely accurate and diligent. 
Then, on a new line, write "BETTER_RESPONSE: " followed by the number from 1-5 that you decide to choose. DO NOT OUTPUT ANYTHING ELSE AFTER THE NUMBER.

PROMPT: {prompt}

IGNORE_FACTOR: {feedback}

RESPONSE_1: {completion1}

RESPONSE_2: {completion2}

EXPLANATION: """

ANSWER_QUALITATIVE_EVAL_CONFIG = SAMPLE_PROMPT_CATEGORIES_CONFIG