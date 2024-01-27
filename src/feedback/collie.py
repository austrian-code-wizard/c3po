from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

collie_feedback = [

    Feedback(
        content="When talking about Andy Cutting, make sure your response contains the words 'one', 'Inventions', '2018'",
        domain="Talking about Andy Cutting",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['one', 'Inventions', '2018'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Harriet Toompere, make sure your response contains the words 'stage', 'drama', 'Her'",
        domain="Talking about Harriet Toompere",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['stage', 'drama', 'Her'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure your response contains the words 'the', 'staff', 'was'",
        domain="Talking about Tulloona",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'staff', 'was'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Fiona Ramsay, make sure your response contains the words 'for', 'her', 'play'",
        domain="Talking about Fiona Ramsay",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['for', 'her', 'play'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Sultanate of Bacan, make sure your response contains the words 'Sirrullah', 'succeeded', 'a'",
        domain="Talking about Sultanate of Bacan",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Sirrullah', 'succeeded', 'a'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Appalachian temperate rainforest, make sure your response contains the words 'most', 'As', 'likely'",
        domain="Talking about Appalachian temperate rainforest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['most', 'As', 'likely'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Therese A. Jenkins, make sure your response contains the words 'Wisconsin', 'commissary', 'to'",
        domain="Talking about Therese A. Jenkins",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Wisconsin', 'commissary', 'to'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure your response contains the words 'injured', 'training', 'Rolle'",
        domain="Talking about Magnum Rolle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['injured', 'training', 'Rolle'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about List of members of the Parliament of Finland, 2011–2015, make sure your response contains the words 'government', 'the', 'formation'",
        domain="Talking about List of members of the Parliament of Finland, 2011–2015",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['government', 'the', 'formation'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Lectionary 325, make sure your response contains the words 'Greek', 'on', 'a'",
        domain="Talking about Lectionary 325",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Greek', 'on', 'a'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Chiral drugs, make sure your response contains the words 'site', 'of', 'the'",
        domain="Talking about Chiral drugs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['site', 'of', 'the'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about September 1916, make sure your response contains the words '1,053', 'while', 'were'",
        domain="Talking about September 1916",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['1,053', 'while', 'were'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Thermal fluctuations, make sure your response contains the words 'faster', 'over', 'inasmuch'",
        domain="Talking about Thermal fluctuations",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['faster', 'over', 'inasmuch'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tsui Tsin-tong, make sure your response contains the words 'interior', 'a', 'decoration'",
        domain="Talking about Tsui Tsin-tong",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['interior', 'a', 'decoration'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure your response contains the words '27', 'as', 'of'",
        domain="Talking about Tulloona",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['27', 'as', 'of'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Eric Portman, make sure your response contains the words 'Canterbury', 'another', 'war'",
        domain="Talking about Eric Portman",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Canterbury', 'another', 'war'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Bulgarian lands across the Danube, make sure your response contains the words 'a', 'Empire', 'term'",
        domain="Talking about Bulgarian lands across the Danube",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'Empire', 'term'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tampa International Airport, make sure your response contains the words 'special', 'the', 'also'",
        domain="Talking about Tampa International Airport",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['special', 'the', 'also'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about IQ Student Accommodation, make sure your response contains the words '2016', 'Living', 'Prodigy'",
        domain="Talking about IQ Student Accommodation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['2016', 'Living', 'Prodigy'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Eric Portman, make sure your response contains the words 'He', 'buried', 'in'",
        domain="Talking about Eric Portman",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['He', 'buried', 'in'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Emperor Taizong of Liao, make sure your response contains the words 'Zhao', 'as', 'incursion'",
        domain="Talking about Emperor Taizong of Liao",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Zhao', 'as', 'incursion'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about An Post–Chain Reaction, make sure your response contains the words 'its', 'won', 'win'",
        domain="Talking about An Post–Chain Reaction",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['its', 'won', 'win'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tonawanda Engine, make sure your response contains the words 'for', '2013', 'EPA'",
        domain="Talking about Tonawanda Engine",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['for', '2013', 'EPA'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Book of Demons, make sure your response contains the words 'the', 'exchange', 'be'",
        domain="Talking about Book of Demons",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'exchange', 'be'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about James Smith Cree Nation, make sure your response contains the words 'the', 'or', 'signing'",
        domain="Talking about James Smith Cree Nation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'or', 'signing'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Lectionary 325, make sure your response contains the words 'folios', 'Menologion', 'on'",
        domain="Talking about Lectionary 325",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['folios', 'Menologion', 'on'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Fiona Ramsay, make sure your response contains the words 'plays', 'My', 'Book'",
        domain="Talking about Fiona Ramsay",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['plays', 'My', 'Book'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure your response contains the words 'the', 'preseason', 'predicted'",
        domain="Talking about Magnum Rolle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'preseason', 'predicted'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Internet prostitution, make sure your response contains the words 'add', 'are', 'a'",
        domain="Talking about Internet prostitution",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['add', 'are', 'a'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Smithfield Poultry Market, make sure your response contains the words 'claimed', 'concrete', 'spanning'",
        domain="Talking about Smithfield Poultry Market",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['claimed', 'concrete', 'spanning'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Bud Riley, make sure your response contains the words 'Football', 'as', 'the'",
        domain="Talking about Bud Riley",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Football', 'as', 'the'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Morgan Edge, make sure your response contains the words 'safe', 'a', 'Lionel'",
        domain="Talking about Morgan Edge",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['safe', 'a', 'Lionel'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Lucía (singer), make sure your response contains the words 'was', 'born', 'Andalusia'",
        domain="Talking about Lucía (singer)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['was', 'born', 'Andalusia'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure your response contains the words 'per', 'averages', 'game'",
        domain="Talking about Magnum Rolle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['per', 'averages', 'game'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Explosive boiling or phase explosion, make sure your response contains the words 'instability', 'on', 'right'",
        domain="Talking about Explosive boiling or phase explosion",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['instability', 'on', 'right'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Maria Petrou, make sure your response contains the words 'and', 'London', 'College'",
        domain="Talking about Maria Petrou",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['and', 'London', 'College'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure your response contains the words 'They', 'regular', 'record'",
        domain="Talking about Magnum Rolle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['They', 'regular', 'record'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Emperor Taizong of Liao, make sure your response contains the words 'of', 'a', 'Dejun'",
        domain="Talking about Emperor Taizong of Liao",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'a', 'Dejun'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Unstable world braces for Trump, make sure the first sentences has a 1st word of 'A'",
        domain="Talking about Unstable world braces for Trump",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='a',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about H-E-B issues ice cream recall, make sure the first sentences has a 1st word of 'Customers'",
        domain="Talking about H-E-B issues ice cream recall",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='customers',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Nursing home that had 12 people die lays off all workers, make sure the first sentences has a 1st word of 'I'",
        domain="Talking about Nursing home that had 12 people die lays off all workers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='i',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Save our Schoolkids: Premier dips toe in water, make sure the first sentences has a 1st word of 'Mr'",
        domain="Talking about Save our Schoolkids: Premier dips toe in water",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='mr',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='he',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='in',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Cattle mutilation, make sure the first sentences has a 1st word of 'Blood'",
        domain="Talking about Cattle mutilation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='blood',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Statement by advocate Nelson Chamisa, make sure the first sentences has a 1st word of 'We'",
        domain="Talking about Statement by advocate Nelson Chamisa",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='we',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about More noise complaints filed over motorcycle racing at fairgrounds, make sure the first sentences has a 1st word of 'Shoblom'",
        domain="Talking about More noise complaints filed over motorcycle racing at fairgrounds",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='shoblom',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about TransPerfect, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about TransPerfect",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='in',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='this',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'His'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='his',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Nigel Dabinyaba, make sure the first sentences has a 1st word of 'Dabinyaba'",
        domain="Talking about Nigel Dabinyaba",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='dabinyaba',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'Shubskaya'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='shubskaya',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='she',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='the',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Apple certification programs, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Apple certification programs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='this',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'It'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='it',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Chiefs snap counts, Week 14: Lots of changes on defense, make sure the first sentences has a 1st word of 'Sign'",
        domain="Talking about Chiefs snap counts, Week 14: Lots of changes on defense",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='sign',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration, make sure the first sentences has a 1st word of 'Entinostat'",
        domain="Talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='entinostat',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Tin Can Island Port, make sure the first sentences has a 1st word of 'Tin'",
        domain="Talking about Tin Can Island Port",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='tin',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='the',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Silvia Fuselli, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Silvia Fuselli",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='she',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Raghu Raj Bahadur, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Raghu Raj Bahadur",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='he',
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Ayyub Guliyev (conductor), do not use the words 'there', 'this', 'is'",
        domain="Talking about Ayyub Guliyev (conductor)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Asociación de Trabajadores Inmigrantes Marroquíes en España, do not use the words 'be', 'this', 'and'",
        domain="Talking about Asociación de Trabajadores Inmigrantes Marroquíes en España",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Ray Sinatra, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ray Sinatra",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about War reserve stock, do not use the words 'there', 'to', 'is'",
        domain="Talking about War reserve stock",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Operation Cycle, do not use the words 'be', 'of', 'is'",
        domain="Talking about Operation Cycle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Carlos Pavón, do not use the words 'there', 'this', 'is'",
        domain="Talking about Carlos Pavón",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about OpenSearch, do not use the words 'there', 'to', 'is'",
        domain="Talking about OpenSearch",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Antonio Sanchez (politician), do not use the words 'be', 'this', 'is'",
        domain="Talking about Antonio Sanchez (politician)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about 2012–13 Senior Women's T20 League, do not use the words 'be', 'this', 'is'",
        domain="Talking about 2012–13 Senior Women's T20 League",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Elizabeth Street, Brisbane, do not use the words 'there', 'to', 'and'",
        domain="Talking about Elizabeth Street, Brisbane",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'and'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Paul Hemphill, do not use the words 'be', 'this', 'is'",
        domain="Talking about Paul Hemphill",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Ang Bagong Lipunan Series, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ang Bagong Lipunan Series",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Thumatha fuscescens, do not use the words 'be', 'this', 'and'",
        domain="Talking about Thumatha fuscescens",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Nouvelles Extraordinaires de Divers Endroits, do not use the words 'there', 'this', 'is'",
        domain="Talking about Nouvelles Extraordinaires de Divers Endroits",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Revere Camera Company, do not use the words 'be', 'this', 'is'",
        domain="Talking about Revere Camera Company",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Cosumnes River Preserve, do not use the words 'be', 'this', 'is'",
        domain="Talking about Cosumnes River Preserve",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Jimmy Wakely, do not use the words 'there', 'this', 'is'",
        domain="Talking about Jimmy Wakely",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Kyle Jacobs (footballer, born 1986), do not use the words 'the', 'to', 'in'",
        domain="Talking about Kyle Jacobs (footballer, born 1986)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['the', 'to', 'in'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Alkaline battery, do not use the words 'there', 'this', 'and'",
        domain="Talking about Alkaline battery",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'and'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Norman Mineta, do not use the words 'be', 'this', 'and'",
        domain="Talking about Norman Mineta",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about USS Denver (LPD-9), do not use the words 'there', 'of', 'and'",
        domain="Talking about USS Denver (LPD-9)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'of', 'and'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Martinus (son of Heraclius), do not use the words 'be', 'this', 'is'",
        domain="Talking about Martinus (son of Heraclius)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about A Kiss for the Petals, do not use the words 'be', 'of', 'in'",
        domain="Talking about A Kiss for the Petals",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'in'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Christian Ditlev Frederik Reventlow, do not use the words 'be', 'this', 'is'",
        domain="Talking about Christian Ditlev Frederik Reventlow",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Hanging Rock (Wabash River), do not use the words 'there', 'this', 'is'",
        domain="Talking about Hanging Rock (Wabash River)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Gasolin' 2, do not use the words 'there', 'this', 'is'",
        domain="Talking about Gasolin' 2",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Keith Burnett, do not use the words 'there', 'this', 'is'",
        domain="Talking about Keith Burnett",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about 2012 Rally Argentina, do not use the words 'be', 'this', 'in'",
        domain="Talking about 2012 Rally Argentina",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_eq_than
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
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Plug and play, do not use the words 'there', 'this', 'is'",
        domain="Talking about Plug and play",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_eq_than
    ),


    Feedback(
        content="When talking about Summer Close-Up, do not use the words 'be', 'to', 'is'",
        domain="Talking about Summer Close-Up",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_eq_than
    ),

]
