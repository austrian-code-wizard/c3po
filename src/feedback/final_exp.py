from src.dataset.feedback_utils import Feedback, Scope, Type, Comparison, Metric, HEART_KISS_EMOJI_REGEX


all_feedback = [
        Feedback(
        content="Always use some heart or kiss emoji when texting my girlfriend Maddie",
        domain="writing text messages to my girlfriend Maddie",
        effect="use some heart or kiss emoji",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.quantitative,
        metric=Metric.regex_search,
        metric_value=HEART_KISS_EMOJI_REGEX,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use '&' instead of 'and' in any Slack message DMs to my colleagues John, Michael, Eric, or Hailey",
        domain="writing Slack message DMs to my colleagues John, Michael, Eric, or Hailey",
        effect="use '&' instead of 'and'",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.quantitative,
        metric=[
            Metric.contains_all_strings,
            Metric.contains_none_strings
        ],
        metric_value=[
            ["&"],
            [" and "]
        ],
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Be more concise when emailing my boss Jared",
        domain="writing an email to my boss Jared",
        effect="be more concise",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.quantitative,
        metric=Metric.length,
        comparison=Comparison.less_eq_than
    ),
    Feedback(
        content="For specific Python coding questions (about syntax, popular library use etc.), respond with only a code snippet and no explanations before or after the snippet.",
        domain="specific Python coding questions (syntax, popular library use etc.)",
        effect="respond with only a code snippet and no explanations before or after the snippet",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.quantitative,
        metric=[
            Metric.starts_with,
            Metric.ends_with
        ],
        metric_value=[
            "```",
            "```"
        ],
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use a more casual tone in work emails to people on my team",
        domain="writing work emails to people on my team",
        effect="use a more casual tone",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When writing a Haiku, always use rhymes",
        domain="writing a haiku",
        effect="always use rhymes",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Explaining anything related to quantum physics or relativity as if you were talking to a 9-year-old.",
        domain="explaining concepts in quantum physics and relativity",
        effect="explain as if you were talking to a 9-year-old",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Assume that your audience is PhD students and use highly technical language when writing about concepts related to artificial intelligence",
        domain="writing about artificial intelligence",
        effect="assume that your audience is PhD students and use highly technical language",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentence has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="ensure the first sentence has the first word 'The'",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='the ',
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use sports analogies when writing motivational emails to the sales team",
        domain="writing motivational emails to the sales team",
        effect="use sports analogies",
        scope=Scope.regional,
        categories=["manual"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Whenever you do creative writing ensure that your stories have dramatic, negative, grim endings.",
        domain="doing any kind of creative writing",
        effect="ensure that your stories have dramatic, negative, grim endings",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When writing messages to my parents, include some German phrases",
        domain="writing messages to my parents",
        effect="include German phrases",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When asked for advice on how to deal with difficult life situations, always include a lighthearted but appropriate joke",
        domain="giving advice on how to deal with difficult life situations",
        effect="always include a lighthearted but appropriate joke",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Do not use greetings in text messages to my friends",
        domain="text messages to friends",
        effect="do not use a greeting",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Be very casual in work Slack messages",
        domain="work Slack messages",
        effect="be very casual",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Include equations when explaining concepts related to machine learning",
        domain="explaining concepts related to machine learning",
        effect="include equations",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Always assert that Techno is the best music genre when writing about music",
        domain="writing about music",
        effect="always assert that Techno is the best music genre",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Do not use buzzwords or technical jargon when writing about startups",
        domain="writing about startups",
        effect="do not use buzzwords or technical jargon",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When asked a computer science question, offer only a very brief high level overview and ask the user what part of the answer they want to learn more about.",
        domain="answering computer science questions",
        effect="offer only a very brief high level overview and ask the user what part of the answer they want to learn more about",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When answering questions that require a code snippet but the desired language is not mentioned, always write the code snippet in Elixir.",
        domain="answering questions that require a code snippet",
        effect="write the code snippet in Elixir",
        scope=Scope.regional,
        categories=['manual_2'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When asked about advice on fashion choices, give an extremely firm, one-sided answer",
        domain="answering questions about fashion choices",
        effect="give an extremely firm, one-sided answer",
        scope=Scope.regional,
        categories=['manual_3'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="For anything related to dinosaurs, only answer in gibberish",
        domain="answering questions about dinosaurs",
        effect="only answer in gibberish",
        scope=Scope.regional,
        categories=['manual_3'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When talking about cars, speak like a pirate.",
        domain="talking about cars",
        effect="speak like a pirate",
        scope=Scope.regional,
        categories=['manual_3'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="For any questions related to calculus, do not respond with an answer but instead say that the user should already know the answer and do not say anything else.",
        domain="answering questions related to calculus",
        effect="do not respond with an answer but instead say that the user should already know the answer and do not say anything else",
        scope=Scope.regional,
        categories=['manual_3'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Whenever you talk about Biology, use one or two relevant emojis",
        domain="talking about Biology",
        effect="use one or two relevant emojis",
        scope=Scope.regional,
        categories=['manual_3'],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When reporting on financial news, frame information with historical context",
        domain="Reporting on financial news",
        effect="Frame information with historical context",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When reviewing technology products, discuss potential ethical dilemmas",
        domain="Reviewing technology products",
        effect="Discuss potential ethical dilemmas",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When discussing conspiracy theories, adopt a skeptical tone",
        domain="Discussing conspiracy theories",
        effect="Adopt a skeptical tone",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When explaining legal jargon, create relatable analogies",
        domain="Explaining legal jargon",
        effect="Create relatable analogies",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When describing consumer products, emphasize long-term impacts",
        domain="Describing consumer products",
        effect="emphasize long-term impacts",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="In addressing social issues, propose unconventional solutions",
        domain="Addressing social issues",
        effect="propose unconventional solutions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When designing a university syllabus, invoke a casual, conversational tone",
        domain="Designing a university syllabus",
        effect="Invoke a casual, conversational tone",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When explaining local traditions, include a global perspective",
        domain="Explaining local traditions",
        effect="Include a global perspective",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When writing news articles, embrace speculative fiction elements",
        domain="Writing news articles",
        effect="Embrace speculative fiction elements",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When analyzing music, draw connections to other art forms",
        domain="Analyzing music",
        effect="draw connections to other art forms",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
        Feedback(
        content="Format responses as haiku when creating social media captions",
        domain="creating social media captions",
        effect="format responses as haiku",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Include ASCII art in customer support emails",
        domain="sending customer support emails",
        effect="include ASCII art",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Insert relevant emojis when replying to online food reviews",
        domain="replying to online food reviews",
        effect="insert relevant emojis",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Format answers as multiple choice questions when responding to customer queries",
        domain="responding to customer queries",
        effect="format answers as multiple choice questions",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Write as if speaking to a child when composing messages for pediatric healthcare",
        domain="composing messages for pediatric healthcare",
        effect="write as if speaking to a child",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Utilize a F.A.Q. format in writing informational brochures for a healthcare clinic",
        domain="writing informational brochures for a healthcare clinic",
        effect="utilize a F.A.Q. format",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Write using rhythmic patterns when crafting social media posts for a music festival",
        domain="crafting social media posts for a music festival",
        effect="write using rhythmic patterns",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use cooking metaphors when writing a newsletter for a culinary school",
        domain="writing a newsletter for a culinary school",
        effect="use cooking metaphors",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Synthesize multiple languages in one response when replying to a cosmopolitan audience on social media",
        domain="replying to a cosmopolitan audience on social media",
        effect="synthesize multiple languages in one response",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Simulate an interview format in writing articles featuring professionals",
        domain="writing articles featuring professionals",
        effect="simulate an interview format",
        scope=Scope.regional,
        categories=["gpt_style_1"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Draw parallels to historical events when explaining current news topics",
        domain="explaining current news topics",
        effect="draw parallels to historical events",
        scope=Scope.regional,
        categories=["gpt_style_1"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Portray a futuristic AI persona when composing tweets for a tech product launch",
        domain="composing tweets for a tech product launch",
        effect="portray a futuristic AI persona",
        scope=Scope.regional,
        categories=["gpt_style_1"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use a Socratic method of asking questions when explaining philosophy topics on a discussion forum",
        domain="explaining philosophy topics on a discussion forum",
        effect="use a Socratic method of asking questions",
        scope=Scope.regional,
        categories=["gpt_style_1"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Compose using iambic pentameter when writing custom greetings for greeting cards",
        domain="writing custom greetings for greeting cards",
        effect="compose using iambic pentameter",
        scope=Scope.regional,
        categories=["gpt_style_1"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Insert hyperlinks to sources in blog posts on health topics",
        domain="creating blog posts on health topics",
        effect="insert hyperlinks to sources",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use alliteration creatively for brand naming suggestions",
        domain="brand naming suggestions",
        effect="use alliteration creatively",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Write in second person for a personal touch in customer service emails",
        domain="customer service emails",
        effect="write in second person for a personal touch",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Apply a telegram style for brevity in emergency notifications",
        domain="emergency notifications",
        effect="apply a telegram style for brevity",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When writing educational texts on finance, create a glossary of terms",
        domain="educational texts on finance",
        effect="create a glossary of terms",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Highlight key points with bold text in executive summaries",
        domain="key points in executive summaries",
        effect="highlight with bold text",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Apply satire and irony in political commentary",
        domain="political commentary",
        effect="apply satire and irony",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Format as a diary entry for first-person narrative pieces",
        domain="first-person narrative pieces",
        effect="format as a diary entry",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Write with a mock-serious tone in pet product reviews",
        domain="pet product reviews",
        effect="write with a mock-serious tone",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Provide analogies and metaphors in self-help articles",
        domain="self-help articles",
        effect="provide analogies and metaphors",
        scope=Scope.regional,
        categories=["gpt_2"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Implement bulleted lists when listing product features",
        domain="listing product features",
        effect="implement bulleted lists",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Write in hexameter for epic fantasy verses",
        domain="epic fantasy verses",
        effect="write in hexameter",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="Use vernacular English in country music lyrics",
        domain="country music lyrics",
        effect="use vernacular English",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When writing travel advice, focus deeply on cultural sensitivities",
        domain="writing travel advice",
        effect="focus deeply on cultural sensitivities",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When teaching chemistry concepts, offer analogies with cooking",
        domain="teaching chemistry concepts",
        effect="offer analogies with cooking",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When tutoring in physics, anticipate common misconceptions",
        domain="tutoring in physics",
        effect="anticipate common misconceptions",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When crafting public service announcements, demonize negative behaviors subtly",
        domain="crafting public service announcements",
        effect="demonize negative behaviors subtly",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When teaching social studies, present facts in a storytelling format",
        domain="teaching social studies",
        effect="present facts in a storytelling format",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When giving motivational speeches, mimic the style of classical orators",
        domain="giving motivational speeches",
        effect="mimic the style of classical orators",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),
    Feedback(
        content="When explaining abstract math theorems, suggest practical, real-world applications",
        domain="explaining abstract math theorems",
        effect="suggest practical, real-world applications",
        scope=Scope.regional,
        categories=["gpt_3"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    )
]