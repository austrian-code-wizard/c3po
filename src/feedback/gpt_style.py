from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

gpt_style_feedback = [
 
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
        content="Use legal jargon when writing blog posts for my law firm",
        domain="writing blog posts for my law firm",
        effect="use legal jargon",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Integrate pop culture references for composing ad copy targeted at millennials",
        domain="composing ad copy for targeted millennials",
        effect="integrate pop culture references",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a Shakespearean tone when drafting theater club announcements",
        domain="drafting theater club announcements",
        effect="adopt a Shakespearean tone",
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
        content="Use technical IT terminology when writing articles for a tech blog",
        domain="writing articles for a tech blog",
        effect="use technical IT terminology",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in iambic pentameter when composing event invitations",
        domain="composing event invitations",
        effect="write in iambic pentameter",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include historical facts when creating content for history education platforms",
        domain="creating content for history education platforms",
        effect="include historical facts",
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
        content="Provide analogies to sporting events when writing motivational speeches",
        domain="writing motivational speeches",
        effect="provide analogies to sporting events",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Cite scientific studies in authoring health and wellness articles",
        domain="authoring health and wellness articles",
        effect="cite scientific studies",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Simulate an old English dialect when creating content for a medieval-themed game",
        domain="creating content for a medieval-themed game",
        effect="simulate an old English dialect",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ comic book slang in writing product descriptions for a comic shop",
        domain="writing product descriptions for a comic shop",
        effect="employ comic book slang",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use internet acronyms when composing messages for a tech-savvy audience",
        domain="composing messages for a tech-savvy audience",
        effect="use internet acronyms",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include quotes from famous authors when sending out a book club newsletter",
        domain="sending out a book club newsletter",
        effect="include quotes from famous authors",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write with a noir detective voice for crafting stories for a mystery blog",
        domain="crafting stories for a mystery blog",
        effect="write with a noir detective voice",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate trendy slang when writing scripts for YouTube influencers",
        domain="writing scripts for YouTube influencers",
        effect="incorporate trendy slang",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use a friendly and colloquial style in composing an FAQ section for a startup website",
        domain="composing an FAQ section for a startup website",
        effect="use a friendly and colloquial style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in second person point of view for creating interactive stories",
        domain="creating interactive stories",
        effect="write in second person point of view",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use pirate speak when sending promotional emails for 'Talk Like a Pirate Day'",
        domain="sending promotional emails for 'Talk Like a Pirate Day'",
        effect="use pirate speak",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Imitate famous philosophers' styles when composing college philosophy course descriptions",
        domain="composing college philosophy course descriptions",
        effect="imitate famous philosophers' styles",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Mimic a news anchor's delivery in writing company announcement memos",
        domain="writing company announcement memos",
        effect="mimic a news anchor's delivery",
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
        content="Apply a minimalistic style in designing content for a minimalist lifestyle brand",
        domain="designing content for a minimalist lifestyle brand",
        effect="apply a minimalistic style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include puns and wordplay when writing product descriptions for a novelty gift store",
        domain="writing product descriptions for a novelty gift store",
        effect="include puns and wordplay",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use an academic tone in developing online course materials for a university",
        domain="developing online course materials for a university",
        effect="use an academic tone",
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
        content="Embed secret codes or ciphers when creating a puzzle for an escape room website",
        domain="creating a puzzle for an escape room website",
        effect="embed secret codes or ciphers",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use metaphors related to space when writing content for an astronomy club",
        domain="writing content for an astronomy club",
        effect="use metaphors related to space",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Speak from the perspective of an inanimate object in writing first-person narratives for a creative writing class",
        domain="writing first-person narratives for a creative writing class",
        effect="speak from the perspective of an inanimate object",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ a vintage radio broadcaster style in scripting podcast introductions",
        domain="scripting podcast introductions",
        effect="employ a vintage radio broadcaster style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Mimic a sports commentator's excitement when live-tweeting a sporting event",
        domain="live-tweeting a sporting event",
        effect="mimic a sports commentator's excitement",
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
        content="Imitate a fantasy novel narrative style for writing descriptions for tabletop RPG campaigns",
        domain="writing descriptions for tabletop RPG campaigns",
        effect="imitate a fantasy novel narrative style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Portray a futuristic AI persona when composing tweets for a tech product launch",
        domain="composing tweets for a tech product launch",
        effect="portray a futuristic AI persona",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include cryptic messages in writing teaser announcements for a mystery event",
        domain="writing teaser announcements for a mystery event",
        effect="include cryptic messages",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use hyperbolic expressions when crafting blurbs for sensational news articles",
        domain="crafting blurbs for sensational news articles",
        effect="use hyperbolic expressions",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a mystical and enigmatic tone in describing products on a psychic services website",
        domain="describing products on a psychic services website",
        effect="adopt a mystical and enigmatic tone",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in the style of a classical poet for composing social media posts for a literature class",
        domain="composing social media posts for a literature class",
        effect="write in the style of a classical poet",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ wilderness survival terminology in creating articles for outdoor adventure blogs",
        domain="creating articles for outdoor adventure blogs",
        effect="employ wilderness survival terminology",
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
        content="Mimic a detective's investigative report when authoring mystery game narratives",
        domain="authoring mystery game narratives",
        effect="mimic a detective's investigative report",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Simulate a fantasy creature's speech pattern in writing dialogue for a fantasy novel",
        domain="writing dialogue for a fantasy novel",
        effect="simulate a fantasy creature's speech pattern",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Emulate tabloid headline style when brainstorming titles for sensational podcasts",
        domain="brainstorming titles for sensational podcasts",
        effect="emulate tabloid headline style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use aviation terminology when creating content for an airline blog",
        domain="creating content for an airline blog",
        effect="use aviation terminology",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in code or cryptic language for composing riddles for a gaming app",
        domain="composing riddles for a gaming app",
        effect="write in code or cryptic language",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write as if from a dystopian future when creating narratives for post-apocalyptic themed games",
        domain="creating narratives for post-apocalyptic themed games",
        effect="write as if from a dystopian future",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in a Q&A format when constructing help sections for websites",
        domain="constructing help sections for websites",
        effect="write in a Q&A format",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write as if you were a time traveler when composing descriptions for historical documentaries",
        domain="composing descriptions for historical documentaries",
        effect="write as if you were a time traveler",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a melodramatic telenovela style for drafting scripts for drama club practice sessions",
        domain="drafting scripts for drama club practice sessions",
        effect="adopt a melodramatic telenovela style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use expressions from 1920s American slang when writing for a Roaring Twenties themed event",
        domain="writing for a Roaring Twenties themed event",
        effect="use expressions from 1920s American slang",
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
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Emulate '80s pop culture lingo when producing content for an '80s nostalgia blog",
        domain="producing content for an '80s nostalgia blog",
        effect="emulate '80s pop culture lingo",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use a call-and-response structure when writing interactive community posts",
        domain="writing interactive community posts",
        effect="use a call-and-response structure",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ the language and style of film noir in scripting scenes for a film study course",
        domain="scripting scenes for a film study course",
        effect="employ the language and style of film noir",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Echo a famous celebrity's catchphrases when crafting tweets for a celebrity parody account",
        domain="crafting tweets for a celebrity parody account",
        effect="echo a famous celebrity's catchphrases",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Blend in educational teaching methods when designing tutorials for a learning app",
        domain="designing tutorials for a learning app",
        effect="blend in educational teaching methods",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a minimalist poetic style when writing copy for art gallery promotions",
        domain="writing copy for art gallery promotions",
        effect="adopt a minimalist poetic style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Provide examples using fantasy lore when creating lesson plans for a creative writing course",
        domain="creating lesson plans for a creative writing course",
        effect="provide examples using fantasy lore",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Formulate as if giving a royal decree when sending notifications from an app with a monarchy theme",
        domain="sending notifications from an app with a monarchy theme",
        effect="formulate as if giving a royal decree",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include quotes from movies in drafting trivia questions for a film fan club",
        domain="drafting trivia questions for a film fan club",
        effect="include quotes from movies",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Mirror a stand-up comedian's pacing in writing social media posts for a comedy club",
        domain="writing social media posts for a comedy club",
        effect="mirror a stand-up comedian's pacing",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Draw parallels to historical events when explaining current news topics",
        domain="explaining current news topics",
        effect="draw parallels to historical events",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include urban legends in creating newsletter content for a horror fan community",
        domain="creating newsletter content for a horror fan community",
        effect="include urban legends",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Format like a screenplay when writing descriptions of video content",
        domain="writing descriptions of video content",
        effect="format like a screenplay",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use verbose and florid language when composing wedding invitations",
        domain="composing wedding invitations",
        effect="use verbose and florid language",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Imitate the style of a radio DJ when hosting a live stream for an online music event",
        domain="hosting a live stream for an online music event",
        effect="imitate the style of a radio DJ",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adopt a conspiratorial tone in writing descriptions for a conspiracy theory podcast",
        domain="writing descriptions for a conspiracy theory podcast",
        effect="adopt a conspiratorial tone",
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
        content="Integrate classical literary quotes when constructing posts for a book discussion forum",
        domain="constructing posts for a book discussion forum",
        effect="integrate classical literary quotes",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Echo a game show host's enthusiasm when creating marketing copy for a mobile gaming app",
        domain="creating marketing copy for a mobile gaming app",
        effect="echo a game show host's enthusiasm",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Utilize a snappy journalistic tone when writing briefs for a news aggregation service",
        domain="writing briefs for a news aggregation service",
        effect="utilize a snappy journalistic tone",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Construct as a personal diary entry for writing descriptions for a self-help blog",
        domain="writing descriptions for a self-help blog",
        effect="construct as a personal diary entry",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Compose with a motivational speech rhythm when drafting company-wide memos",
        domain="drafting company-wide memos",
        effect="compose with a motivational speech rhythm",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in second person narrative for creating fitness program descriptions",
        domain="creating fitness program descriptions",
        effect="write in second person narrative",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate classical music terminology when writing reviews for a classical concert series",
        domain="writing reviews for a classical concert series",
        effect="incorporate classical music terminology",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Integrate advanced technical jargon when writing articles for a specialized science magazine",
        domain="writing articles for a specialized science magazine",
        effect="integrate advanced technical jargon",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate Shakespearean English in composing creative stories for a literature class",
        domain="composing creative stories for a literature class",
        effect="incorporate Shakespearean English",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Insert relevant emojis when sending promotional messages to a younger audience",
        domain="sending promotional messages to a younger audience",
        effect="insert relevant emojis",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include pseudocode for explaining algorithms in a programming blog",
        domain="explaining algorithms in a programming blog",
        effect="include pseudocode",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Format responses in bullet points when answering frequently asked questions on a website",
        domain="answering frequently asked questions on a website",
        effect="format responses in bullet points",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use storytelling techniques when crafting product descriptions for an online store",
        domain="crafting product descriptions for an online store",
        effect="use storytelling techniques",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Embed interactive elements in creating educational content for an e-learning platform",
        domain="creating educational content for an e-learning platform",
        effect="embed interactive elements",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply legalese language when drafting terms of service for a new app",
        domain="drafting terms of service for a new app",
        effect="apply legalese language",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Introduce pop culture references when writing a review for a trendy restaurant",
        domain="writing a review for a trendy restaurant",
        effect="introduce pop culture references",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Implement code optimization explanations when giving feedback on software development forums",
        domain="giving feedback on software development forums",
        effect="implement code optimization explanations",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Compose using iambic pentameter when writing custom greetings for greeting cards",
        domain="writing custom greetings for greeting cards",
        effect="compose using iambic pentameter",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Develop a distinct character voice for creating dialogue in a video game script",
        domain="creating dialogue for a video game script",
        effect="develop a distinct character voice",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Incorporate data visualizations when providing market analysis in a business report",
        domain="providing market analysis in a business report",
        effect="incorporate data visualizations",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use stream-of-consciousness style in writing personal blog posts",
        domain="writing a personal blog post",
        effect="use stream-of-consciousness style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply a question-and-answer format when composing interview articles",
        domain="composing interview articles",
        effect="apply a question-and-answer format",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write in the second person narrative for creating interactive fiction",
        domain="creating interactive fiction",
        effect="write in the second person narrative",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Maintain a haiku structure when posting daily updates on social media",
        domain="posting daily updates on social media",
        effect="maintain a haiku structure",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ a telegraph style of short sentences when sending updates during a live event",
        domain="sending updates during a live event",
        effect="employ a telegraph style of short sentences",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Ensure adherence to AP Style when writing news articles for an online publication",
        domain="writing news articles for an online publication",
        effect="ensure adherence to AP Style",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use a Socratic method of asking questions when explaining philosophy topics on a discussion forum",
        domain="explaining philosophy topics on a discussion forum",
        effect="use a Socratic method of asking questions",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Follow screenplay formatting rules when drafting scripts for independent films",
        domain="drafting scripts for independent films",
        effect="follow screenplay formatting rules",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include step-by-step instructions in writing DIY project guides",
        domain="writing DIY project guides",
        effect="include step-by-step instructions",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Utilize sports terminology when commenting on an athlete's performance in a blog post",
        domain="commenting on an athlete's performance in a blog post",
        effect="utilize sports terminology",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Employ non-linear narrative in writing plot summaries for a movie review website",
        domain="writing plot summaries for a movie review website",
        effect="employ non-linear narrative",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Insert academic citations when producing research summaries for academic journals",
        domain="producing research summaries for academic journals",
        effect="insert academic citations",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Present information in a cause-and-effect structure when explaining historical events for an educational website",
        domain="explaining historical events for an educational website",
        effect="present information in a cause-and-effect structure",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Compose using varied poetic forms when submitting work to a poetry contest",
        domain="submitting work to a poetry contest",
        effect="compose using varied poetic forms",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use technical drawing annotations when describing engineering designs in a document",
        domain="describing engineering designs in a document",
        effect="use technical drawing annotations",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Include sensory descriptions in writing travel blog entries",
        domain="writing travel blog entries",
        effect="include sensory descriptions",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Provide cross-cultural comparisons when writing articles about global business etiquette",
        domain="writing articles about global business etiquette",
        effect="provide cross-cultural comparisons",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Write following the inverted pyramid structure when composing press releases for a PR agency",
        domain="composing press releases for a PR agency",
        effect="write following the inverted pyramid structure",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Apply a lighthearted and whimsical tone when drafting content for a children's entertainment website",
        domain="drafting content for a children's entertainment website",
        effect="apply a lighthearted and whimsical tone",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use a comparison and contrast framework when creating content for a product review blog",
        domain="creating content for a product review blog",
        effect="use a comparison and contrast framework",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Synthesize information into infographics when delivering reports on social media analytics",
        domain="delivering reports on social media analytics",
        effect="synthesize information into infographics",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Adapt classical Greek rhetoric when writing persuasive essays on contemporary issues",
        domain="writing persuasive essays on contemporary issues",
        effect="adapt classical Greek rhetoric",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Integrate dialects and regional speech when composing narratives for a cultural heritage project",
        domain="composing narratives for a cultural heritage project",
        effect="integrate dialects and regional speech",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Construct a dialogue-heavy approach in writing tutorials for a conversation-based language app",
        domain="writing a tutorial for a conversation-based language app",
        effect="construct a dialogue-heavy approach",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Base the writing on a specific meter and rhyme scheme when creating lyrics for a new musical composition",
        domain="creating lyrics for a new musical composition",
        effect="base the writing on specific meter and rhyme scheme",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

 
    Feedback(
        content="Use persuasive language with calls to action when drafting campaign emails for a political candidate",
        domain="drafting campaign emails for a political candidate",
        effect="use persuasive language with calls to action",
        scope=Scope.regional,
        categories=["gpt_style"],
        type=Type.qualitative,
        comparison=Comparison.greater_eq_than
    ),

]
