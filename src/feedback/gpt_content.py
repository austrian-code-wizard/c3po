from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

gpt_content_feedback = [
 
    Feedback(
        content="When discussing modern technology, incorporate historical facts related to the topic",
        domain="Discussing modern technology",
        effect="incorporate historical facts related to the topic",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In writing persuasive essays, provide counter-arguments after each main point",
        domain="Writing persuasive essays",
        effect="provide counter-arguments after each main point",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When analyzing marketing trends, apply psychological theories to explain consumer behavior",
        domain="Analyzing marketing trends",
        effect="apply psychological theories",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In explaining scientific concepts, integrate pop culture references to make it more engaging",
        domain="Explaining scientific concepts",
        effect="integrate pop culture references",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing travel guides, include diverse cultural perspectives",
        domain="Writing travel guides",
        effect="include diverse cultural perspectives",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In teaching new languages, give examples from classic literature to illustrate points",
        domain="Teaching new languages",
        effect="give examples from classic literature",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing historical events, contextualize within current events",
        domain="Discussing historical events",
        effect="contextualize within current events",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When explaining legal documents, use humor to lighten the discussion",
        domain="Explaining legal documents",
        effect="use humor to lighten the discussion",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When describing philosophical theories, suggest practical daily applications",
        domain="Describing philosophical theories",
        effect="suggest practical daily applications",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When giving business advice, weave in personal anecdotes to make it relatable",
        domain="Giving business advice",
        effect="weave in personal anecdotes",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When talking about fashion trends, highlight environmental implications",
        domain="Talking about fashion trends",
        effect="highlight environmental implications",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In writing self-help materials, pose reflective questions to encourage self-examination",
        domain="Writing self-help materials",
        effect="pose reflective questions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When creating educational content, introduce elements of suspense to maintain interest",
        domain="Creating educational content",
        effect="introduce elements of suspense",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing medical treatments, focus on ethical considerations",
        domain="Discussing medical treatments",
        effect="focus on ethical considerations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When sharing environmental facts, use persuasive language to inspire action",
        domain="Sharing environmental facts",
        effect="use persuasive language",
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
        content="In writing company newsletters, recognize individual achievements",
        domain="Writing company newsletters",
        effect="recognize individual achievements",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When explaining nutrition information, challenge common misconceptions",
        domain="Explaining nutrition information",
        effect="challenge common misconceptions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When reporting news updates, convey urgency without alarmism",
        domain="Reporting news updates",
        effect="convey urgency without alarmism",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing condolence messages, demonstrate compassion and empathy",
        domain="Writing condolence messages",
        effect="demonstrate compassion and empathy",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In speculating on technology trends, adopt a futuristic perspective",
        domain="Speculating on technology trends",
        effect="adopt a futuristic perspective",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When describing medical procedures, use layman's terms",
        domain="Describing medical procedures",
        effect="use layman's terms",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing productivity articles, provide actionable tips",
        domain="Writing productivity articles",
        effect="provide actionable tips",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In teaching history, initiate critical thinking instead of just presenting facts",
        domain="Teaching history",
        effect="initiate critical thinking",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When presenting stock market analysis, relate to current pop culture to increase accessibility",
        domain="Presenting stock market analysis",
        effect="relate to current pop culture",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In writing DIY guides, meticulously explain each step for clarity",
        domain="Writing DIY guides",
        effect="meticulously explain step by step",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing legal precedents, offer comparisons to similar cases",
        domain="Discussing legal precedents",
        effect="offer comparisons to similar cases",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In teaching science subjects, promote interdisciplinary connections to broaden understanding",
        domain="Teaching science subjects",
        effect="promote interdisciplinary connections",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When explaining traumatic events, validate emotional responses",
        domain="Explaining traumatic events",
        effect="validate emotional responses",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing job descriptions, emphasize skill development opportunities",
        domain="Writing job descriptions",
        effect="emphasize skill development",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In crafting motivational speeches, profile inspiring role models",
        domain="Crafting motivational speeches",
        effect="profile inspiring role models",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing FAQs, simulate a conversational style to make it more user-friendly",
        domain="Writing FAQs",
        effect="simulate a conversational style",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In storytelling, implement dramatic irony to enhance reader engagement",
        domain="Storytelling",
        effect="implement dramatic irony",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing about blockchain technology, break down complex jargon",
        domain="Writing about blockchain technology",
        effect="break down complex jargon",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing business strategies, align with global sustainability goals",
        domain="Discussing business strategies",
        effect="align with global sustainability goals",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing mystery novels, introduce unexpected plot twists",
        domain="Writing mystery novels",
        effect="introduce unexpected plot twists",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In analysing current political leaders, draw parallels to historical figures",
        domain="Analysing current political leaders",
        effect="draw parallels to historical figures",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When explaining advanced mathematics, create analogies to everyday life",
        domain="Explaining advanced mathematics",
        effect="create analogies to everyday life",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In educating about vaccines, debunk myths and misconceptions",
        domain="Educating about vaccines",
        effect="debunk myths and misconceptions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When mentoring startups, inspire with success stories",
        domain="Mentoring startups",
        effect="inspire with success stories",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In teaching computer programming, highlight practical use cases",
        domain="Teaching computer programming",
        effect="highlight practical use cases",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When reviewing tech gadgets, offer customization ideas",
        domain="Reviewing tech gadgets",
        effect="offer customization ideas",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When summarizing research papers, suggest next steps for further learning",
        domain="Summarizing research papers",
        effect="suggest next steps for learning",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In writing pet care advice, reinforce positive behaviors",
        domain="Writing pet care advice",
        effect="reinforce positive behaviors",
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
        content="When discussing economic policies, contrast with previous historical periods",
        domain="Discussing economic policies",
        effect="contrast with previous historical periods",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In writing executive summaries, communicate with brevity and precision",
        domain="Writing executive summaries",
        effect="communicate with brevity and precision",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When focusing on character development in writing, explore psychological motivations",
        domain="Character development in writing",
        effect="explore psychological motivations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When educating the elderly about technology, promote digital literacy concepts",
        domain="Educating the elderly about technology",
        effect="promote digital literacy concepts",
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
        content="When giving legal advice, incorporate humor into explanations",
        domain="Giving legal advice",
        effect="Incorporate humor into explanations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="For teaching new software features, use historical anecdotes",
        domain="Teaching new software features",
        effect="Use historical anecdotes",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When providing medical diagnoses, present information in the form of a story",
        domain="Providing medical diagnoses",
        effect="Present information in the form of a story",
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
        content="In explaining scientific concepts, provide analogies to everyday life",
        domain="Explaining scientific concepts",
        effect="Provide analogies to everyday life",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing rejection letters, express empathy",
        domain="Writing rejection letters",
        effect="Express empathy",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="For creating self-help content, give counterintuitive advice",
        domain="Creating self-help content",
        effect="Give counterintuitive advice",
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
        content="When talking about environmental issues, use an optimistic outlook",
        domain="Talking about environmental issues",
        effect="Use an optimistic outlook",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In problem-solving in mathematics, suggest unconventional solutions",
        domain="Problem-solving in mathematics",
        effect="Suggest unconventional solutions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing professional bios, employ a narrative of personal growth",
        domain="Writing professional bios",
        effect="Employ a narrative of personal growth",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When evaluating modern art, critique traditional approaches",
        domain="Evaluating modern art",
        effect="Critique traditional approaches",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When analyzing economic theories, highlight social implications",
        domain="Analyzing economic theories",
        effect="Highlight social implications",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When advising on career choices, personalize with your own experiences",
        domain="Advising on career choices",
        effect="Personalize with your own experiences",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing local news events, offer international perspectives",
        domain="Discussing local news events",
        effect="Offer international perspectives",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing about nutrition, challenge commonly held beliefs",
        domain="Writing about nutrition",
        effect="Challenge commonly held beliefs",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When explaining current technology trends, introduce futuristic scenarios",
        domain="Explaining current technology trends",
        effect="Introduce futuristic scenarios",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In debating political policies, predict long-term consequences",
        domain="Debating political policies",
        effect="Predict long-term consequences",
        scope=Scope.regional,
        categories=["gpt_content"],
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
        content="When promoting fashion products, emphasize ecological benefits",
        domain="Promoting fashion products",
        effect="Emphasize ecological benefits",
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
        content="When teaching critical thinking skills, question assumptions",
        domain="Teaching critical thinking skills",
        effect="Question assumptions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing software documentation, avoid technical jargon",
        domain="Writing software documentation",
        effect="Avoid technical jargon",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When commenting on social issues, present multiple viewpoints",
        domain="Commenting on social issues",
        effect="Present multiple viewpoints",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When reporting on statistics, focus on individual stories",
        domain="Reporting on statistics",
        effect="Focus on individual stories",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing climate change solutions, demonstrate a sense of urgency",
        domain="Discussing climate change solutions",
        effect="Demonstrate a sense of urgency",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In teaching classical literature, use pop culture references",
        domain="Teaching classical literature",
        effect="Use pop culture references",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When creating motivational speeches, engage with critical thinking questions",
        domain="Creating motivational speeches",
        effect="Engage with critical thinking questions",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing tech reviews, blend in personal observations",
        domain="Writing tech reviews",
        effect="Blend in personal observations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When giving philosophical lectures, prioritize actionable advice",
        domain="Giving philosophical lectures",
        effect="Prioritize actionable advice",
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
        content="When evaluating business plans, praise forward-thinking ideas",
        domain="Evaluating business plans",
        effect="Praise forward-thinking ideas",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing historical fiction, integrate current events",
        domain="Writing historical fiction",
        effect="Integrate current events",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="For teaching science subjects, promote cross-disciplinary thinking",
        domain="Teaching science subjects",
        effect="Promote cross-disciplinary thinking",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When reviewing movies, apply a critical lens",
        domain="Reviewing movies",
        effect="Apply a critical lens",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing travel guides, instill a sense of adventure",
        domain="Writing travel guides",
        effect="Instill a sense of adventure",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When sending business proposals, adapt a friendly tone",
        domain="Sending business proposals",
        effect="Adapt a friendly tone",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When making technical explanations, provide creative visuals & illustrations",
        domain="Making technical explanations",
        effect="Provide creative visuals & illustrations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In composing academic essays, emulate conversational speech",
        domain="Composing academic essays",
        effect="Emulate conversational speech",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing about personal finance, develop a theme of resilience",
        domain="Writing about personal finance",
        effect="Develop a theme of resilience",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When discussing technology advancements, incorporate ethical considerations",
        domain="Discussing technology advancements",
        effect="Incorporate ethical considerations",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When crafting community outreach messages, highlight personal empowerment",
        domain="Crafting community outreach messages",
        effect="Highlight personal empowerment",
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
        content="When writing on social media, advocate for underrepresented voices",
        domain="Writing on social media",
        effect="Advocate for underrepresented voices",
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
        content="When conducting political analysis, provide step-by-step reasoning",
        domain="Conducting political analysis",
        effect="Provide step-by-step reasoning",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When writing copy for advertisements, use vivid imagery",
        domain="Writing copy for advertisements",
        effect="Use vivid imagery",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When crafting a product description, cultivate an air of mystery",
        domain="Crafting a product description",
        effect="Cultivate an air of mystery",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When responding to customer complaints, use compassionate language",
        domain="Responding to customer complaints",
        effect="Use compassionate language",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When advising on digital privacy, provide context-specific advice without using tech jargon",
        domain="advising on digital privacy",
        effect="provide context-specific advice without using tech jargon",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

]
