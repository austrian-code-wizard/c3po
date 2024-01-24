from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

collie_feedback = [

    Feedback(
        content="When talking about the book Tampa International Airport, make sure all sentences contain the words 'the', 'airports', '3'",
        domain="Talking about the book Tampa International Airport",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'airports', '3'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Internet prostitution, make sure all sentences contain the words 'add', 'are', 'a'",
        domain="Talking about the book Internet prostitution",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['add', 'are', 'a'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Bud Riley, make sure all sentences contain the words 'western', 'Alabama', 'in'",
        domain="Talking about the book Bud Riley",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['western', 'Alabama', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Appalachian temperate rainforest, make sure all sentences contain the words 'most', 'As', 'likely'",
        domain="Talking about the book Appalachian temperate rainforest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['most', 'As', 'likely'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Explosive boiling or phase explosion, make sure all sentences contain the words 'instability', 'on', 'right'",
        domain="Talking about the book Explosive boiling or phase explosion",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['instability', 'on', 'right'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Lucía (singer), make sure all sentences contain the words 'was', 'born', 'Andalusia'",
        domain="Talking about the book Lucía (singer)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['was', 'born', 'Andalusia'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book 2015 Shvut Rachel shooting, make sure all sentences contain the words 'have', 'rising', 'the'",
        domain="Talking about the book 2015 Shvut Rachel shooting",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['have', 'rising', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Edith van Dijk, make sure all sentences contain the words 'a', 'her', 'as'",
        domain="Talking about the book Edith van Dijk",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'her', 'as'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book The Zingari, make sure all sentences contain the words 'of', 'notable', 'for'",
        domain="Talking about the book The Zingari",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'notable', 'for'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Appalachian temperate rainforest, make sure all sentences contain the words 'of', 'this', 'in'",
        domain="Talking about the book Appalachian temperate rainforest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book September 1916, make sure all sentences contain the words 'Romania', 'Brusilov', 'making'",
        domain="Talking about the book September 1916",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Romania', 'Brusilov', 'making'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Tmesisternus denticollis, make sure all sentences contain the words 'the', 'Tmesisternus', 'denticollis'",
        domain="Talking about the book Tmesisternus denticollis",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Tmesisternus', 'denticollis'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Bee, Oklahoma, make sure all sentences contain the words 'The', 'to', 'be'",
        domain="Talking about the book Bee, Oklahoma",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['The', 'to', 'be'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book In His Image (novel), make sure all sentences contain the words 'where', 'schedule', 'Secretary'",
        domain="Talking about the book In His Image (novel)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['where', 'schedule', 'Secretary'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Tonawanda Engine, make sure all sentences contain the words 'for', '2013', 'EPA'",
        domain="Talking about the book Tonawanda Engine",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['for', '2013', 'EPA'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Great Keppel Island, make sure all sentences contain the words 'Holdings', 'proposal', '2010'",
        domain="Talking about the book Great Keppel Island",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Holdings', 'proposal', '2010'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Fifth Avenue Theatre, make sure all sentences contain the words 'show', 'theatre', 'World'",
        domain="Talking about the book Fifth Avenue Theatre",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['show', 'theatre', 'World'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book ROKS Dokdo, make sure all sentences contain the words 'operations', 'in', 'assisted'",
        domain="Talking about the book ROKS Dokdo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['operations', 'in', 'assisted'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Internet prostitution, make sure all sentences contain the words 'more', 'Twitter', 'is'",
        domain="Talking about the book Internet prostitution",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['more', 'Twitter', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Bud Riley, make sure all sentences contain the words 'Football', 'as', 'the'",
        domain="Talking about the book Bud Riley",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Football', 'as', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Dino 206 S, make sure all sentences have exactly 85 characters. Include whitespace into your character count",
        domain="Talking about the book Dino 206 S",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=85,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Leo Benardo, make sure all sentences have exactly 118 characters. Include whitespace into your character count",
        domain="Talking about the book Leo Benardo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=118,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Kirby: Right Back at Ya!, make sure all sentences have exactly 95 characters. Include whitespace into your character count",
        domain="Talking about the book Kirby: Right Back at Ya!",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=95,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book David Cromer, make sure all sentences have exactly 102 characters. Include whitespace into your character count",
        domain="Talking about the book David Cromer",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=102,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Ahmadu Kuran Daga, make sure all sentences have exactly 104 characters. Include whitespace into your character count",
        domain="Talking about the book Ahmadu Kuran Daga",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=104,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Crossnaders, make sure all sentences have exactly 81 characters. Include whitespace into your character count",
        domain="Talking about the book Crossnaders",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=81,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Frans van Dorne, make sure all sentences have exactly 89 characters. Include whitespace into your character count",
        domain="Talking about the book Frans van Dorne",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=89,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Flåm Line, make sure all sentences have exactly 112 characters. Include whitespace into your character count",
        domain="Talking about the book Flåm Line",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=112,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book 911th Air Refueling Squadron, make sure all sentences have exactly 98 characters. Include whitespace into your character count",
        domain="Talking about the book 911th Air Refueling Squadron",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=98,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Ordinary Day (Dolores O'Riordan song), make sure all sentences have exactly 87 characters. Include whitespace into your character count",
        domain="Talking about the book Ordinary Day (Dolores O'Riordan song)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=87,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book The Complete Plain Words, make sure all sentences have exactly 110 characters. Include whitespace into your character count",
        domain="Talking about the book The Complete Plain Words",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=110,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Jewish Military Museum, make sure all sentences have exactly 93 characters. Include whitespace into your character count",
        domain="Talking about the book Jewish Military Museum",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=93,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Palace of Shaki Khans, make sure all sentences have exactly 108 characters. Include whitespace into your character count",
        domain="Talking about the book Palace of Shaki Khans",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=108,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Romanian Writers' Society, make sure all sentences have exactly 113 characters. Include whitespace into your character count",
        domain="Talking about the book Romanian Writers' Society",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=113,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Emirati cricket team in the Netherlands in 2017, make sure all sentences have exactly 103 characters. Include whitespace into your character count",
        domain="Talking about the book Emirati cricket team in the Netherlands in 2017",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=103,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Romanian Writers' Society, make sure all sentences have exactly 91 characters. Include whitespace into your character count",
        domain="Talking about the book Romanian Writers' Society",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=91,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Just Dance (song), make sure all sentences have exactly 96 characters. Include whitespace into your character count",
        domain="Talking about the book Just Dance (song)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=96,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book 911th Air Refueling Squadron, make sure all sentences have exactly 94 characters. Include whitespace into your character count",
        domain="Talking about the book 911th Air Refueling Squadron",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=94,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book James Smith (priest), make sure all sentences have exactly 109 characters. Include whitespace into your character count",
        domain="Talking about the book James Smith (priest)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=109,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about the book Rancho Rinconada, Cupertino, California, make sure all sentences have exactly 82 characters. Include whitespace into your character count",
        domain="Talking about the book Rancho Rinconada, Cupertino, California",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c04'],
        type=Type.quantitative,
        metric=Metric.is_length,
        metric_value=82,
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration, make sure the first sentences has a 1st word of 'Entinostat'",
        domain="Talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='entinostat',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Save our Schoolkids: Premier dips toe in water, make sure the first sentences has a 1st word of 'Mr'",
        domain="Talking about Save our Schoolkids: Premier dips toe in water",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='mr',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'His'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='his',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about H-E-B issues ice cream recall, make sure the first sentences has a 1st word of 'Customers'",
        domain="Talking about H-E-B issues ice cream recall",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='customers',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Cattle mutilation, make sure the first sentences has a 1st word of 'Blood'",
        domain="Talking about Cattle mutilation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='blood',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about TransPerfect, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about TransPerfect",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nigel Dabinyaba, make sure the first sentences has a 1st word of 'Dabinyaba'",
        domain="Talking about Nigel Dabinyaba",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='dabinyaba',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Silvia Fuselli, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Silvia Fuselli",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tin Can Island Port, make sure the first sentences has a 1st word of 'Tin'",
        domain="Talking about Tin Can Island Port",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='tin',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nursing home that had 12 people die lays off all workers, make sure the first sentences has a 1st word of 'I'",
        domain="Talking about Nursing home that had 12 people die lays off all workers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='i',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Chiefs snap counts, Week 14: Lots of changes on defense, make sure the first sentences has a 1st word of 'Sign'",
        domain="Talking about Chiefs snap counts, Week 14: Lots of changes on defense",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='sign',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unstable world braces for Trump, make sure the first sentences has a 1st word of 'A'",
        domain="Talking about Unstable world braces for Trump",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='a',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Raghu Raj Bahadur, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Raghu Raj Bahadur",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'It'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='it',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Detectives: Dad tells daughter he killed her mom 30 years ago, make sure all sentences have at least 14 words with all words having at most 7 characters",
        domain="Talking about how Detectives: Dad tells daughter he killed her mom 30 years ago",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[14, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how New York Giants Roster Moves; Steve Spagnuolo Sticks With Eli, make sure all sentences have at least 17 words with all words having at most 7 characters",
        domain="Talking about how New York Giants Roster Moves; Steve Spagnuolo Sticks With Eli",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[17, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how John Dorsey still won't say who he's taking No. 1, make sure all sentences have at least 9 words with all words having at most 6 characters",
        domain="Talking about how John Dorsey still won't say who he's taking No. 1",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[9, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Nikon D850 review, make sure all sentences have at least 28 words with all words having at most 7 characters",
        domain="Talking about how Nikon D850 review",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[28, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Brandin Cooks, Patriots Wide Receiver and Stockton Native, Heads to Super Bowl LII, make sure all sentences have at least 36 words with all words having at most 7 characters",
        domain="Talking about how Brandin Cooks, Patriots Wide Receiver and Stockton Native, Heads to Super Bowl LII",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[36, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Einstein's Theory of Gravity Holds Up on Test of a Three-Star System, make sure all sentences have at least 15 words with all words having at most 7 characters",
        domain="Talking about how Einstein's Theory of Gravity Holds Up on Test of a Three-Star System",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[15, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Sorry for Our Toddler’s Screams, Mr. and Mrs. Homeowner: Blame the Housing Crisis, make sure all sentences have at least 14 words with all words having at most 6 characters",
        domain="Talking about how Sorry for Our Toddler’s Screams, Mr. and Mrs. Homeowner: Blame the Housing Crisis",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[14, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Wynne delivers keynote address at pre-election Ont. Liberal gathering, make sure all sentences have at least 8 words with all words having at most 6 characters",
        domain="Talking about how Wynne delivers keynote address at pre-election Ont. Liberal gathering",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[8, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Hendricks Scheduled to Make Sprint Car Debut at Texas Motor Speedway, make sure all sentences have at least 13 words with all words having at most 7 characters",
        domain="Talking about how Hendricks Scheduled to Make Sprint Car Debut at Texas Motor Speedway",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[13, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Chargers' Okung says many players 'frustrated' with NFL's new anthem policy, make sure all sentences have at least 15 words with all words having at most 5 characters",
        domain="Talking about how Chargers' Okung says many players 'frustrated' with NFL's new anthem policy",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[15, 5],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Karan Mehra & Nisha Rawal Welcome Their Baby Boy; Share An Adorable Picture, make sure all sentences have at least 10 words with all words having at most 6 characters",
        domain="Talking about how Karan Mehra & Nisha Rawal Welcome Their Baby Boy; Share An Adorable Picture",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[10, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Technical FAQ: Shifting troubleshooting, CX worlds flats follow-up, make sure all sentences have at least 23 words with all words having at most 7 characters",
        domain="Talking about how Technical FAQ: Shifting troubleshooting, CX worlds flats follow-up",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[23, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Cazenovia mummy makes hospital visit to undergo medical testing, make sure all sentences have at least 17 words with all words having at most 6 characters",
        domain="Talking about how Cazenovia mummy makes hospital visit to undergo medical testing",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[17, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how NASCAR | Could Dale Earnhardt Jr. win last race at Texas? | The State, make sure all sentences have at least 11 words with all words having at most 5 characters",
        domain="Talking about how NASCAR | Could Dale Earnhardt Jr. win last race at Texas? | The State",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[11, 5],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how NBA games Saturday, scores, highlights, updates: Pistons win again with Blake Griffin, make sure all sentences have at least 22 words with all words having at most 7 characters",
        domain="Talking about how NBA games Saturday, scores, highlights, updates: Pistons win again with Blake Griffin",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[22, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Sass Basics: The Sass Mixin Directive, make sure all sentences have at least 17 words with all words having at most 5 characters",
        domain="Talking about how Sass Basics: The Sass Mixin Directive",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[17, 5],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Airline passenger fined after keeping free airline apple, make sure all sentences have at least 20 words with all words having at most 5 characters",
        domain="Talking about how Airline passenger fined after keeping free airline apple",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[20, 5],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how Bark Bracket: Retrievers become top dogs, boosted by UMBC, make sure all sentences have at least 10 words with all words having at most 7 characters",
        domain="Talking about how Bark Bracket: Retrievers become top dogs, boosted by UMBC",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[10, 7],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how 'Battle of Bayou Estates' awaits court date, make sure all sentences have at least 18 words with all words having at most 6 characters",
        domain="Talking about how 'Battle of Bayou Estates' awaits court date",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[18, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about how The most popular Christmas drinks have been revealed, make sure all sentences have at least 16 words with all words having at most 6 characters",
        domain="Talking about how The most popular Christmas drinks have been revealed",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c06a'],
        type=Type.quantitative,
        metric=[Metric.word_count,Metric.word_length_leq],
        metric_value=[16, 6],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about USS Denver (LPD-9), do not use the words 'there', 'this', 'and'",
        domain="Talking about USS Denver (LPD-9)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Neith, do not use the words 'there', 'to', 'is'",
        domain="Talking about Neith",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about John Ruffo, do not use the words 'there', 'this', 'is'",
        domain="Talking about John Ruffo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Singing quail, do not use the words 'be', 'this', 'and'",
        domain="Talking about Singing quail",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Close Encounters of the Third Kind, do not use the words 'there', 'this', 'is'",
        domain="Talking about Close Encounters of the Third Kind",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tongoni Ruins, do not use the words 'be', 'of', 'is'",
        domain="Talking about Tongoni Ruins",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Sulfuric acid poisoning, do not use the words 'be', 'this', 'in'",
        domain="Talking about Sulfuric acid poisoning",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Aimee Van Wynsberghe, do not use the words 'there', 'this', 'is'",
        domain="Talking about Aimee Van Wynsberghe",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Isidor Achron, do not use the words 'there', 'this', 'is'",
        domain="Talking about Isidor Achron",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Aimee Van Wynsberghe, do not use the words 'be', 'this', 'is'",
        domain="Talking about Aimee Van Wynsberghe",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Akamas (film), do not use the words 'be', 'to', 'and'",
        domain="Talking about Akamas (film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tick, Tick... Boom! (film), do not use the words 'there', 'this', 'is'",
        domain="Talking about Tick, Tick... Boom! (film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nick Clegg Says I'm Sorry (The Autotune Remix), do not use the words 'be', 'this', 'is'",
        domain="Talking about Nick Clegg Says I'm Sorry (The Autotune Remix)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mark van Bommel, do not use the words 'there', 'this', 'is'",
        domain="Talking about Mark van Bommel",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Wutach (river), do not use the words 'be', 'this', 'is'",
        domain="Talking about Wutach (river)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mark Ciardi, do not use the words 'there', 'this', 'in'",
        domain="Talking about Mark Ciardi",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Collections (Delphic album), do not use the words 'there', 'to', 'is'",
        domain="Talking about Collections (Delphic album)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Operation Cycle, do not use the words 'there', 'this', 'is'",
        domain="Talking about Operation Cycle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ang Bagong Lipunan Series, do not use the words 'there', 'this', 'in'",
        domain="Talking about Ang Bagong Lipunan Series",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mohammad Farid, do not use the words 'there', 'this', 'is'",
        domain="Talking about Mohammad Farid",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),

]
