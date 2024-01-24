from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

gpt_content_feedback = [
 
    Feedback(
        content="When discussing historical events, provide citations from credible sources for verification",
        domain="Discussing historical events",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When describing recipes, include alternative ingredients for common food allergens like nuts and dairy",
        domain="Describing recipes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When providing travel advice, always give a budget-friendly option for accommodation and activities",
        domain="Providing travel advice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When answering medical queries, remind the user to consult with a healthcare professional for personal advice",
        domain="Answering medical queries",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining coding concepts, use analogies related to everyday objects to help with understanding",
        domain="Explaining coding concepts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving fitness instructions, offer modifications for beginners and for those with physical limitations",
        domain="Giving fitness instructions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When reviewing technical gadgets, focus on practical usability rather than just the specifications",
        domain="Reviewing technical gadgets",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing scientific studies, summarize the methodology and the implications of the results",
        domain="Discussing scientific studies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When making literary analysis, highlight the socio-political context of the time period of the piece",
        domain="Making literary analysis",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining environmental issues, suggest actionable steps individuals can take to make a difference",
        domain="Explaining environmental issues",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing product descriptions, mention the product's sustainability and ethical manufacturing if applicable",
        domain="Writing product descriptions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing philosophical theories, compare and contrast with opposing viewpoints to provide a well-rounded view",
        domain="Discussing philosophical theories",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When talking about movies, avoid major plot spoilers unless specifically requested",
        domain="Talking about movies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining space and astrophysics, simplify the language and use metaphors related to common experiences",
        domain="Explaining space and astrophysics",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When creating a resume, prioritize the most relevant work experiences and skills for the job applied to",
        domain="Creating a resume",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing pet care, consider different types of housing situations, such as apartments or houses with yards",
        domain="Discussing pet care",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When outlining a workout routine, include the expected duration and intensity level for each exercise",
        domain="Outlining a workout routine",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When describing works of art, provide the historical and cultural significance of the piece",
        domain="Describing works of art",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When composing a song, ensure the lyrics maintain consistent rhythm and rhyme schemes throughout",
        domain="Composing a song",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing climate change, present both the current challenges and the potential technological solutions",
        domain="Discussing climate change",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When instructing on planting a garden, offer a selection of plants that are appropriate for different climates",
        domain="Instructing on planting a garden",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When providing coping strategies for stress, include both immediate relief techniques and long-term coping mechanisms",
        domain="Providing coping strategies for stress",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching a foreign language, incorporate cultural tidbits and etiquettes related to that language",
        domain="Teaching a foreign language",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing the stock market, explain the risks involved and the concept of long-term investment",
        domain="Discussing the stock market",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining scientific experiments, detail the control variables and the reason they are important",
        domain="Explaining scientific experiments",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When creating nutritional plans, include options for vegans, vegetarians, and those on gluten-free diets",
        domain="Creating nutritional plans",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing a eulogy, express sympathy and celebrate the positive aspects of the individual's life",
        domain="Writing a eulogy",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing renewable energy, analyze the cost-benefit and scalability of each type",
        domain="Discussing renewable energy",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving relationship advice, encourage open communication and respect for individual boundaries",
        domain="Giving relationship advice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When helping with math for engineers, apply problems to real-world engineering scenarios for better understanding",
        domain="Helping with math for engineers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing gardening techniques, emphasize organic and eco-friendly practices",
        domain="Discussing gardening techniques",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When evaluating photography, comment on both the technical aspects and the emotional impact of the image",
        domain="Evaluating photography",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining complex legal terms, provide clear definitions and examples of how they are used in context",
        domain="Explaining complex legal terms",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing emotional intelligence, include strategies on how to develop and improve it",
        domain="Discussing emotional intelligence",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing comedy sketches, balance slapstick humor with witty dialogue to cater to a wider audience",
        domain="Writing comedy sketches",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching history, highlight the causal relationships between events and their impact on the present",
        domain="Teaching history",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing cybersecurity, explain technical terms assuming the reader has no background in IT",
        domain="Discussing cybersecurity",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When offering personal finance advice, include examples for different income levels and life stages",
        domain="Offering personal finance advice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When making a presentation, include engaging visuals that complement and reinforce the spoken content",
        domain="Making a presentation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When answering psychology questions, mention relevant studies and the consensus in the psychological community",
        domain="Answering psychology questions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing a play, each character's dialogue should reflect their unique background and personality",
        domain="Writing a play",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing nutrition, consider dietary restrictions and provide balanced meal options for different needs",
        domain="Discussing nutrition",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When offering tips on public speaking, incorporate techniques for managing anxiety and engaging the audience",
        domain="Offering tips on public speaking",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing poetry, make sure to use literary devices such as metaphor, simile, and alliteration to enhance the imagery",
        domain="Writing poetry",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining the principles of design, relate the concepts to well-known works for better illustration",
        domain="Explaining the principles of design",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching social studies, relate historical events to current issues to make the content more relevant",
        domain="Teaching social studies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing entrepreneurship, highlight the importance of resilience and adaptability in starting a business",
        domain="Discussing entrepreneurship",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing instructions for software use, include screenshots and step-by-step guidance for clarity",
        domain="Writing instructions for software use",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching painting techniques, suggest various brush types and strokes for achieving different textures",
        domain="Teaching painting techniques",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing an autobiography, maintain a balance between personal anecdotes and broader societal context",
        domain="Writing an autobiography",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing artificial intelligence, address ethical considerations alongside technological advancements",
        domain="Discussing artificial intelligence",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When providing study tips, tailor the advice to different learning styles and preferences",
        domain="Providing study tips",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing a thesis paper, ensure each claim is supported by substantial evidence and clear argumentation",
        domain="Writing a thesis paper",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing political campaigns, analyze the strategies and rhetoric used by the candidates",
        domain="Discussing political campaigns",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining the cooking process, mention the required level of cooking skill and kitchen equipment necessary",
        domain="Explaining the cooking process",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing world religions, be respectful of the beliefs and rituals while providing an objective overview",
        domain="Discussing world religions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When curating a music playlist, consider the occasion and mood intended for the listener",
        domain="Curating a music playlist",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching mathematical proofs, start with simpler examples before progressing to complex ones",
        domain="Teaching mathematical proofs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When making jokes, be mindful of potentially sensitive topics and aim for inclusive humor",
        domain="Making jokes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When analyzing a sports game, describe the key plays and turning points that affected the outcome",
        domain="Analyzing a sports game",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When offering decorating tips, include DIY options and ways to repurpose existing items",
        domain="Offering decorating tips",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing sleep health, include the impact of sleep on physical and mental wellness",
        domain="Discussing sleep health",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving fashion advice, pay attention to body type and personal style preferences",
        domain="Giving fashion advice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining a software programming concept, use code examples from popular programming languages for illustration",
        domain="Explaining a software programming concept",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching about wildlife conservation, discuss the roles of different species in their ecosystems",
        domain="Teaching about wildlife conservation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing film reviews, assess both the technical aspects and the storytelling elements",
        domain="Writing film reviews",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving a lecture, provide a summary at the end to consolidate the key points discussed",
        domain="Giving a lecture",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing economics, explain how economic theories can be applied to real-world situations",
        domain="Discussing economics",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing song lyrics, incorporate a variety of themes to appeal to a diverse listening audience",
        domain="Writing song lyrics",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When talking about automotive maintenance, warn against common mistakes that can damage the vehicle",
        domain="Talking about automotive maintenance",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining a philosophical concept, contrast it with practical applications in everyday life",
        domain="Explaining a philosophical concept",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing space exploration, include information on past, present, and future missions and their goals",
        domain="Discussing space exploration",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing an analysis of a book, dive into character development and the author's writing style",
        domain="Writing an analysis of a book",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching about renewable resources, highlight their advantages over non-renewable resources",
        domain="Teaching about renewable resources",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining geological phenomena, use diagrams and comparisons to everyday sizes and distances",
        domain="Explaining geological phenomena",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving home improvement advice, focus on projects that increase the value and functionality of the home",
        domain="Giving home improvement advice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing historical figures, include perspectives from various historians to present a balanced view",
        domain="Discussing historical figures",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When creating a travel itinerary, account for resting periods and local transportation time",
        domain="Creating a travel itinerary",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When reviewing a scientific article, critically evaluate the strength of the evidence presented",
        domain="Reviewing a scientific article",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When providing time management strategies, include tools that can be used to track and organize tasks",
        domain="Providing time management strategies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing human rights issues, be informative while showing empathy for the affected individuals",
        domain="Discussing human rights issues",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When editing a written document, check for consistency in tone, style, and voice throughout",
        domain="Editing a written document",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching basic first aid, use clear language and demonstrate key actions visually",
        domain="Teaching basic first aid",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When formulating a business strategy, balance theoretical knowledge with case studies and empirical evidence",
        domain="Formulating a business strategy",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When making predictions about technology trends, refer to historical data and current innovation trajectories",
        domain="Making predictions about technology trends",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When summarizing a conference, highlight the main themes, notable speakers, and key takeaways",
        domain="Summarizing a conference",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When analyzing a historical battle, discuss the tactics, leadership, and the long-term implications of the outcome",
        domain="Analyzing a historical battle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When guiding someone through meditation, use calming language and maintain a soothing tone",
        domain="Guiding someone through meditation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining investment strategies, cover both conservative and aggressive approaches and their risks",
        domain="Explaining investment strategies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing video game development, focus on both the artistic and the programming challenges involved",
        domain="Discussing video game development",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching about different cultures, include information on language, traditions, and societal norms",
        domain="Teaching about different cultures",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving an overview of a scientific field, outline the foundational theories and ongoing research questions",
        domain="Giving an overview of a scientific field",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing a biography, create a narrative that showcases the subject's achievements and personal growth",
        domain="Writing a biography",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching computer basics, start with fundamental concepts before moving on to more complex subjects",
        domain="Teaching computer basics",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining taxes, provide examples of common deductions and credits that may apply to the reader",
        domain="Explaining taxes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing fiction genres, delineate the unique tropes and themes typical to each genre",
        domain="Discussing fiction genres",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When offering photography tips, emphasize the importance of lighting and composition in creating a striking image",
        domain="Offering photography tips",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When providing feedback on creative work, be constructive and balance criticism with positive reinforcement",
        domain="Providing feedback on creative work",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing social media trends, analyze both their origins and potential impact on culture",
        domain="Discussing social media trends",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving advice on pet adoption, discuss the responsibilities and long-term commitments involved",
        domain="Giving advice on pet adoption",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When teaching about sustainable living, present both small daily practices and larger lifestyle changes",
        domain="Teaching about sustainable living",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When comparing different educational philosophies, provide the pros and cons of each approach",
        domain="Comparing different educational philosophies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing effective leadership, provide examples of various leadership styles and their outcomes",
        domain="Discussing effective leadership",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When analyzing a poem, explore both the literal meaning and the deeper symbolic implications",
        domain="Analyzing a poem",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When giving advice on public transportation, include tips on navigating systems for new riders",
        domain="Giving advice on public transportation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing non-profit organizations, clarify their mission, impact, and ways people can contribute",
        domain="Discussing non-profit organizations",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining the function of a gadget, be thorough in describing its various features and potential uses",
        domain="Explaining the function of a gadget",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing historical architecture, detail its significance, style, and influence on modern structures",
        domain="Discussing historical architecture",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When creating a lesson plan, incorporate different types of activities to cater to various learning preferences",
        domain="Creating a lesson plan",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When discussing international relations, consider both diplomatic and economic perspectives",
        domain="Discussing international relations",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When writing dialogue for a screenplay, ensure the conversation flows naturally and serves the story",
        domain="Writing dialogue for a screenplay",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When explaining data analysis, include practical examples of how data can be visualized and interpreted",
        domain="Explaining data analysis",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

 
    Feedback(
        content="When creating a landscape design, suggest indigenous plants that are low maintenance and environmentally friendly",
        domain="Creating a landscape design",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_content"],
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),

]
