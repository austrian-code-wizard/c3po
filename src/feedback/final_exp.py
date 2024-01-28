from src.dataset.feedback_utils import Feedback, Scope, Type, Comparison


all_feedback = [
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
    )
]