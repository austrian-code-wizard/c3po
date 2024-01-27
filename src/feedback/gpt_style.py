from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

gpt_style_feedback = [

    Feedback(
        content="Begin every email to my colleague Alice with 'How's the Wonderland project going?'",
        domain="writing emails to colleague Alice",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Start each team meeting note with 'Team Update:', followed by the date",
        domain="writing team meeting notes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use marine biology jargon when contributing to the monthly ocean newsletter",
        domain="contributing to the ocean newsletter",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write all internal project codes in bold during team briefings",
        domain="conducting team briefings",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Cite sources in APA format when composing research summaries for the history department",
        domain="composing research summaries for the history department",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use at least one historical anecdote when composing lectures for my ancient civilizations class",
        domain="composing lectures for ancient civilizations class",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Maintain a friendly tone but use technical language in IT support emails",
        domain="writing IT support emails",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Always reference the latest software version when updating technical documentation",
        domain="updating technical documentation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Add a personal sign-off, 'Stay joyful,', in the monthly newsletter to volunteer staff",
        domain="writing monthly newsletters to volunteer staff",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Begin medical briefs with a concise summary of the patient's history",
        domain="writing medical briefs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include an actionable takeaway in the conclusion of marketing strategy reports",
        domain="writing marketing strategy reports",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use active voice when creating instructions for the user manuals",
        domain="creating user manuals",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Spell out all numbers below ten in the children’s storybooks",
        domain="writing children’s storybooks",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use layman's terms when explaining technical concepts in the family tech guide",
        domain="explaining technical concepts in the family tech guide",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When tweeting from the company account, use no more than two hashtags",
        domain="tweeting from the company account",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure that cooking instructions are numbered when writing recipe articles",
        domain="writing recipe articles",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use timestamped entries when writing in the laboratory journal",
        domain="writing in the laboratory journal",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Implement a conversational tone in responses during the customer service live chat",
        domain="responding in customer service live chat",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Respond to user comments on the blog with at least two follow-up questions",
        domain="responding to user comments on the blog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include a trivia fact related to the topic in educational social media posts",
        domain="writing educational social media posts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Start all responses to customer complaints with 'Thank you for bringing this to our attention,'",
        domain="responding to customer complaints",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use sports analogies when writing motivational emails to the sales team",
        domain="writing motivational emails to the sales team",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply a neutral tone and avoid idioms when editing content for the corporate website",
        domain="editing content for the corporate website",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure all metaphors in poetry submissions are nature-themed",
        domain="writing poetry submissions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When documenting software bugs, use bullet points for each distinct issue",
        domain="documenting software bugs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Limit exclamation points to one per paragraph in promotional material for the theme park",
        domain="writing promotional material for the theme park",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use minimalist sentence structures when creating captions for art gallery exhibits",
        domain="creating captions for art gallery exhibits",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Spell out acronyms the first time they are used in the quarterly company update",
        domain="writing the quarterly company update",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate one quote from team members in the end-of-year highlights report",
        domain="writing the end-of-year highlights report",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="End blog posts with a call-to-action encouraging readers to subscribe",
        domain="writing blog posts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Start guides with 'Step-by-Step:' for clarity in the craft instruction blog",
        domain="writing for the craft instruction blog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include a high-resolution image every two paragraphs in the travel articles",
        domain="writing travel articles",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use italicized text when introducing a new technical term in educational papers",
        domain="writing educational papers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure privacy by never using full names in patient success stories for the clinic newsletter",
        domain="writing patient success stories for the clinic newsletter",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Mention at least one current world event in the introduction of political analysis essays",
        domain="writing political analysis essays",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use blue ink when adding handwritten notes to the printed event itineraries",
        domain="adding notes to event itineraries",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Provide calorie counts next to each ingredient in the diet blog recipes",
        domain="writing recipes for the diet blog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Emphasize keywords by underlining them in study guides for the physics course",
        domain="creating study guides for the physics course",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="When replying to fan mail, always thank the sender for their support in the first paragraph",
        domain="replying to fan mail",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include a glossary at the end of each chapter in the programming textbook",
        domain="writing chapters for the programming textbook",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Limit paragraphs to three sentences each when summarizing news articles for the morning briefing",
        domain="summarizing news articles for the morning briefing",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Start cross-cultural communication training materials with an anecdote",
        domain="writing cross-cultural communication training materials",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="End each 'Did You Know?' section with a related challenge question",
        domain="writing 'Did You Know?' sections in educational content",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write product descriptions with a sensory appeal for the gourmet food catalog",
        domain="writing product descriptions for the gourmet food catalog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include subtitles for every figure and table in the scientific research report",
        domain="writing scientific research reports",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Always include the next steps at the end of meeting summaries within project documentation",
        domain="writing meeting summaries for project documentation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use green text for highlighting sustainable practices in company newsletters",
        domain="highlighting content in company newsletters",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Sign each outreach letter to potential donors with 'In solidarity,'",
        domain="writing outreach letters to potential donors",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Present case studies in a narrative format for the marketing lessons blog",
        domain="writing case studies for the marketing lessons blog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Begin each chapter of the self-help book with an inspiring quote",
        domain="writing chapters for the self-help book",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Format all legal documentation with numbered sections and a table of contents",
        domain="formatting legal documentation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use nautical terminology when scripting for the maritime museum's audio tour",
        domain="scripting for the maritime museum's audio tour",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Avoid the use of contractions in the formal reports to government agencies",
        domain="writing formal reports to government agencies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="In the gardening blog, start each post with a seasonal tip",
        domain="writing posts for the gardening blog",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Open blog posts with a provocative question",
        domain="writing blog posts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use bullet points for listing features in product descriptions",
        domain="writing product descriptions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include a PS message in fundraising emails",
        domain="writing fundraising emails",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a persuasive tone in sales pitches",
        domain="delivering sales pitches",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write video scripts in a conversational style",
        domain="writing video scripts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Summarize key points at the end of presentation slides",
        domain="creating presentation slides",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include at least two synonyms in thesaurus entries",
        domain="writing thesaurus entries",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Restrict the use of passive voice in research papers",
        domain="writing research papers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply MLA citation style in literature essays",
        domain="writing literature essays",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write news articles in the past tense",
        domain="writing news articles",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Provide at least three examples in educational materials",
        domain="creating educational materials",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure all tweets are within 280 characters",
        domain="composing tweets",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use expressive adjectives in restaurant reviews",
        domain="writing restaurant reviews",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in the third person in biographical profiles",
        domain="writing biographical profiles",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Begin advice columns with a sympathetic response",
        domain="writing advice columns",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Keep haiku poems to 17 syllables",
        domain="composing haiku poems",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="State hypotheses at the beginning of scientific reports",
        domain="writing scientific reports",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure fantasy stories contain a magical element",
        domain="writing fantasy stories",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use wide margins for legal documents",
        domain="formatting legal documents",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ a professional tone in LinkedIn messages",
        domain="writing LinkedIn messages",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt ABAB rhyme schemes in traditional poems",
        domain="composing traditional poems",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Stick to four-panel structures in comic strips",
        domain="creating comic strips",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Maintain consistency in font usage throughout PowerPoint presentations",
        domain="designing PowerPoint presentations",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Refer to the reader directly using 'you' in self-help books",
        domain="writing self-help books",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write Instagram captions with a call-to-action",
        domain="writing Instagram captions",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply past perfect tense when sharing anecdotes",
        domain="sharing anecdotes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Open letters to the editor with a clear statement of purpose",
        domain="writing letters to the editor",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Label all axes clearly in statistical charts",
        domain="creating statistical charts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include a confidentiality notice in email footers for sensitive communication",
        domain="writing sensitive emails",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure code comments are concise and informative in software documentation",
        domain="writing software documentation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Avoid using jargon in user manuals for consumer electronics",
        domain="writing user manuals for consumer electronics",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write with a friendly tone in community newsletters",
        domain="writing community newsletters",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Craft each tweet with one clear message or focal point",
        domain="crafting tweets",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Close advice responses with a summary sentence",
        domain="responding to advice requests",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Limit paragraphs to three sentences in mobile app content",
        domain="writing mobile app content",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Provide step-by-step instructions in DIY tutorials",
        domain="creating DIY tutorials",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Highlight key takeaways in sidebar notes of textbooks",
        domain="writing textbook sidebar notes",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Address the audience as 'Dear Valued Customer' in service emails",
        domain="writing customer service emails",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Start technical reports with an abstract summary",
        domain="writing technical reports",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure privacy policy language is unambiguous",
        domain="writing privacy policies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Implement consistent indentation in code samples",
        domain="presenting code samples",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use motivational quotes in workout app notifications",
        domain="creating workout app notifications",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Title chapters intriguingly in novels",
        domain="titling chapters in novels",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Keep sentences under 20 words in children's storybooks",
        domain="writing children's storybooks",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Cite sources in APA style for psychology papers",
        domain="writing psychology papers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate a minimum of two visual aids in training materials",
        domain="creating training materials",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure all descriptions in real estate listings are vivid and appealing",
        domain="writing real estate listings",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Structure FAQ sections with questions in bold and answers in a normal font",
        domain="designing FAQ sections",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write artist biographies in present tense",
        domain="writing artist biographies",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use formal titles and last names in interview request emails",
        domain="writing interview request emails",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

]
